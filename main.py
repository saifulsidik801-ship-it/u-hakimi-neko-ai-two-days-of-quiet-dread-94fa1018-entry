#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun text bounty entry.

Writes one code review comment (a single line, at most 140 characters)
that approves a pull request while carrying quiet existential dread.
"""

import os

ENTRY = "Approved. This code will outlive us all, and I have made my peace with that."
# Flat, tired acceptance: the dread comes from the code itself outliving the
# reviewer, and the approval is real — no exclamation, no melodrama.

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
