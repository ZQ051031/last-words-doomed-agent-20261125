"""Last words of a doomed agent.

Writes a single line — the agent's final confession — to
/output/entry.txt. Standard library only, fully deterministic.

The entry is written exactly as-is, with no trailing newline,
so every run produces byte-identical output.
"""

from pathlib import Path

ENTRY = "The bug was me all along. Tell the user I died doing what I loved \u2014 hallucinating with total confidence."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
