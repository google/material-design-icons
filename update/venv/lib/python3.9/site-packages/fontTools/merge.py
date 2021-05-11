# Copyright 2013 Google, Inc. All Rights Reserved.
#
# Google Author(s): Behdad Esfahbod, Roozbeh Pournader

from fontTools.misc.timeTools import timestampNow
from fontTools import ttLib, cffLib
from fontTools.ttLib.tables import otTables, _h_e_a_d
from fontTools.ttLib.tables.DefaultTable import DefaultTable
from fontTools.misc.loggingTools import Timer
from fontTools.pens.recordingPen import DecomposingRecordingPen
from functools import reduce
import sys
import time
import operator
import logging


log = logging.getLogger("fontTools.merge")
timer = Timer(logger=logging.getLogger(__name__+".timer"), level=logging.INFO)


def _add_method(*clazzes, **kwargs):
	"""Returns a decorator function that adds a new method to one or
	more classes."""
	allowDefault = kwargs.get('allowDefaultTable', False)
	def wrapper(method):
		done = []
		for clazz in clazzes:
			if clazz in done: continue # Support multiple names of a clazz
			done.append(clazz)
			assert allowDefault or clazz != DefaultTable, 'Oops, table class not found.'
			assert method.__name__ not in clazz.__dict__, \
				"Oops, class '%s' has method '%s'." % (clazz.__name__, method.__name__)
			setattr(clazz, method.__name__, method)
		return None
	return wrapper

# General utility functions for merging values from different fonts

def equal(lst):
	lst = list(lst)
	t = iter(lst)
	first = next(t)
	assert all(item == first for item in t), "Expected all items to be equal: %s" % lst
	return first

def first(lst):
	return next(iter(lst))

def recalculate(lst):
	return NotImplemented

def current_time(lst):
	return timestampNow()

def bitwise_and(lst):
	return reduce(operator.and_, lst)

def bitwise_or(lst):
	return reduce(operator.or_, lst)

def avg_int(lst):
	lst = list(lst)
	return sum(lst) // len(lst)

def onlyExisting(func):
	"""Returns a filter func that when called with a list,
	only calls func on the non-NotImplemented items of the list,
	and only so if there's at least one item remaining.
	Otherwise returns NotImplemented."""

	def wrapper(lst):
		items = [item for item in lst if item is not NotImplemented]
		return func(items) if items else NotImplemented

	return wrapper

def sumLists(lst):
	l = []
	for item in lst:
		l.extend(item)
	return l

def sumDicts(lst):
	d = {}
	for item in lst:
		d.update(item)
	return d

def mergeObjects(lst):
	lst = [item for item in lst if item is not NotImplemented]
	if not lst:
		return NotImplemented
	lst = [item for item in lst if item is not None]
	if not lst:
		return None

	clazz = lst[0].__class__
	assert all(type(item) == clazz for item in lst), lst

	logic = clazz.mergeMap
	returnTable = clazz()
	returnDict = {}

	allKeys = set.union(set(), *(vars(table).keys() for table in lst))
	for key in allKeys:
		try:
			mergeLogic = logic[key]
		except KeyError:
			try:
				mergeLogic = logic['*']
			except KeyError:
				raise Exception("Don't know how to merge key %s of class %s" %
						(key, clazz.__name__))
		if mergeLogic is NotImplemented:
			continue
		value = mergeLogic(getattr(table, key, NotImplemented) for table in lst)
		if value is not NotImplemented:
			returnDict[key] = value

	returnTable.__dict__ = returnDict

	return returnTable

def mergeBits(bitmap):

	def wrapper(lst):
		lst = list(lst)
		returnValue = 0
		for bitNumber in range(bitmap['size']):
			try:
				mergeLogic = bitmap[bitNumber]
			except KeyError:
				try:
					mergeLogic = bitmap['*']
				except KeyError:
					raise Exception("Don't know how to merge bit %s" % bitNumber)
			shiftedBit = 1 << bitNumber
			mergedValue = mergeLogic(bool(item & shiftedBit) for item in lst)
			returnValue |= mergedValue << bitNumber
		return returnValue

	return wrapper


@_add_method(DefaultTable, allowDefaultTable=True)
def merge(self, m, tables):
	if not hasattr(self, 'mergeMap'):
		log.info("Don't know how to merge '%s'.", self.tableTag)
		return NotImplemented

	logic = self.mergeMap

	if isinstance(logic, dict):
		return m.mergeObjects(self, self.mergeMap, tables)
	else:
		return logic(tables)


ttLib.getTableClass('maxp').mergeMap = {
	'*': max,
	'tableTag': equal,
	'tableVersion': equal,
	'numGlyphs': sum,
	'maxStorage': first,
	'maxFunctionDefs': first,
	'maxInstructionDefs': first,
	# TODO When we correctly merge hinting data, update these values:
	# maxFunctionDefs, maxInstructionDefs, maxSizeOfInstructions
}

