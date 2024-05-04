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
from joblib import Parallel, delayed, wrap_non_picklable_objects
from fontTools.ttLib import woff2
import os

FLAGS = flags.FLAGS


flags.DEFINE_bool("fetch", True, "Whether we can attempt to download assets.")
flags.DEFINE_bool("overwrite", False, "Update and overwrite existing assets.")
flags.DEFINE_integer("icon_limit", 0, "If > 0, the max # of icons to process.")


_METADATA_URL = "http://fonts.google.com/metadata/icons?incomplete=1&key=material_symbols"


class Asset(NamedTuple):
    src_url_pattern: str
    dest_dir_pattern: str


class Fetch(NamedTuple):
    src_url: str
    dest_file: Path


class Icon(NamedTuple):
    name: str
    version: int
    stylistic_sets: Set[str]

_ICON_ASSETS = (
    Asset(
        "https://{host}/s/i/short-term/release/{stylistic_set_snake}/{icon.name}/{style}/{size_px}px.svg",
        "symbols/web/{icon.name}/{stylistic_set_snake}/{icon.name}{style_suffix}_{size_px}px.svg",
    ),
    Asset(
        "https://{host}/s/i/short-term/release/{stylistic_set_snake}/{icon.name}/{style}/{size_px}px.xml",
        "symbols/android/{icon.name}/{stylistic_set_snake}/{icon.name}{style_suffix}_{size_px}px.xml",
    ),
)
# no wght variants for apple symbols.
_ICON_IOS_ASSETS = (
    Asset(
        "https://{host}/s/i/short-term/release/{stylistic_set_snake}/{icon.name}/{style}/{icon.name}{style_suffix}_symbol.svg",
        "symbols/ios/{icon.name}/{stylistic_set_snake}/{icon.name}{style_suffix}_symbol.svg"
    ),
)

_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

_SET_ASSETS = (
    # Fonts are acquired by abusing the Google Fonts web api. Nobody tell them :D
    Asset(
        "https://fonts.googleapis.com/css2?family={stylistic_set_url}:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200",
        "variablefont/{stylistic_set_font}.css",
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
    return f"symbols::{icon.name}"


def _symbol_families(metadata):
    return set(s for s in set(metadata["families"]) if "Symbols" in s)


def _icons(metadata):
    all_sets = _symbol_families(metadata)
    for raw_icon in metadata["icons"]:
        unsupported = set(raw_icon["unsupported_families"])
        yield Icon(
            raw_icon["name"],
            raw_icon["version"],
            all_sets - unsupported,
        )


def _create_fetch(asset, args):
    src_url = asset.src_url_pattern.format(**args)
    dest_file = asset.dest_dir_pattern.format(**args)
    dest_file = (Path(__file__) / "../.." / dest_file).resolve()
    return Fetch(src_url, dest_file)


@delayed
def _do_fetch_delayed(src_url, dest_file, i, total):
    _do_fetch(src_url, dest_file)
    if i % 5000 == 0:
        print("%d/%d complete" % (i, total))


def _do_fetch(src_url, dest_file):
    try :
        resp = requests.get(src_url, headers = _HEADERS)
        resp.raise_for_status()
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        dest_file.write_bytes(resp.content)
    except Exception as e:
        print(str(e))


def _do_fetches(fetches):
    print(f"Starting {len(fetches)} fetches")
    total = len(fetches)
    Parallel(n_jobs=50)(_do_fetch_delayed(f.src_url, f.dest_file, i, total) for i,f in enumerate(fetches))
    if total:
        print("%d/%d complete" % (total, total))
    

def decompress(infilepath: Path, outfilepath: Path):
    with infilepath.open(mode='rb') as infile:
        with outfilepath.open(mode='wb') as outfile:
            woff2.decompress(infile, outfile)


def _fetch_fonts(css_files: Sequence[Path]):
    for css_file in css_files:
        css = css_file.read_text()
        url = re.search(r"src:\s+url\(([^)]+)\)", css).group(1)
        assert url.endswith(".woff2")
        woff2_file = css_file.parent / (css_file.stem + ".woff2")
        dest_file = css_file.parent / (css_file.stem + ".ttf")
        _do_fetch(url, woff2_file)
        decompress(woff2_file, dest_file)
        css_file.unlink()
        with open(dest_file.with_suffix(".codepoints"), "w") as f:
            for name, codepoint in sorted(icons.enumerate(dest_file)):
                f.write(f"{name} {codepoint:04x}\n")


def _is_css(p: Path):
    return p.suffix == ".css"


def _files(fetches: Sequence[Fetch], pred):
    return [f.dest_file for f in fetches if pred(f.dest_file)]


def _should_skip(fetch: Fetch):
    return not FLAGS.overwrite and fetch.dest_file.is_file()


def _pattern_args(metadata, stylistic_set):
    return {
        "host": metadata["host"],
        "stylistic_set_snake": stylistic_set.replace(" ", "").lower(),
        "stylistic_set_url": stylistic_set.replace(" ", "+"),
        "stylistic_set_font": stylistic_set.replace(" ", "") + "[FILL,GRAD,opsz,wght]",
    }

def _create_fetches(style, opsz, pattern_args, fetches, skips, assets):
    pattern_args["style"] = style if style else "default"  
    pattern_args["style_suffix"] = f"_{style}" if style else ""
    pattern_args["size_px"] = str(opsz)
                        
    for asset in assets:
        fetch = _create_fetch(asset, pattern_args)
        if _should_skip(fetch):
            skips.append(fetch)
        else:
            fetches.append(fetch)


def main(_):
    current_versions = json.loads(_current_versions().read_text())
    metadata = _latest_metadata()
    stylistic_sets = _symbol_families(metadata)

    fetches = []
    skips = []
    num_changed = 0
    icons = tuple(_icons(metadata))
    if FLAGS.icon_limit > 0:
        icons = icons[: FLAGS.icon_limit]

    for icon in icons:
        ver_key = _version_key(icon)
        if not FLAGS.overwrite and icon.version <= current_versions.get(ver_key, 0):
            continue
        current_versions[ver_key] = icon.version

        num_changed += 1
        for stylistic_set in stylistic_sets:
            if stylistic_set not in icon.stylistic_sets:
                continue
            pattern_args = _pattern_args(metadata, stylistic_set)
            pattern_args["icon"] = icon
            for opsz in [20,24,40,48] :
                for fill in ["","fill1"] :
                    for grad in ["gradN25","","grad200"]:
                        _create_fetches(grad + fill, opsz, pattern_args, fetches, skips, _ICON_IOS_ASSETS)
                        for wght in ["wght100","wght200","wght300","","wght500","wght600","wght700"] :
                            _create_fetches(wght + grad + fill, opsz, pattern_args, fetches, skips, _ICON_ASSETS)


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

    _fetch_fonts(_files(fetches + skips, _is_css))

    with open(_current_versions(), "w") as f:
        json.dump(current_versions, f, indent=4, sort_keys=True)


if __name__ == "__main__":
    app.run(main)
