# A (28,13,4) covering design with 53 blocks

**Brock Falfas** (brock@thebrockchain.com)
7 August 2026

DOI: [10.5281/zenodo.21834602](https://doi.org/10.5281/zenodo.21834602)

This repository contains a (28,13,4) covering design with **53 blocks**, improving
the best known upper bound on the covering number C(28,13,4) from 54 to 53.

The previous best of 54 blocks was found by Kamal Fadlaoui on 22 September 2008
and had stood since. The proven lower bound (Schonheim) is 39, so the true value
of C(28,13,4) lies somewhere in [39, 53].

The design is in [`records/C28_13_4_53blocks.txt`](records/C28_13_4_53blocks.txt).

## What a covering design is

A (v, k, t)-covering design is a collection of k-element subsets, called blocks,
of the set {1, ..., v}, such that every t-element subset of {1, ..., v} is
contained in at least one block. C(v, k, t) is the smallest number of blocks that
suffices.

For v = 28, k = 13, t = 4: every one of the 20,475 four-element subsets of
{1, ..., 28} must appear inside at least one 13-element block. This design does
that with 53 blocks.

The same question appears in combinatorial software testing, where it asks how
few test configurations are needed to exercise every combination of any 4 of 28
settings, and in pooled sample testing.

## Verifying this result

You do not have to take my word for any of it. The design either covers all
20,475 four-subsets or it does not, and checking takes about a second.

```bash
python3 src/verify.py 28 13 4 records/C28_13_4_53blocks.txt
```

Expected output:

```
OK: C(28,13,4) covering verified, 53 blocks, all 20475 4-subsets covered
```

[`src/verify.py`](src/verify.py) is deliberately short and dependency free, so it
can be read end to end in a couple of minutes. Readers who prefer their own
checker should write one; the file format is one block per line, 13 space
separated integers in the range 1 to 28.

Before this result was announced it was checked by two verifiers written
independently of each other and of the search program. Both report all 20,475
four-subsets covered, none missing, and 53 distinct blocks.

## Method

The result came from a local search that starts warm rather than from scratch.

Cold random starts do not get close on instances this size. The search instead
takes the known 54-block design, deletes one block, and treats the resulting
53-block configuration as a starting point with a known deficit. Deleting each of
the 54 blocks in turn gives 54 distinct starting points to cycle through.

The search uses dynamic constraint weighting. Its cost function is not the count
of uncovered 4-subsets but the sum of their weights, and each time the search
reaches a local minimum the weight of the 4-subset it failed to cover is
increased. Stubborn 4-subsets therefore become progressively more expensive to
leave uncovered, which reshapes the landscape until the configuration has to
change around them. It is combined with occasional macro-moves that discard a
block and rebuild it greedily around an uncovered 4-subset, since single element
swaps cannot cross the distance between basins.

The search program itself is not published. In this the work follows the practice
of the most active contributors to the covering repository, whose submissions are
recorded with the method listed as private tools. The result is public and fully
checkable; the tool that found it is not part of the result.

## Provenance

The design was found at 03:18 EDT on 7 August 2026, on a single Apple M5.

The starting point was the 54-block design of Fadlaoui with one block removed,
leaving 53 blocks and **110 of the 20,475 four-subsets uncovered**. The search
closed all 110.

The resulting design shares **no blocks** with the 2008 design. Every block
differs. The 54-block design is included in [`reference/`](reference/) so that
this can be checked directly.

## Files

| Path | What it is |
| --- | --- |
| `records/C28_13_4_53blocks.txt` | The 53-block design. One block per line, 13 space separated values in 1..28. |
| `src/verify.py` | Independent verifier. No dependencies. |
| `reference/C28_13_4_54blocks_Fadlaoui2008.txt` | The previous 54-block design, for comparison. |

## Data sources

Known bounds and previous designs were taken from the La Jolla Covering
Repository (https://dmgordo.github.io/, archived data, CC BY 4.0) and from the
Covering Repository (https://coveringrepository.com/), which maintains the live
tables and listed C(28,13,4) at 54 blocks as of 7 August 2026.

## License

The designs are released into the public domain under CC0. A covering design is a
mathematical fact and is not the sort of thing anyone should be claiming rights
over. `verify.py` is MIT.

## Citation

Falfas, B. (2026). *A (28,13,4) covering design with 53 blocks* [Dataset].
Zenodo. https://doi.org/10.5281/zenodo.21834602
