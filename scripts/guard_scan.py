#!/usr/bin/env python3
"""Scan text on stdin for the high-signal guard patterns in guard_patterns.txt.

Exit 1 when any pattern matches, 0 otherwise. Matched text is never printed:
a hit may be a real credential, and workflow logs are public.
"""

from __future__ import annotations

import pathlib
import re
import sys


def load_patterns() -> list[re.Pattern[str]]:
    path = pathlib.Path(__file__).with_name("guard_patterns.txt")
    patterns: list[re.Pattern[str]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        try:
            patterns.append(re.compile(line))
        except re.error as exc:
            raise SystemExit(f"guard: invalid pattern {line!r}: {exc}") from exc
    if not patterns:
        raise SystemExit("guard: no patterns loaded")
    return patterns


def main() -> int:
    text = sys.stdin.read()
    patterns = load_patterns()
    hits = [index for index, pattern in enumerate(patterns, start=1) if pattern.search(text)]
    if hits:
        listed = ", ".join(f"#{index}" for index in hits)
        print(f"guard: blocked by pattern(s) {listed}")
        return 1
    print("guard: no matches")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
