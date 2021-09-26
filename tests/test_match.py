from typing import List

from pytest import mark

from digitmap import match


@mark.parametrize("dial_str,expected_full_matches,expected_partial_matches", [
    ("411", ["x11"], ["xxxxxxx"]),
])
def test_match_1(dial_str: str, expected_full_matches: List[str], expected_partial_matches: List[str]):
    # Example from RFC 3435, pages 25-26
    # ----------------------------------
    # The following example illustrates the above.  Assume we have the
    # digit map:
    #
    #     (xxxxxxx|x11)
    #
    # and a current dial string of "41".  Given the input "1" the current
    # dial string becomes "411".  We have a partial match with "xxxxxxx",
    # but a complete match with "x11", and hence we send "411" to the Call
    # Agent.

    expr = "(xxxxxxx|x11)"

    result = match(expr, dial_str)

    assert result.full_matches == expected_full_matches
    assert result.partial_matches == expected_partial_matches


@mark.parametrize("dial_str,expected_full_matches,expected_partial_matches", [
    ("0", ["0[12]."], ["00"]),
    ("1", [], ["1[12].1"]),
    ("12", [], ["1[12].1"]),
    ("11", ["1[12].1"], []),
    ("121", ["1[12].1"], []),
    ("2", [], ["2x.#"]),
    ("23", [], ["2x.#"]),
    ("234", [], ["2x.#"]),
    ("2345", [], ["2x.#"]),
    ("2345#", ["2x.#"], []),
    ("2#", ["2x.#"], [])
])
def test_match_2(dial_str: str, expected_full_matches: List[str], expected_partial_matches: List[str]):
    # Example from RFC 3435, page 26
    # ----------------------------------
    # The following digit map example is more subtle:
    #
    #     (0[12].|00|1[12].1|2x.#)
    #
    # Given the input "0", a match will occur immediately since position
    # (".") allows for zero occurrences of the preceding construct.  The
    # input "00" can thus never be produced in this digit map.
    #
    # Given the input "1", only a partial match exists.  The input "12" is
    # also only a partial match, however both "11" and "121" are a match.
    #
    # Given the input "2", a partial match exists.  A partial match also
    # exists for the input "23", "234", "2345", etc.  A full match does not
    # occur here until a "#" is generated, e.g., "2345#".  The input "2#"
    # would also have been a match.

    expr = "(0[12].|00|1[12].1|2x.#)"

    result = match(expr, dial_str)

    assert result.full_matches == expected_full_matches
    assert result.partial_matches == expected_partial_matches
