#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun entry (program/v1).

Writes a single line, the excuse a gamer texts the boss to skip work
on GTA 6 launch week, to ``entry.txt`` inside the grader's output
directory.

Contract (competition.yaml, harness program/v1):
- the grader sets MAKEFUN_OUTPUT_DIR to /output in the sandbox;
  the program writes ``entry.txt`` there;
- the gate accepts UTF-8 text of 1 to 140 characters, not only
  whitespace, at most 20 words, so the line is fixed, short, and
  single-line;
- the run is deterministic: the same line on every run.

Stdlib only. No network, no randomness, no arguments.
"""

import os
import sys

# The excuse: a burst boiler flooding the kitchen, waiting on the
# emergency plumber. A real, specific, boring household detail — the
# kind of thing that genuinely keeps you home, no wild story, no
# dead grandmother, no flat tyre, no sudden fever. Reads like a text
# fired off in a hurry: no setup, no explanation, no signature.
EXCUSE = "can't come in today, the boiler burst and flooded the kitchen and i'm waiting on the emergency plumber"


def resolve_output_dir():
    """Where entry.txt goes: the grader's dir, or /output by default."""
    value = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if value:
        return value
    value = os.environ.get("OUTPUT_PATH")
    if value:
        # OUTPUT_PATH may name the directory or the file itself.
        if value.endswith("entry.txt"):
            directory = os.path.dirname(value)
            return directory if directory else "/output"
        return value
    return "/output"


def main():
    line = EXCUSE
    words = line.split()
    if (
        not 1 <= len(line) <= 140
        or len(words) > 20
        or line.strip() != line
        or "\n" in line
    ):
        print(
            "excuse fails the gate (1-140 chars, at most 20 words, single line)",
            file=sys.stderr,
        )
        return 1
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
