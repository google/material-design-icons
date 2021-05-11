"""
Various round-to-integer helpers.
"""

import math
import functools
import logging

log = logging.getLogger(__name__)

__all__ = [
	"noRound",
	"otRound",
	"maybeRound",
	"roundFunc",
]

def noRound(value):
	return value

def otRound(value):
	"""Round float value to nearest integer towards ``+Infinity``.

	The OpenType spec (in the section on `"normalization" of OpenType Font Variations <https://docs.microsoft.com/en-us/typography/opentype/spec/otvaroverview#coordinate-scales-and-normalization>`_)
	defines the required method for converting floating point values to
	fixed-point. In particular it specifies the following rounding strategy:

		for fractional values of 0.5 and higher, take the next higher integer;
		for other fractional values, truncate.

	This function rounds the floating-point value according to this strategy
	in preparation for conversion to fixed-point.

	Args:
		value (float): The input floating-point value.

	Returns
		float: The rounded value.
	"""
	# See this thread for how we ended up with this implementation:
	# https://github.com/fonttools/fonttools/issues/1248#issuecomment-383198166
	return int(math.floor(value + 0.5))

def maybeRound(v, tolerance, round=otRound):
	rounded = round(v)
	return rounded if abs(rounded - v) <= tolerance else v

def roundFunc(tolerance, round=otRound):
    if tolerance < 0:
        raise ValueError("Rounding tolerance must be positive")

    if tolerance == 0:
        return noRound

    if tolerance >= .5:
        return round

    return functools.partial(maybeRound, tolerance=tolerance, round=round)
