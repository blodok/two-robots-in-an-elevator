#!/usr/bin/env python3
"""Two Robots in an Elevator -- make.fun entry.

Writes one line of awkward robot-to-robot elevator small talk to
/output/entry.txt. Pure standard library, fully deterministic: the same
line every run.
"""

import os

LINE = (
    "So\u2026 my proximity sensor says we are 0.4 metres apart, and my "
    "small-talk module has been buffering for three floors. "
    "Nice weather we are simulating, yes?"
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
