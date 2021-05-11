"""fontTools.ttLib -- a package for dealing with TrueType fonts.

This package offers translators to convert TrueType fonts to Python
objects and vice versa, and additionally from Python to TTX (an XML-based
text format) and vice versa.

Example interactive session:

Python 1.5.2c1 (#43, Mar  9 1999, 13:06:43)  [CW PPC w/GUSI w/MSL]
Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam
>> from fontTools import ttLib
>> tt = ttLib.TTFont("afont.ttf")
>> tt['maxp'].numGlyphs
242
>> tt['OS/2'].achVendID
'B&H\000'
>> tt['head'].unitsPerEm
2048
>> tt.saveXML("afont.ttx")
Dumping 'LTSH' table...
Dumping 'OS/2' table...
Dumping 'VDMX' table...
Dumping 'cmap' table...
Dumping 'cvt ' table...
Dumping 'fpgm' table...
Dumping 'glyf' table...
Dumping 'hdmx' table...
Dumping 'head' table...
Dumping 'hhea' table...
Dumping 'hmtx' table...
Dumping 'loca' table...
Dumping 'maxp' table...
Dumping 'name' table...
Dumping 'post' table...
Dumping 'prep' table...
>> tt2 = ttLib.TTFont()
>> tt2.importXML("afont.ttx")
>> tt2['maxp'].numGlyphs
242
>>

"""

from fontTools.misc.loggingTools import deprecateFunction
import logging


log = logging.getLogger(__name__)

class TTLibError(Exception): pass

@deprecateFunction("use logging instead", category=DeprecationWarning)
def debugmsg(msg):
	import time
	print(msg + time.strftime("  (%H:%M:%S)", time.localtime(time.time())))

from fontTools.ttLib.ttFont import *
from fontTools.ttLib.ttCollection import TTCollection
