"""make.fun bounty: Say What Actually Broke.

Deterministic, no-network program. Writes one line of software
error copy, at most 200 characters, to /output/entry.txt. It tells
the brutal truth instead of apologising in generalities: the file
is lost, not deleted, just misplaced between two servers that
refuse to talk to each other. One line, shippable in a real error
dialog. Running twice writes identical bytes.
"""
from pathlib import Path

LINE = "We lost your file: not deleted, just misplaced somewhere between two servers that refuse to talk to each other, and yes, we are embarrassed."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")
    print(f"Wrote {OUT} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
