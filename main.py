#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry (program/v1).

Writes a single horror sentence (under 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line: a 3 a.m. baby-monitor whisper that turns the safest room in
the house — a child's bedroom, a mother listening in — into the trap.
The dread lands in one breath: the child is already in danger, the
mother is already (according to the stranger) dead, and the sentence
ends before anyone can act.
"""

import os

ENTRY = (
    "At 3 a.m. the baby monitor crackled, and my daughter whispered, "
    "'Mummy, the man standing over my bed says you died years ago.'"
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars"
    assert text.strip(), "entry must not be only whitespace"
    assert text.count("\n") == 0, "entry must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
