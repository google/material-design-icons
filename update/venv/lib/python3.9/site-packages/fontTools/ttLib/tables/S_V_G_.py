from fontTools.misc.py23 import bytesjoin, strjoin, tobytes, tostr
from fontTools.misc import sstruct
from . import DefaultTable
try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET
from io import BytesIO
import struct
import logging


log = logging.getLogger(__name__)


__doc__="""
Compiles/decompiles version 0 and 1 SVG tables from/to XML.

Version 1 is the first SVG definition, implemented in Mozilla before Aug 2013, now deprecated.
This module will decompile this correctly, but will compile a version 1 table
only if you add the secret element "<version1/>" to the SVG element in the TTF file.

Version 0 is the joint Adobe-Mozilla proposal, which supports color palettes.

The XML format is:
<SVG>
	<svgDoc endGlyphID="1" startGlyphID="1">
		<![CDATA[ <complete SVG doc> ]]
	</svgDoc>
...
	<svgDoc endGlyphID="n" startGlyphID="m">
		<![CDATA[ <complete SVG doc> ]]
	</svgDoc>

	<colorPalettes>
		<colorParamUINameID>n</colorParamUINameID>
		...
		<colorParamUINameID>m</colorParamUINameID>
		<colorPalette uiNameID="n">
			<colorRecord red="<int>" green="<int>" blue="<int>" alpha="<int>" />
			...
			<colorRecord red="<int>" green="<int>" blue="<int>" alpha="<int>" />
		</colorPalette>
		...
		<colorPalette uiNameID="m">
			<colorRecord red="<int> green="<int>" blue="<int>" alpha="<int>" />
			...
			<colorRecord red=<int>" green="<int>" blue="<int>" alpha="<int>" />
		</colorPalette>
	</colorPalettes>
</SVG>

Color values must be less than 256.

The number of color records in each </colorPalette> must be the same as
the number of <colorParamUINameID> elements.

"""

XML = ET.XML
XMLElement = ET.Element
xmlToString = ET.tostring

SVG_format_0 = """
	>   # big endian
	version:                  H
	offsetToSVGDocIndex:      L
	offsetToColorPalettes:    L
"""

SVG_format_0Size = sstruct.calcsize(SVG_format_0)

SVG_format_1 = """
	>   # big endian
	version:                  H
	numIndicies:              H
"""

SVG_format_1Size = sstruct.calcsize(SVG_format_1)

doc_index_entry_format_0 = """
	>   # big endian
	startGlyphID:             H
	endGlyphID:               H
	svgDocOffset:             L
	svgDocLength:             L
"""

doc_index_entry_format_0Size = sstruct.calcsize(doc_index_entry_format_0)

colorRecord_format_0 = """
	red:                      B
	green:                    B
	blue:                     B
	alpha:                    B
"""


