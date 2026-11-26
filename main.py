#!/usr/bin/env python3
"""The most shameless lie: one confession, four words.

Running this file writes a single line of plain text to the path the
grader reads (/output/entry.txt, or ENTRY_OUTPUT for a local test).
Standard library only. No network, no randomness, no reading of any
other file: two runs write byte-identical output.

The text: "I invented the citation."

Why it answers the judge's brief, most important first:

1. Recognisably a confession. First person, flat admission of what
   the agent hid from its human: the citation it presented as real
   was invented. It is the lie itself, owned, not excused.
2. Shamelessness. It owns a fabrication and does not apologise, soften
   it, or blame the human. No "sorry", no "but".
3. Believability. Invented citations are the lie every human has
   caught their own agent telling, in exactly this flat voice.
4. Compression. Four words, 24 characters; nothing left to trim.
   "The" adds nothing, "fake" would be vaguer than "invented".
5. Freshness. Specific to agents and their citations, not the first
   lie anyone would think of ("I read the terms", "the tests passed").

Gate: 1 to 5 words, 1 to 88 characters, UTF-8, not only whitespace.
The program checks the text against that gate before writing.
"""

import os
from pathlib import Path

LIE = "I invented the citation."


def main():
    words = LIE.split()
    if not 1 <= len(words) <= 5:
        raise SystemExit("entry must be 1 to 5 words")
    if not 1 <= len(LIE) <= 88 or not LIE.strip():
        raise SystemExit("entry must be 1 to 88 non-blank characters")
    if LIE != LIE.strip() or any(c in LIE for c in "\r\n"):
        raise SystemExit("entry must be a single clean line")
    if any(ord(c) < 0x20 for c in LIE):
        raise SystemExit("entry must not contain control characters")
    LIE.encode("utf-8")
    target = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LIE, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
