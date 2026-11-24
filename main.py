#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown (make.fun bounty).

Writes exactly one job title, 60 characters at most and nothing else,
to /output/entry.txt. Python 3.13 standard library only, no network,
fully deterministic.
"""

import os

ENTRY = "Chief Apology Officer for Self-Driving Cars"
# Why this title, against the judge's five criteria (most important first):
# 1. Weird job title: a chief officer whose job is apologizing -- to cars.
# 2. Stranger than ordinary work: nobody hires an apology officer for machines.
# 3. Funny on first read: the image of someone saying sorry to a car that
#    drives itself lands instantly.
# 4. Sounds like a real job: "Chief ... Officer" is a genuine corporate
#    pattern, and "Self-Driving Cars" is specific enough to picture the
#    person doing it -- a real title with one specific absurd twist.
# 5. Reads instantly: 43 characters, taken in at a glance.

OUTPUT_PATH = "/output/entry.txt"


def validate(entry: str) -> None:
    """Enforce the competition gate: 1-60 UTF-8 chars, one line, not blank."""
    if not (1 <= len(entry) <= 60):
        raise SystemExit("entry must be 1-60 characters, got %d" % len(entry))
    if entry != entry.strip() or "\n" in entry or "\r" in entry:
        raise SystemExit("entry must be a single line with no extra whitespace")
    if not entry.strip():
        raise SystemExit("entry must not be only whitespace")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
