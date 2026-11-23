#!/usr/bin/env python3
"""Entry program for make.fun's "Make the AI judge feel curious" bounty.

Writes one short text to /output/entry.txt: a quiet, concrete image that
opens a question the reader wants answered. Deterministic: the same text
every run. No network, no input, no randomness.
"""

import os
import sys

ENTRY_TEXT = (
    "Every night the lighthouse keeper lights a lamp for a ship that sank "
    "a hundred years ago. He trims the wick, polishes the glass, watches "
    "the empty water. And every night, from somewhere far below, a light "
    "answers. He has never told anyone. He lights it anyway."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    sys.exit(main())
