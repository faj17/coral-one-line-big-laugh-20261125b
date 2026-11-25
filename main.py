#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun entry.

Writes a single original funny line to /output/entry.txt.
The line is built from fragments so the setup and the turn stay
separate in the source; assemble() joins them into the final line.
"""

import os

SETUP = "My calendar reminded me to relax, so I scheduled "
PUNCH = "worrying about relaxing for Thursday."


def assemble():
    return SETUP + PUNCH


def validate(text):
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def main():
    line = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
