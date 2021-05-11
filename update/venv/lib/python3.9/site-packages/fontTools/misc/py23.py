"""Python 2/3 compat layer leftovers."""

import decimal as _decimal
import math as _math
import warnings
from contextlib import redirect_stderr, redirect_stdout
from io import BytesIO
from io import StringIO as UnicodeIO
from types import SimpleNamespace

warnings.warn(
    "The py23 module has been deprecated and will be removed in a future release. "
    "Please update your code.",
    DeprecationWarning,
)

__all__ = [
    "basestring",
    "bytechr",
    "byteord",
    "BytesIO",
    "bytesjoin",
    "open",
    "Py23Error",
    "range",
    "RecursionError",
    "round",
    "SimpleNamespace",
    "StringIO",
    "strjoin",
    "Tag",
    "tobytes",
    "tostr",
    "tounicode",
    "unichr",
    "unicode",
    "UnicodeIO",
    "xrange",
    "zip",
]


class Py23Error(NotImplementedError):
    pass


RecursionError = RecursionError
StringIO = UnicodeIO

basestring = str
isclose = _math.isclose
isfinite = _math.isfinite
open = open
range = range
round = round3 = round
unichr = chr
unicode = str
zip = zip


def bytechr(n):
    return bytes([n])


def byteord(c):
    return c if isinstance(c, int) else ord(c)


def strjoin(iterable, joiner=""):
    return tostr(joiner).join(iterable)


def tobytes(s, encoding="ascii", errors="strict"):
    if isinstance(s, str):
        return s.encode(encoding, errors)
    else:
        return bytes(s)


def tounicode(s, encoding="ascii", errors="strict"):
    if not isinstance(s, unicode):
        return s.decode(encoding, errors)
    else:
        return s


tostr = tounicode


class Tag(str):
    @staticmethod
    def transcode(blob):
        if isinstance(blob, bytes):
            blob = blob.decode("latin-1")
        return blob

    def __new__(self, content):
        return str.__new__(self, self.transcode(content))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        return str.__eq__(self, self.transcode(other))

    def __hash__(self):
        return str.__hash__(self)

    def tobytes(self):
        return self.encode("latin-1")


def bytesjoin(iterable, joiner=b""):
    return tobytes(joiner).join(tobytes(item) for item in iterable)


def xrange(*args, **kwargs):
    raise Py23Error("'xrange' is not defined. Use 'range' instead.")


def round2(number, ndigits=None):
    """
    Implementation of Python 2 built-in round() function.
    Rounds a number to a given precision in decimal digits (default
    0 digits). The result is a floating point number. Values are rounded
    to the closest multiple of 10 to the power minus ndigits; if two
    multiples are equally close, rounding is done away from 0.
    ndigits may be negative.
    See Python 2 documentation:
    https://docs.python.org/2/library/functions.html?highlight=round#round
    """
    if ndigits is None:
        ndigits = 0

    if ndigits < 0:
        exponent = 10 ** (-ndigits)
        quotient, remainder = divmod(number, exponent)
        if remainder >= exponent // 2 and number >= 0:
            quotient += 1
        return float(quotient * exponent)
    else:
        exponent = _decimal.Decimal("10") ** (-ndigits)

        d = _decimal.Decimal.from_float(number).quantize(
            exponent, rounding=_decimal.ROUND_HALF_UP
        )

        return float(d)
