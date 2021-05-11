# Copyright 2019 The Abseil Authors.
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

"""Import workaround so that Bazel, Py2/Py3, and enum34 package work together.

This works around a problem due to the combination of Bazel putting
third party packages before the stdlib in PYTHONPATH. What happens is:
  * The enum34 PyPi package is imported as 'enum'.
  * Bazel puts the path to enum34 before the stdlib, hence 'import enum'
    will prefer to use enum34 from above instead of the stdlib.
  * In Python 3, enum34 is used instead of the stdlib, which breaks
    lots of things. It works fine in Python 2, since there is no enum
    module.

To work around this, we do 3 things:
  1. Put the enum34 code on PYTHONPATH, but not directly importable as
     'enum'; it is under the (non importable) directory name with the
     PyPi package name and version.
  2. Try to import enum normally, if it works, great. This makes Py3 work
     (as well as Py2 when enum is available as normal).
  3. If the normal enum import failed, then try to find the enum34
     entry on sys.path, and append the missing directory name.

Once it is successfully imported, expose the module directly. This
prevents importing the module twice under different names. e.g.,
the following is true:
  from absl._enum_module import enum as absl_enum
  import enum as normal_enum
  assert absl_enum is normal_enum
"""
# pylint: disable=unused-import
import sys
import six

try:
  import enum
except ImportError:
  if six.PY3:
    # While not all Py3's have enum, only the ones we support do.
    raise
  for i, path in enumerate(sys.path):
    if '/enum34_archive' in path:
      sys.path[i] = path + '/enum34-1.1.6'

  import enum
