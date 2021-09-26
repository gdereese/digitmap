import re
from typing import Iterable
from typing import NamedTuple

from ._translator import translate


class DigitMapResult(NamedTuple):
    full_matches: Iterable[str]
    partial_matches: Iterable[str]


def match(expr: str, dial_str: str) -> DigitMapResult:
    string_patterns = translate(expr)

    full_matches = []
    partial_matches = []
    for string, pattern in string_patterns:
        pattern_match = re.fullmatch(pattern, dial_str)

        if not pattern_match:
            continue

        if None in pattern_match.groups():
            partial_matches.append(string)
        else:
            full_matches.append(string)

    if not full_matches and not partial_matches:
        return None

    return DigitMapResult(full_matches, partial_matches)
