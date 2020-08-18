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
import json
from pathlib import Path
import requests
import time
from typing import NamedTuple, Sequence, Tuple
from zipfile import ZipFile


FLAGS = flags.FLAGS


flags.DEFINE_bool(
    "skip_existing",
    False,
    "Do not download if local file exists, even if an update is available.",
)
flags.DEFINE_bool("fetch", True, "Whether we can attempt to download assets.")
flags.DEFINE_bool("explode_zips", True, "Whether to unzip any zip assets.")
flags.DEFINE_integer("icon_limit", 0, "If > 0, the max # of icons to process.")


_METADATA_URL = "http://fonts.google.com/metadata/icons"


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


_ASSETS = (
    Asset(
        "https://{host}/s/i/{stylistic_set}/{icon.name}/v{icon.version}/{size_px}px.svg",
        "src/{icon.category}/{icon.name}/{stylistic_set}/{size_px}px.svg",
    ),
    Asset(
        "https://{host}/s/i/{stylistic_set}/{icon.name}/v{icon.version}/black-android.zip",
        "android/{icon.category}/{icon.name}/{stylistic_set}/black.zip",
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
    for raw_icon in metadata["icons"]:
        yield Icon(
            raw_icon["name"],
            raw_icon["categories"][0],
            raw_icon["version"],
            tuple(raw_icon["sizes_px"]),
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


def _explode_zips(zips: Sequence[Path]):
    for zip_path in zips:
        assert zip_path.suffix == ".zip", zip_path
        if not zip_path.is_file():
            continue

        unzip_target = _unzip_target(zip_path)
        print(f"Unzip {zip_path} => {unzip_target}")
        with ZipFile(zip_path) as zip_file:
            zip_file.extractall(unzip_target)
        zip_path.unlink()


def _is_zip(p: Path):
    return p.suffix == ".zip"


def _zips(fetches: Sequence[Fetch]):
    return [f.dest_file for f in fetches if _is_zip(f.dest_file)]


def _should_skip(fetch: Fetch):
    if not FLAGS.skip_existing:
        return False
    if _is_zip(fetch.dest_file):
        return _unzip_target(fetch.dest_file).is_dir()

    return fetch.dest_file.is_file()


def main(_):
    metadata = _latest_metadata()
    current_versions = json.loads(_current_versions().read_text())

    host = metadata["host"]
    stylistic_sets = tuple(s.replace(" ", "").lower() for s in metadata["families"])

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
                pattern_args = {
                    "host": host,
                    "stylistic_set": stylistic_set,
                    "icon": icon,
                    "size_px": size_px,
                }
                for asset in _ASSETS:
                    fetch = _create_fetch(asset, pattern_args)
                    if _should_skip(fetch):
                        skips.append(fetch)
                    else:
                        fetches.append(fetch)

    print(f"{num_changed}/{len(icons)} have changed")
    if skips:
        print(f"{len(skips)} fetches skipped because assets exist")

    if fetches:
        if FLAGS.fetch:
            _do_fetches(fetches)
        else:
            print(f"fetch disabled; not fetching {len(fetches)} assets")

    if FLAGS.explode_zips:
        _explode_zips([f.dest_file for f in fetches + skips if _is_zip(f.dest_file)])

    with open(_current_versions(), "w") as f:
        json.dump(current_versions, f, indent=4, sort_keys=True)


if __name__ == "__main__":
    app.run(main)
