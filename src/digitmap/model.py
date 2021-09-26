from typing import Iterable
from typing import Union


class Element:
    pass


class Digit:
    def __init__(self, value: str):
        if len(value) != 1 or not value.isdigit():
            raise ValueError("value must be a single-character string with a digit 0-9")
        self._value = value

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.value == other.value
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._value!r})"

    def __str__(self) -> str:
        return self._value

    @property
    def value(self) -> str:
        return self._value


class DtmfElement(Element):
    def __init__(self, value: str):
        if len(value) != 1 or value not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f", "#", "*"]:
            raise ValueError("value must be a single-character string with a digit 0-9, letter A-D/a-d, #, or *")
        self._value = value

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.value == other.value
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._value!r})"

    def __str__(self) -> str:
        return self._value

    @property
    def value(self) -> str:
        return self._value


class TimerElement(Element):
    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def __str__(self) -> str:
        return "T"


class WildcardElement(Element):
    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def __str__(self) -> str:
        return "x"


class SubRange():
    def __init__(self, start: Digit = None, end: Digit = None):
        self.end = end
        self.start = start

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.start == other.start and
            self.end == other.end
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.start!r}, {self.end!r})"

    def __str__(self) -> str:
        return f"{self.start!s}-{self.end!s}"


RangeItem = Union[Digit, SubRange]


class RangeElement(Element):
    def __init__(self, items: Iterable[RangeItem]):
        self._items = list(items)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.items == other.items
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._items!r})"

    def __str__(self) -> str:
        return f"[{''.join(map(str, self._items))}]"

    @property
    def items(self) -> Iterable[RangeItem]:
        return self._items


class PositionElement(Element):
    def __init__(self, element: Element = None):
        self.element = element

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.element == other.element
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.element!r})"

    def __str__(self) -> str:
        return f"{self.element!s}."


class DigitMapString:
    def __init__(self, elements: Iterable[Element]):
        self._elements = list(elements)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.elements == other.elements
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._elements!r})"

    def __str__(self) -> str:
        return ''.join(map(str, self._elements))

    @property
    def elements(self) -> Iterable[Element]:
        return self._elements


class DigitMap:
    def __init__(self, strings: Iterable[DigitMapString]):
        self._strings = list(strings)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.strings == other.strings
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._strings!r})"

    def __str__(self) -> str:
        if len(self._strings) == 1:
            return str(self._strings[0])
        return f"({'|'.join(map(str, self._strings))})"

    @property
    def strings(self) -> Iterable[DigitMapString]:
        return self._strings
