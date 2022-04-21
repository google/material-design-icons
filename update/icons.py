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

"""Utility to generate codepoint files for Google-style iconfonts."""

from fontTools import ttLib
import functools
from pathlib import Path


_PUA_CODEPOINTS = [
    range(0xE000, 0xF8FF + 1),
    range(0xF0000, 0xFFFFD + 1),
    range(0x100000, 0x10FFFD + 1)
]


def _is_pua(codepoint):
  return any(r for r in _PUA_CODEPOINTS if codepoint in r)


def _cmap(ttfont):

  def _cmap_reducer(acc, u):
    acc.update(u)
    return acc

  unicode_cmaps = (t.cmap for t in ttfont['cmap'].tables if t.isUnicode())
  return functools.reduce(_cmap_reducer, unicode_cmaps, {})

def _LookupSubtablesOfType(lookup_list, lookup_type):
  # Direct matches
  for lookup in lookup_list.Lookup:
    if lookup.LookupType == lookup_type:
      for subtable in lookup.SubTable:
        yield subtable

def _ligatures(ttfont):
  lookup_list = ttfont['GSUB'].table.LookupList

  # Direct ligatures
  for subtable in _LookupSubtablesOfType(lookup_list, 4):
    yield subtable.ligatures

  # Extensions
  for ext_subtable in _LookupSubtablesOfType(lookup_list, 7):
    if ext_subtable.ExtensionLookupType == 4:
      yield ext_subtable.ExtSubTable.ligatures

def enumerate(font_file: Path):
  """Yields (icon name, codepoint) tuples for icon font."""
  with ttLib.TTFont(font_file) as ttfont:
    cmap = _cmap(ttfont)
    rev_cmap = {v: k for k, v in cmap.items()}

    for lig_root in _ligatures(ttfont):
      for first_glyph_name, ligatures in lig_root.items():
        for ligature in ligatures:
          glyph_names = (first_glyph_name,) + tuple(ligature.Component)
          icon_name = ''.join(chr(rev_cmap[n]) for n in glyph_names)
          codepoint = rev_cmap[ligature.LigGlyph]
          if not _is_pua(codepoint):
            continue
          yield (icon_name, codepoint)