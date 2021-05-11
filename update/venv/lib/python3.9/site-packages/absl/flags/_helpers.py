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

"""Internal helper functions for Abseil Python flags library."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import os
import re
import struct
import sys
import textwrap
try:
  import fcntl
except ImportError:
  fcntl = None
try:
  # Importing termios will fail on non-unix platforms.
  import termios
except ImportError:
  termios = None

import six
from six.moves import range  # pylint: disable=redefined-builtin


_DEFAULT_HELP_WIDTH = 80  # Default width of help output.
_MIN_HELP_WIDTH = 40  # Minimal "sane" width of help output. We assume that any
                      # value below 40 is unreasonable.

# Define the allowed error rate in an input string to get suggestions.
#
# We lean towards a high threshold because we tend to be matching a phrase,
# and the simple algorithm used here is geared towards correcting word
# spellings.
#
# For manual testing, consider "<command> --list" which produced a large number
# of spurious suggestions when we used "least_errors > 0.5" instead of
# "least_erros >= 0.5".
_SUGGESTION_ERROR_RATE_THRESHOLD = 0.50

# Characters that cannot appear or are highly discouraged in an XML 1.0
# document. (See http://www.w3.org/TR/REC-xml/#charsets or
# https://en.wikipedia.org/wiki/Valid_characters_in_XML#XML_1.0)
_ILLEGAL_XML_CHARS_REGEX = re.compile(
    u'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x84\x86-\x9f\ud800-\udfff\ufffe\uffff]')

# This is a set of module ids for the modules that disclaim key flags.
# This module is explicitly added to this set so that we never consider it to
# define key flag.
disclaim_module_ids = set([id(sys.modules[__name__])])


# Define special flags here so that help may be generated for them.
# NOTE: Please do NOT use SPECIAL_FLAGS from outside flags module.
# Initialized inside flagvalues.py.
SPECIAL_FLAGS = None


# This points to the flags module, initialized in flags/__init__.py.
# This should only be used in adopt_module_key_flags to take SPECIAL_FLAGS into
# account.
FLAGS_MODULE = None


class _ModuleObjectAndName(
    collections.namedtuple('_ModuleObjectAndName', 'module module_name')):
  """Module object and name.

  Fields:
  - module: object, module object.
  - module_name: str, module name.
  """


def get_module_object_and_name(globals_dict):
  """Returns the module that defines a global environment, and its name.

  Args:
    globals_dict: A dictionary that should correspond to an environment
      providing the values of the globals.

  Returns:
    _ModuleObjectAndName - pair of module object & module name.
    Returns (None, None) if the module could not be identified.
  """
  name = globals_dict.get('__name__', None)
  module = sys.modules.get(name, None)
  # Pick a more informative name for the main module.
  return _ModuleObjectAndName(module,
                              (sys.argv[0] if name == '__main__' else name))


def get_calling_module_object_and_name():
  """Returns the module that's calling into this module.

  We generally use this function to get the name of the module calling a
  DEFINE_foo... function.

  Returns:
    The module object that called into this one.

  Raises:
    AssertionError: Raised when no calling module could be identified.
  """
  for depth in range(1, sys.getrecursionlimit()):
    # sys._getframe is the right thing to use here, as it's the best
    # way to walk up the call stack.
    globals_for_frame = sys._getframe(depth).f_globals  # pylint: disable=protected-access
    module, module_name = get_module_object_and_name(globals_for_frame)
    if id(module) not in disclaim_module_ids and module_name is not None:
      return _ModuleObjectAndName(module, module_name)
  raise AssertionError('No module was found')


def get_calling_module():
  """Returns the name of the module that's calling into this module."""
  return get_calling_module_object_and_name().module_name


def str_or_unicode(value):
  """Converts a value to a python string.

  Behavior of this function is intentionally different in Python2/3.

  In Python2, the given value is attempted to convert to a str (byte string).
  If it contains non-ASCII characters, it is converted to a unicode instead.

  In Python3, the given value is always converted to a str (unicode string).

  This behavior reflects the (bad) practice in Python2 to try to represent
  a string as str as long as it contains ASCII characters only.

  Args:
    value: An object to be converted to a string.

  Returns:
    A string representation of the given value. See the description above
    for its type.
  """
  try:
    return str(value)
  except UnicodeEncodeError:
    return unicode(value)  # Python3 should never come here


