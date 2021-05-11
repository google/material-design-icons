# Copyright 2018 The Abseil Authors.
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

"""TestResult implementing default output for test execution status."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest
from absl.third_party import unittest3_backport


class TextTestResult(unittest3_backport.TextTestResult):
  """TestResult class that provides the default text result formatting."""

  def __init__(self, stream, descriptions, verbosity):
    # Disable the verbose per-test output from the superclass, since it would
    # conflict with our customized output.
    super(TextTestResult, self).__init__(stream, descriptions, 0)
    self._per_test_output = verbosity > 0

  def _print_status(self, tag, test):
    if self._per_test_output:
      test_id = test.id()
      if test_id.startswith('__main__.'):
        test_id = test_id[len('__main__.'):]
      print('[%s] %s' % (tag, test_id), file=self.stream)
      self.stream.flush()

  def startTest(self, test):
    super(TextTestResult, self).startTest(test)
    self._print_status(' RUN      ', test)

  def addSuccess(self, test):
    super(TextTestResult, self).addSuccess(test)
    self._print_status('       OK ', test)

  def addError(self, test, err):
    super(TextTestResult, self).addError(test, err)
    self._print_status('  FAILED  ', test)

  def addFailure(self, test, err):
    super(TextTestResult, self).addFailure(test, err)
    self._print_status('  FAILED  ', test)

  def addSkip(self, test, reason):
    super(TextTestResult, self).addSkip(test, reason)
    self._print_status('  SKIPPED ', test)

  def addExpectedFailure(self, test, err):
    super(TextTestResult, self).addExpectedFailure(test, err)
    self._print_status('       OK ', test)

  def addUnexpectedSuccess(self, test):
    super(TextTestResult, self).addUnexpectedSuccess(test)
    self._print_status('  FAILED  ', test)


class TextTestRunner(unittest.TextTestRunner):
  """A test runner that produces formatted text results."""

  _TEST_RESULT_CLASS = TextTestResult

  # Set this to true at the class or instance level to run tests using a
  # debug-friendly method (e.g, one that doesn't catch exceptions and interacts
  # better with debuggers).
  # Usually this is set using --pdb_post_mortem.
  run_for_debugging = False

  def run(self, test):
    # type: (TestCase) -> TestResult
    if self.run_for_debugging:
      return self._run_debug(test)
    else:
      return super(TextTestRunner, self).run(test)

  def _run_debug(self, test):
    # type: (TestCase) -> TestResult
    test.debug()
    # Return an empty result to indicate success.
    return self._makeResult()

  def _makeResult(self):
    return TextTestResult(self.stream, self.descriptions, self.verbosity)
