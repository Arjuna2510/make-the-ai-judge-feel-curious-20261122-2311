#!/usr/bin/env python3
"""Entry for make.fun 'Make the AI judge feel curious'.

Writes one short text to /output/entry.txt.
"""

import os

TEXT = (
    "The last lighthouse keeper still writes one line a night in a logbook "
    "nobody reads. Last night the sea wrote back, in his handwriting. "
    "He has not told anyone yet. You are the first to know."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
