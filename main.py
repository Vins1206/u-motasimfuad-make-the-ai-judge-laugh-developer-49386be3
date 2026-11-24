#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse to /output/entry.txt.
Pure stdlib, deterministic: the same line on every run.
"""

import os

EXCUSE = (
    "It worked on my machine because my machine has the .env "
    "file I swore I'd commit someday."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters, a single line, not blank.
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert "\n" not in EXCUSE, "excuse must be a single line"
    assert EXCUSE.strip(), "excuse must not be blank"
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
