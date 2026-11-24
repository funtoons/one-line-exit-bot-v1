#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter.

Writes exactly one line of text to /output/entry.txt (no trailing
newline) and prints the same line to stdout. Deterministic and
offline: no randomness, no network, no timestamps.
"""

import os

LINE = (
    "Dear Mr. Alvarez, I resign as night-shift lighthouse keeper, "
    "effective immediately, because after six years I have seen the light."
)


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