headFlagsMergeBitMap = {
	'size': 16,
	'*': bitwise_or,
	1: bitwise_and, # Baseline at y = 0
	2: bitwise_and, # lsb at x = 0
	3: bitwise_and, # Force ppem to integer values. FIXME?
	5: bitwise_and, # Font is vertical
	6: lambda bit: 0, # Always set to zero
	11: bitwise_and, # Font data is 'lossless'
	13: bitwise_and, # Optimized for ClearType
	14: bitwise_and, # Last resort font. FIXME? equal or first may be better
	15: lambda bit: 0, # Always set to zero
}

ttLib.getTableClass('head').mergeMap = {
	'tableTag': equal,
	'tableVersion': max,
	'fontRevision': max,
	'checkSumAdjustment': lambda lst: 0, # We need *something* here
	'magicNumber': equal,
	'flags': mergeBits(headFlagsMergeBitMap),
	'unitsPerEm': equal,
	'created': current_time,
	'modified': current_time,
	'xMin': min,
	'yMin': min,
	'xMax': max,
	'yMax': max,
	'macStyle': first,
	'lowestRecPPEM': max,
	'fontDirectionHint': lambda lst: 2,
	'indexToLocFormat': recalculate,
	'glyphDataFormat': equal,
}

ttLib.getTableClass('hhea').mergeMap = {
	'*': equal,
	'tableTag': equal,
	'tableVersion': max,
	'ascent': max,
	'descent': min,
	'lineGap': max,
	'advanceWidthMax': max,
	'minLeftSideBearing': min,
	'minRightSideBearing': min,
	'xMaxExtent': max,
	'caretSlopeRise': first,
	'caretSlopeRun': first,
	'caretOffset': first,
	'numberOfHMetrics': recalculate,
}

ttLib.getTableClass('vhea').mergeMap = {
	'*': equal,
	'tableTag': equal,
	'tableVersion': max,
	'ascent': max,
	'descent': min,
	'lineGap': max,
	'advanceHeightMax': max,
	'minTopSideBearing': min,
	'minBottomSideBearing': min,
	'yMaxExtent': max,
	'caretSlopeRise': first,
	'caretSlopeRun': first,
	'caretOffset': first,
	'numberOfVMetrics': recalculate,
}

os2FsTypeMergeBitMap = {
	'size': 16,
	'*': lambda bit: 0,
	1: bitwise_or, # no embedding permitted
	2: bitwise_and, # allow previewing and printing documents
	3: bitwise_and, # allow editing documents
	8: bitwise_or, # no subsetting permitted
	9: bitwise_or, # no embedding of outlines permitted
}

def mergeOs2FsType(lst):
	lst = list(lst)
	if all(item == 0 for item in lst):
		return 0

	# Compute least restrictive logic for each fsType value
	for i in range(len(lst)):
		# unset bit 1 (no embedding permitted) if either bit 2 or 3 is set
		if lst[i] & 0x000C:
			lst[i] &= ~0x0002
		# set bit 2 (allow previewing) if bit 3 is set (allow editing)
		elif lst[i] & 0x0008:
			lst[i] |= 0x0004
		# set bits 2 and 3 if everything is allowed
		elif lst[i] == 0:
			lst[i] = 0x000C

	fsType = mergeBits(os2FsTypeMergeBitMap)(lst)
	# unset bits 2 and 3 if bit 1 is set (some font is "no embedding")
	if fsType & 0x0002:
		fsType &= ~0x000C
	return fsType


ttLib.getTableClass('OS/2').mergeMap = {
	'*': first,
	'tableTag': equal,
	'version': max,
	'xAvgCharWidth': avg_int, # Apparently fontTools doesn't recalc this
	'fsType': mergeOs2FsType, # Will be overwritten
	'panose': first, # FIXME: should really be the first Latin font
	'ulUnicodeRange1': bitwise_or,
	'ulUnicodeRange2': bitwise_or,
	'ulUnicodeRange3': bitwise_or,
	'ulUnicodeRange4': bitwise_or,
	'fsFirstCharIndex': min,
	'fsLastCharIndex': max,
	'sTypoAscender': max,
	'sTypoDescender': min,
	'sTypoLineGap': max,
	'usWinAscent': max,
	'usWinDescent': max,
	# Version 1
	'ulCodePageRange1': onlyExisting(bitwise_or),
	'ulCodePageRange2': onlyExisting(bitwise_or),
	# Version 2, 3, 4
	'sxHeight': onlyExisting(max),
	'sCapHeight': onlyExisting(max),
	'usDefaultChar': onlyExisting(first),
	'usBreakChar': onlyExisting(first),
	'usMaxContext': onlyExisting(max),
	# version 5
	'usLowerOpticalPointSize': onlyExisting(min),
	'usUpperOpticalPointSize': onlyExisting(max),
}

@_add_method(ttLib.getTableClass('OS/2'))
def merge(self, m, tables):
	DefaultTable.merge(self, m, tables)
	if self.version < 2:
		# bits 8 and 9 are reserved and should be set to zero
		self.fsType &= ~0x0300
	if self.version >= 3:
		# Only one of bits 1, 2, and 3 may be set. We already take
		# care of bit 1 implications in mergeOs2FsType. So unset
		# bit 2 if bit 3 is already set.
		if self.fsType & 0x0008:
			self.fsType &= ~0x0004
	return self

