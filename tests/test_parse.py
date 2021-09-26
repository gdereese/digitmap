from digitmap import parse
from digitmap.model import Digit
from digitmap.model import DigitMap
from digitmap.model import DigitMapString
from digitmap.model import DtmfElement
from digitmap.model import PositionElement
from digitmap.model import RangeElement
from digitmap.model import WildcardElement


def test_parse_1():
    expr = "(xxxxxxx|x11)"

    result = parse(expr)

    assert result == DigitMap([
        DigitMapString([
            WildcardElement(),
            WildcardElement(),
            WildcardElement(),
            WildcardElement(),
            WildcardElement(),
            WildcardElement(),
            WildcardElement()
        ]),
        DigitMapString([
            WildcardElement(),
            DtmfElement("1"),
            DtmfElement("1")
        ])
    ])


def test_parse_2():
    expr = "(0[12].|00|1[12].1|2x.#)"

    result = parse(expr)

    assert result == DigitMap([
        DigitMapString([
            DtmfElement("0"),
            PositionElement(
                RangeElement([
                    Digit("1"),
                    Digit("2")
                ])
            )
        ]),
        DigitMapString([
            DtmfElement("0"),
            DtmfElement("0")
        ]),
        DigitMapString([
            DtmfElement("1"),
            PositionElement(
                RangeElement([
                    Digit("1"),
                    Digit("2")
                ])
            ),
            DtmfElement("1")
        ]),
        DigitMapString([
            DtmfElement("2"),
            PositionElement(
                WildcardElement()
            ),
            DtmfElement("#")
        ])
    ])
