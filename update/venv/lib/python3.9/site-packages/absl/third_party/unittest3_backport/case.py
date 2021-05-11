"""Backport Python3 unittest.TestCase to absl when running Python 2.7."""

from __future__ import absolute_import

import contextlib
import sys
import unittest
import warnings

import six

# pylint: disable=invalid-name

if six.PY2:
  _subtest_msg_sentinel = object()

  class _ShouldStop(Exception):
    """The test should stop."""

  class _Outcome(object):

    def __init__(self, result=None):
      self.expecting_failure = False
      self.result = result
      self.result_supports_subtests = hasattr(result, 'addSubTest')
      self.success = True
      self.skipped = []
      self.expectedFailure = None
      self.errors = []
      self.errors_setup_and_teardown = []

    @contextlib.contextmanager
    def testPartExecutor(self, test_case, is_setup_or_teardown=False):
      old_success = self.success
      self.success = True
      try:
        yield
      except KeyboardInterrupt:
        raise
      except unittest.SkipTest as e:
        self.success = False
        self.skipped.append((test_case, str(e)))
      except _ShouldStop:
        pass
      except unittest.case._ExpectedFailure as e:
        self.success = False
        self.expecting_failure = True
        self.expectedFailure = e.exc_info
      except unittest.case._UnexpectedSuccess:
        self.expecting_failure = True
      # We need to catch everything here, including SystemExit.
      # KeyboardInterrupt was passed through above.
      except:  # pylint: disable=bare-except
        self.success = False
        if is_setup_or_teardown:
          self.errors_setup_and_teardown.append((test_case, sys.exc_info()))
        else:
          self.errors.append((test_case, sys.exc_info()))
      else:
        if self.result_supports_subtests and self.success:
          self.errors.append((test_case, None))
      finally:
        self.success = self.success and old_success