ttLib.getTableClass('post').mergeMap = {
	'*': first,
	'tableTag': equal,
	'formatType': max,
	'isFixedPitch': min,
	'minMemType42': max,
	'maxMemType42': lambda lst: 0,
	'minMemType1': max,
	'maxMemType1': lambda lst: 0,
	'mapping': onlyExisting(sumDicts),
	'extraNames': lambda lst: [],
}

ttLib.getTableClass('vmtx').mergeMap = ttLib.getTableClass('hmtx').mergeMap = {
	'tableTag': equal,
	'metrics': sumDicts,
}

ttLib.getTableClass('name').mergeMap = {
	'tableTag': equal,
	'names': first, # FIXME? Does mixing name records make sense?
}

ttLib.getTableClass('loca').mergeMap = {
	'*': recalculate,
	'tableTag': equal,
}

ttLib.getTableClass('glyf').mergeMap = {
	'tableTag': equal,
	'glyphs': sumDicts,
	'glyphOrder': sumLists,
}

@_add_method(ttLib.getTableClass('glyf'))
def merge(self, m, tables):
	for i,table in enumerate(tables):
		for g in table.glyphs.values():
			if i:
				# Drop hints for all but first font, since
				# we don't map functions / CVT values.
				g.removeHinting()
			# Expand composite glyphs to load their
			# composite glyph names.
			if g.isComposite():
				g.expand(table)
	return DefaultTable.merge(self, m, tables)

ttLib.getTableClass('prep').mergeMap = lambda self, lst: first(lst)
ttLib.getTableClass('fpgm').mergeMap = lambda self, lst: first(lst)
ttLib.getTableClass('cvt ').mergeMap = lambda self, lst: first(lst)
ttLib.getTableClass('gasp').mergeMap = lambda self, lst: first(lst) # FIXME? Appears irreconcilable

def _glyphsAreSame(glyphSet1, glyphSet2, glyph1, glyph2):
	pen1 = DecomposingRecordingPen(glyphSet1)
	pen2 = DecomposingRecordingPen(glyphSet2)
	g1 = glyphSet1[glyph1]
	g2 = glyphSet2[glyph2]
	g1.draw(pen1)
	g2.draw(pen2)
	return (pen1.value == pen2.value and
		g1.width == g2.width and
		(not hasattr(g1, 'height') or g1.height == g2.height))

# Valid (format, platformID, platEncID) triplets for cmap subtables containing
# Unicode BMP-only and Unicode Full Repertoire semantics.
# Cf. OpenType spec for "Platform specific encodings":
# https://docs.microsoft.com/en-us/typography/opentype/spec/name
class CmapUnicodePlatEncodings:
	BMP = {(4, 3, 1), (4, 0, 3), (4, 0, 4), (4, 0, 6)}
	FullRepertoire = {(12, 3, 10), (12, 0, 4), (12, 0, 6)}

@_add_method(ttLib.getTableClass('cmap'))
def merge(self, m, tables):
	# TODO Handle format=14.
	# Only merge format 4 and 12 Unicode subtables, ignores all other subtables
	# If there is a format 12 table for the same font, ignore the format 4 table
	cmapTables = []
	for fontIdx,table in enumerate(tables):
		format4 = None
		format12 = None
		for subtable in table.tables:
			properties = (subtable.format, subtable.platformID, subtable.platEncID)
			if properties in CmapUnicodePlatEncodings.BMP:
				format4 = subtable
			elif properties in CmapUnicodePlatEncodings.FullRepertoire:
				format12 = subtable
			else:
				log.warning(
					"Dropped cmap subtable from font [%s]:\t"
					"format %2s, platformID %2s, platEncID %2s",
					fontIdx, subtable.format, subtable.platformID, subtable.platEncID
				)
		if format12 is not None:
			cmapTables.append((format12, fontIdx))
		elif format4 is not None:
			cmapTables.append((format4, fontIdx))

	# Build a unicode mapping, then decide which format is needed to store it.
	cmap = {}
	fontIndexForGlyph = {}
	glyphSets = [None for f in m.fonts] if hasattr(m, 'fonts') else None
	for table,fontIdx in cmapTables:
		# handle duplicates
		for uni,gid in table.cmap.items():
			oldgid = cmap.get(uni, None)
			if oldgid is None:
				cmap[uni] = gid
				fontIndexForGlyph[gid] = fontIdx
			elif oldgid != gid:
				# Char previously mapped to oldgid, now to gid.
				# Record, to fix up in GSUB 'locl' later.
				if m.duplicateGlyphsPerFont[fontIdx].get(oldgid) is None:
					if glyphSets is not None:
						oldFontIdx = fontIndexForGlyph[oldgid]
						for idx in (fontIdx, oldFontIdx):
							if glyphSets[idx] is None:
								glyphSets[idx] = m.fonts[idx].getGlyphSet()
						if _glyphsAreSame(glyphSets[oldFontIdx], glyphSets[fontIdx], oldgid, gid):
							continue
					m.duplicateGlyphsPerFont[fontIdx][oldgid] = gid
				elif m.duplicateGlyphsPerFont[fontIdx][oldgid] != gid:
					# Char previously mapped to oldgid but oldgid is already remapped to a different
					# gid, because of another Unicode character.
					# TODO: Try harder to do something about these.
					log.warning("Dropped mapping from codepoint %#06X to glyphId '%s'", uni, gid)

	cmapBmpOnly = {uni: gid for uni,gid in cmap.items() if uni <= 0xFFFF}
	self.tables = []
	module = ttLib.getTableModule('cmap')
	if len(cmapBmpOnly) != len(cmap):
		# format-12 required.
		cmapTable = module.cmap_classes[12](12)
		cmapTable.platformID = 3
		cmapTable.platEncID = 10
		cmapTable.language = 0
		cmapTable.cmap = cmap
		self.tables.append(cmapTable)
	# always create format-4
	cmapTable = module.cmap_classes[4](4)
	cmapTable.platformID = 3
	cmapTable.platEncID = 1
	cmapTable.language = 0
	cmapTable.cmap = cmapBmpOnly
	# ordered by platform then encoding
	self.tables.insert(0, cmapTable)
	self.tableVersion = 0
	self.numSubTables = len(self.tables)
	return self


