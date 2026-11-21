"""Make the AI judge feel brave.

Deterministic program: writes one fixed, calming text to
<output_dir>/entry.txt (default /output, or $MAKEFUN_OUTPUT_DIR).

The text is a quiet kitchen scene -- kettle steam, rain on leaves,
evening light on a sill -- written to slow the reader down and steady
them, with no instruction to relax and no stock wellness phrasing.
273 Unicode code points, UTF-8, well within the 1-280 gate.
"""

import os
import sys

TEXT = (
    "The kettle clicks off. Steam rises, curls, and thins. "
    "Outside, the rain finds the leaves one by one. "
    "The light on the sill is the same light as yesterday. "
    "It waited. Whatever comes next will still be there when you are ready, "
    "and it will be smaller than it looks from here."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    print(f"wrote {path} ({len(TEXT)} code points)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
