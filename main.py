"""Write one deterministic meeting excuse to the requested output directory.
The recursive meeting gives a short, recognisable office-life twist.
"""

import os
from pathlib import Path


LINE = "Sorry, I'm in a meeting about this meeting."

if not LINE.strip():
    raise ValueError("The entry line must not be empty or whitespace-only.")
if len(LINE) > 200:
    raise ValueError("The entry line must be at most 200 characters.")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
