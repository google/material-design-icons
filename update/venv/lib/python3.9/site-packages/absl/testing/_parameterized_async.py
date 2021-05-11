# Lint as: python3
# Copyright 2020 The Abseil Authors.
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
"""Private module implementing async_wrapped method for wrapping async tests.

This is a separate private module so that parameterized still optionally
supports Python 2 syntax.
"""

import functools
import inspect


def async_wrapped(func):
  @functools.wraps(func)
  async def wrapper(*args, **kwargs):
    return await func(*args, **kwargs)
  return wrapper


def iscoroutinefunction(func):
  return inspect.iscoroutinefunction(func)
