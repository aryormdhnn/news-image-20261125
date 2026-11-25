"""World News — 25 November 2026, in One Image.

Entry for make.fun's "Sum up 25 November's world news in one image" bounty.

The program writes the front page to /output/entry.png (or to
$MAKEFUN_OUTPUT_DIR when set). The image is the entry.png beside this file:
a 1024x1024 editorial front page summing up Wednesday 25 November 2026 —
a Houthi drone striking Riyadh's tallest tower, Zelenskiy confirming
Ukraine's strike on a Russian ship in the Gulf of Finland, Sarkozy and
Bruni ordered to stand trial in France, and NATO sending early-warning
jets to Poland. The front page's hero photo shows the Public Investment
Fund Tower in Riyadh at dusk — the tower the Houthis hit for the second
time in less than a week.

Standard library only. No network. Deterministic: the output bytes are
exactly the bytes of entry.png, every run. The image is 1024x1024 and
under the 1 MiB limit, so the copy is byte-identical on every machine.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print(f"missing source image: {source}", file=sys.stderr)
        return 1
    source_digest = hashlib.sha256(source.read_bytes()).hexdigest()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    if digest != source_digest:
        print(f"mismatch: output {digest} != source {source_digest}", file=sys.stderr)
        return 1
    print(f"wrote {target} ({target.stat().st_size} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