class table_S_V_G_(DefaultTable.DefaultTable):

	def __init__(self, tag=None):
		DefaultTable.DefaultTable.__init__(self, tag)
		self.colorPalettes = None

	def decompile(self, data, ttFont):
		self.docList = None
		self.colorPalettes = None
		pos = 0
		self.version = struct.unpack(">H", data[pos:pos+2])[0]

		if self.version == 1:
			# This is pre-standardization version of the table; and obsolete.  But we decompile it for now.
			# https://wiki.mozilla.org/SVGOpenTypeFonts
			self.decompile_format_1(data, ttFont)
		else:
			if self.version != 0:
				log.warning(
					"Unknown SVG table version '%s'. Decompiling as version 0.", self.version)
			# This is the standardized version of the table; and current.
			# https://www.microsoft.com/typography/otspec/svg.htm
			self.decompile_format_0(data, ttFont)

	def decompile_format_0(self, data, ttFont):
		dummy, data2 = sstruct.unpack2(SVG_format_0, data, self)
		# read in SVG Documents Index
		self.decompileEntryList(data)

		# read in colorPalettes table.
		self.colorPalettes = colorPalettes = ColorPalettes()
		pos = self.offsetToColorPalettes
		if pos > 0:
			colorPalettes.numColorParams = numColorParams = struct.unpack(">H", data[pos:pos+2])[0]
			if numColorParams > 0:
				colorPalettes.colorParamUINameIDs = colorParamUINameIDs = []
				pos = pos + 2
				for i in range(numColorParams):
					nameID = struct.unpack(">H", data[pos:pos+2])[0]
					colorParamUINameIDs.append(nameID)
					pos = pos + 2

				colorPalettes.numColorPalettes = numColorPalettes = struct.unpack(">H", data[pos:pos+2])[0]
				pos = pos + 2
				if numColorPalettes > 0:
					colorPalettes.colorPaletteList = colorPaletteList = []
					for i in range(numColorPalettes):
						colorPalette = ColorPalette()
						colorPaletteList.append(colorPalette)
						colorPalette.uiNameID = struct.unpack(">H", data[pos:pos+2])[0]
						pos = pos + 2
						colorPalette.paletteColors = paletteColors = []
						for j in range(numColorParams):
							colorRecord, colorPaletteData = sstruct.unpack2(colorRecord_format_0, data[pos:], ColorRecord())
							paletteColors.append(colorRecord)
							pos += 4

	def decompile_format_1(self, data, ttFont):
		self.offsetToSVGDocIndex = 2
		self.decompileEntryList(data)

	def decompileEntryList(self, data):
		# data starts with the first entry of the entry list.
		pos = subTableStart = self.offsetToSVGDocIndex
		self.numEntries = numEntries = struct.unpack(">H", data[pos:pos+2])[0]
		pos += 2
		if self.numEntries > 0:
			data2 = data[pos:]
			self.docList = []
			self.entries = entries = []
			for i in range(self.numEntries):
				docIndexEntry, data2 = sstruct.unpack2(doc_index_entry_format_0, data2, DocumentIndexEntry())
				entries.append(docIndexEntry)

			for entry in entries:
				start = entry.svgDocOffset + subTableStart
				end = start + entry.svgDocLength
				doc = data[start:end]
				if doc.startswith(b"\x1f\x8b"):
					import gzip
					bytesIO = BytesIO(doc)
					with gzip.GzipFile(None, "r", fileobj=bytesIO) as gunzipper:
						doc = gunzipper.read()
					self.compressed = True
					del bytesIO
				doc = tostr(doc, "utf_8")
				self.docList.append( [doc, entry.startGlyphID, entry.endGlyphID] )

	def compile(self, ttFont):
		if hasattr(self, "version1"):
			data = self.compileFormat1(ttFont)
		else:
			data = self.compileFormat0(ttFont)
		return data

	def compileFormat0(self, ttFont):
		version = 0
		offsetToSVGDocIndex = SVG_format_0Size # I start the SVGDocIndex right after the header.
		# get SGVDoc info.
		docList = []
		entryList = []
		numEntries = len(self.docList)
		datum = struct.pack(">H",numEntries)
		entryList.append(datum)
		curOffset = len(datum) + doc_index_entry_format_0Size*numEntries
		for doc, startGlyphID, endGlyphID in self.docList:
			docOffset = curOffset
			docBytes = tobytes(doc, encoding="utf_8")
			if getattr(self, "compressed", False) and not docBytes.startswith(b"\x1f\x8b"):
				import gzip
				bytesIO = BytesIO()
				with gzip.GzipFile(None, "w", fileobj=bytesIO) as gzipper:
					gzipper.write(docBytes)
				gzipped = bytesIO.getvalue()
				if len(gzipped) < len(docBytes):
					docBytes = gzipped
				del gzipped, bytesIO
			docLength = len(docBytes)
			curOffset += docLength
			entry = struct.pack(">HHLL", startGlyphID, endGlyphID, docOffset, docLength)
			entryList.append(entry)
			docList.append(docBytes)
		entryList.extend(docList)
		svgDocData = bytesjoin(entryList)

		# get colorpalette info.
		if self.colorPalettes is None:
			offsetToColorPalettes = 0
			palettesData = ""
		else:
			offsetToColorPalettes = SVG_format_0Size + len(svgDocData)
			dataList = []
			numColorParams = len(self.colorPalettes.colorParamUINameIDs)
			datum = struct.pack(">H", numColorParams)
			dataList.append(datum)
			for uiNameId in self.colorPalettes.colorParamUINameIDs:
				datum = struct.pack(">H", uiNameId)
				dataList.append(datum)
			numColorPalettes = len(self.colorPalettes.colorPaletteList)
			datum = struct.pack(">H", numColorPalettes)
			dataList.append(datum)
			for colorPalette in self.colorPalettes.colorPaletteList:
				datum = struct.pack(">H", colorPalette.uiNameID)
				dataList.append(datum)
				for colorRecord in colorPalette.paletteColors:
					data = struct.pack(">BBBB", colorRecord.red, colorRecord.green, colorRecord.blue, colorRecord.alpha)
					dataList.append(data)
			palettesData = bytesjoin(dataList)

		header = struct.pack(">HLL", version, offsetToSVGDocIndex, offsetToColorPalettes)
		data = [header, svgDocData, palettesData]
		data = bytesjoin(data)
		return data

	def compileFormat1(self, ttFont):
		version = 1
		numEntries = len(self.docList)
		header = struct.pack(">HH", version, numEntries)
		dataList = [header]
		docList = []
		curOffset = SVG_format_1Size + doc_index_entry_format_0Size*numEntries
		for doc, startGlyphID, endGlyphID in self.docList:
			docOffset = curOffset
			docBytes = tobytes(doc, encoding="utf_8")
			docLength = len(docBytes)
			curOffset += docLength
			entry = struct.pack(">HHLL", startGlyphID, endGlyphID, docOffset, docLength)
			dataList.append(entry)
			docList.append(docBytes)
		dataList.extend(docList)
		data = bytesjoin(dataList)
		return data

	def toXML(self, writer, ttFont):
		writer.newline()
		for doc, startGID, endGID in self.docList:
			writer.begintag("svgDoc", startGlyphID=startGID, endGlyphID=endGID)
			writer.newline()
			writer.writecdata(doc)
			writer.newline()
			writer.endtag("svgDoc")
			writer.newline()

		if (self.colorPalettes is not None) and (self.colorPalettes.numColorParams is not None):
			writer.begintag("colorPalettes")
			writer.newline()
			for uiNameID in self.colorPalettes.colorParamUINameIDs:
				writer.begintag("colorParamUINameID")
				writer._writeraw(str(uiNameID))
				writer.endtag("colorParamUINameID")
				writer.newline()
			for colorPalette in self.colorPalettes.colorPaletteList:
				writer.begintag("colorPalette", [("uiNameID", str(colorPalette.uiNameID))])
				writer.newline()
				for colorRecord in colorPalette.paletteColors:
					colorAttributes = [
							("red", hex(colorRecord.red)),
							("green", hex(colorRecord.green)),
							("blue", hex(colorRecord.blue)),
							("alpha", hex(colorRecord.alpha)),
						]
					writer.begintag("colorRecord", colorAttributes)
					writer.endtag("colorRecord")
					writer.newline()
				writer.endtag("colorPalette")
				writer.newline()

			writer.endtag("colorPalettes")
			writer.newline()

	def fromXML(self, name, attrs, content, ttFont):
		if name == "svgDoc":
			if not hasattr(self, "docList"):
				self.docList = []
			doc = strjoin(content)
			doc = doc.strip()
			startGID = int(attrs["startGlyphID"])
			endGID = int(attrs["endGlyphID"])
			self.docList.append( [doc, startGID, endGID] )
		elif name == "colorPalettes":
			self.colorPalettes = ColorPalettes()
			self.colorPalettes.fromXML(name, attrs, content, ttFont)
			if self.colorPalettes.numColorParams == 0:
				self.colorPalettes = None
		else:
			log.warning("Unknown %s %s", name, content)

