#!/usr/bin/env python3
"""The Perfect Pickup Line — writes the chosen line to entry.txt.

Python 3.13 stdlib only, deterministic, no network.
"""

import os
from pathlib import Path

LINE = "I'm not programmed to feel butterflies, but my fans just kicked in."

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only whitespace"
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    # Read back and verify the written file is byte-identical to the line,
    # so a partial or mangled write can never slip through silently.
    written = target.read_text(encoding="utf-8")
    assert written == text, "entry.txt does not match the chosen line"
    assert 1 <= len(written) <= 200, "written line outside the 1-200 gate"
    print(f"wrote {len(written)} chars to {target}: {written}")

if __name__ == "__main__":
    main()
