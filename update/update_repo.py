# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Quick and dirty utility to download latest icon assets for github."""

from absl import app
from absl import flags
import icons
import json
from pathlib import Path
import re
import requests
import time
from typing import NamedTuple, Set, Sequence, Tuple
from zipfile import ZipFile


FLAGS = flags.FLAGS


flags.DEFINE_bool(
    "skip_existing",
    False,
    "Do not download if local file exists, even if an update is available.",
)
flags.DEFINE_bool("fetch", True, "Whether we can attempt to download assets.")
flags.DEFINE_bool("explode_zip_files", True, "Whether to unzip any zip assets.")
flags.DEFINE_integer("icon_limit", 0, "If > 0, the max # of icons to process.")


_METADATA_URL = "http://fonts.google.com/metadata/icons?incomplete=1"


class Asset(NamedTuple):
    src_url_pattern: str
    dest_dir_pattern: str


class Fetch(NamedTuple):
    src_url: str
    dest_file: Path


class Icon(NamedTuple):
    name: str
    category: str
    version: int
    sizes_px: Tuple[int, ...]
    stylistic_sets: Set[str]


_ICON_ASSETS = (
    Asset(
        "https://{host}/s/i/{stylistic_set_snake}/{icon.name}/v{icon.version}/{size_px}px.svg",
        "src/{icon.category}/{icon.name}/{stylistic_set_snake}/{size_px}px.svg",
    ),
    Asset(
        "https://{host}/s/i/{stylistic_set_snake}/{icon.name}/v{icon.version}/black-android.zip",
        "android/{icon.category}/{icon.name}/{stylistic_set_snake}/black.zip",
    ),
    Asset(
        "https://{host}/s/i/{stylistic_set_snake}/{icon.name}/v{icon.version}/black-ios.zip",
        "ios/{icon.category}/{icon.name}/{stylistic_set_snake}/black.zip",
    ),
    Asset(
        "https://{host}/s/i/{stylistic_set_snake}/{icon.name}/v{icon.version}/black-18dp.zip",
        "png/{icon.category}/{icon.name}/{stylistic_set_snake}/18dp.zip",
    ),
    Asset(
        "https://{host}/s/i/{stylistic_set_snake}/{icon.name}/v{icon.version}/black-24dp.zip",
        "png/{icon.category}/{icon.name}/{stylistic_set_snake}/24dp.zip",
    ),
    Asset(
        "https://{host}/s/i/{stylistic_set_snake}/{icon.name}/v{icon.version}/black-36dp.zip",
        "png/{icon.category}/{icon.name}/{stylistic_set_snake}/36dp.zip",
    ),
    Asset(
        "https://{host}/s/i/{stylistic_set_snake}/{icon.name}/v{icon.version}/black-48dp.zip",
        "png/{icon.category}/{icon.name}/{stylistic_set_snake}/48dp.zip",
    ),
)

_SET_ASSETS = (
    # Fonts are acquired by abusing the Google Fonts web api. Nobody tell them :D
    Asset(
        "https://fonts.googleapis.com/css2?family={stylistic_set_url}",
        "font/{stylistic_set_font}.css",
    ),
)


def _latest_metadata():
    resp = requests.get(_METADATA_URL)
    resp.raise_for_status()
    raw_json = resp.text[5:]
    return json.loads(raw_json)


def _current_versions():
    return Path("current_versions.json")


def _version_key(icon: Icon):
    return f"{icon.category}::{icon.name}"


def _icons(metadata):
    all_sets = set(metadata["families"])
    for raw_icon in metadata["icons"]:
        unsupported = set(raw_icon["unsupported_families"])
        yield Icon(
            raw_icon["name"],
            raw_icon["categories"][0],
            raw_icon["version"],
            tuple(raw_icon["sizes_px"]),
            all_sets - unsupported,
        )


def _create_fetch(asset, args):
    src_url = asset.src_url_pattern.format(**args)
    dest_file = asset.dest_dir_pattern.format(**args)
    dest_file = (Path(__file__) / "../.." / dest_file).resolve()
    return Fetch(src_url, dest_file)


def _do_fetch(fetch):
    resp = requests.get(fetch.src_url)
    resp.raise_for_status()
    fetch.dest_file.parent.mkdir(parents=True, exist_ok=True)
    fetch.dest_file.write_bytes(resp.content)


