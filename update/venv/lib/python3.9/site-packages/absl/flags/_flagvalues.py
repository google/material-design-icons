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
"""Defines the FlagValues class - registry of 'Flag' objects.

Do NOT import this module directly. Import the flags package and use the
aliases defined at the package level instead.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import copy
import itertools
import logging
import os
import sys
from xml.dom import minidom

from absl.flags import _exceptions
from absl.flags import _flag
from absl.flags import _helpers
import six

# pylint: disable=unused-import
try:
  import typing
  from typing import Text, Optional
except ImportError:
  typing = None
# pylint: enable=unused-import

# Add flagvalues module to disclaimed module ids.
_helpers.disclaim_module_ids.add(id(sys.modules[__name__]))


class FlagValues(object):
  """Registry of 'Flag' objects.

  A 'FlagValues' can then scan command line arguments, passing flag
  arguments through to the 'Flag' objects that it owns.  It also
  provides easy access to the flag values.  Typically only one
  'FlagValues' object is needed by an application: flags.FLAGS

  This class is heavily overloaded:

  'Flag' objects are registered via __setitem__:
       FLAGS['longname'] = x   # register a new flag

  The .value attribute of the registered 'Flag' objects can be accessed
  as attributes of this 'FlagValues' object, through __getattr__.  Both
  the long and short name of the original 'Flag' objects can be used to
  access its value:
       FLAGS.longname          # parsed flag value
       FLAGS.x                 # parsed flag value (short name)

  Command line arguments are scanned and passed to the registered 'Flag'
  objects through the __call__ method.  Unparsed arguments, including
  argv[0] (e.g. the program name) are returned.
       argv = FLAGS(sys.argv)  # scan command line arguments

  The original registered Flag objects can be retrieved through the use
  of the dictionary-like operator, __getitem__:
       x = FLAGS['longname']   # access the registered Flag object

  The str() operator of a 'FlagValues' object provides help for all of
  the registered 'Flag' objects.
  """

  # A note on collections.abc.Mapping:
  # FlagValues defines __getitem__, __iter__, and __len__. It makes perfect
  # sense to let it be a collections.abc.Mapping class. However, we are not
  # able to do so. The mixin methods, e.g. keys, values, are not uncommon flag
  # names. Those flag values would not be accessible via the FLAGS.xxx form.

  def __init__(self):
    # Since everything in this class is so heavily overloaded, the only
    # way of defining and using fields is to access __dict__ directly.

    # Dictionary: flag name (string) -> Flag object.
    self.__dict__['__flags'] = {}

    # Set: name of hidden flag (string).
    # Holds flags that should not be directly accessible from Python.
    self.__dict__['__hiddenflags'] = set()

    # Dictionary: module name (string) -> list of Flag objects that are defined
    # by that module.
    self.__dict__['__flags_by_module'] = {}
    # Dictionary: module id (int) -> list of Flag objects that are defined by
    # that module.
    self.__dict__['__flags_by_module_id'] = {}
    # Dictionary: module name (string) -> list of Flag objects that are
    # key for that module.
    self.__dict__['__key_flags_by_module'] = {}

    # Bool: True if flags were parsed.
    self.__dict__['__flags_parsed'] = False

    # Bool: True if unparse_flags() was called.
    self.__dict__['__unparse_flags_called'] = False

    # None or Method(name, value) to call from __setattr__ for an unknown flag.
    self.__dict__['__set_unknown'] = None

    # A set of banned flag names. This is to prevent users from accidentally
    # defining a flag that has the same name as a method on this class.
    # Users can still allow defining the flag by passing
    # allow_using_method_names=True in DEFINE_xxx functions.
    self.__dict__['__banned_flag_names'] = frozenset(dir(FlagValues))

    # Bool: Whether to use GNU style scanning.
    self.__dict__['__use_gnu_getopt'] = True

    # Bool: Whether use_gnu_getopt has been explicitly set by the user.
    self.__dict__['__use_gnu_getopt_explicitly_set'] = False

    # Function: Takes a flag name as parameter, returns a tuple
    # (is_retired, type_is_bool).
    self.__dict__['__is_retired_flag_func'] = None

  def set_gnu_getopt(self, gnu_getopt=True):
    """Sets whether or not to use GNU style scanning.

    GNU style allows mixing of flag and non-flag arguments. See
    http://docs.python.org/library/getopt.html#getopt.gnu_getopt

    Args:
      gnu_getopt: bool, whether or not to use GNU style scanning.
    """
    self.__dict__['__use_gnu_getopt'] = gnu_getopt
    self.__dict__['__use_gnu_getopt_explicitly_set'] = True

  def is_gnu_getopt(self):
    return self.__dict__['__use_gnu_getopt']

  def _flags(self):
    return self.__dict__['__flags']

  def flags_by_module_dict(self):
    """Returns the dictionary of module_name -> list of defined flags.

    Returns:
      A dictionary.  Its keys are module names (strings).  Its values
      are lists of Flag objects.
    """
    return self.__dict__['__flags_by_module']

  def flags_by_module_id_dict(self):
    """Returns the dictionary of module_id -> list of defined flags.

    Returns:
      A dictionary.  Its keys are module IDs (ints).  Its values
      are lists of Flag objects.
    """
    return self.__dict__['__flags_by_module_id']

  def key_flags_by_module_dict(self):
    """Returns the dictionary of module_name -> list of key flags.

    Returns:
      A dictionary.  Its keys are module names (strings).  Its values
      are lists of Flag objects.
    """
    return self.__dict__['__key_flags_by_module']

  def register_flag_by_module(self, module_name, flag):
    """Records the module that defines a specific flag.

    We keep track of which flag is defined by which module so that we
    can later sort the flags by module.

    Args:
      module_name: str, the name of a Python module.
      flag: Flag, the Flag instance that is key to the module.
    """
    flags_by_module = self.flags_by_module_dict()
    flags_by_module.setdefault(module_name, []).append(flag)

  def register_flag_by_module_id(self, module_id, flag):
    """Records the module that defines a specific flag.

    Args:
      module_id: int, the ID of the Python module.
      flag: Flag, the Flag instance that is key to the module.
    """
    flags_by_module_id = self.flags_by_module_id_dict()
    flags_by_module_id.setdefault(module_id, []).append(flag)

  def register_key_flag_for_module(self, module_name, flag):
    """Specifies that a flag is a key flag for a module.

    Args:
      module_name: str, the name of a Python module.
      flag: Flag, the Flag instance that is key to the module.
    """
    key_flags_by_module = self.key_flags_by_module_dict()
    # The list of key flags for the module named module_name.
    key_flags = key_flags_by_module.setdefault(module_name, [])
    # Add flag, but avoid duplicates.
    if flag not in key_flags:
      key_flags.append(flag)

  def _flag_is_registered(self, flag_obj):
    """Checks whether a Flag object is registered under long name or short name.

    Args:
      flag_obj: Flag, the Flag instance to check for.

    Returns:
      bool, True iff flag_obj is registered under long name or short name.
    """
    flag_dict = self._flags()
    # Check whether flag_obj is registered under its long name.
    name = flag_obj.name
    if flag_dict.get(name, None) == flag_obj:
      return True
    # Check whether flag_obj is registered under its short name.
    short_name = flag_obj.short_name
    if (short_name is not None and flag_dict.get(short_name, None) == flag_obj):
      return True
    return False

  def _cleanup_unregistered_flag_from_module_dicts(self, flag_obj):
    """Cleans up unregistered flags from all module -> [flags] dictionaries.

    If flag_obj is registered under either its long name or short name, it
    won't be removed from the dictionaries.

    Args:
      flag_obj: Flag, the Flag instance to clean up for.
    """
    if self._flag_is_registered(flag_obj):
      return
    for flags_by_module_dict in (self.flags_by_module_dict(),
                                 self.flags_by_module_id_dict(),
                                 self.key_flags_by_module_dict()):
      for flags_in_module in six.itervalues(flags_by_module_dict):
        # While (as opposed to if) takes care of multiple occurrences of a
        # flag in the list for the same module.
        while flag_obj in flags_in_module:
          flags_in_module.remove(flag_obj)

  def get_flags_for_module(self, module):
    """Returns the list of flags defined by a module.

    Args:
      module: module|str, the module to get flags from.

    Returns:
      [Flag], a new list of Flag instances.  Caller may update this list as
      desired: none of those changes will affect the internals of this
      FlagValue instance.
    """
    if not isinstance(module, str):
      module = module.__name__
    if module == '__main__':
      module = sys.argv[0]

    return list(self.flags_by_module_dict().get(module, []))

  def get_key_flags_for_module(self, module):
    """Returns the list of key flags for a module.

    Args:
      module: module|str, the module to get key flags from.

    Returns:
      [Flag], a new list of Flag instances.  Caller may update this list as
      desired: none of those changes will affect the internals of this
      FlagValue instance.
    """
    if not isinstance(module, str):
      module = module.__name__
    if module == '__main__':
      module = sys.argv[0]

    # Any flag is a key flag for the module that defined it.  NOTE:
    # key_flags is a fresh list: we can update it without affecting the
    # internals of this FlagValues object.
    key_flags = self.get_flags_for_module(module)

    # Take into account flags explicitly declared as key for a module.
    for flag in self.key_flags_by_module_dict().get(module, []):
      if flag not in key_flags:
        key_flags.append(flag)
    return key_flags

  def find_module_defining_flag(self, flagname, default=None):
    """Return the name of the module defining this flag, or default.

    Args:
      flagname: str, name of the flag to lookup.
      default: Value to return if flagname is not defined. Defaults to None.

    Returns:
      The name of the module which registered the flag with this name.
      If no such module exists (i.e. no flag with this name exists),
      we return default.
    """
    registered_flag = self._flags().get(flagname)
    if registered_flag is None:
      return default
    for module, flags in six.iteritems(self.flags_by_module_dict()):
      for flag in flags:
        # It must compare the flag with the one in _flags. This is because a
        # flag might be overridden only for its long name (or short name),
        # and only its short name (or long name) is considered registered.
        if (flag.name == registered_flag.name and
            flag.short_name == registered_flag.short_name):
          return module
    return default

  def find_module_id_defining_flag(self, flagname, default=None):
    """Return the ID of the module defining this flag, or default.

    Args:
      flagname: str, name of the flag to lookup.
      default: Value to return if flagname is not defined. Defaults to None.

    Returns:
      The ID of the module which registered the flag with this name.
      If no such module exists (i.e. no flag with this name exists),
      we return default.
    """
    registered_flag = self._flags().get(flagname)
    if registered_flag is None:
      return default
    for module_id, flags in six.iteritems(self.flags_by_module_id_dict()):
      for flag in flags:
        # It must compare the flag with the one in _flags. This is because a
        # flag might be overridden only for its long name (or short name),
        # and only its short name (or long name) is considered registered.
        if (flag.name == registered_flag.name and
            flag.short_name == registered_flag.short_name):
          return module_id
    return default

  def _register_unknown_flag_setter(self, setter):
    """Allow set default values for undefined flags.

    Args:
      setter: Method(name, value) to call to __setattr__ an unknown flag. Must
        raise NameError or ValueError for invalid name/value.
    """
    self.__dict__['__set_unknown'] = setter

  def _set_unknown_flag(self, name, value):
    """Returns value if setting flag |name| to |value| returned True.

    Args:
      name: str, name of the flag to set.
      value: Value to set.

    Returns:
      Flag value on successful call.

    Raises:
      UnrecognizedFlagError
      IllegalFlagValueError
    """
    setter = self.__dict__['__set_unknown']
    if setter:
      try:
        setter(name, value)
        return value
      except (TypeError, ValueError):  # Flag value is not valid.
        raise _exceptions.IllegalFlagValueError(
            '"{1}" is not valid for --{0}'.format(name, value))
      except NameError:  # Flag name is not valid.
        pass
    raise _exceptions.UnrecognizedFlagError(name, value)

  def append_flag_values(self, flag_values):
    """Appends flags registered in another FlagValues instance.

    Args:
      flag_values: FlagValues, the FlagValues instance from which to copy flags.
    """
    for flag_name, flag in six.iteritems(flag_values._flags()):  # pylint: disable=protected-access
      # Each flags with short_name appears here twice (once under its
      # normal name, and again with its short name).  To prevent
      # problems (DuplicateFlagError) with double flag registration, we
      # perform a check to make sure that the entry we're looking at is
      # for its normal name.
      if flag_name == flag.name:
        try:
          self[flag_name] = flag
        except _exceptions.DuplicateFlagError:
          raise _exceptions.DuplicateFlagError.from_flag(
              flag_name, self, other_flag_values=flag_values)

  def remove_flag_values(self, flag_values):
    """Remove flags that were previously appended from another FlagValues.

    Args:
      flag_values: FlagValues, the FlagValues instance containing flags to
        remove.
    """
    for flag_name in flag_values:
      self.__delattr__(flag_name)

  def __setitem__(self, name, flag):
    """Registers a new flag variable."""
    fl = self._flags()
    if not isinstance(flag, _flag.Flag):
      raise _exceptions.IllegalFlagValueError(flag)
    if str is bytes and isinstance(name, unicode):
      # When using Python 2 with unicode_literals, allow it but encode it
      # into the bytes type we require.
      name = name.encode('utf-8')
    if not isinstance(name, type('')):
      raise _exceptions.Error('Flag name must be a string')
    if not name:
      raise _exceptions.Error('Flag name cannot be empty')
    if ' ' in name:
      raise _exceptions.Error('Flag name cannot contain a space')
    self._check_method_name_conflicts(name, flag)
    if name in fl and not flag.allow_override and not fl[name].allow_override:
      module, module_name = _helpers.get_calling_module_object_and_name()
      if (self.find_module_defining_flag(name) == module_name and
          id(module) != self.find_module_id_defining_flag(name)):
        # If the flag has already been defined by a module with the same name,
        # but a different ID, we can stop here because it indicates that the
        # module is simply being imported a subsequent time.
        return
      raise _exceptions.DuplicateFlagError.from_flag(name, self)
    short_name = flag.short_name
    # If a new flag overrides an old one, we need to cleanup the old flag's
    # modules if it's not registered.
    flags_to_cleanup = set()
    if short_name is not None:
      if (short_name in fl and not flag.allow_override and
          not fl[short_name].allow_override):
        raise _exceptions.DuplicateFlagError.from_flag(short_name, self)
      if short_name in fl and fl[short_name] != flag:
        flags_to_cleanup.add(fl[short_name])
      fl[short_name] = flag
    if (name not in fl  # new flag
        or fl[name].using_default_value or not flag.using_default_value):
      if name in fl and fl[name] != flag:
        flags_to_cleanup.add(fl[name])
      fl[name] = flag
    for f in flags_to_cleanup:
      self._cleanup_unregistered_flag_from_module_dicts(f)

  def __dir__(self):
    """Returns list of names of all defined flags.

    Useful for TAB-completion in ipython.

    Returns:
      [str], a list of names of all defined flags.
    """
    return sorted(self.__dict__['__flags'])

  def __getitem__(self, name):
    """Returns the Flag object for the flag --name."""
    return self._flags()[name]

  def _hide_flag(self, name):
    """Marks the flag --name as hidden."""
    self.__dict__['__hiddenflags'].add(name)

  def __getattr__(self, name):
    """Retrieves the 'value' attribute of the flag --name."""
    fl = self._flags()
    if name not in fl:
      raise AttributeError(name)
    if name in self.__dict__['__hiddenflags']:
      raise AttributeError(name)

    if self.__dict__['__flags_parsed'] or fl[name].present:
      return fl[name].value
    else:
      error_message = ('Trying to access flag --%s before flags were parsed.' %
                       name)
      if six.PY2:
        # In Python 2, hasattr returns False if getattr raises any exception.
        # That means if someone calls hasattr(FLAGS, 'flag'), it returns False
        # instead of raises UnparsedFlagAccessError even if --flag is already
        # defined. To make the error more visible, the best we can do is to
        # log an error message before raising the exception.
        # Don't log a full stacktrace here since that makes other callers
        # get too much noise.
        logging.error(error_message)
      raise _exceptions.UnparsedFlagAccessError(error_message)

  def __setattr__(self, name, value):
    """Sets the 'value' attribute of the flag --name."""
    self._set_attributes(**{name: value})
    return value

  def _set_attributes(self, **attributes):
    """Sets multiple flag values together, triggers validators afterwards."""
    fl = self._flags()
    known_flags = set()
    for name, value in six.iteritems(attributes):
      if name in self.__dict__['__hiddenflags']:
        raise AttributeError(name)
      if name in fl:
        fl[name].value = value
        known_flags.add(name)
      else:
        self._set_unknown_flag(name, value)
    for name in known_flags:
      self._assert_validators(fl[name].validators)
      fl[name].using_default_value = False

  def validate_all_flags(self):
    """Verifies whether all flags pass validation.

    Raises:
      AttributeError: Raised if validators work with a non-existing flag.
      IllegalFlagValueError: Raised if validation fails for at least one
          validator.
    """
    all_validators = set()
    for flag in six.itervalues(self._flags()):
      all_validators.update(flag.validators)
    self._assert_validators(all_validators)

  def _assert_validators(self, validators):
    """Asserts if all validators in the list are satisfied.

    It asserts validators in the order they were created.

    Args:
      validators: Iterable(validators.Validator), validators to be verified.

    Raises:
      AttributeError: Raised if validators work with a non-existing flag.
      IllegalFlagValueError: Raised if validation fails for at least one
          validator.
    """
    for validator in sorted(
        validators, key=lambda validator: validator.insertion_index):
      try:
        validator.verify(self)
      except _exceptions.ValidationError as e:
        message = validator.print_flags_with_values(self)
        raise _exceptions.IllegalFlagValueError('%s: %s' % (message, str(e)))

  def __delattr__(self, flag_name):
    """Deletes a previously-defined flag from a flag object.

    This method makes sure we can delete a flag by using

      del FLAGS.<flag_name>

    E.g.,

      flags.DEFINE_integer('foo', 1, 'Integer flag.')
      del flags.FLAGS.foo

    If a flag is also registered by its the other name (long name or short
    name), the other name won't be deleted.

    Args:
      flag_name: str, the name of the flag to be deleted.

    Raises:
      AttributeError: Raised when there is no registered flag named flag_name.
    """
    fl = self._flags()
    if flag_name not in fl:
      raise AttributeError(flag_name)

    flag_obj = fl[flag_name]
    del fl[flag_name]

    self._cleanup_unregistered_flag_from_module_dicts(flag_obj)

  def set_default(self, name, value):
    """Changes the default value of the named flag object.

    The flag's current value is also updated if the flag is currently using
    the default value, i.e. not specified in the command line, and not set
    by FLAGS.name = value.

    Args:
      name: str, the name of the flag to modify.
      value: The new default value.

    Raises:
      UnrecognizedFlagError: Raised when there is no registered flag named name.
      IllegalFlagValueError: Raised when value is not valid.
    """
    fl = self._flags()
    if name not in fl:
      self._set_unknown_flag(name, value)
      return
    fl[name]._set_default(value)  # pylint: disable=protected-access
    self._assert_validators(fl[name].validators)

  def __contains__(self, name):
    """Returns True if name is a value (flag) in the dict."""
    return name in self._flags()

  def __len__(self):
    return len(self.__dict__['__flags'])

  def __iter__(self):
    return iter(self._flags())

  def __call__(self, argv, known_only=False):
    """Parses flags from argv; stores parsed flags into this FlagValues object.

    All unparsed arguments are returned.

    Args:
       argv: a tuple/list of strings.
       known_only: bool, if True, parse and remove known flags; return the rest
         untouched. Unknown flags specified by --undefok are not returned.

    Returns:
       The list of arguments not parsed as options, including argv[0].

    Raises:
       Error: Raised on any parsing error.
       TypeError: Raised on passing wrong type of arguments.
       ValueError: Raised on flag value parsing error.
    """
    if _helpers.is_bytes_or_string(argv):
      raise TypeError(
          'argv should be a tuple/list of strings, not bytes or string.')
    if not argv:
      raise ValueError(
          'argv cannot be an empty list, and must contain the program name as '
          'the first element.')

    # This pre parses the argv list for --flagfile=<> options.
    program_name = argv[0]
    args = self.read_flags_from_files(argv[1:], force_gnu=False)

    # Parse the arguments.
    unknown_flags, unparsed_args = self._parse_args(args, known_only)

    # Handle unknown flags by raising UnrecognizedFlagError.
    # Note some users depend on us raising this particular error.
    for name, value in unknown_flags:
      suggestions = _helpers.get_flag_suggestions(name, list(self))
      raise _exceptions.UnrecognizedFlagError(
          name, value, suggestions=suggestions)

    self.mark_as_parsed()
    self.validate_all_flags()
    return [program_name] + unparsed_args

  def __getstate__(self):
    raise TypeError("can't pickle FlagValues")

  def __copy__(self):
    raise TypeError('FlagValues does not support shallow copies. '
                    'Use absl.testing.flagsaver or copy.deepcopy instead.')

  def __deepcopy__(self, memo):
    result = object.__new__(type(self))
    result.__dict__.update(copy.deepcopy(self.__dict__, memo))
    return result

  def _set_is_retired_flag_func(self, is_retired_flag_func):
    """Sets a function for checking retired flags.

    Do not use it. This is a private absl API used to check retired flags
    registered by the absl C++ flags library.

    Args:
      is_retired_flag_func: Callable(str) -> (bool, bool), a function takes flag
        name as parameter, returns a tuple (is_retired, type_is_bool).
    """
    self.__dict__['__is_retired_flag_func'] = is_retired_flag_func

  def _parse_args(self, args, known_only):
    """Helper function to do the main argument parsing.

    This function goes through args and does the bulk of the flag parsing.
    It will find the corresponding flag in our flag dictionary, and call its
    .parse() method on the flag value.

    Args:
      args: [str], a list of strings with the arguments to parse.
      known_only: bool, if True, parse and remove known flags; return the rest
        untouched. Unknown flags specified by --undefok are not returned.

    Returns:
      A tuple with the following:
          unknown_flags: List of (flag name, arg) for flags we don't know about.
          unparsed_args: List of arguments we did not parse.

    Raises:
       Error: Raised on any parsing error.
       ValueError: Raised on flag value parsing error.
    """
    unparsed_names_and_args = []  # A list of (flag name or None, arg).
    undefok = set()
    retired_flag_func = self.__dict__['__is_retired_flag_func']

    flag_dict = self._flags()
    args = iter(args)
    for arg in args:
      value = None

      def get_value():
        # pylint: disable=cell-var-from-loop
        try:
          return next(args) if value is None else value
        except StopIteration:
          raise _exceptions.Error('Missing value for flag ' + arg)  # pylint: disable=undefined-loop-variable

      if not arg.startswith('-'):
        # A non-argument: default is break, GNU is skip.
        unparsed_names_and_args.append((None, arg))
        if self.is_gnu_getopt():
          continue
        else:
          break

      if arg == '--':
        if known_only:
          unparsed_names_and_args.append((None, arg))
        break

      # At this point, arg must start with '-'.
      if arg.startswith('--'):
        arg_without_dashes = arg[2:]
      else:
        arg_without_dashes = arg[1:]

      if '=' in arg_without_dashes:
        name, value = arg_without_dashes.split('=', 1)
      else:
        name, value = arg_without_dashes, None

      if not name:
        # The argument is all dashes (including one dash).
        unparsed_names_and_args.append((None, arg))
        if self.is_gnu_getopt():
          continue
        else:
          break

      # --undefok is a special case.
      if name == 'undefok':
        value = get_value()
        undefok.update(v.strip() for v in value.split(','))
        undefok.update('no' + v.strip() for v in value.split(','))
        continue

      flag = flag_dict.get(name)
      if flag:
        if flag.boolean and value is None:
          value = 'true'
        else:
          value = get_value()
      elif name.startswith('no') and len(name) > 2:
        # Boolean flags can take the form of --noflag, with no value.
        noflag = flag_dict.get(name[2:])
        if noflag and noflag.boolean:
          if value is not None:
            raise ValueError(arg + ' does not take an argument')
          flag = noflag
          value = 'false'

      if retired_flag_func and not flag:
        is_retired, is_bool = retired_flag_func(name)

        # If we didn't recognize that flag, but it starts with
        # "no" then maybe it was a boolean flag specified in the
        # --nofoo form.
        if not is_retired and name.startswith('no'):
          is_retired, is_bool = retired_flag_func(name[2:])
          is_retired = is_retired and is_bool

        if is_retired:
          if not is_bool and value is None:
            # This happens when a non-bool retired flag is specified
            # in format of "--flag value".
            get_value()
          logging.error(
              'Flag "%s" is retired and should no longer '
              'be specified. See go/totw/90.', name)
          continue

      if flag:
        flag.parse(value)
        flag.using_default_value = False
      else:
        unparsed_names_and_args.append((name, arg))

    unknown_flags = []
    unparsed_args = []
    for name, arg in unparsed_names_and_args:
      if name is None:
        # Positional arguments.
        unparsed_args.append(arg)
      elif name in undefok:
        # Remove undefok flags.
        continue
      else:
        # This is an unknown flag.
        if known_only:
          unparsed_args.append(arg)
        else:
          unknown_flags.append((name, arg))

    unparsed_args.extend(list(args))
    return unknown_flags, unparsed_args

  def is_parsed(self):
    """Returns whether flags were parsed."""
    return self.__dict__['__flags_parsed']

  def mark_as_parsed(self):
    """Explicitly marks flags as parsed.

    Use this when the caller knows that this FlagValues has been parsed as if
    a __call__() invocation has happened.  This is only a public method for
    use by things like appcommands which do additional command like parsing.
    """
    self.__dict__['__flags_parsed'] = True

  def unparse_flags(self):
    """Unparses all flags to the point before any FLAGS(argv) was called."""
    for f in self._flags().values():
      f.unparse()
    # We log this message before marking flags as unparsed to avoid a
    # problem when the logging library causes flags access.
    logging.info('unparse_flags() called; flags access will now raise errors.')
    self.__dict__['__flags_parsed'] = False
    self.__dict__['__unparse_flags_called'] = True

  def flag_values_dict(self):
    """Returns a dictionary that maps flag names to flag values."""
    return {name: flag.value for name, flag in six.iteritems(self._flags())}

  def __str__(self):
    """Returns a help string for all known flags."""
    return self.get_help()

  def get_help(self, prefix='', include_special_flags=True):
    """Returns a help string for all known flags.

    Args:
      prefix: str, per-line output prefix.
      include_special_flags: bool, whether to include description of
        SPECIAL_FLAGS, i.e. --flagfile and --undefok.

    Returns:
      str, formatted help message.
    """
    flags_by_module = self.flags_by_module_dict()
    if flags_by_module:
      modules = sorted(flags_by_module)
      # Print the help for the main module first, if possible.
      main_module = sys.argv[0]
      if main_module in modules:
        modules.remove(main_module)
        modules = [main_module] + modules
      return self._get_help_for_modules(modules, prefix, include_special_flags)
    else:
      output_lines = []
      # Just print one long list of flags.
      values = six.itervalues(self._flags())
      if include_special_flags:
        values = itertools.chain(values,
                                 six.itervalues(
                                     _helpers.SPECIAL_FLAGS._flags()))  # pylint: disable=protected-access
      self._render_flag_list(values, output_lines, prefix)
      return '\n'.join(output_lines)

  def _get_help_for_modules(self, modules, prefix, include_special_flags):
    """Returns the help string for a list of modules.

    Private to absl.flags package.

    Args:
      modules: List[str], a list of modules to get the help string for.
      prefix: str, a string that is prepended to each generated help line.
      include_special_flags: bool, whether to include description of
        SPECIAL_FLAGS, i.e. --flagfile and --undefok.
    """
    output_lines = []
    for module in modules:
      self._render_our_module_flags(module, output_lines, prefix)
    if include_special_flags:
      self._render_module_flags(
          'absl.flags',
          six.itervalues(_helpers.SPECIAL_FLAGS._flags()),  # pylint: disable=protected-access
          output_lines,
          prefix)
    return '\n'.join(output_lines)

  def _render_module_flags(self, module, flags, output_lines, prefix=''):
    """Returns a help string for a given module."""
    if not isinstance(module, str):
      module = module.__name__
    output_lines.append('\n%s%s:' % (prefix, module))
    self._render_flag_list(flags, output_lines, prefix + '  ')

  def _render_our_module_flags(self, module, output_lines, prefix=''):
    """Returns a help string for a given module."""
    flags = self.get_flags_for_module(module)
    if flags:
      self._render_module_flags(module, flags, output_lines, prefix)

  def _render_our_module_key_flags(self, module, output_lines, prefix=''):
    """Returns a help string for the key flags of a given module.

    Args:
      module: module|str, the module to render key flags for.
      output_lines: [str], a list of strings.  The generated help message lines
        will be appended to this list.
      prefix: str, a string that is prepended to each generated help line.
    """
    key_flags = self.get_key_flags_for_module(module)
    if key_flags:
      self._render_module_flags(module, key_flags, output_lines, prefix)

  def module_help(self, module):
    """Describes the key flags of a module.

    Args:
      module: module|str, the module to describe the key flags for.

    Returns:
      str, describing the key flags of a module.
    """
    helplist = []
    self._render_our_module_key_flags(module, helplist)
    return '\n'.join(helplist)

  def main_module_help(self):
    """Describes the key flags of the main module.

    Returns:
      str, describing the key flags of the main module.
    """
    return self.module_help(sys.argv[0])

  def _render_flag_list(self, flaglist, output_lines, prefix='  '):
    fl = self._flags()
    special_fl = _helpers.SPECIAL_FLAGS._flags()  # pylint: disable=protected-access
    flaglist = [(flag.name, flag) for flag in flaglist]
    flaglist.sort()
    flagset = {}
    for (name, flag) in flaglist:
      # It's possible this flag got deleted or overridden since being
      # registered in the per-module flaglist.  Check now against the
      # canonical source of current flag information, the _flags.
      if fl.get(name, None) != flag and special_fl.get(name, None) != flag:
        # a different flag is using this name now
        continue
      # only print help once
      if flag in flagset:
        continue
      flagset[flag] = 1
      flaghelp = ''
      if flag.short_name:
        flaghelp += '-%s,' % flag.short_name
      if flag.boolean:
        flaghelp += '--[no]%s:' % flag.name
      else:
        flaghelp += '--%s:' % flag.name
      flaghelp += ' '
      if flag.help:
        flaghelp += flag.help
      flaghelp = _helpers.text_wrap(
          flaghelp, indent=prefix + '  ', firstline_indent=prefix)
      if flag.default_as_str:
        flaghelp += '\n'
        flaghelp += _helpers.text_wrap(
            '(default: %s)' % flag.default_as_str, indent=prefix + '  ')
      if flag.parser.syntactic_help:
        flaghelp += '\n'
        flaghelp += _helpers.text_wrap(
            '(%s)' % flag.parser.syntactic_help, indent=prefix + '  ')
      output_lines.append(flaghelp)

  def get_flag_value(self, name, default):  # pylint: disable=invalid-name
    """Returns the value of a flag (if not None) or a default value.

    Args:
      name: str, the name of a flag.
      default: Default value to use if the flag value is None.

    Returns:
      Requested flag value or default.
    """

    value = self.__getattr__(name)
    if value is not None:  # Can't do if not value, b/c value might be '0' or ""
      return value
    else:
      return default

  def _is_flag_file_directive(self, flag_string):
    """Checks whether flag_string contain a --flagfile=<foo> directive."""
    if isinstance(flag_string, type('')):
      if flag_string.startswith('--flagfile='):
        return 1
      elif flag_string == '--flagfile':
        return 1
      elif flag_string.startswith('-flagfile='):
        return 1
      elif flag_string == '-flagfile':
        return 1
      else:
        return 0
    return 0

  def _extract_filename(self, flagfile_str):
    """Returns filename from a flagfile_str of form -[-]flagfile=filename.

    The cases of --flagfile foo and -flagfile foo shouldn't be hitting
    this function, as they are dealt with in the level above this
    function.

    Args:
      flagfile_str: str, the flagfile string.

    Returns:
      str, the filename from a flagfile_str of form -[-]flagfile=filename.

    Raises:
      Error: Raised when illegal --flagfile is provided.
    """
    if flagfile_str.startswith('--flagfile='):
      return os.path.expanduser((flagfile_str[(len('--flagfile=')):]).strip())
    elif flagfile_str.startswith('-flagfile='):
      return os.path.expanduser((flagfile_str[(len('-flagfile=')):]).strip())
    else:
      raise _exceptions.Error('Hit illegal --flagfile type: %s' % flagfile_str)

  def _get_flag_file_lines(self, filename, parsed_file_stack=None):
    """Returns the useful (!=comments, etc) lines from a file with flags.

    Args:
      filename: str, the name of the flag file.
      parsed_file_stack: [str], a list of the names of the files that we have
        recursively encountered at the current depth. MUTATED BY THIS FUNCTION
        (but the original value is preserved upon successfully returning from
        function call).

    Returns:
      List of strings. See the note below.

    NOTE(springer): This function checks for a nested --flagfile=<foo>
    tag and handles the lower file recursively. It returns a list of
    all the lines that _could_ contain command flags. This is
    EVERYTHING except whitespace lines and comments (lines starting
    with '#' or '//').
    """
    # For consistency with the cpp version, ignore empty values.
    if not filename:
      return []
    if parsed_file_stack is None:
      parsed_file_stack = []
    # We do a little safety check for reparsing a file we've already encountered
    # at a previous depth.
    if filename in parsed_file_stack:
      sys.stderr.write('Warning: Hit circular flagfile dependency. Ignoring'
                       ' flagfile: %s\n' % (filename,))
      return []
    else:
      parsed_file_stack.append(filename)

    line_list = []  # All line from flagfile.
    flag_line_list = []  # Subset of lines w/o comments, blanks, flagfile= tags.
    try:
      file_obj = open(filename, 'r')
    except IOError as e_msg:
      raise _exceptions.CantOpenFlagFileError(
          'ERROR:: Unable to open flagfile: %s' % e_msg)

    with file_obj:
      line_list = file_obj.readlines()

    # This is where we check each line in the file we just read.
    for line in line_list:
      if line.isspace():
        pass
      # Checks for comment (a line that starts with '#').
      elif line.startswith('#') or line.startswith('//'):
        pass
      # Checks for a nested "--flagfile=<bar>" flag in the current file.
      # If we find one, recursively parse down into that file.
      elif self._is_flag_file_directive(line):
        sub_filename = self._extract_filename(line)
        included_flags = self._get_flag_file_lines(
            sub_filename, parsed_file_stack=parsed_file_stack)
        flag_line_list.extend(included_flags)
      else:
        # Any line that's not a comment or a nested flagfile should get
        # copied into 2nd position.  This leaves earlier arguments
        # further back in the list, thus giving them higher priority.
        flag_line_list.append(line.strip())

    parsed_file_stack.pop()
    return flag_line_list

  def read_flags_from_files(self, argv, force_gnu=True):
    """Processes command line args, but also allow args to be read from file.

    Args:
      argv: [str], a list of strings, usually sys.argv[1:], which may contain
        one or more flagfile directives of the form --flagfile="./filename".
        Note that the name of the program (sys.argv[0]) should be omitted.
      force_gnu: bool, if False, --flagfile parsing obeys the
        FLAGS.is_gnu_getopt() value. If True, ignore the value and always follow
        gnu_getopt semantics.

    Returns:
      A new list which has the original list combined with what we read
      from any flagfile(s).

    Raises:
      IllegalFlagValueError: Raised when --flagfile is provided with no
          argument.

    This function is called by FLAGS(argv).
    It scans the input list for a flag that looks like:
    --flagfile=<somefile>. Then it opens <somefile>, reads all valid key
    and value pairs and inserts them into the input list in exactly the
    place where the --flagfile arg is found.

    Note that your application's flags are still defined the usual way
    using absl.flags DEFINE_flag() type functions.

    Notes (assuming we're getting a commandline of some sort as our input):
    --> For duplicate flags, the last one we hit should "win".
    --> Since flags that appear later win, a flagfile's settings can be "weak"
        if the --flagfile comes at the beginning of the argument sequence,
        and it can be "strong" if the --flagfile comes at the end.
    --> A further "--flagfile=<otherfile.cfg>" CAN be nested in a flagfile.
        It will be expanded in exactly the spot where it is found.
    --> In a flagfile, a line beginning with # or // is a comment.
    --> Entirely blank lines _should_ be ignored.
    """
    rest_of_args = argv
    new_argv = []
    while rest_of_args:
      current_arg = rest_of_args[0]
      rest_of_args = rest_of_args[1:]
      if self._is_flag_file_directive(current_arg):
        # This handles the case of -(-)flagfile foo.  In this case the
        # next arg really is part of this one.
        if current_arg == '--flagfile' or current_arg == '-flagfile':
          if not rest_of_args:
            raise _exceptions.IllegalFlagValueError(
                '--flagfile with no argument')
          flag_filename = os.path.expanduser(rest_of_args[0])
          rest_of_args = rest_of_args[1:]
        else:
          # This handles the case of (-)-flagfile=foo.
          flag_filename = self._extract_filename(current_arg)
        new_argv.extend(self._get_flag_file_lines(flag_filename))
      else:
        new_argv.append(current_arg)
        # Stop parsing after '--', like getopt and gnu_getopt.
        if current_arg == '--':
          break
        # Stop parsing after a non-flag, like getopt.
        if not current_arg.startswith('-'):
          if not force_gnu and not self.__dict__['__use_gnu_getopt']:
            break
        else:
          if ('=' not in current_arg and rest_of_args and
              not rest_of_args[0].startswith('-')):
            # If this is an occurrence of a legitimate --x y, skip the value
            # so that it won't be mistaken for a standalone arg.
            fl = self._flags()
            name = current_arg.lstrip('-')
            if name in fl and not fl[name].boolean:
              current_arg = rest_of_args[0]
              rest_of_args = rest_of_args[1:]
              new_argv.append(current_arg)

    if rest_of_args:
      new_argv.extend(rest_of_args)

    return new_argv

  def flags_into_string(self):
    """Returns a string with the flags assignments from this FlagValues object.

    This function ignores flags whose value is None.  Each flag
    assignment is separated by a newline.

    NOTE: MUST mirror the behavior of the C++ CommandlineFlagsIntoString
    from https://github.com/gflags/gflags.

    Returns:
      str, the string with the flags assignments from this FlagValues object.
      The flags are ordered by (module_name, flag_name).
    """
    module_flags = sorted(self.flags_by_module_dict().items())
    s = ''
    for unused_module_name, flags in module_flags:
      flags = sorted(flags, key=lambda f: f.name)
      for flag in flags:
        if flag.value is not None:
          s += flag.serialize() + '\n'
    return s

  def append_flags_into_file(self, filename):
    """Appends all flags assignments from this FlagInfo object to a file.

    Output will be in the format of a flagfile.

    NOTE: MUST mirror the behavior of the C++ AppendFlagsIntoFile
    from https://github.com/gflags/gflags.

    Args:
      filename: str, name of the file.
    """
    with open(filename, 'a') as out_file:
      out_file.write(self.flags_into_string())

  def write_help_in_xml_format(self, outfile=None):
    """Outputs flag documentation in XML format.

    NOTE: We use element names that are consistent with those used by
    the C++ command-line flag library, from
    https://github.com/gflags/gflags.
    We also use a few new elements (e.g., <key>), but we do not
    interfere / overlap with existing XML elements used by the C++
    library.  Please maintain this consistency.

    Args:
      outfile: File object we write to.  Default None means sys.stdout.
    """
    doc = minidom.Document()
    all_flag = doc.createElement('AllFlags')
    doc.appendChild(all_flag)

    all_flag.appendChild(
        _helpers.create_xml_dom_element(doc, 'program',
                                        os.path.basename(sys.argv[0])))

    usage_doc = sys.modules['__main__'].__doc__
    if not usage_doc:
      usage_doc = '\nUSAGE: %s [flags]\n' % sys.argv[0]
    else:
      usage_doc = usage_doc.replace('%s', sys.argv[0])
    all_flag.appendChild(
        _helpers.create_xml_dom_element(doc, 'usage', usage_doc))

    # Get list of key flags for the main module.
    key_flags = self.get_key_flags_for_module(sys.argv[0])

    # Sort flags by declaring module name and next by flag name.
    flags_by_module = self.flags_by_module_dict()
    all_module_names = list(flags_by_module.keys())
    all_module_names.sort()
    for module_name in all_module_names:
      flag_list = [(f.name, f) for f in flags_by_module[module_name]]
      flag_list.sort()
      for unused_flag_name, flag in flag_list:
        is_key = flag in key_flags
        all_flag.appendChild(
            flag._create_xml_dom_element(  # pylint: disable=protected-access
                doc,
                module_name,
                is_key=is_key))

    outfile = outfile or sys.stdout
    if six.PY2:
      outfile.write(doc.toprettyxml(indent='  ', encoding='utf-8'))
    else:
      outfile.write(
          doc.toprettyxml(indent='  ', encoding='utf-8').decode('utf-8'))
    outfile.flush()

  def _check_method_name_conflicts(self, name, flag):
    if flag.allow_using_method_names:
      return
    short_name = flag.short_name
    flag_names = {name} if short_name is None else {name, short_name}
    for flag_name in flag_names:
      if flag_name in self.__dict__['__banned_flag_names']:
        raise _exceptions.FlagNameConflictsWithMethodError(
            'Cannot define a flag named "{name}". It conflicts with a method '
            'on class "{class_name}". To allow defining it, use '
            'allow_using_method_names and access the flag value with '
            "FLAGS['{name}'].value. FLAGS.{name} returns the method, "
            'not the flag value.'.format(
                name=flag_name, class_name=type(self).__name__))


FLAGS = FlagValues()

if typing:
  _T = typing.TypeVar('_T')
  _Base = typing.Generic[_T]
else:
  _Base = object


class FlagHolder(_Base):
  """Holds a defined flag.

  This facilitates a cleaner api around global state. Instead of

  ```
  flags.DEFINE_integer('foo', ...)
  flags.DEFINE_integer('bar', ...)
  ...
  def method():
    # prints parsed value of 'bar' flag
    print(flags.FLAGS.foo)
    # runtime error due to typo or possibly bad coding style.
    print(flags.FLAGS.baz)
  ```

  it encourages code like

  ```
  FOO_FLAG = flags.DEFINE_integer('foo', ...)
  BAR_FLAG = flags.DEFINE_integer('bar', ...)
  ...
  def method():
    print(FOO_FLAG.value)
    print(BAR_FLAG.value)
  ```

  since the name of the flag appears only once in the source code.
  """

  def __init__(self, flag_values, flag, ensure_non_none_value=False):
    """Constructs a FlagHolder instance providing typesafe access to flag.

    Args:
      flag_values: The container the flag is registered to.
      flag: The flag object for this flag.
      ensure_non_none_value: Is the value of the flag allowed to be None.
    """
    self._flagvalues = flag_values
    # We take the entire flag object, but only keep the name. Why?
    # - We want FlagHolder[T] to be generic container
    # - flag_values contains all flags, so has no reference to T.
    # - typecheckers don't like to see a generic class where none of the ctor
    #   arguments refer to the generic type.
    self._name = flag.name
    # We intentionally do NOT check if the default value is None.
    # This allows future use of this for "required flags with None default"
    self._ensure_non_none_value = ensure_non_none_value

  def __eq__(self, other):
    raise TypeError(
        "unsupported operand type(s) for ==: '{0}' and '{1}' "
        "(did you mean to use '{0}.value' instead?)".format(
            type(self).__name__, type(other).__name__))

  def __bool__(self):
    raise TypeError(
        "bool() not supported for instances of type '{0}' "
        "(did you mean to use '{0}.value' instead?)".format(
            type(self).__name__))

  __nonzero__ = __bool__

  @property
  def name(self):
    return self._name

  @property
  def value(self):
    """Returns the value of the flag.

    If _ensure_non_none_value is True, then return value is not None.

    Raises:
      UnparsedFlagAccessError: if flag parsing has not finished.
      IllegalFlagValueError: if value is None unexpectedly.
    """
    val = getattr(self._flagvalues, self._name)
    if self._ensure_non_none_value and val is None:
      raise _exceptions.IllegalFlagValueError(
          'Unexpected None value for flag %s' % self._name)
    return val

  @property
  def default(self):
    """Returns the default value of the flag."""
    return self._flagvalues[self._name].default