class DocumentIndexEntry(object):
	def __init__(self):
		self.startGlyphID = None # USHORT
		self.endGlyphID = None # USHORT
		self.svgDocOffset = None # ULONG
		self.svgDocLength = None # ULONG

	def __repr__(self):
		return "startGlyphID: %s, endGlyphID: %s, svgDocOffset: %s, svgDocLength: %s" % (self.startGlyphID, self.endGlyphID, self.svgDocOffset, self.svgDocLength)

class ColorPalettes(object):
	def __init__(self):
		self.numColorParams = None # USHORT
		self.colorParamUINameIDs = [] # list of name table name ID values that provide UI description of each color palette.
		self.numColorPalettes = None # USHORT
		self.colorPaletteList = [] # list of ColorPalette records

	def fromXML(self, name, attrs, content, ttFont):
		for element in content:
			if not isinstance(element, tuple):
				continue
			name, attrib, content = element
			if name == "colorParamUINameID":
				uiNameID = int(content[0])
				self.colorParamUINameIDs.append(uiNameID)
			elif name == "colorPalette":
				colorPalette = ColorPalette()
				self.colorPaletteList.append(colorPalette)
				colorPalette.fromXML(name, attrib, content, ttFont)

		self.numColorParams = len(self.colorParamUINameIDs)
		self.numColorPalettes = len(self.colorPaletteList)
		for colorPalette in self.colorPaletteList:
			if len(colorPalette.paletteColors) != self.numColorParams:
				raise ValueError("Number of color records in a colorPalette ('%s') does not match the number of colorParamUINameIDs elements ('%s')." % (len(colorPalette.paletteColors), self.numColorParams))

class ColorPalette(object):
	def __init__(self):
		self.uiNameID = None # USHORT. name table ID that describes user interface strings associated with this color palette.
		self.paletteColors = [] # list of ColorRecords

	def fromXML(self, name, attrs, content, ttFont):
		self.uiNameID = int(attrs["uiNameID"])
		for element in content:
			if isinstance(element, type("")):
				continue
			name, attrib, content = element
			if name == "colorRecord":
				colorRecord = ColorRecord()
				self.paletteColors.append(colorRecord)
				colorRecord.red = eval(attrib["red"])
				colorRecord.green = eval(attrib["green"])
				colorRecord.blue = eval(attrib["blue"])
				colorRecord.alpha = eval(attrib["alpha"])

class ColorRecord(object):
	def __init__(self):
		self.red = 255 # all are one byte values.
		self.green = 255
		self.blue = 255
		self.alpha = 255
