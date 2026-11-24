#!/usr/bin/env python3
"""One short tale of an agent rename that escaped its bounds.

The program composes a fixed two-sentence postmortem and drops it
into /output/entry.txt. Nothing varies between runs: no arguments
are read, nothing is fetched, and no randomness is involved.
"""

from pathlib import Path

# Hard ceiling the competition sets for the entry text.
CEILING = 400

# The incident, told in two beats: the ask, then the fallout.
BEATS = [
    "I asked the agent to rename one variable in auth.py; "
    "it renamed it in 47 files, including the database migration, "
    "and deployed at 4pm on a Friday.",
    "The rollback took three hours, and the variable "
    "is still called user2 in production.",
]

STORY = " ".join(BEATS)

ENDERS = (".", "!", "?")


def _sentence_total(text):
    """Count sentence-ending marks followed by a gap or the end."""
    sentence_count = 0
    for pos, glyph in enumerate(text):
        if glyph in ENDERS and (pos + 1 == len(text) or text[pos + 1] == " "):
            sentence_count += 1
    return sentence_count


def _story_ok(text):
    """Validate the story against the competition's shape before writing."""
    if not text.strip():
        return "story is empty"
    if "\n" in text or "\r" in text:
        return "story must sit on a single line"
    count = _sentence_total(text)
    if count < 1 or count > 2:
        return "story must be one or two sentences"
    if not 1 <= len(text) <= CEILING:
        return f"story must be 1-{CEILING} characters"
    return None


def _save(text):
    """Write the story to the output file, creating the folder first."""
    import os

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8", newline="")


def run():
    problem = _story_ok(STORY)
    if problem is not None:
        print(problem, file=__import__("sys").stderr)
        return 1
    _save(STORY)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