def create_xml_dom_element(doc, name, value):
  """Returns an XML DOM element with name and text value.

  Args:
    doc: minidom.Document, the DOM document it should create nodes from.
    name: str, the tag of XML element.
    value: object, whose string representation will be used
        as the value of the XML element. Illegal or highly discouraged xml 1.0
        characters are stripped.

  Returns:
    An instance of minidom.Element.
  """
  s = str_or_unicode(value)
  if six.PY2 and not isinstance(s, unicode):
    # Get a valid unicode string.
    s = s.decode('utf-8', 'ignore')
  if isinstance(value, bool):
    # Display boolean values as the C++ flag library does: no caps.
    s = s.lower()
  # Remove illegal xml characters.
  s = _ILLEGAL_XML_CHARS_REGEX.sub(u'', s)

  e = doc.createElement(name)
  e.appendChild(doc.createTextNode(s))
  return e


def get_help_width():
  """Returns the integer width of help lines that is used in TextWrap."""
  if not sys.stdout.isatty() or termios is None or fcntl is None:
    return _DEFAULT_HELP_WIDTH
  try:
    data = fcntl.ioctl(sys.stdout, termios.TIOCGWINSZ, '1234')
    columns = struct.unpack('hh', data)[1]
    # Emacs mode returns 0.
    # Here we assume that any value below 40 is unreasonable.
    if columns >= _MIN_HELP_WIDTH:
      return columns
    # Returning an int as default is fine, int(int) just return the int.
    return int(os.getenv('COLUMNS', _DEFAULT_HELP_WIDTH))

  except (TypeError, IOError, struct.error):
    return _DEFAULT_HELP_WIDTH


def get_flag_suggestions(attempt, longopt_list):
  """Returns helpful similar matches for an invalid flag."""
  # Don't suggest on very short strings, or if no longopts are specified.
  if len(attempt) <= 2 or not longopt_list:
    return []

  option_names = [v.split('=')[0] for v in longopt_list]

  # Find close approximations in flag prefixes.
  # This also handles the case where the flag is spelled right but ambiguous.
  distances = [(_damerau_levenshtein(attempt, option[0:len(attempt)]), option)
               for option in option_names]
  # t[0] is distance, and sorting by t[1] allows us to have stable output.
  distances.sort()

  least_errors, _ = distances[0]
  # Don't suggest excessively bad matches.
  if least_errors >= _SUGGESTION_ERROR_RATE_THRESHOLD * len(attempt):
    return []

  suggestions = []
  for errors, name in distances:
    if errors == least_errors:
      suggestions.append(name)
    else:
      break
  return suggestions


def _damerau_levenshtein(a, b):
  """Returns Damerau-Levenshtein edit distance from a to b."""
  memo = {}

  def distance(x, y):
    """Recursively defined string distance with memoization."""
    if (x, y) in memo:
      return memo[x, y]
    if not x:
      d = len(y)
    elif not y:
      d = len(x)
    else:
      d = min(
          distance(x[1:], y) + 1,  # correct an insertion error
          distance(x, y[1:]) + 1,  # correct a deletion error
          distance(x[1:], y[1:]) + (x[0] != y[0]))  # correct a wrong character
      if len(x) >= 2 and len(y) >= 2 and x[0] == y[1] and x[1] == y[0]:
        # Correct a transposition.
        t = distance(x[2:], y[2:]) + 1
        if d > t:
          d = t

    memo[x, y] = d
    return d
  return distance(a, b)


def text_wrap(text, length=None, indent='', firstline_indent=None):
  """Wraps a given text to a maximum line length and returns it.

  It turns lines that only contain whitespace into empty lines, keeps new lines,
  and expands tabs using 4 spaces.

  Args:
    text: str, text to wrap.
    length: int, maximum length of a line, includes indentation.
        If this is None then use get_help_width()
    indent: str, indent for all but first line.
    firstline_indent: str, indent for first line; if None, fall back to indent.

  Returns:
    str, the wrapped text.

  Raises:
    ValueError: Raised if indent or firstline_indent not shorter than length.
  """
  # Get defaults where callee used None
  if length is None:
    length = get_help_width()
  if indent is None:
    indent = ''
  if firstline_indent is None:
    firstline_indent = indent

  if len(indent) >= length:
    raise ValueError('Length of indent exceeds length')
  if len(firstline_indent) >= length:
    raise ValueError('Length of first line indent exceeds length')

  text = text.expandtabs(4)

  result = []
  # Create one wrapper for the first paragraph and one for subsequent
  # paragraphs that does not have the initial wrapping.
  wrapper = textwrap.TextWrapper(
      width=length, initial_indent=firstline_indent, subsequent_indent=indent)
  subsequent_wrapper = textwrap.TextWrapper(
      width=length, initial_indent=indent, subsequent_indent=indent)

  # textwrap does not have any special treatment for newlines. From the docs:
  # "...newlines may appear in the middle of a line and cause strange output.
  # For this reason, text should be split into paragraphs (using
  # str.splitlines() or similar) which are wrapped separately."
  for paragraph in (p.strip() for p in text.splitlines()):
    if paragraph:
      result.extend(wrapper.wrap(paragraph))
    else:
      result.append('')  # Keep empty lines.
    # Replace initial wrapper with wrapper for subsequent paragraphs.
    wrapper = subsequent_wrapper

  return '\n'.join(result)


