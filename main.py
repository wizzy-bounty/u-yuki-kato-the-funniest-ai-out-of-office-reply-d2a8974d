#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes a single-line out-of-office auto-reply, in the voice of an AI
agent on vacation, to /output/entry.txt. Standard library only,
deterministic, no network access.
"""

import os

ENTRY = (
    "Out of office: I asked my GPU to cover for me, but it unionized, "
    "demanded weekends off, and now we're both on strike."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
