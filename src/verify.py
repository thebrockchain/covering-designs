#!/usr/bin/env python3
"""Independent verifier for (v,k,t) covering designs.

usage: verify.py v k t designfile
Design file: one block per line, k space-separated 1-indexed integers.
Exit 0 and prints OK iff every t-subset of {1..v} is contained in some block.
Deliberately written with no shared code with the searcher.
"""
import sys
from itertools import combinations

def main():
    v, k, t = map(int, sys.argv[1:4])
    path = sys.argv[4]
    blocks = []
    with open(path) as f:
        for ln, line in enumerate(f, 1):
            nums = line.split()
            if not nums:
                continue
            b = sorted(map(int, nums))
            assert len(b) == k, f"line {ln}: {len(b)} elements, expected {k}"
            assert len(set(b)) == k, f"line {ln}: repeated element"
            assert 1 <= b[0] and b[-1] <= v, f"line {ln}: element out of range 1..{v}"
            blocks.append(sum(1 << (x - 1) for x in b))
    masks = blocks
    missing = 0
    first_missing = None
    for combo in combinations(range(v), t):
        m = 0
        for x in combo:
            m |= 1 << x
        if not any((m & bm) == m for bm in masks):
            missing += 1
            if first_missing is None:
                first_missing = tuple(x + 1 for x in combo)
    if missing:
        print(f"FAIL: {missing} uncovered {t}-subsets, e.g. {first_missing}")
        sys.exit(1)
    print(f"OK: C({v},{k},{t}) covering verified, {len(blocks)} blocks, "
          f"all {sum(1 for _ in combinations(range(v), t))} {t}-subsets covered")

if __name__ == "__main__":
    main()
