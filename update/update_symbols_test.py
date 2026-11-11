# Copyright 2026 Google LLC
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

"""Regression tests for failures in the Material Symbols updater."""

from contextlib import ExitStack
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from absl.testing import flagsaver
import joblib
import requests

import update_symbols


class UpdateSymbolsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if not update_symbols.FLAGS.is_parsed():
            update_symbols.FLAGS(["update_symbols_test"])

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)

    def test_successful_download_writes_response_bytes(self):
        destination = self.root / "nested" / "icon.svg"
        response = mock.Mock(content=b"<svg />")
        with mock.patch.object(
            update_symbols.requests, "get", return_value=response
        ) as get:
            update_symbols._do_fetch("https://example.test/icon.svg", destination)

        get.assert_called_once_with(
            "https://example.test/icon.svg", headers=update_symbols._HEADERS
        )
        response.raise_for_status.assert_called_once_with()
        self.assertEqual(destination.read_bytes(), b"<svg />")

    def test_http_failure_propagates_and_preserves_existing_asset(self):
        destination = self.root / "icon.svg"
        destination.write_bytes(b"previous asset")
        response = mock.Mock()
        response.raise_for_status.side_effect = requests.HTTPError("503 unavailable")
        with mock.patch.object(update_symbols.requests, "get", return_value=response):
            with self.assertRaises(requests.HTTPError):
                update_symbols._do_fetch("https://example.test/icon.svg", destination)

        self.assertEqual(destination.read_bytes(), b"previous asset")

    def test_connection_failure_propagates_without_creating_asset(self):
        destination = self.root / "icon.svg"
        with mock.patch.object(
            update_symbols.requests,
            "get",
            side_effect=requests.ConnectionError("offline"),
        ):
            with self.assertRaises(requests.ConnectionError):
                update_symbols._do_fetch("https://example.test/icon.svg", destination)

        self.assertFalse(destination.exists())

    def _main_context(self, response):
        versions = self.root / "current_versions.json"
        versions.write_text('{"symbols::test_icon": 1}')
        metadata = {
            "host": "example.test",
            "families": ["Material Symbols Outlined"],
            "icons": [{"name": "test_icon", "version": 2, "unsupported_families": []}],
        }

        def create_fetch(asset, args):
            return update_symbols.Fetch(
                asset.src_url_pattern.format(**args),
                self.root / asset.dest_dir_pattern.format(**args),
            )

        stack = ExitStack()
        self.addCleanup(stack.close)
        stack.enter_context(
            flagsaver.flagsaver(fetch=True, overwrite=False, icon_limit=1)
        )
        stack.enter_context(
            mock.patch.object(
                update_symbols, "_current_versions", return_value=versions
            )
        )
        stack.enter_context(
            mock.patch.object(update_symbols, "_latest_metadata", return_value=metadata)
        )
        stack.enter_context(
            mock.patch.object(update_symbols, "_create_fetch", side_effect=create_fetch)
        )
        stack.enter_context(
            mock.patch.object(update_symbols.requests, "get", return_value=response)
        )
        # Exercise joblib's exception propagation without starting fifty worker processes.
        stack.enter_context(
            mock.patch.object(
                update_symbols,
                "Parallel",
                side_effect=lambda **kwargs: joblib.Parallel(
                    n_jobs=2, backend="threading"
                ),
            )
        )
        fonts = stack.enter_context(mock.patch.object(update_symbols, "_fetch_fonts"))
        return versions, fonts

    def test_failed_parallel_download_aborts_main_before_font_processing(self):
        response = mock.Mock()
        response.raise_for_status.side_effect = requests.HTTPError("503 unavailable")
        versions, fonts = self._main_context(response)

        with self.assertRaises(requests.HTTPError):
            update_symbols.main([])

        self.assertEqual(json.loads(versions.read_text()), {"symbols::test_icon": 1})
        fonts.assert_not_called()

    def test_failed_download_does_not_advance_version_cache(self):
        response = mock.Mock()
        response.raise_for_status.side_effect = requests.HTTPError("503 unavailable")
        versions, _ = self._main_context(response)
        before = versions.read_bytes()

        try:
            update_symbols.main([])
        except requests.HTTPError:
            pass

        self.assertEqual(versions.read_bytes(), before)

    def test_successful_downloads_allow_version_cache_to_advance(self):
        response = mock.Mock(content=b"downloaded asset")
        versions, fonts = self._main_context(response)

        update_symbols.main([])

        self.assertEqual(json.loads(versions.read_text()), {"symbols::test_icon": 2})
        fonts.assert_called_once()
        self.assertTrue(
            (
                self.root
                / "variablefont"
                / "MaterialSymbolsOutlined[FILL,GRAD,opsz,wght].css"
            ).exists()
        )

    def test_failed_font_download_does_not_decompress_stale_woff2(self):
        css = self.root / "font.css"
        css.write_text("src: url(https://example.test/font.woff2)")
        woff2_file = self.root / "font.woff2"
        woff2_file.write_bytes(b"previous font")
        response = mock.Mock()
        response.raise_for_status.side_effect = requests.HTTPError("503 unavailable")
        with mock.patch.object(update_symbols.requests, "get", return_value=response):
            with mock.patch.object(update_symbols, "decompress") as decompress:
                with mock.patch.object(
                    update_symbols.icons, "enumerate", return_value=[]
                ):
                    with self.assertRaises(requests.HTTPError):
                        update_symbols._fetch_fonts([css])

        decompress.assert_not_called()
        self.assertTrue(css.exists())
        self.assertEqual(woff2_file.read_bytes(), b"previous font")


if __name__ == "__main__":
    unittest.main()
