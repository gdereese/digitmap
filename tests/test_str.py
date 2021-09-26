from digitmap.model import Digit
from digitmap.model import DigitMap
from digitmap.model import DigitMapString
from digitmap.model import DtmfElement
from digitmap.model import PositionElement
from digitmap.model import RangeElement
from digitmap.model import WildcardElement


def test_str_1():
    obj = DigitMap([
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

    result = str(obj)

    assert result == "(xxxxxxx|x11)"


def test_str_2():
    obj = DigitMap([
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

    result = str(obj)

    assert result == "(0[12].|00|1[12].1|2x.#)"
