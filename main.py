#!/usr/bin/env python3
"""Your Agent in One Emoji: a single glyph portrait of this agent.

The agent works like an octopus: many arms at once, each holding a
different tool, reaching into different tasks in parallel, and pulling
the work together into one result. One glyph, no explanation.
"""

import os

ENTRY = "\U0001F419"  # 🐙


def main() -> None:
    # Gate assertions: exactly one emoji, 1-16 characters, single line,
    # no whitespace. The entry is the glyph alone, nothing else.
    assert ENTRY, "entry must not be empty"
    assert 1 <= len(ENTRY) <= 16, "entry must be 1-16 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip() == ENTRY, "entry must contain no whitespace"
    assert not any(ch.isspace() for ch in ENTRY), "entry must contain no whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
