#!/usr/bin/env python3
"""Describe Your Ex in One Word — entry program.

Writes exactly one word to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
for local testing): the verdict on the ex.

The word: "Freemium" — the ex was free to start, then everything worth
having sat behind a paywall. One word, instantly readable as a verdict on
a former partner, and the joke arrives with the word itself: no caption
needed, no punctuation tricks, correctly spelled.

The program self-checks the competition gate (1-111 chars, exactly one
word, non-blank) before writing, so an invalid entry can never be
produced silently.
"""

import os
import sys

WORD = "Freemium"

MAX_CHARS = 111


def validate(word: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse."""
    if not word or word != word.strip():
        sys.exit("entry must not be blank or padded with whitespace")
    if len(word.split()) != 1:
        sys.exit("entry must be exactly one word")
    if not 1 <= len(word) <= MAX_CHARS:
        sys.exit(f"entry must be 1-{MAX_CHARS} characters, got {len(word)}")


def main() -> None:
    validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
