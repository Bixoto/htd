import re
from datetime import timedelta

__all__ = ['parse', '__version__']
__version__ = '0.0.1'

SYMBOLS = {
    "s": 1,
    "m": 60,
    "h": 60 * 60,
    "d": 60 * 60 * 24,
    "w": 60 * 60 * 24 * 7,
}

RE = re.compile(rf"(\d+(?:\.\d+)?[{''.join(SYMBOLS)}])")


def parse(s: str) -> timedelta:
    """
    Parse a string such as `"2d4h10s"` and return a `datetime.timedelta` object.
    """
    total_seconds = 0.0
    for fragment in RE.findall(s):
        unit = fragment[-1]
        total_seconds += float(fragment[:-1]) * SYMBOLS[unit]

    return timedelta(seconds=total_seconds)
