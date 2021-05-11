# Copyright 2017 The Abseil Authors.
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

"""Module to enforce different constraints on flags.

Flags validators can be registered using following functions / decorators:
    flags.register_validator
    @flags.validator
    flags.register_multi_flags_validator
    @flags.multi_flags_validator

Three convenience functions are also provided for common flag constraints:
    flags.mark_flag_as_required
    flags.mark_flags_as_required
    flags.mark_flags_as_mutual_exclusive
    flags.mark_bool_flags_as_mutual_exclusive

See their docstring in this module for a usage manual.

Do NOT import this module directly. Import the flags package and use the
aliases defined at the package level instead.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import warnings

from absl.flags import _exceptions
from absl.flags import _flagvalues


class Validator(object):
  """Base class for flags validators.

  Users should NOT overload these classes, and use flags.Register...
  methods instead.
  """

  # Used to assign each validator an unique insertion_index
  validators_count = 0

  def __init__(self, checker, message):
    """Constructor to create all validators.

    Args:
      checker: function to verify the constraint.
          Input of this method varies, see SingleFlagValidator and
          multi_flags_validator for a detailed description.
      message: str, error message to be shown to the user.
    """
    self.checker = checker
    self.message = message
    Validator.validators_count += 1
    # Used to assert validators in the order they were registered.
    self.insertion_index = Validator.validators_count

  def verify(self, flag_values):
    """Verifies that constraint is satisfied.

    flags library calls this method to verify Validator's constraint.

    Args:
      flag_values: flags.FlagValues, the FlagValues instance to get flags from.
    Raises:
      Error: Raised if constraint is not satisfied.
    """
    param = self._get_input_to_checker_function(flag_values)
    if not self.checker(param):
      raise _exceptions.ValidationError(self.message)

  def get_flags_names(self):
    """Returns the names of the flags checked by this validator.

    Returns:
      [string], names of the flags.
    """
    raise NotImplementedError('This method should be overloaded')

  def print_flags_with_values(self, flag_values):
    raise NotImplementedError('This method should be overloaded')

  def _get_input_to_checker_function(self, flag_values):
    """Given flag values, returns the input to be given to checker.

    Args:
      flag_values: flags.FlagValues, containing all flags.
    Returns:
      The input to be given to checker. The return type depends on the specific
      validator.
    """
    raise NotImplementedError('This method should be overloaded')


class SingleFlagValidator(Validator):
  """Validator behind register_validator() method.

  Validates that a single flag passes its checker function. The checker function
  takes the flag value and returns True (if value looks fine) or, if flag value
  is not valid, either returns False or raises an Exception.
  """

  def __init__(self, flag_name, checker, message):
    """Constructor.

    Args:
      flag_name: string, name of the flag.
      checker: function to verify the validator.
          input  - value of the corresponding flag (string, boolean, etc).
          output - bool, True if validator constraint is satisfied.
              If constraint is not satisfied, it should either return False or
              raise flags.ValidationError(desired_error_message).
      message: str, error message to be shown to the user if validator's
          condition is not satisfied.
    """
    super(SingleFlagValidator, self).__init__(checker, message)
    self.flag_name = flag_name

  def get_flags_names(self):
    return [self.flag_name]

  def print_flags_with_values(self, flag_values):
    return 'flag --%s=%s' % (self.flag_name, flag_values[self.flag_name].value)

  def _get_input_to_checker_function(self, flag_values):
    """Given flag values, returns the input to be given to checker.

    Args:
      flag_values: flags.FlagValues, the FlagValues instance to get flags from.
    Returns:
      object, the input to be given to checker.
    """
    return flag_values[self.flag_name].value


class MultiFlagsValidator(Validator):
  """Validator behind register_multi_flags_validator method.

  Validates that flag values pass their common checker function. The checker
  function takes flag values and returns True (if values look fine) or,
  if values are not valid, either returns False or raises an Exception.
  """

  def __init__(self, flag_names, checker, message):
    """Constructor.

    Args:
      flag_names: [str], containing names of the flags used by checker.
      checker: function to verify the validator.
          input  - dict, with keys() being flag_names, and value for each
              key being the value of the corresponding flag (string, boolean,
              etc).
          output - bool, True if validator constraint is satisfied.
              If constraint is not satisfied, it should either return False or
              raise flags.ValidationError(desired_error_message).
      message: str, error message to be shown to the user if validator's
          condition is not satisfied
    """
    super(MultiFlagsValidator, self).__init__(checker, message)
    self.flag_names = flag_names

  def _get_input_to_checker_function(self, flag_values):
    """Given flag values, returns the input to be given to checker.

    Args:
      flag_values: flags.FlagValues, the FlagValues instance to get flags from.
    Returns:
      dict, with keys() being self.lag_names, and value for each key
      being the value of the corresponding flag (string, boolean, etc).
    """
    return dict([key, flag_values[key].value] for key in self.flag_names)

  def print_flags_with_values(self, flag_values):
    prefix = 'flags '
    flags_with_values = []
    for key in self.flag_names:
      flags_with_values.append('%s=%s' % (key, flag_values[key].value))
    return prefix + ', '.join(flags_with_values)

  def get_flags_names(self):
    return self.flag_names


def register_validator(flag_name,
                       checker,
                       message='Flag validation failed',
                       flag_values=_flagvalues.FLAGS):
  """Adds a constraint, which will be enforced during program execution.

  The constraint is validated when flags are initially parsed, and after each
  change of the corresponding flag's value.
  Args:
    flag_name: str, name of the flag to be checked.
    checker: callable, a function to validate the flag.
        input - A single positional argument: The value of the corresponding
            flag (string, boolean, etc.  This value will be passed to checker
            by the library).
        output - bool, True if validator constraint is satisfied.
            If constraint is not satisfied, it should either return False or
            raise flags.ValidationError(desired_error_message).
    message: str, error text to be shown to the user if checker returns False.
        If checker raises flags.ValidationError, message from the raised
        error will be shown.
    flag_values: flags.FlagValues, optional FlagValues instance to validate
        against.
  Raises:
    AttributeError: Raised when flag_name is not registered as a valid flag
        name.
  """
  v = SingleFlagValidator(flag_name, checker, message)
  _add_validator(flag_values, v)


def validator(flag_name, message='Flag validation failed',
              flag_values=_flagvalues.FLAGS):
  """A function decorator for defining a flag validator.

  Registers the decorated function as a validator for flag_name, e.g.

  @flags.validator('foo')
  def _CheckFoo(foo):
    ...

  See register_validator() for the specification of checker function.

  Args:
    flag_name: str, name of the flag to be checked.
    message: str, error text to be shown to the user if checker returns False.
        If checker raises flags.ValidationError, message from the raised
        error will be shown.
    flag_values: flags.FlagValues, optional FlagValues instance to validate
        against.
  Returns:
    A function decorator that registers its function argument as a validator.
  Raises:
    AttributeError: Raised when flag_name is not registered as a valid flag
        name.
  """

  def decorate(function):
    register_validator(flag_name, function,
                       message=message,
                       flag_values=flag_values)
    return function
  return decorate


def register_multi_flags_validator(flag_names,
                                   multi_flags_checker,
                                   message='Flags validation failed',
                                   flag_values=_flagvalues.FLAGS):
  """Adds a constraint to multiple flags.

  The constraint is validated when flags are initially parsed, and after each
  change of the corresponding flag's value.

  Args:
    flag_names: [str], a list of the flag names to be checked.
    multi_flags_checker: callable, a function to validate the flag.
        input - dict, with keys() being flag_names, and value for each key
            being the value of the corresponding flag (string, boolean, etc).
        output - bool, True if validator constraint is satisfied.
            If constraint is not satisfied, it should either return False or
            raise flags.ValidationError.
    message: str, error text to be shown to the user if checker returns False.
        If checker raises flags.ValidationError, message from the raised
        error will be shown.
    flag_values: flags.FlagValues, optional FlagValues instance to validate
        against.

  Raises:
    AttributeError: Raised when a flag is not registered as a valid flag name.
  """
  v = MultiFlagsValidator(
      flag_names, multi_flags_checker, message)
  _add_validator(flag_values, v)


def multi_flags_validator(flag_names,
                          message='Flag validation failed',
                          flag_values=_flagvalues.FLAGS):
  """A function decorator for defining a multi-flag validator.

  Registers the decorated function as a validator for flag_names, e.g.

  @flags.multi_flags_validator(['foo', 'bar'])
  def _CheckFooBar(flags_dict):
    ...

  See register_multi_flags_validator() for the specification of checker
  function.

  Args:
    flag_names: [str], a list of the flag names to be checked.
    message: str, error text to be shown to the user if checker returns False.
        If checker raises flags.ValidationError, message from the raised
        error will be shown.
    flag_values: flags.FlagValues, optional FlagValues instance to validate
        against.

  Returns:
    A function decorator that registers its function argument as a validator.

  Raises:
    AttributeError: Raised when a flag is not registered as a valid flag name.
  """

  def decorate(function):
    register_multi_flags_validator(flag_names,
                                   function,
                                   message=message,
                                   flag_values=flag_values)
    return function

  return decorate


def mark_flag_as_required(flag_name, flag_values=_flagvalues.FLAGS):
  """Ensures that flag is not None during program execution.

  Registers a flag validator, which will follow usual validator rules.
  Important note: validator will pass for any non-None value, such as False,
  0 (zero), '' (empty string) and so on.

  If your module might be imported by others, and you only wish to make the flag
  required when the module is directly executed, call this method like this:

    if __name__ == '__main__':
      flags.mark_flag_as_required('your_flag_name')
      app.run()

  Args:
    flag_name: str, name of the flag
    flag_values: flags.FlagValues, optional FlagValues instance where the flag
        is defined.
  Raises:
    AttributeError: Raised when flag_name is not registered as a valid flag
        name.
  """
  if flag_values[flag_name].default is not None:
    warnings.warn(
        'Flag --%s has a non-None default value; therefore, '
        'mark_flag_as_required will pass even if flag is not specified in the '
        'command line!' % flag_name)
  register_validator(
      flag_name,
      lambda value: value is not None,
      message='Flag --{} must have a value other than None.'.format(flag_name),
      flag_values=flag_values)


def mark_flags_as_required(flag_names, flag_values=_flagvalues.FLAGS):
  """Ensures that flags are not None during program execution.

  If your module might be imported by others, and you only wish to make the flag
  required when the module is directly executed, call this method like this:

    if __name__ == '__main__':
      flags.mark_flags_as_required(['flag1', 'flag2', 'flag3'])
      app.run()

  Args:
    flag_names: Sequence[str], names of the flags.
    flag_values: flags.FlagValues, optional FlagValues instance where the flags
        are defined.
  Raises:
    AttributeError: If any of flag name has not already been defined as a flag.
  """
  for flag_name in flag_names:
    mark_flag_as_required(flag_name, flag_values)


def mark_flags_as_mutual_exclusive(flag_names, required=False,
                                   flag_values=_flagvalues.FLAGS):
  """Ensures that only one flag among flag_names is not None.

  Important note: This validator checks if flag values are None, and it does not
  distinguish between default and explicit values. Therefore, this validator
  does not make sense when applied to flags with default values other than None,
  including other false values (e.g. False, 0, '', []). That includes multi
  flags with a default value of [] instead of None.

  Args:
    flag_names: [str], names of the flags.
    required: bool. If true, exactly one of the flags must have a value other
        than None. Otherwise, at most one of the flags can have a value other
        than None, and it is valid for all of the flags to be None.
    flag_values: flags.FlagValues, optional FlagValues instance where the flags
        are defined.
  """
  for flag_name in flag_names:
    if flag_values[flag_name].default is not None:
      warnings.warn(
          'Flag --{} has a non-None default value. That does not make sense '
          'with mark_flags_as_mutual_exclusive, which checks whether the '
          'listed flags have a value other than None.'.format(flag_name))

  def validate_mutual_exclusion(flags_dict):
    flag_count = sum(1 for val in flags_dict.values() if val is not None)
    if flag_count == 1 or (not required and flag_count == 0):
      return True
    raise _exceptions.ValidationError(
        '{} one of ({}) must have a value other than None.'.format(
            'Exactly' if required else 'At most', ', '.join(flag_names)))

  register_multi_flags_validator(
      flag_names, validate_mutual_exclusion, flag_values=flag_values)


def mark_bool_flags_as_mutual_exclusive(flag_names, required=False,
                                        flag_values=_flagvalues.FLAGS):
  """Ensures that only one flag among flag_names is True.

  Args:
    flag_names: [str], names of the flags.
    required: bool. If true, exactly one flag must be True. Otherwise, at most
        one flag can be True, and it is valid for all flags to be False.
    flag_values: flags.FlagValues, optional FlagValues instance where the flags
        are defined.
  """
  for flag_name in flag_names:
    if not flag_values[flag_name].boolean:
      raise _exceptions.ValidationError(
          'Flag --{} is not Boolean, which is required for flags used in '
          'mark_bool_flags_as_mutual_exclusive.'.format(flag_name))

  def validate_boolean_mutual_exclusion(flags_dict):
    flag_count = sum(bool(val) for val in flags_dict.values())
    if flag_count == 1 or (not required and flag_count == 0):
      return True
    raise _exceptions.ValidationError(
        '{} one of ({}) must be True.'.format(
            'Exactly' if required else 'At most', ', '.join(flag_names)))

  register_multi_flags_validator(
      flag_names, validate_boolean_mutual_exclusion, flag_values=flag_values)


def _add_validator(fv, validator_instance):
  """Register new flags validator to be checked.

  Args:
    fv: flags.FlagValues, the FlagValues instance to add the validator.
    validator_instance: validators.Validator, the validator to add.
  Raises:
    KeyError: Raised when validators work with a non-existing flag.
  """
  for flag_name in validator_instance.get_flags_names():
    fv[flag_name].validators.append(validator_instance)
