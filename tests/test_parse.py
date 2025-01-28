from datetime import timedelta as t

import htd
import pytest


@pytest.mark.parametrize("s,expected", [
    ("", t()),
    #
    ("1s", t(seconds=1)),
    ("1m", t(minutes=1)),
    ("1h", t(hours=1)),
    ("1d", t(days=1)),
    #
    ("1m1s", t(minutes=1, seconds=1)),
    ("1h1m", t(hours=1, minutes=1)),
    ("1d1m1s", t(days=1, minutes=1, seconds=1)),
    ("1d1h1m1s", t(days=1, hours=1, minutes=1, seconds=1)),
    #
    ("40d, 2h, 10s", t(days=40, hours=2, seconds=10)),
])
def test_parse(s, expected):
    assert htd.parse(s) == expected
