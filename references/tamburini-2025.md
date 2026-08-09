---
type: Reference
authors: "Tamburini, Fabio"
year: 2025
title: "On automatic decipherment of lost ancient scripts relying on combinatorial optimisation and coupled simulated annealing"
container: "Frontiers in Artificial Intelligence 8"
ref_type: paper
doi: "10.3389/frai.2025.1581129"
url: "https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1581129/full"
accessed: 2026-08-09
status: unread
subfield:
  - Computational method
  - The problem space
belongs_to: "[[Decipherment]]"
---

# Tamburini 2025

Encodes candidate sign mappings as k-permutations (allowing null, one-to-many and many-to-one) and minimizes an energy function by coupled simulated annealing, matching lexica with a modified Hungarian algorithm.

Two things make it useful here beyond its results. First, it supplies the **three-case taxonomy** this vault uses as the spine of the problem space: different script and same language, different script and different language, same script and different language. Second, the author is explicit about the limits: the method needs segmented and clean corpora, extensive cognate lists, and human paleographic expertise, and assists paleographers rather than replacing them.

Reported accuracy: about 95.5% on Ugaritic to Old Hebrew (noiseless) and 89.4% on Linear B to Greek, both above the prior neural baseline.

## Sources

- [Frontiers in Artificial Intelligence](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1581129/full)
