"""
colorLib.table_builder: Generic helper for filling in BaseTable derivatives from tuples and maps and such.

"""

import collections
import enum
from fontTools.ttLib.tables.otBase import (
    BaseTable,
    FormatSwitchingBaseTable,
    UInt8FormatSwitchingBaseTable,
)
from fontTools.ttLib.tables.otConverters import (
    ComputedInt,
    SimpleValue,
    Struct,
    Short,
    UInt8,
    UShort,
    VarInt16,
    VarUInt16,
    IntValue,
    FloatValue,
)
from fontTools.misc.roundTools import otRound


class BuildCallback(enum.Enum):
    """Keyed on (BEFORE_BUILD, class[, Format if available]).
    Receives (dest, source).
    Should return (dest, source), which can be new objects.
    """

    BEFORE_BUILD = enum.auto()

    """Keyed on (AFTER_BUILD, class[, Format if available]).
    Receives (dest).
    Should return dest, which can be a new object.
    """
    AFTER_BUILD = enum.auto()

    """Keyed on (CREATE_DEFAULT, class).
    Receives no arguments.
    Should return a new instance of class.
    """
    CREATE_DEFAULT = enum.auto()


def _assignable(convertersByName):
    return {k: v for k, v in convertersByName.items() if not isinstance(v, ComputedInt)}


def convertTupleClass(tupleClass, value):
    if isinstance(value, tupleClass):
        return value
    if isinstance(value, tuple):
        return tupleClass(*value)
    return tupleClass(value)


def _isNonStrSequence(value):
    return isinstance(value, collections.abc.Sequence) and not isinstance(value, str)


def _set_format(dest, source):
    if _isNonStrSequence(source):
        assert len(source) > 0, f"{type(dest)} needs at least format from {source}"
        dest.Format = source[0]
        source = source[1:]
    elif isinstance(source, collections.abc.Mapping):
        assert "Format" in source, f"{type(dest)} needs at least Format from {source}"
        dest.Format = source["Format"]
    else:
        raise ValueError(f"Not sure how to populate {type(dest)} from {source}")

    assert isinstance(
        dest.Format, collections.abc.Hashable
    ), f"{type(dest)} Format is not hashable: {dest.Format}"
    assert (
        dest.Format in dest.convertersByName
    ), f"{dest.Format} invalid Format of {cls}"

    return source


class TableBuilder:
    """
    Helps to populate things derived from BaseTable from maps, tuples, etc.

    A table of lifecycle callbacks may be provided to add logic beyond what is possible
    based on otData info for the target class. See BuildCallbacks.
    """

    def __init__(self, callbackTable=None):
        if callbackTable is None:
            callbackTable = {}
        self._callbackTable = callbackTable

    def _convert(self, dest, field, converter, value):
        tupleClass = getattr(converter, "tupleClass", None)
        enumClass = getattr(converter, "enumClass", None)

        if tupleClass:
            value = convertTupleClass(tupleClass, value)

        elif enumClass:
            if isinstance(value, enumClass):
                pass
            elif isinstance(value, str):
                try:
                    value = getattr(enumClass, value.upper())
                except AttributeError:
                    raise ValueError(f"{value} is not a valid {enumClass}")
            else:
                value = enumClass(value)

        elif isinstance(converter, IntValue):
            value = otRound(value)
        elif isinstance(converter, FloatValue):
            value = float(value)

        elif isinstance(converter, Struct):
            if converter.repeat:
                if _isNonStrSequence(value):
                    value = [self.build(converter.tableClass, v) for v in value]
                else:
                    value = [self.build(converter.tableClass, value)]
                setattr(dest, converter.repeat, len(value))
            else:
                value = self.build(converter.tableClass, value)
        elif callable(converter):
            value = converter(value)

        setattr(dest, field, value)

    def build(self, cls, source):
        assert issubclass(cls, BaseTable)

        if isinstance(source, cls):
            return source

        callbackKey = (cls,)
        dest = self._callbackTable.get(
            (BuildCallback.CREATE_DEFAULT,) + callbackKey, lambda: cls()
        )()
        assert isinstance(dest, cls)

        convByName = _assignable(cls.convertersByName)
        skippedFields = set()

        # For format switchers we need to resolve converters based on format
        if issubclass(cls, FormatSwitchingBaseTable):
            source = _set_format(dest, source)

            convByName = _assignable(convByName[dest.Format])
            skippedFields.add("Format")
            callbackKey = (cls, dest.Format)

        # Convert sequence => mapping so before thunk only has to handle one format
        if _isNonStrSequence(source):
            # Sequence (typically list or tuple) assumed to match fields in declaration order
            assert len(source) <= len(
                convByName
            ), f"Sequence of {len(source)} too long for {cls}; expected <= {len(convByName)} values"
            source = dict(zip(convByName.keys(), source))

        dest, source = self._callbackTable.get(
            (BuildCallback.BEFORE_BUILD,) + callbackKey, lambda d, s: (d, s)
        )(dest, source)

        if isinstance(source, collections.abc.Mapping):
            for field, value in source.items():
                if field in skippedFields:
                    continue
                converter = convByName.get(field, None)
                if not converter:
                    raise ValueError(
                        f"Unrecognized field {field} for {cls}; expected one of {sorted(convByName.keys())}"
                    )
                self._convert(dest, field, converter, value)
        else:
            # let's try as a 1-tuple
            dest = self.build(cls, (source,))

        dest = self._callbackTable.get(
            (BuildCallback.AFTER_BUILD,) + callbackKey, lambda d: d
        )(dest)

        return dest


class TableUnbuilder:
    def __init__(self, callbackTable=None):
        if callbackTable is None:
            callbackTable = {}
        self._callbackTable = callbackTable

    def unbuild(self, table):
        assert isinstance(table, BaseTable)

        source = {}

        callbackKey = (type(table),)
        if isinstance(table, FormatSwitchingBaseTable):
            source["Format"] = int(table.Format)
            callbackKey += (table.Format,)

        for converter in table.getConverters():
            if isinstance(converter, ComputedInt):
                continue
            value = getattr(table, converter.name)

            tupleClass = getattr(converter, "tupleClass", None)
            enumClass = getattr(converter, "enumClass", None)
            if tupleClass:
                source[converter.name] = tuple(value)
            elif enumClass:
                source[converter.name] = value.name.lower()
            elif isinstance(converter, Struct):
                if converter.repeat:
                    source[converter.name] = [self.unbuild(v) for v in value]
                else:
                    source[converter.name] = self.unbuild(value)
            elif isinstance(converter, SimpleValue):
                # "simple" values (e.g. int, float, str) need no further un-building
                source[converter.name] = value
            else:
                raise NotImplementedError(
                    "Don't know how unbuild {value!r} with {converter!r}"
                )

        source = self._callbackTable.get(callbackKey, lambda s: s)(source)

        return source
