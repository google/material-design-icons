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
"""This modules contains flags DEFINE functions.

Do NOT import this module directly. Import the flags package and use the
aliases defined at the package level instead.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import types

from absl.flags import _argument_parser
from absl.flags import _exceptions
from absl.flags import _flag
from absl.flags import _flagvalues
from absl.flags import _helpers
from absl.flags import _validators

# pylint: disable=unused-import
try:
  from typing import Text, List, Any
except ImportError:
  pass

try:
  import enum
except ImportError:
  pass
# pylint: enable=unused-import

_helpers.disclaim_module_ids.add(id(sys.modules[__name__]))


def _register_bounds_validator_if_needed(parser, name, flag_values):
  """Enforces lower and upper bounds for numeric flags.

  Args:
    parser: NumericParser (either FloatParser or IntegerParser), provides lower
      and upper bounds, and help text to display.
    name: str, name of the flag
    flag_values: FlagValues.
  """
  if parser.lower_bound is not None or parser.upper_bound is not None:

    def checker(value):
      if value is not None and parser.is_outside_bounds(value):
        message = '%s is not %s' % (value, parser.syntactic_help)
        raise _exceptions.ValidationError(message)
      return True

    _validators.register_validator(name, checker, flag_values=flag_values)


def DEFINE(  # pylint: disable=invalid-name
    parser,
    name,
    default,
    help,  # pylint: disable=redefined-builtin
    flag_values=_flagvalues.FLAGS,
    serializer=None,
    module_name=None,
    required=False,
    **args):
  """Registers a generic Flag object.

  NOTE: in the docstrings of all DEFINE* functions, "registers" is short
  for "creates a new flag and registers it".

  Auxiliary function: clients should use the specialized DEFINE_<type>
  function instead.

  Args:
    parser: ArgumentParser, used to parse the flag arguments.
    name: str, the flag name.
    default: The default value of the flag.
    help: str, the help message.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    serializer: ArgumentSerializer, the flag serializer instance.
    module_name: str, the name of the Python module declaring this flag. If not
      provided, it will be computed using the stack trace of this call.
    required: bool, is this a required flag. This must be used as a keyword
      argument.
    **args: dict, the extra keyword args that are passed to Flag __init__.

  Returns:
    a handle to defined flag.
  """
  return DEFINE_flag(
      _flag.Flag(parser, serializer, name, default, help, **args), flag_values,
      module_name, required)


def DEFINE_flag(  # pylint: disable=invalid-name
    flag,
    flag_values=_flagvalues.FLAGS,
    module_name=None,
    required=False):
  """Registers a 'Flag' object with a 'FlagValues' object.

  By default, the global FLAGS 'FlagValue' object is used.

  Typical users will use one of the more specialized DEFINE_xxx
  functions, such as DEFINE_string or DEFINE_integer.  But developers
  who need to create Flag objects themselves should use this function
  to register their flags.

  Args:
    flag: Flag, a flag that is key to the module.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    module_name: str, the name of the Python module declaring this flag. If not
      provided, it will be computed using the stack trace of this call.
    required: bool, is this a required flag. This must be used as a keyword
      argument.

  Returns:
    a handle to defined flag.
  """
  if required and flag.default is not None:
    raise ValueError('Required flag --%s cannot have a non-None default' %
                     flag.name)
  # Copying the reference to flag_values prevents pychecker warnings.
  fv = flag_values
  fv[flag.name] = flag
  # Tell flag_values who's defining the flag.
  if module_name:
    module = sys.modules.get(module_name)
  else:
    module, module_name = _helpers.get_calling_module_object_and_name()
  flag_values.register_flag_by_module(module_name, flag)
  flag_values.register_flag_by_module_id(id(module), flag)
  if required:
    _validators.mark_flag_as_required(flag.name, fv)
  ensure_non_none_value = (flag.default is not None) or required
  return _flagvalues.FlagHolder(
      fv, flag, ensure_non_none_value=ensure_non_none_value)


def _internal_declare_key_flags(flag_names,
                                flag_values=_flagvalues.FLAGS,
                                key_flag_values=None):
  """Declares a flag as key for the calling module.

  Internal function.  User code should call declare_key_flag or
  adopt_module_key_flags instead.

  Args:
    flag_names: [str], a list of strings that are names of already-registered
      Flag objects.
    flag_values: FlagValues, the FlagValues instance with which the flags listed
      in flag_names have registered (the value of the flag_values argument from
      the DEFINE_* calls that defined those flags). This should almost never
      need to be overridden.
    key_flag_values: FlagValues, the FlagValues instance that (among possibly
      many other things) keeps track of the key flags for each module. Default
      None means "same as flag_values".  This should almost never need to be
      overridden.

  Raises:
    UnrecognizedFlagError: Raised when the flag is not defined.
  """
  key_flag_values = key_flag_values or flag_values

  module = _helpers.get_calling_module()

  for flag_name in flag_names:
    flag = flag_values[flag_name]
    key_flag_values.register_key_flag_for_module(module, flag)


def declare_key_flag(flag_name, flag_values=_flagvalues.FLAGS):
  """Declares one flag as key to the current module.

  Key flags are flags that are deemed really important for a module.
  They are important when listing help messages; e.g., if the
  --helpshort command-line flag is used, then only the key flags of the
  main module are listed (instead of all flags, as in the case of
  --helpfull).

  Sample usage:

    flags.declare_key_flag('flag_1')

  Args:
    flag_name: str, the name of an already declared flag. (Redeclaring flags as
      key, including flags implicitly key because they were declared in this
      module, is a no-op.)
    flag_values: FlagValues, the FlagValues instance in which the flag will be
      declared as a key flag. This should almost never need to be overridden.

  Raises:
    ValueError: Raised if flag_name not defined as a Python flag.
  """
  if flag_name in _helpers.SPECIAL_FLAGS:
    # Take care of the special flags, e.g., --flagfile, --undefok.
    # These flags are defined in SPECIAL_FLAGS, and are treated
    # specially during flag parsing, taking precedence over the
    # user-defined flags.
    _internal_declare_key_flags([flag_name],
                                flag_values=_helpers.SPECIAL_FLAGS,
                                key_flag_values=flag_values)
    return
  try:
    _internal_declare_key_flags([flag_name], flag_values=flag_values)
  except KeyError:
    raise ValueError('Flag --%s is undefined. To set a flag as a key flag '
                     'first define it in Python.' % flag_name)


def adopt_module_key_flags(module, flag_values=_flagvalues.FLAGS):
  """Declares that all flags key to a module are key to the current module.

  Args:
    module: module, the module object from which all key flags will be declared
      as key flags to the current module.
    flag_values: FlagValues, the FlagValues instance in which the flags will be
      declared as key flags. This should almost never need to be overridden.

  Raises:
    Error: Raised when given an argument that is a module name (a string),
        instead of a module object.
  """
  if not isinstance(module, types.ModuleType):
    raise _exceptions.Error('Expected a module object, not %r.' % (module,))
  _internal_declare_key_flags(
      [f.name for f in flag_values.get_key_flags_for_module(module.__name__)],
      flag_values=flag_values)
  # If module is this flag module, take _helpers.SPECIAL_FLAGS into account.
  if module == _helpers.FLAGS_MODULE:
    _internal_declare_key_flags(
        # As we associate flags with get_calling_module_object_and_name(), the
        # special flags defined in this module are incorrectly registered with
        # a different module.  So, we can't use get_key_flags_for_module.
        # Instead, we take all flags from _helpers.SPECIAL_FLAGS (a private
        # FlagValues, where no other module should register flags).
        [_helpers.SPECIAL_FLAGS[name].name for name in _helpers.SPECIAL_FLAGS],
        flag_values=_helpers.SPECIAL_FLAGS,
        key_flag_values=flag_values)


def disclaim_key_flags():
  """Declares that the current module will not define any more key flags.

  Normally, the module that calls the DEFINE_xxx functions claims the
  flag to be its key flag.  This is undesirable for modules that
  define additional DEFINE_yyy functions with its own flag parsers and
  serializers, since that module will accidentally claim flags defined
  by DEFINE_yyy as its key flags.  After calling this function, the
  module disclaims flag definitions thereafter, so the key flags will
  be correctly attributed to the caller of DEFINE_yyy.

  After calling this function, the module will not be able to define
  any more flags.  This function will affect all FlagValues objects.
  """
  globals_for_caller = sys._getframe(1).f_globals  # pylint: disable=protected-access
  module, _ = _helpers.get_module_object_and_name(globals_for_caller)
  _helpers.disclaim_module_ids.add(id(module))


def DEFINE_string(  # pylint: disable=invalid-name,redefined-builtin
    name,
    default,
    help,
    flag_values=_flagvalues.FLAGS,
    required=False,
    **args):
  """Registers a flag whose value can be any string."""
  parser = _argument_parser.ArgumentParser()
  serializer = _argument_parser.ArgumentSerializer()
  return DEFINE(
      parser,
      name,
      default,
      help,
      flag_values,
      serializer,
      required=required,
      **args)


def DEFINE_boolean(  # pylint: disable=invalid-name,redefined-builtin
    name,
    default,
    help,
    flag_values=_flagvalues.FLAGS,
    module_name=None,
    required=False,
    **args):
  """Registers a boolean flag.

  Such a boolean flag does not take an argument.  If a user wants to
  specify a false value explicitly, the long option beginning with 'no'
  must be used: i.e. --noflag

  This flag will have a value of None, True or False.  None is possible
  if default=None and the user does not specify the flag on the command
  line.

  Args:
    name: str, the flag name.
    default: bool|str|None, the default value of the flag.
    help: str, the help message.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    module_name: str, the name of the Python module declaring this flag. If not
      provided, it will be computed using the stack trace of this call.
    required: bool, is this a required flag. This must be used as a keyword
      argument.
    **args: dict, the extra keyword args that are passed to Flag __init__.

  Returns:
    a handle to defined flag.
  """
  return DEFINE_flag(
      _flag.BooleanFlag(name, default, help, **args), flag_values, module_name,
      required)


def DEFINE_float(  # pylint: disable=invalid-name,redefined-builtin
    name,
    default,
    help,
    lower_bound=None,
    upper_bound=None,
    flag_values=_flagvalues.FLAGS,
    required=False,
    **args):
  """Registers a flag whose value must be a float.

  If lower_bound or upper_bound are set, then this flag must be
  within the given range.

  Args:
    name: str, the flag name.
    default: float|str|None, the default value of the flag.
    help: str, the help message.
    lower_bound: float, min value of the flag.
    upper_bound: float, max value of the flag.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    required: bool, is this a required flag. This must be used as a keyword
      argument.
    **args: dict, the extra keyword args that are passed to DEFINE.

  Returns:
    a handle to defined flag.
  """
  parser = _argument_parser.FloatParser(lower_bound, upper_bound)
  serializer = _argument_parser.ArgumentSerializer()
  result = DEFINE(
      parser,
      name,
      default,
      help,
      flag_values,
      serializer,
      required=required,
      **args)
  _register_bounds_validator_if_needed(parser, name, flag_values=flag_values)
  return result


def DEFINE_integer(  # pylint: disable=invalid-name,redefined-builtin
    name,
    default,
    help,
    lower_bound=None,
    upper_bound=None,
    flag_values=_flagvalues.FLAGS,
    required=False,
    **args):
  """Registers a flag whose value must be an integer.

  If lower_bound, or upper_bound are set, then this flag must be
  within the given range.

  Args:
    name: str, the flag name.
    default: int|str|None, the default value of the flag.
    help: str, the help message.
    lower_bound: int, min value of the flag.
    upper_bound: int, max value of the flag.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    required: bool, is this a required flag. This must be used as a keyword
      argument.
    **args: dict, the extra keyword args that are passed to DEFINE.

  Returns:
    a handle to defined flag.
  """
  parser = _argument_parser.IntegerParser(lower_bound, upper_bound)
  serializer = _argument_parser.ArgumentSerializer()
  result = DEFINE(
      parser,
      name,
      default,
      help,
      flag_values,
      serializer,
      required=required,
      **args)
  _register_bounds_validator_if_needed(parser, name, flag_values=flag_values)
  return result


def DEFINE_enum(  # pylint: disable=invalid-name,redefined-builtin
    name,
    default,
    enum_values,
    help,
    flag_values=_flagvalues.FLAGS,
    module_name=None,
    required=False,
    **args):
  """Registers a flag whose value can be any string from enum_values.

  Instead of a string enum, prefer `DEFINE_enum_class`, which allows
  defining enums from an `enum.Enum` class.

  Args:
    name: str, the flag name.
    default: str|None, the default value of the flag.
    enum_values: [str], a non-empty list of strings with the possible values for
      the flag.
    help: str, the help message.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    module_name: str, the name of the Python module declaring this flag. If not
      provided, it will be computed using the stack trace of this call.
    required: bool, is this a required flag. This must be used as a keyword
      argument.
    **args: dict, the extra keyword args that are passed to Flag __init__.

  Returns:
    a handle to defined flag.
  """
  return DEFINE_flag(
      _flag.EnumFlag(name, default, help, enum_values, **args), flag_values,
      module_name, required)


def DEFINE_enum_class(  # pylint: disable=invalid-name,redefined-builtin
    name,
    default,
    enum_class,
    help,
    flag_values=_flagvalues.FLAGS,
    module_name=None,
    case_sensitive=False,
    required=False,
    **args):
  """Registers a flag whose value can be the name of enum members.

  Args:
    name: str, the flag name.
    default: Enum|str|None, the default value of the flag.
    enum_class: class, the Enum class with all the possible values for the flag.
    help: str, the help message.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    module_name: str, the name of the Python module declaring this flag. If not
      provided, it will be computed using the stack trace of this call.
    case_sensitive: bool, whether to map strings to members of the enum_class
      without considering case.
    required: bool, is this a required flag. This must be used as a keyword
      argument.
    **args: dict, the extra keyword args that are passed to Flag __init__.

  Returns:
    a handle to defined flag.
  """
  return DEFINE_flag(
      _flag.EnumClassFlag(
          name,
          default,
          help,
          enum_class,
          case_sensitive=case_sensitive,
          **args), flag_values, module_name, required)


def DEFINE_list(  # pylint: disable=invalid-name,redefined-builtin
    name,
    default,
    help,
    flag_values=_flagvalues.FLAGS,
    required=False,
    **args):
  """Registers a flag whose value is a comma-separated list of strings.

  The flag value is parsed with a CSV parser.

  Args:
    name: str, the flag name.
    default: list|str|None, the default value of the flag.
    help: str, the help message.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    required: bool, is this a required flag. This must be used as a keyword
      argument.
    **args: Dictionary with extra keyword args that are passed to the Flag
      __init__.

  Returns:
    a handle to defined flag.
  """
  parser = _argument_parser.ListParser()
  serializer = _argument_parser.CsvListSerializer(',')
  return DEFINE(
      parser,
      name,
      default,
      help,
      flag_values,
      serializer,
      required=required,
      **args)


def DEFINE_spaceseplist(  # pylint: disable=invalid-name,redefined-builtin
    name,
    default,
    help,
    comma_compat=False,
    flag_values=_flagvalues.FLAGS,
    required=False,
    **args):
  """Registers a flag whose value is a whitespace-separated list of strings.

  Any whitespace can be used as a separator.

  Args:
    name: str, the flag name.
    default: list|str|None, the default value of the flag.
    help: str, the help message.
    comma_compat: bool - Whether to support comma as an additional separator. If
      false then only whitespace is supported.  This is intended only for
      backwards compatibility with flags that used to be comma-separated.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    required: bool, is this a required flag. This must be used as a keyword
      argument.
    **args: Dictionary with extra keyword args that are passed to the Flag
      __init__.

  Returns:
    a handle to defined flag.
  """
  parser = _argument_parser.WhitespaceSeparatedListParser(
      comma_compat=comma_compat)
  serializer = _argument_parser.ListSerializer(' ')
  return DEFINE(
      parser,
      name,
      default,
      help,
      flag_values,
      serializer,
      required=required,
      **args)


def DEFINE_multi(  # pylint: disable=invalid-name,redefined-builtin
    parser,
    serializer,
    name,
    default,
    help,
    flag_values=_flagvalues.FLAGS,
    module_name=None,
    required=False,
    **args):
  """Registers a generic MultiFlag that parses its args with a given parser.

  Auxiliary function.  Normal users should NOT use it directly.

  Developers who need to create their own 'Parser' classes for options
  which can appear multiple times can call this module function to
  register their flags.

  Args:
    parser: ArgumentParser, used to parse the flag arguments.
    serializer: ArgumentSerializer, the flag serializer instance.
    name: str, the flag name.
    default: Union[Iterable[T], Text, None], the default value of the flag. If
      the value is text, it will be parsed as if it was provided from the
      command line. If the value is a non-string iterable, it will be iterated
      over to create a shallow copy of the values. If it is None, it is left
      as-is.
    help: str, the help message.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    module_name: A string, the name of the Python module declaring this flag. If
      not provided, it will be computed using the stack trace of this call.
    required: bool, is this a required flag. This must be used as a keyword
      argument.
    **args: Dictionary with extra keyword args that are passed to the Flag
      __init__.

  Returns:
    a handle to defined flag.
  """
  return DEFINE_flag(
      _flag.MultiFlag(parser, serializer, name, default, help, **args),
      flag_values, module_name, required)


def DEFINE_multi_string(  # pylint: disable=invalid-name,redefined-builtin
    name,
    default,
    help,
    flag_values=_flagvalues.FLAGS,
    required=False,
    **args):
  """Registers a flag whose value can be a list of any strings.

  Use the flag on the command line multiple times to place multiple
  string values into the list.  The 'default' may be a single string
  (which will be converted into a single-element list) or a list of
  strings.


  Args:
    name: str, the flag name.
    default: Union[Iterable[Text], Text, None], the default value of the flag;
      see `DEFINE_multi`.
    help: str, the help message.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    required: bool, is this a required flag. This must be used as a keyword
      argument.
    **args: Dictionary with extra keyword args that are passed to the Flag
      __init__.

  Returns:
    a handle to defined flag.
  """
  parser = _argument_parser.ArgumentParser()
  serializer = _argument_parser.ArgumentSerializer()
  return DEFINE_multi(
      parser,
      serializer,
      name,
      default,
      help,
      flag_values,
      required=required,
      **args)


def DEFINE_multi_integer(  # pylint: disable=invalid-name,redefined-builtin
    name,
    default,
    help,
    lower_bound=None,
    upper_bound=None,
    flag_values=_flagvalues.FLAGS,
    required=False,
    **args):
  """Registers a flag whose value can be a list of arbitrary integers.

  Use the flag on the command line multiple times to place multiple
  integer values into the list.  The 'default' may be a single integer
  (which will be converted into a single-element list) or a list of
  integers.

  Args:
    name: str, the flag name.
    default: Union[Iterable[int], Text, None], the default value of the flag;
      see `DEFINE_multi`.
    help: str, the help message.
    lower_bound: int, min values of the flag.
    upper_bound: int, max values of the flag.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    required: bool, is this a required flag. This must be used as a keyword
      argument.
    **args: Dictionary with extra keyword args that are passed to the Flag
      __init__.

  Returns:
    a handle to defined flag.
  """
  parser = _argument_parser.IntegerParser(lower_bound, upper_bound)
  serializer = _argument_parser.ArgumentSerializer()
  return DEFINE_multi(
      parser,
      serializer,
      name,
      default,
      help,
      flag_values,
      required=required,
      **args)


def DEFINE_multi_float(  # pylint: disable=invalid-name,redefined-builtin
    name,
    default,
    help,
    lower_bound=None,
    upper_bound=None,
    flag_values=_flagvalues.FLAGS,
    required=False,
    **args):
  """Registers a flag whose value can be a list of arbitrary floats.

  Use the flag on the command line multiple times to place multiple
  float values into the list.  The 'default' may be a single float
  (which will be converted into a single-element list) or a list of
  floats.

  Args:
    name: str, the flag name.
    default: Union[Iterable[float], Text, None], the default value of the flag;
      see `DEFINE_multi`.
    help: str, the help message.
    lower_bound: float, min values of the flag.
    upper_bound: float, max values of the flag.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    required: bool, is this a required flag. This must be used as a keyword
      argument.
    **args: Dictionary with extra keyword args that are passed to the Flag
      __init__.

  Returns:
    a handle to defined flag.
  """
  parser = _argument_parser.FloatParser(lower_bound, upper_bound)
  serializer = _argument_parser.ArgumentSerializer()
  return DEFINE_multi(
      parser,
      serializer,
      name,
      default,
      help,
      flag_values,
      required=required,
      **args)


def DEFINE_multi_enum(  # pylint: disable=invalid-name,redefined-builtin
    name,
    default,
    enum_values,
    help,
    flag_values=_flagvalues.FLAGS,
    case_sensitive=True,
    required=False,
    **args):
  """Registers a flag whose value can be a list strings from enum_values.

  Use the flag on the command line multiple times to place multiple
  enum values into the list.  The 'default' may be a single string
  (which will be converted into a single-element list) or a list of
  strings.

  Args:
    name: str, the flag name.
    default: Union[Iterable[Text], Text, None], the default value of the flag;
      see `DEFINE_multi`.
    enum_values: [str], a non-empty list of strings with the possible values for
      the flag.
    help: str, the help message.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    case_sensitive: Whether or not the enum is to be case-sensitive.
    required: bool, is this a required flag. This must be used as a keyword
      argument.
    **args: Dictionary with extra keyword args that are passed to the Flag
      __init__.

  Returns:
    a handle to defined flag.
  """
  parser = _argument_parser.EnumParser(enum_values, case_sensitive)
  serializer = _argument_parser.ArgumentSerializer()
  return DEFINE_multi(
      parser,
      serializer,
      name,
      default,
      help,
      flag_values,
      required=required,
      **args)


def DEFINE_multi_enum_class(  # pylint: disable=invalid-name,redefined-builtin
    name,
    default,
    enum_class,
    help,
    flag_values=_flagvalues.FLAGS,
    module_name=None,
    case_sensitive=False,
    required=False,
    **args):
  """Registers a flag whose value can be a list of enum members.

  Use the flag on the command line multiple times to place multiple
  enum values into the list.

  Args:
    name: str, the flag name.
    default: Union[Iterable[Enum], Iterable[Text], Enum, Text, None], the
      default value of the flag; see `DEFINE_multi`; only differences are
      documented here. If the value is a single Enum, it is treated as a
      single-item list of that Enum value. If it is an iterable, text values
      within the iterable will be converted to the equivalent Enum objects.
    enum_class: class, the Enum class with all the possible values for the flag.
        help: str, the help message.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    module_name: A string, the name of the Python module declaring this flag. If
      not provided, it will be computed using the stack trace of this call.
    case_sensitive: bool, whether to map strings to members of the enum_class
      without considering case.
    required: bool, is this a required flag. This must be used as a keyword
      argument.
    **args: Dictionary with extra keyword args that are passed to the Flag
      __init__.

  Returns:
    a handle to defined flag.
  """
  return DEFINE_flag(
      _flag.MultiEnumClassFlag(
          name, default, help, enum_class, case_sensitive=case_sensitive),
      flag_values,
      module_name,
      required=required,
      **args)


def DEFINE_alias(  # pylint: disable=invalid-name
    name,
    original_name,
    flag_values=_flagvalues.FLAGS,
    module_name=None):
  """Defines an alias flag for an existing one.

  Args:
    name: str, the flag name.
    original_name: str, the original flag name.
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      registered. This should almost never need to be overridden.
    module_name: A string, the name of the module that defines this flag.

  Returns:
    a handle to defined flag.

  Raises:
    flags.FlagError:
      UnrecognizedFlagError: if the referenced flag doesn't exist.
      DuplicateFlagError: if the alias name has been used by some existing flag.
  """
  if original_name not in flag_values:
    raise _exceptions.UnrecognizedFlagError(original_name)
  flag = flag_values[original_name]

  class _FlagAlias(_flag.Flag):
    """Overrides Flag class so alias value is copy of original flag value."""

    def parse(self, argument):
      flag.parse(argument)
      self.present += 1

    def _parse_from_default(self, value):
      # The value was already parsed by the aliased flag, so there is no
      # need to call the parser on it a second time.
      # Additionally, because of how MultiFlag parses and merges values,
      # it isn't possible to delegate to the aliased flag and still get
      # the correct values.
      return value

    @property
    def value(self):
      return flag.value

    @value.setter
    def value(self, value):
      flag.value = value

  help_msg = 'Alias for --%s.' % flag.name
  # If alias_name has been used, flags.DuplicatedFlag will be raised.
  return DEFINE_flag(
      _FlagAlias(
          flag.parser,
          flag.serializer,
          name,
          flag.default,
          help_msg,
          boolean=flag.boolean), flag_values, module_name)