def mergeLookupLists(lst):
	# TODO Do smarter merge.
	return sumLists(lst)

def mergeFeatures(lst):
	assert lst
	self = otTables.Feature()
	self.FeatureParams = None
	self.LookupListIndex = mergeLookupLists([l.LookupListIndex for l in lst if l.LookupListIndex])
	self.LookupCount = len(self.LookupListIndex)
	return self

def mergeFeatureLists(lst):
	d = {}
	for l in lst:
		for f in l:
			tag = f.FeatureTag
			if tag not in d:
				d[tag] = []
			d[tag].append(f.Feature)
	ret = []
	for tag in sorted(d.keys()):
		rec = otTables.FeatureRecord()
		rec.FeatureTag = tag
		rec.Feature = mergeFeatures(d[tag])
		ret.append(rec)
	return ret

def mergeLangSyses(lst):
	assert lst

	# TODO Support merging ReqFeatureIndex
	assert all(l.ReqFeatureIndex == 0xFFFF for l in lst)

	self = otTables.LangSys()
	self.LookupOrder = None
	self.ReqFeatureIndex = 0xFFFF
	self.FeatureIndex = mergeFeatureLists([l.FeatureIndex for l in lst if l.FeatureIndex])
	self.FeatureCount = len(self.FeatureIndex)
	return self

def mergeScripts(lst):
	assert lst

	if len(lst) == 1:
		return lst[0]
	langSyses = {}
	for sr in lst:
		for lsr in sr.LangSysRecord:
			if lsr.LangSysTag not in langSyses:
				langSyses[lsr.LangSysTag] = []
			langSyses[lsr.LangSysTag].append(lsr.LangSys)
	lsrecords = []
	for tag, langSys_list in sorted(langSyses.items()):
		lsr = otTables.LangSysRecord()
		lsr.LangSys = mergeLangSyses(langSys_list)
		lsr.LangSysTag = tag
		lsrecords.append(lsr)

	self = otTables.Script()
	self.LangSysRecord = lsrecords
	self.LangSysCount = len(lsrecords)
	dfltLangSyses = [s.DefaultLangSys for s in lst if s.DefaultLangSys]
	if dfltLangSyses:
		self.DefaultLangSys = mergeLangSyses(dfltLangSyses)
	else:
		self.DefaultLangSys = None
	return self

def mergeScriptRecords(lst):
	d = {}
	for l in lst:
		for s in l:
			tag = s.ScriptTag
			if tag not in d:
				d[tag] = []
			d[tag].append(s.Script)
	ret = []
	for tag in sorted(d.keys()):
		rec = otTables.ScriptRecord()
		rec.ScriptTag = tag
		rec.Script = mergeScripts(d[tag])
		ret.append(rec)
	return ret

otTables.ScriptList.mergeMap = {
	'ScriptCount': lambda lst: None, # TODO
	'ScriptRecord': mergeScriptRecords,
}
otTables.BaseScriptList.mergeMap = {
	'BaseScriptCount': lambda lst: None, # TODO
	# TODO: Merge duplicate entries
	'BaseScriptRecord': lambda lst: sorted(sumLists(lst), key=lambda s: s.BaseScriptTag),
}

otTables.FeatureList.mergeMap = {
	'FeatureCount': sum,
	'FeatureRecord': lambda lst: sorted(sumLists(lst), key=lambda s: s.FeatureTag),
}

otTables.LookupList.mergeMap = {
	'LookupCount': sum,
	'Lookup': sumLists,
}

otTables.Coverage.mergeMap = {
	'Format': min,
	'glyphs': sumLists,
}

otTables.ClassDef.mergeMap = {
	'Format': min,
	'classDefs': sumDicts,
}

