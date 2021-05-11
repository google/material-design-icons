__all__ = ['popCount']


def popCount(v):
    """Return number of 1 bits (population count) of an integer.

    If the integer is negative, the number of 1 bits in the
    twos-complement representation of the integer is returned. i.e.
    ``popCount(-30) == 28`` because -30 is::

        1111 1111 1111 1111 1111 1111 1110 0010

    Uses the algorithm from `HAKMEM item 169 <https://www.inwap.com/pdp10/hbaker/hakmem/hacks.html#item169>`_.

    Args:
        v (int): Value to count.

    Returns:
        Number of 1 bits in the binary representation of ``v``.
    """

    if v > 0xFFFFFFFF:
        return popCount(v >> 32) + popCount(v & 0xFFFFFFFF)

    # HACKMEM 169
    y = (v >> 1) & 0xDB6DB6DB
    y = v - y - ((y >> 1) & 0xDB6DB6DB)
    return (((y + (y >> 3)) & 0xC71C71C7) % 0x3F)
