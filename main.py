#!/usr/bin/env python3
"""One Word From Grandma.

Writes exactly one word to /output/entry.txt: the single word Grandma
would text about AI.

The word: "contraption" -- the warm, slightly baffled word a grandma
reaches for when a grandchild shows her a machine that talks back.
Not a brand name, not jargon, just the old word for a clever device
she does not quite trust yet. It lands the joke on its own: the most
powerful technology on earth, dismissed in one fond, grandmotherly
syllable-stack as a mere contraption.
"""

import os

WORD = "contraption"

# Grader sandbox path; ENTRY_OUTPUT lets a local run point elsewhere.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