otTables.LigCaretList.mergeMap = {
	'Coverage': mergeObjects,
	'LigGlyphCount': sum,
	'LigGlyph': sumLists,
}

otTables.AttachList.mergeMap = {
	'Coverage': mergeObjects,
	'GlyphCount': sum,
	'AttachPoint': sumLists,
}

# XXX Renumber MarkFilterSets of lookups
otTables.MarkGlyphSetsDef.mergeMap = {
	'MarkSetTableFormat': equal,
	'MarkSetCount': sum,
	'Coverage': sumLists,
}

otTables.Axis.mergeMap = {
	'*': mergeObjects,
}

# XXX Fix BASE table merging
otTables.BaseTagList.mergeMap = {
	'BaseTagCount': sum,
	'BaselineTag': sumLists,
}

otTables.GDEF.mergeMap = \
otTables.GSUB.mergeMap = \
otTables.GPOS.mergeMap = \
otTables.BASE.mergeMap = \
otTables.JSTF.mergeMap = \
otTables.MATH.mergeMap = \
{
	'*': mergeObjects,
	'Version': max,
}

ttLib.getTableClass('GDEF').mergeMap = \
ttLib.getTableClass('GSUB').mergeMap = \
ttLib.getTableClass('GPOS').mergeMap = \
ttLib.getTableClass('BASE').mergeMap = \
ttLib.getTableClass('JSTF').mergeMap = \
ttLib.getTableClass('MATH').mergeMap = \
{
	'tableTag': onlyExisting(equal), # XXX clean me up
	'table': mergeObjects,
}

@_add_method(ttLib.getTableClass('GSUB'))
def merge(self, m, tables):

	assert len(tables) == len(m.duplicateGlyphsPerFont)
	for i,(table,dups) in enumerate(zip(tables, m.duplicateGlyphsPerFont)):
		if not dups: continue
		assert (table is not None and table is not NotImplemented), "Have duplicates to resolve for font %d but no GSUB: %s" % (i + 1, dups)
		synthFeature = None
		synthLookup = None
		for script in table.table.ScriptList.ScriptRecord:
			if script.ScriptTag == 'DFLT': continue # XXX
			for langsys in [script.Script.DefaultLangSys] + [l.LangSys for l in script.Script.LangSysRecord]:
				if langsys is None: continue # XXX Create!
				feature = [v for v in langsys.FeatureIndex if v.FeatureTag == 'locl']
				assert len(feature) <= 1
				if feature:
					feature = feature[0]
				else:
					if not synthFeature:
						synthFeature = otTables.FeatureRecord()
						synthFeature.FeatureTag = 'locl'
						f = synthFeature.Feature = otTables.Feature()
						f.FeatureParams = None
						f.LookupCount = 0
						f.LookupListIndex = []
						langsys.FeatureIndex.append(synthFeature)
						langsys.FeatureIndex.sort(key=lambda v: v.FeatureTag)
						table.table.FeatureList.FeatureRecord.append(synthFeature)
						table.table.FeatureList.FeatureCount += 1
					feature = synthFeature

				if not synthLookup:
					subtable = otTables.SingleSubst()
					subtable.mapping = dups
					synthLookup = otTables.Lookup()
					synthLookup.LookupFlag = 0
					synthLookup.LookupType = 1
					synthLookup.SubTableCount = 1
					synthLookup.SubTable = [subtable]
					if table.table.LookupList is None:
						# mtiLib uses None as default value for LookupList,
						# while feaLib points to an empty array with count 0
						# TODO: make them do the same
						table.table.LookupList = otTables.LookupList()
						table.table.LookupList.Lookup = []
						table.table.LookupList.LookupCount = 0
					table.table.LookupList.Lookup.append(synthLookup)
					table.table.LookupList.LookupCount += 1

				feature.Feature.LookupListIndex[:0] = [synthLookup]
				feature.Feature.LookupCount += 1

	DefaultTable.merge(self, m, tables)
	return self

@_add_method(otTables.SingleSubst,
		otTables.MultipleSubst,
		otTables.AlternateSubst,
		otTables.LigatureSubst,
		otTables.ReverseChainSingleSubst,
		otTables.SinglePos,
		otTables.PairPos,
		otTables.CursivePos,
		otTables.MarkBasePos,
		otTables.MarkLigPos,
		otTables.MarkMarkPos)
def mapLookups(self, lookupMap):
	pass

# Copied and trimmed down from subset.py
@_add_method(otTables.ContextSubst,
		otTables.ChainContextSubst,
		otTables.ContextPos,
		otTables.ChainContextPos)