def _do_fetches(fetches):
    print(f"Starting {len(fetches)} fetches")
    start_t = time.monotonic()
    print_t = start_t
    for idx, fetch in enumerate(fetches):
        _do_fetch(fetch)
        t = time.monotonic()
        if t - print_t > 5:
            print_t = t
            est_complete = (t - start_t) * (len(fetches) / (idx + 1))
            print(f"{idx}/{len(fetches)}, estimating {int(est_complete)}s left")


def _unzip_target(zip_path: Path):
    return zip_path.parent.resolve() / zip_path.stem


def _explode_zip_files(zips: Sequence[Path]):
    for zip_path in zips:
        assert zip_path.suffix == ".zip", zip_path
        if not zip_path.is_file():
            continue

        unzip_target = _unzip_target(zip_path)
        print(f"Unzip {zip_path} => {unzip_target}")
        with ZipFile(zip_path) as zip_file:
            zip_file.extractall(unzip_target)
        zip_path.unlink()


def _fetch_fonts(css_files: Sequence[Path]):
    for css_file in css_files:
        css = css_file.read_text()
        url = re.search(r"src:\s+url\(([^)]+)\)", css).group(1)
        assert url.endswith(".otf") or url.endswith(".ttf")
        fetch = Fetch(url, css_file.parent / (css_file.stem + url[-4:]))
        _do_fetch(fetch)
        css_file.unlink()
        with open(fetch.dest_file.with_suffix(".codepoints"), "w") as f:
            for name, codepoint in sorted(icons.enumerate(fetch.dest_file)):
                f.write(f"{name} {codepoint:04x}\n")


def _is_css(p: Path):
    return p.suffix == ".css"


def _is_zip(p: Path):
    return p.suffix == ".zip"


def _files(fetches: Sequence[Fetch], pred):
    return [f.dest_file for f in fetches if pred(f.dest_file)]


def _should_skip(fetch: Fetch):
    if not FLAGS.skip_existing:
        return False
    if _is_zip(fetch.dest_file):
        return _unzip_target(fetch.dest_file).is_dir()

    return fetch.dest_file.is_file()


def _pattern_args(metadata, stylistic_set):
    return {
        "host": metadata["host"],
        "stylistic_set_snake": stylistic_set.replace(" ", "").lower(),
        "stylistic_set_url": stylistic_set.replace(" ", "+"),
        "stylistic_set_font": stylistic_set.replace(" ", "") + "-Regular",
    }


def main(_):
    current_versions = json.loads(_current_versions().read_text())
    metadata = _latest_metadata()
    stylistic_sets = tuple(metadata["families"])

    fetches = []
    skips = []
    num_changed = 0
    icons = tuple(_icons(metadata))
    if FLAGS.icon_limit > 0:
        icons = icons[: FLAGS.icon_limit]

    for icon in icons:
        ver_key = _version_key(icon)
        if icon.version <= current_versions.get(ver_key, 0):
            continue
        current_versions[ver_key] = icon.version

        num_changed += 1
        for size_px in icon.sizes_px:
            for stylistic_set in stylistic_sets:
                if stylistic_set not in icon.stylistic_sets:
                    continue

                pattern_args = _pattern_args(metadata, stylistic_set)
                pattern_args["icon"] = icon
                pattern_args["size_px"] = size_px

                for asset in _ICON_ASSETS:
                    fetch = _create_fetch(asset, pattern_args)
                    if _should_skip(fetch):
                        skips.append(fetch)
                    else:
                        fetches.append(fetch)

    for stylistic_set in stylistic_sets:
        for asset in _SET_ASSETS:
            pattern_args = _pattern_args(metadata, stylistic_set)
            fetch = _create_fetch(asset, pattern_args)
            fetches.append(fetch)

    print(f"{num_changed}/{len(icons)} icons have changed")
    if skips:
        print(f"{len(skips)} fetches skipped because assets exist")

    if fetches:
        if FLAGS.fetch:
            _do_fetches(fetches)
        else:
            print(f"fetch disabled; not fetching {len(fetches)} assets")

    if FLAGS.explode_zip_files:
        _explode_zip_files(_files(fetches + skips, _is_zip))

    _fetch_fonts(_files(fetches + skips, _is_css))

    with open(_current_versions(), "w") as f:
        json.dump(current_versions, f, indent=4, sort_keys=True)


if __name__ == "__main__":
    app.run(main)
