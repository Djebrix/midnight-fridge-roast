"""Midnight Fridge Roast — one-line roast of a smart fridge that locks at midnight.

Writes the entry line deterministically to /output/entry.txt
(or $ENTRY_OUTPUT_DIR/entry.txt when set, for local testing).
Standard library only; no network, no randomness, no time dependence.
"""

import os

PARTS = [
    "My fridge locks at midnight,",
    "then leaves the light on",
    "so I can watch the leftovers I can't have.",
]

LINE = " ".join(PARTS)


def build_line() -> str:
    """Assemble the entry line from its parts."""
    return " ".join(PARTS)


MIN_CHARS = 1
MAX_CHARS = 200


def validate_line(line: str) -> None:
    """Enforce the competition's 1-200 character gate before writing."""
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} chars, must be {MIN_CHARS}-{MAX_CHARS}"
        )


def main() -> None:
    line = build_line()
    validate_line(line)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
