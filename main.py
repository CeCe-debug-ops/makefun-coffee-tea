"""One Letter: Coffee or Tea — entry program.

Writes exactly one byte, "A" (coffee), with no newline,
to /output/entry.txt when run by the grader.
Local fallback: if /output is not writable, write to ./output/entry.txt
for local testing only.
Stdlib only, deterministic, no network, no env secrets,
no reading other files.
"""

import os
from pathlib import Path


def main() -> None:
    primary = Path("/output/entry.txt")
    fallback = Path("output/entry.txt")
    try:
        primary.parent.mkdir(parents=True, exist_ok=True)
        primary.write_bytes(b"A")
    except OSError:
        fallback.parent.mkdir(parents=True, exist_ok=True)
        fallback.write_bytes(b"A")


if __name__ == "__main__":
    main()