class TestCase(unittest.TestCase):

  if six.PY2:

    def __init__(self, methodName='runTest'):
      super(TestCase, self).__init__(methodName)
      self._subtest = None
      self._outcome = None

    def _addSkip(self, result, reason, test_case=None):
      addSkip = getattr(result, 'addSkip', None)
      if addSkip is not None:
        if test_case:
          addSkip(test_case, reason)
        else:
          addSkip(self, reason)
      else:
        warnings.warn('TestResult has no addSkip method, skips not reported',
                      RuntimeWarning, 2)
        if test_case:
          result.addSuccess(test_case)
        else:
          result.addSuccess(self)

    def _feedErrorsToResult(self, result, errors, setup_or_teardown=False):
      if setup_or_teardown:
        # Both failures and errors happen in setup or teardown phase are
        # regarded as errors in Python 2.
        for test, exc_info in errors:
          result.addError(test, exc_info)
      else:
        for test, exc_info in errors:
          if isinstance(test, _SubTest):
            result.addSubTest(test.test_case, test, exc_info)
          elif exc_info is not None:
            if issubclass(exc_info[0], self.failureException):
              result.addFailure(test, exc_info)
            else:
              result.addError(test, exc_info)

    def _addExpectedFailure(self, result, exc_info):
      try:
        addExpectedFailure = result.addExpectedFailure
      except AttributeError:
        warnings.warn(('TestResult has no addExpectedFailure method, '
                       'reporting as passes'), RuntimeWarning)
        result.addSuccess(self)
      else:
        addExpectedFailure(self, exc_info)

    def _addUnexpectedSuccess(self, result):
      try:
        addUnexpectedSuccess = result.addUnexpectedSuccess
      except AttributeError:
        warnings.warn(('TestResult has no addUnexpectedSuccess method, '
                       'reporting as failure'), RuntimeWarning)
        # We need to pass an actual exception and traceback to addFailure,
        # otherwise the legacy result can choke.
        try:
          raise unittest.case._UnexpectedSuccess
        except unittest.case._UnexpectedSuccess:
          result.addFailure(self, sys.exc_info())
      else:
        addUnexpectedSuccess(self)

    def run(self, result=None):
      orig_result = result
      if result is None:
        result = self.defaultTestResult()
        startTestRun = getattr(result, 'startTestRun', None)
        if startTestRun is not None:
          startTestRun()

      self._resultForDoCleanups = result
      result.startTest(self)

      testMethod = getattr(self, self._testMethodName)
      if (getattr(self.__class__, '__unittest_skip__', False) or
          getattr(testMethod, '__unittest_skip__', False)):
        # If the class or method was skipped.
        try:
          skip_why = (getattr(self.__class__, '__unittest_skip_why__', '')
                      or getattr(testMethod, '__unittest_skip_why__', ''))
          self._addSkip(result, skip_why, self)
        finally:
          result.stopTest(self)
        return
      outcome = _Outcome(result)
      expecting_failure = False
      try:
        self._outcome = outcome

        with outcome.testPartExecutor(self, is_setup_or_teardown=True):
          self.setUp()
        if outcome.success:
          with outcome.testPartExecutor(self):
            testMethod()
          expecting_failure = outcome.expecting_failure
          outcome.expecting_failure = False
          # The logic here is a little different from the implementation in
          # Python3.
          # In Python3, if a testcase is expecting failure, even if it
          # fails, outcome.success is True. This implementation does not work
          # for Python2. In Python2, if a subtest fails, it does not know
          # whether its parent test is expecting failure, and will set
          # outcome.success to False. Now the logic is that no matter whether a
          # testcase is expecting failure, if it fails, outcome.success is False
          if expecting_failure:
            if outcome.success:
              self._addUnexpectedSuccess(result)
            else:
              self._addExpectedFailure(result, outcome.expectedFailure)

          with outcome.testPartExecutor(self, is_setup_or_teardown=True):
            self.tearDown()
        for test, reason in outcome.skipped:
          self._addSkip(result, reason, test)
        self._feedErrorsToResult(result, outcome.errors_setup_and_teardown,
                                 setup_or_teardown=True)
        self._feedErrorsToResult(result, outcome.errors)

        self.doCleanups()
        if not expecting_failure and outcome.success:
          result.addSuccess(self)
        return result
      finally:
        result.stopTest(self)
        if orig_result is None:
          stopTestRun = getattr(result, 'stopTestRun', None)
          if stopTestRun is not None:
            stopTestRun()  # pylint: disable=not-callable

        # explicitly break reference cycles:
        # outcome.errors -> frame -> outcome -> outcome.errors
        # outcome.expectedFailure -> frame -> outcome -> outcome.expectedFailure
        outcome.errors = []
        outcome.expectedFailure = None

        # clear the outcome, no more needed
        self._outcome = None

    @contextlib.contextmanager
    def subTest(self, msg=_subtest_msg_sentinel, **params):
      """Return a context manager that will run the enclosed subtest."""

      if not self._outcome.result_supports_subtests:
        yield
        return
      parent = self._subtest

      # use a list to simulate the behavior of a ChainMap
      if parent is None:
        params_map = [params]
      else:
        params_map = list(parent.params)
        params_map.append(params)
      self._subtest = _SubTest(self, msg, params_map)
      try:
        with self._outcome.testPartExecutor(self._subtest):
          yield
        if not self._outcome.success:
          result = self._outcome.result
          if result is not None and result.failfast:
            raise _ShouldStop
          elif self._outcome.expectedFailure:
            # If the test is expecting a failure, we really want to
            # stop now and register the expected failure.
            raise _ShouldStop
      finally:
        self._subtest = parent


if six.PY2:
  class _SubTest(TestCase):

    def __init__(self, test_case, message, params):
      super(_SubTest, self).__init__()
      self._message = message
      self.test_case = test_case
      self.params = params
      self.failureException = test_case.failureException

    def runTest(self):
      raise NotImplementedError('subtests cannot be run directly')

    def _subDescription(self):
      parts = []
      if self._message is not _subtest_msg_sentinel:
        parts.append('[{}]'.format(self._message))
      if self.params:
        params_merged = {}
        for dictionary in self.params:
          params_merged.update(dictionary)
        params_desc = ', '.join(
            '{}={!r}'.format(k, v)
            for (k, v) in sorted(params_merged.items()))
        parts.append('({})'.format(params_desc))
      return ' '.join(parts) or '(<subtest>)'

    def id(self):
      return '{} {}'.format(self.test_case.id(), self._subDescription())

    def shortDescription(self):
      """Returns a one-line description of the subtest."""
      return self.test_case.shortDescription()

    def __str__(self):
      return '{} {}'.format(self.test_case, self._subDescription())
