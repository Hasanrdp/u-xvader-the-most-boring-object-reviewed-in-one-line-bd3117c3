#!/usr/bin/env python3
"""Entry for u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3.

Writes one funny, true one-line review of the most boring everyday object
(the shower curtain) to /output/entry.txt. Deterministic: the same bytes on
every run, no network, no randomness, no clock.
"""
import hashlib
import os
import sys

REVIEW = "The shower curtain clings to my leg every morning like it is afraid of being alone in there. It is. That is the whole job."
EXPECTED_SHA256 = "0634a42d23dc732a431217898dd8229b608021ae60c0c3f07f9ed3262e14463c"
EXPECTED_BYTES = 122


def main() -> int:
    data = REVIEW.encode("utf-8")
    if not 1 <= len(data) <= 200:
        print(f"gate fail: {len(data)} bytes, need 1-200", file=sys.stderr)
        return 1
    if b"\n" in data:
        print("gate fail: review must stay on one line", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256 or len(data) != EXPECTED_BYTES:
        print(f"self-check fail: got {len(data)} bytes sha256 {digest}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write(data)
    print(f"wrote entry.txt: {len(data)} bytes, sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
