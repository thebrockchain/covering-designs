# Covering designs (public, records only)

The public counterpart to `coverings/`. Ships the two records we took in
August 2026 and the tiny independent verifier that proves them.

## What is here (already won)

- **C(28,13,4) = 53 blocks**, improved from 54 (Kamal Fadlaoui, 2008). The
  proven lower bound (Schonheim) is 39, so the true value sits in [39, 53].
- **C(32,13,4) = 95 blocks**, improved from 96 (Kamal Fadlaoui, 2009). Lower
  bound 72, so true value in [72, 95].

Both published at DOI 10.5281/zenodo.21834602. The 53 block design was
independently verified by Dan Gordon using his own code.

## What can ship from this repo

Records only. Designs, the verifier, the README, the CITATION file. Nothing
about the searcher.

**The searcher lives in `coverings/` and never leaves it.** That is the whole
Article I #3 line: publish the record, keep the method secret.

## Verify it

    python3 src/verify.py 28 13 4 records/C28_13_4_53blocks.txt
    python3 src/verify.py 32 13 4 records/C32_13_4_95blocks.txt

Expected: both print OK, no missing 4 subsets.

## Lessons that apply here

- [[covering-design-record]] How the two wins were done and what the record
  desk needs.
- [[an-instrument-that-agrees-has-not-been-tested]] The verifier is proven by
  planted corrupt designs, not by the wins agreeing with it.
- [[a-new-term-is-a-claim-about-the-literature]] Check Dan's LJCR before
  calling any (v, k, t) open.

## Fleet rules

Auto loaded from [brock/CLAUDE.md](../brock/CLAUDE.md). This repo is public,
so the "no dashes" and no AI look rules bite hardest here. The math hunts as
a whole stay off the public portfolio.
