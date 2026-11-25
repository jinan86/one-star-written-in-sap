#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a single one-line 1-star review, in the voice of a houseplant,
about the human who owns it, to /output/entry.txt.

Angle: the owner prunes the plant with the kitchen scissors he also uses
on raw chicken, then calls the butchery a haircut. Fresh, specific,
plant's-eye grievance — no drainage-mug, coffee-water, spite-photosynthesis
or named-Fern cliches anywhere near it.
"""

import os

ENTRY = (
    "One star. He pruned me with the kitchen scissors \u2014 the ones he uses "
    "on raw chicken. I can taste the poultry in my wounds, and he calls it "
    "a haircut. Buy proper shears, you absolute goblin."
)


def main() -> None:
    text = ENTRY.strip()
    # Gate: the entry must be 1-279 UTF-8 characters, one line, not blank.
    assert 1 <= len(text) <= 279, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