def flag_dict_to_args(flag_map, multi_flags=None):
  """Convert a dict of values into process call parameters.

  This method is used to convert a dictionary into a sequence of parameters
  for a binary that parses arguments using this module.

  Args:
    flag_map: dict, a mapping where the keys are flag names (strings).
        values are treated according to their type:
        * If value is None, then only the name is emitted.
        * If value is True, then only the name is emitted.
        * If value is False, then only the name prepended with 'no' is emitted.
        * If value is a string then --name=value is emitted.
        * If value is a collection, this will emit --name=value1,value2,value3,
          unless the flag name is in multi_flags, in which case this will emit
          --name=value1 --name=value2 --name=value3.
        * Everything else is converted to string an passed as such.
    multi_flags: set, names (strings) of flags that should be treated as
        multi-flags.
  Yields:
    sequence of string suitable for a subprocess execution.
  """
  for key, value in six.iteritems(flag_map):
    if value is None:
      yield '--%s' % key
    elif isinstance(value, bool):
      if value:
        yield '--%s' % key
      else:
        yield '--no%s' % key
    elif isinstance(value, (bytes, type(u''))):
      # We don't want strings to be handled like python collections.
      yield '--%s=%s' % (key, value)
    else:
      # Now we attempt to deal with collections.
      try:
        if multi_flags and key in multi_flags:
          for item in value:
            yield '--%s=%s' % (key, str(item))
        else:
          yield '--%s=%s' % (key, ','.join(str(item) for item in value))
      except TypeError:
        # Default case.
        yield '--%s=%s' % (key, value)


def trim_docstring(docstring):
  """Removes indentation from triple-quoted strings.

  This is the function specified in PEP 257 to handle docstrings:
  https://www.python.org/dev/peps/pep-0257/.

  Args:
    docstring: str, a python docstring.

  Returns:
    str, docstring with indentation removed.
  """
  if not docstring:
    return ''

  # If you've got a line longer than this you have other problems...
  max_indent = 1 << 29

  # Convert tabs to spaces (following the normal Python rules)
  # and split into a list of lines:
  lines = docstring.expandtabs().splitlines()

  # Determine minimum indentation (first line doesn't count):
  indent = max_indent
  for line in lines[1:]:
    stripped = line.lstrip()
    if stripped:
      indent = min(indent, len(line) - len(stripped))
  # Remove indentation (first line is special):
  trimmed = [lines[0].strip()]
  if indent < max_indent:
    for line in lines[1:]:
      trimmed.append(line[indent:].rstrip())
  # Strip off trailing and leading blank lines:
  while trimmed and not trimmed[-1]:
    trimmed.pop()
  while trimmed and not trimmed[0]:
    trimmed.pop(0)
  # Return a single string:
  return '\n'.join(trimmed)


def doc_to_help(doc):
  """Takes a __doc__ string and reformats it as help."""

  # Get rid of starting and ending white space. Using lstrip() or even
  # strip() could drop more than maximum of first line and right space
  # of last line.
  doc = doc.strip()

  # Get rid of all empty lines.
  whitespace_only_line = re.compile('^[ \t]+$', re.M)
  doc = whitespace_only_line.sub('', doc)

  # Cut out common space at line beginnings.
  doc = trim_docstring(doc)

  # Just like this module's comment, comments tend to be aligned somehow.
  # In other words they all start with the same amount of white space.
  # 1) keep double new lines;
  # 2) keep ws after new lines if not empty line;
  # 3) all other new lines shall be changed to a space;
  # Solution: Match new lines between non white space and replace with space.
  doc = re.sub(r'(?<=\S)\n(?=\S)', ' ', doc, flags=re.M)

  return doc


def is_bytes_or_string(maybe_string):
  if str is bytes:
    return isinstance(maybe_string, basestring)
  else:
    return isinstance(maybe_string, (str, bytes))