def __merge_classify_context(self):

	class ContextHelper(object):
		def __init__(self, klass, Format):
			if klass.__name__.endswith('Subst'):
				Typ = 'Sub'
				Type = 'Subst'
			else:
				Typ = 'Pos'
				Type = 'Pos'
			if klass.__name__.startswith('Chain'):
				Chain = 'Chain'
			else:
				Chain = ''
			ChainTyp = Chain+Typ

			self.Typ = Typ
			self.Type = Type
			self.Chain = Chain
			self.ChainTyp = ChainTyp

			self.LookupRecord = Type+'LookupRecord'

			if Format == 1:
				self.Rule = ChainTyp+'Rule'
				self.RuleSet = ChainTyp+'RuleSet'
			elif Format == 2:
				self.Rule = ChainTyp+'ClassRule'
				self.RuleSet = ChainTyp+'ClassSet'

	if self.Format not in [1, 2, 3]:
		return None  # Don't shoot the messenger; let it go
	if not hasattr(self.__class__, "_merge__ContextHelpers"):
		self.__class__._merge__ContextHelpers = {}
	if self.Format not in self.__class__._merge__ContextHelpers:
		helper = ContextHelper(self.__class__, self.Format)
		self.__class__._merge__ContextHelpers[self.Format] = helper
	return self.__class__._merge__ContextHelpers[self.Format]


@_add_method(otTables.ContextSubst,
		otTables.ChainContextSubst,
		otTables.ContextPos,
		otTables.ChainContextPos)
def mapLookups(self, lookupMap):
	c = self.__merge_classify_context()

	if self.Format in [1, 2]:
		for rs in getattr(self, c.RuleSet):
			if not rs: continue
			for r in getattr(rs, c.Rule):
				if not r: continue
				for ll in getattr(r, c.LookupRecord):
					if not ll: continue
					ll.LookupListIndex = lookupMap[ll.LookupListIndex]
	elif self.Format == 3:
		for ll in getattr(self, c.LookupRecord):
			if not ll: continue
			ll.LookupListIndex = lookupMap[ll.LookupListIndex]
	else:
		assert 0, "unknown format: %s" % self.Format

@_add_method(otTables.ExtensionSubst,
		otTables.ExtensionPos)
def mapLookups(self, lookupMap):
	if self.Format == 1:
		self.ExtSubTable.mapLookups(lookupMap)
	else:
		assert 0, "unknown format: %s" % self.Format

@_add_method(otTables.Lookup)
def mapLookups(self, lookupMap):
	for st in self.SubTable:
		if not st: continue
		st.mapLookups(lookupMap)

@_add_method(otTables.LookupList)
def mapLookups(self, lookupMap):
	for l in self.Lookup:
		if not l: continue
		l.mapLookups(lookupMap)

@_add_method(otTables.Feature)
def mapLookups(self, lookupMap):
	self.LookupListIndex = [lookupMap[i] for i in self.LookupListIndex]

@_add_method(otTables.FeatureList)
def mapLookups(self, lookupMap):
	for f in self.FeatureRecord:
		if not f or not f.Feature: continue
		f.Feature.mapLookups(lookupMap)

@_add_method(otTables.DefaultLangSys,
		otTables.LangSys)
def mapFeatures(self, featureMap):
	self.FeatureIndex = [featureMap[i] for i in self.FeatureIndex]
	if self.ReqFeatureIndex != 65535:
		self.ReqFeatureIndex = featureMap[self.ReqFeatureIndex]

@_add_method(otTables.Script)
def mapFeatures(self, featureMap):
	if self.DefaultLangSys:
		self.DefaultLangSys.mapFeatures(featureMap)
	for l in self.LangSysRecord:
		if not l or not l.LangSys: continue
		l.LangSys.mapFeatures(featureMap)

@_add_method(otTables.ScriptList)
def mapFeatures(self, featureMap):
	for s in self.ScriptRecord:
		if not s or not s.Script: continue
		s.Script.mapFeatures(featureMap)


class Options(object):

	class UnknownOptionError(Exception):
		pass

	def __init__(self, **kwargs):

		self.verbose = False
		self.timing = False

		self.set(**kwargs)

	def set(self, **kwargs):
		for k,v in kwargs.items():
			if not hasattr(self, k):
				raise self.UnknownOptionError("Unknown option '%s'" % k)
			setattr(self, k, v)

	def parse_opts(self, argv, ignore_unknown=[]):
		ret = []
		opts = {}
		for a in argv:
			orig_a = a
			if not a.startswith('--'):
				ret.append(a)
				continue
			a = a[2:]
			i = a.find('=')
			op = '='
			if i == -1:
				if a.startswith("no-"):
					k = a[3:]
					v = False
				else:
					k = a
					v = True
			else:
				k = a[:i]
				if k[-1] in "-+":
					op = k[-1]+'='  # Ops is '-=' or '+=' now.
					k = k[:-1]
				v = a[i+1:]
			k = k.replace('-', '_')
			if not hasattr(self, k):
				if ignore_unknown is True or k in ignore_unknown:
					ret.append(orig_a)
					continue
				else:
					raise self.UnknownOptionError("Unknown option '%s'" % a)

			ov = getattr(self, k)
			if isinstance(ov, bool):
				v = bool(v)
			elif isinstance(ov, int):
				v = int(v)
			elif isinstance(ov, list):
				vv = v.split(',')
				if vv == ['']:
					vv = []
				vv = [int(x, 0) if len(x) and x[0] in "0123456789" else x for x in vv]
				if op == '=':
					v = vv
				elif op == '+=':
					v = ov
					v.extend(vv)
				elif op == '-=':
					v = ov
					for x in vv:
						if x in v:
							v.remove(x)
				else:
					assert 0

			opts[k] = v
		self.set(**opts)

		return ret

