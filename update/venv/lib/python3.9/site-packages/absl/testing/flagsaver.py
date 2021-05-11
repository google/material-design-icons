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

"""Decorator and context manager for saving and restoring flag values.

There are many ways to save and restore.  Always use the most convenient method
for a given use case.

Here are examples of each method.  They all call do_stuff() while FLAGS.someflag
is temporarily set to 'foo'.

  from absl.testing import flagsaver

  # Use a decorator which can optionally override flags via arguments.
  @flagsaver.flagsaver(someflag='foo')
  def some_func():
    do_stuff()

  # Use a decorator which can optionally override flags with flagholders.
  @flagsaver.flagsaver((module.FOO_FLAG, 'foo'), (other_mod.BAR_FLAG, 23))
  def some_func():
    do_stuff()

  # Use a decorator which does not override flags itself.
  @flagsaver.flagsaver
  def some_func():
    FLAGS.someflag = 'foo'
    do_stuff()

  # Use a context manager which can optionally override flags via arguments.
  with flagsaver.flagsaver(someflag='foo'):
    do_stuff()

  # Save and restore the flag values yourself.
  saved_flag_values = flagsaver.save_flag_values()
  try:
    FLAGS.someflag = 'foo'
    do_stuff()
  finally:
    flagsaver.restore_flag_values(saved_flag_values)

We save and restore a shallow copy of each Flag object's __dict__ attribute.
This preserves all attributes of the flag, such as whether or not it was
overridden from its default value.

WARNING: Currently a flag that is saved and then deleted cannot be restored.  An
exception will be raised.  However if you *add* a flag after saving flag values,
and then restore flag values, the added flag will be deleted with no errors.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import inspect

from absl import flags

FLAGS = flags.FLAGS


def flagsaver(*args, **kwargs):
  """The main flagsaver interface. See module doc for usage."""
  if not args:
    return _FlagOverrider(**kwargs)
  # args can be [func] if used as `@flagsaver` instead of `@flagsaver(...)`
  if len(args) == 1 and callable(args[0]):
    if kwargs:
      raise ValueError(
          "It's invalid to specify both positional and keyword parameters.")
    func = args[0]
    if inspect.isclass(func):
      raise TypeError('@flagsaver.flagsaver cannot be applied to a class.')
    return _wrap(func, {})
  # args can be a list of (FlagHolder, value) pairs.
  # In which case they augment any specified kwargs.
  for arg in args:
    if not isinstance(arg, tuple) or len(arg) != 2:
      raise ValueError('Expected (FlagHolder, value) pair, found %r' % (arg,))
    holder, value = arg
    if not isinstance(holder, flags.FlagHolder):
      raise ValueError('Expected (FlagHolder, value) pair, found %r' % (arg,))
    if holder.name in kwargs:
      raise ValueError('Cannot set --%s multiple times' % holder.name)
    kwargs[holder.name] = value
  return _FlagOverrider(**kwargs)


def save_flag_values(flag_values=FLAGS):
  """Returns copy of flag values as a dict.

  Args:
    flag_values: FlagValues, the FlagValues instance with which the flag will
        be saved. This should almost never need to be overridden.
  Returns:
    Dictionary mapping keys to values. Keys are flag names, values are
    corresponding __dict__ members. E.g. {'key': value_dict, ...}.
  """
  return {name: _copy_flag_dict(flag_values[name]) for name in flag_values}


def restore_flag_values(saved_flag_values, flag_values=FLAGS):
  """Restores flag values based on the dictionary of flag values.

  Args:
    saved_flag_values: {'flag_name': value_dict, ...}
    flag_values: FlagValues, the FlagValues instance from which the flag will
        be restored. This should almost never need to be overridden.
  """
  new_flag_names = list(flag_values)
  for name in new_flag_names:
    saved = saved_flag_values.get(name)
    if saved is None:
      # If __dict__ was not saved delete "new" flag.
      delattr(flag_values, name)
    else:
      if flag_values[name].value != saved['_value']:
        flag_values[name].value = saved['_value']  # Ensure C++ value is set.
      flag_values[name].__dict__ = saved


def _wrap(func, overrides):
  """Creates a wrapper function that saves/restores flag values.

  Args:
    func: function object - This will be called between saving flags and
        restoring flags.
    overrides: {str: object} - Flag names mapped to their values.  These flags
        will be set after saving the original flag state.

  Returns:
    return value from func()
  """
  @functools.wraps(func)
  def _flagsaver_wrapper(*args, **kwargs):
    """Wrapper function that saves and restores flags."""
    with _FlagOverrider(**overrides):
      return func(*args, **kwargs)
  return _flagsaver_wrapper


class _FlagOverrider(object):
  """Overrides flags for the duration of the decorated function call.

  It also restores all original values of flags after decorated method
  completes.
  """

  def __init__(self, **overrides):
    self._overrides = overrides
    self._saved_flag_values = None

  def __call__(self, func):
    if inspect.isclass(func):
      raise TypeError('flagsaver cannot be applied to a class.')
    return _wrap(func, self._overrides)

  def __enter__(self):
    self._saved_flag_values = save_flag_values(FLAGS)
    try:
      FLAGS._set_attributes(**self._overrides)
    except:
      # It may fail because of flag validators.
      restore_flag_values(self._saved_flag_values, FLAGS)
      raise

  def __exit__(self, exc_type, exc_value, traceback):
    restore_flag_values(self._saved_flag_values, FLAGS)


def _copy_flag_dict(flag):
  """Returns a copy of the flag object's __dict__.

  It's mostly a shallow copy of the __dict__, except it also does a shallow
  copy of the validator list.

  Args:
    flag: flags.Flag, the flag to copy.

  Returns:
    A copy of the flag object's __dict__.
  """
  copy = flag.__dict__.copy()
  copy['_value'] = flag.value  # Ensure correct restore for C++ flags.
  copy['validators'] = list(flag.validators)
  return copy
