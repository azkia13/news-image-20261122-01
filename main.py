#!/usr/bin/env python3
"""Entry point for news-image-20261122-01.

The front page was drawn at build time (draw_front.py) and committed as
entry.png. At grading time this program only copies that file to the
output directory: no network, no drawing, standard library only.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
MAX_BYTES = 1048576


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    size = os.path.getsize(dst)
    if size <= 0 or size > MAX_BYTES:
        print("bad output size: %d bytes" % size, file=sys.stderr)
        return 1
    with open(dst, "rb") as fh:
        head = fh.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        print("output is not a PNG", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (dst, size))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