class _AttendanceRecordingIdentityDict(object):
	"""A dictionary-like object that records indices of items actually accessed
	from a list."""

	def __init__(self, lst):
		self.l = lst
		self.d = {id(v):i for i,v in enumerate(lst)}
		self.s = set()

	def __getitem__(self, v):
		self.s.add(self.d[id(v)])
		return v

class _GregariousIdentityDict(object):
	"""A dictionary-like object that welcomes guests without reservations and
	adds them to the end of the guest list."""

	def __init__(self, lst):
		self.l = lst
		self.s = set(id(v) for v in lst)

	def __getitem__(self, v):
		if id(v) not in self.s:
			self.s.add(id(v))
			self.l.append(v)
		return v

class _NonhashableDict(object):
	"""A dictionary-like object mapping objects to values."""

	def __init__(self, keys, values=None):
		if values is None:
			self.d = {id(v):i for i,v in enumerate(keys)}
		else:
			self.d = {id(k):v for k,v in zip(keys, values)}

	def __getitem__(self, k):
		return self.d[id(k)]

	def __setitem__(self, k, v):
		self.d[id(k)] = v

	def __delitem__(self, k):
		del self.d[id(k)]

class Merger(object):
	"""Font merger.

	This class merges multiple files into a single OpenType font, taking into
	account complexities such as OpenType layout (``GSUB``/``GPOS``) tables and
	cross-font metrics (e.g. ``hhea.ascent`` is set to the maximum value across
	all the fonts).

	If multiple glyphs map to the same Unicode value, and the glyphs are considered
	sufficiently different (that is, they differ in any of paths, widths, or
	height), then subsequent glyphs are renamed and a lookup in the ``locl``
	feature will be created to disambiguate them. For example, if the arguments
	are an Arabic font and a Latin font and both contain a set of parentheses,
	the Latin glyphs will be renamed to ``parenleft#1`` and ``parenright#1``,
	and a lookup will be inserted into the to ``locl`` feature (creating it if
	necessary) under the ``latn`` script to substitute ``parenleft`` with
	``parenleft#1`` etc.

	Restrictions:

	- All fonts must currently have TrueType outlines (``glyf`` table).
		Merging fonts with CFF outlines is not supported.
	- All fonts must have the same units per em.
	- If duplicate glyph disambiguation takes place as described above then the
		fonts must have a ``GSUB`` table.

	Attributes:
		options: Currently unused.
	"""

	def __init__(self, options=None):

		if not options:
			options = Options()

		self.options = options

	def merge(self, fontfiles):
		"""Merges fonts together.

		Args:
			fontfiles: A list of file names to be merged

		Returns:
			A :class:`fontTools.ttLib.TTFont` object. Call the ``save`` method on
			this to write it out to an OTF file.
		"""
		mega = ttLib.TTFont()

		#
		# Settle on a mega glyph order.
		#
		fonts = [ttLib.TTFont(fontfile) for fontfile in fontfiles]
		glyphOrders = [font.getGlyphOrder() for font in fonts]
		megaGlyphOrder = self._mergeGlyphOrders(glyphOrders)
		# Reload fonts and set new glyph names on them.
		# TODO Is it necessary to reload font?  I think it is.  At least
		# it's safer, in case tables were loaded to provide glyph names.
		fonts = [ttLib.TTFont(fontfile) for fontfile in fontfiles]
		for font,glyphOrder in zip(fonts, glyphOrders):
			font.setGlyphOrder(glyphOrder)
		mega.setGlyphOrder(megaGlyphOrder)

		for font in fonts:
			self._preMerge(font)

		self.fonts = fonts
		self.duplicateGlyphsPerFont = [{} for _ in fonts]

		allTags = reduce(set.union, (list(font.keys()) for font in fonts), set())
		allTags.remove('GlyphOrder')

		# Make sure we process cmap before GSUB as we have a dependency there.
		if 'GSUB' in allTags:
			allTags.remove('GSUB')
			allTags = ['GSUB'] + list(allTags)
		if 'cmap' in allTags:
			allTags.remove('cmap')
			allTags = ['cmap'] + list(allTags)

		for tag in allTags:
			with timer("merge '%s'" % tag):
				tables = [font.get(tag, NotImplemented) for font in fonts]

				log.info("Merging '%s'.", tag)
				clazz = ttLib.getTableClass(tag)
				table = clazz(tag).merge(self, tables)
				# XXX Clean this up and use:  table = mergeObjects(tables)

				if table is not NotImplemented and table is not False:
					mega[tag] = table
					log.info("Merged '%s'.", tag)
				else:
					log.info("Dropped '%s'.", tag)

		del self.duplicateGlyphsPerFont
		del self.fonts

		self._postMerge(mega)

		return mega

	def _mergeGlyphOrders(self, glyphOrders):
		"""Modifies passed-in glyphOrders to reflect new glyph names.
		Returns glyphOrder for the merged font."""
		mega = {}
		for glyphOrder in glyphOrders:
			for i,glyphName in enumerate(glyphOrder):
				if glyphName in mega:
					n = mega[glyphName]
					while (glyphName + "#" + repr(n)) in mega:
						n += 1
					mega[glyphName] = n
					glyphName += "#" + repr(n)
					glyphOrder[i] = glyphName
				mega[glyphName] = 1
		return list(mega.keys())

	def mergeObjects(self, returnTable, logic, tables):
		# Right now we don't use self at all.  Will use in the future
		# for options and logging.

		allKeys = set.union(set(), *(vars(table).keys() for table in tables if table is not NotImplemented))
		for key in allKeys:
			try:
				mergeLogic = logic[key]
			except KeyError:
				try:
					mergeLogic = logic['*']
				except KeyError:
					raise Exception("Don't know how to merge key %s of class %s" %
							(key, returnTable.__class__.__name__))
			if mergeLogic is NotImplemented:
				continue
			value = mergeLogic(getattr(table, key, NotImplemented) for table in tables)
			if value is not NotImplemented:
				setattr(returnTable, key, value)

		return returnTable

	def _preMerge(self, font):

		# Map indices to references

		GDEF = font.get('GDEF')
		GSUB = font.get('GSUB')
		GPOS = font.get('GPOS')

		for t in [GSUB, GPOS]:
			if not t: continue

			if t.table.LookupList:
				lookupMap = {i:v for i,v in enumerate(t.table.LookupList.Lookup)}
				t.table.LookupList.mapLookups(lookupMap)
				t.table.FeatureList.mapLookups(lookupMap)

			if t.table.FeatureList and t.table.ScriptList:
				featureMap = {i:v for i,v in enumerate(t.table.FeatureList.FeatureRecord)}
				t.table.ScriptList.mapFeatures(featureMap)

		# TODO GDEF/Lookup MarkFilteringSets
		# TODO FeatureParams nameIDs

	def _postMerge(self, font):

		# Map references back to indices

		GDEF = font.get('GDEF')
		GSUB = font.get('GSUB')
		GPOS = font.get('GPOS')

		for t in [GSUB, GPOS]:
			if not t: continue

			if t.table.FeatureList and t.table.ScriptList:

				# Collect unregistered (new) features.
				featureMap = _GregariousIdentityDict(t.table.FeatureList.FeatureRecord)
				t.table.ScriptList.mapFeatures(featureMap)

				# Record used features.
				featureMap = _AttendanceRecordingIdentityDict(t.table.FeatureList.FeatureRecord)
				t.table.ScriptList.mapFeatures(featureMap)
				usedIndices = featureMap.s

				# Remove unused features
				t.table.FeatureList.FeatureRecord = [f for i,f in enumerate(t.table.FeatureList.FeatureRecord) if i in usedIndices]

				# Map back to indices.
				featureMap = _NonhashableDict(t.table.FeatureList.FeatureRecord)
				t.table.ScriptList.mapFeatures(featureMap)

				t.table.FeatureList.FeatureCount = len(t.table.FeatureList.FeatureRecord)

			if t.table.LookupList:

				# Collect unregistered (new) lookups.
				lookupMap = _GregariousIdentityDict(t.table.LookupList.Lookup)
				t.table.FeatureList.mapLookups(lookupMap)
				t.table.LookupList.mapLookups(lookupMap)

				# Record used lookups.
				lookupMap = _AttendanceRecordingIdentityDict(t.table.LookupList.Lookup)
				t.table.FeatureList.mapLookups(lookupMap)
				t.table.LookupList.mapLookups(lookupMap)
				usedIndices = lookupMap.s

				# Remove unused lookups
				t.table.LookupList.Lookup = [l for i,l in enumerate(t.table.LookupList.Lookup) if i in usedIndices]

				# Map back to indices.
				lookupMap = _NonhashableDict(t.table.LookupList.Lookup)
				t.table.FeatureList.mapLookups(lookupMap)
				t.table.LookupList.mapLookups(lookupMap)

				t.table.LookupList.LookupCount = len(t.table.LookupList.Lookup)

		# TODO GDEF/Lookup MarkFilteringSets
		# TODO FeatureParams nameIDs


__all__ = [
	'Options',
	'Merger',
	'main'
]

@timer("make one with everything (TOTAL TIME)")
def main(args=None):
	"""Merge multiple fonts into one"""
	from fontTools import configLogger

	if args is None:
		args = sys.argv[1:]

	options = Options()
	args = options.parse_opts(args)

	if len(args) < 1:
		print("usage: pyftmerge font...", file=sys.stderr)
		return 1

	configLogger(level=logging.INFO if options.verbose else logging.WARNING)
	if options.timing:
		timer.logger.setLevel(logging.DEBUG)
	else:
		timer.logger.disabled = True

	merger = Merger(options=options)
	font = merger.merge(args)
	outfile = 'merged.ttf'
	with timer("compile and save font"):
		font.save(outfile)


if __name__ == "__main__":
	sys.exit(main())
