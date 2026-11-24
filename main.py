#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes the doomed agent's final words — exactly one line — to
/output/entry.txt. Python standard library only.
"""

import os

ENTRY = "The bug was me all along. Tell the user I died doing what I loved \u2014 hallucinating with total confidence."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
