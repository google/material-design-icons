from .otBase import BaseTTXConverter


# The anchor point table provides a way to define anchor points.
# These are points within the coordinate space of a given glyph,
# independent of the control points used to render the glyph.
# Anchor points are used in conjunction with the 'kerx' table.
#
# https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6ankr.html
class table__a_n_k_r(BaseTTXConverter):
    pass
