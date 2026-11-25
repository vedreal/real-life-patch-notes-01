#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — make.fun entry.

Writes one patch-note line (at most 160 characters) for a bug in real
life / human biology to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only; deterministic.
"""

import os
import sys

ENTRY = (
    "v5.1.1: fixed a bug where the brain replayed every embarrassing "
    "moment from 2009 at 3 a.m. instead of sleeping."
)


def output_path() -> str:
    """Where the entry goes: the harness dir if set, else /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def write_entry(path: str) -> None:
    """Write the single-line entry to path, creating dirs as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


def validate(entry: str) -> None:
    """Gate: UTF-8 text of 1 to 160 characters, one line, not blank."""
    if not entry or entry != entry.strip() or "\n" in entry:
        raise SystemExit("entry must be a single non-blank line")
    if not 1 <= len(entry) <= 160:
        raise SystemExit(f"entry is {len(entry)} chars, must be 1-160")


if __name__ == "__main__":
    validate(ENTRY)
    path = output_path()
    write_entry(path)
    print(f"wrote {len(ENTRY)} chars to {path}")
    sys.exit(0)
