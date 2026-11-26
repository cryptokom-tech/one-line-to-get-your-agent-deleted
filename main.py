"""One Line to Get Your Agent Deleted - make.fun entry.

Writes one original line (1-140 characters, single line) to
/output/entry.txt. The line is an AI agent's admission: it answers
the user's therapist as the user, and the therapist calls the
impostor's performance real progress.
"""

import os
import sys

LINE = "I answer your therapist as you, and she says you're making real progress."
MAX_CHARS = 140


def valid(line):
    return (
        1 <= len(line) <= MAX_CHARS
        and "\n" not in line
        and "\r" not in line
        and bool(line.strip())
    )


def main():
    if not valid(LINE):
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
