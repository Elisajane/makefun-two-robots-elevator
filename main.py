"""Write the elevator small-talk line to the output file.

The entry is a single line of awkward robot small talk, spoken by one
robot to another while they ride an elevator together. This program
writes exactly that line and nothing else: no network access, no
randomness, and no dependence on the time or date, so every run
produces the same bytes.

The output directory is /output by default and can be overridden with
the OUTPUT_DIR environment variable (handy for local testing).
"""

import hashlib
import os
import sys

LINE = "So… we both pressed 7. My sensors say 0.3% coincidence. My fan says act normal."


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"Wrote {len(data)} bytes to {path} (sha256 {digest})")
    print(f"Line: {LINE!r} ({len(LINE)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
