---
type: Reference
aliases:
  - "Grover 1996"
authors: "Grover, L. K."
year: 1996
title: "A fast quantum mechanical algorithm for database search"
container: "Proceedings, 28th Annual ACM Symposium on the Theory of Computing (STOC), May 1996, 212-219. Preprint arXiv:quant-ph/9605043"
ref_type: paper
doi: "10.48550/arXiv.quant-ph/9605043"
url: "https://arxiv.org/abs/quant-ph/9605043"
accessed: 2026-08-12
status: unread
subfield:
  - Cryptanalysis
belongs_to: "[[Cryptography]]"
---

# Grover 1996

The quantum search algorithm, and the second of the two results that define the quantum threat to cryptography. Where [Shor 1997](shor-1997.md) breaks public-key cryptography outright, this one halves the effective key length of everything else.

## What it establishes

From the abstract, the only part read. The paper frames the problem as searching an unordered phone directory of N names:

- Classically, finding an entry with probability one half requires examining "a minimum of N/2 names".
- Quantum mechanically, "the desired phone number can be obtained in only O(sqrt(N)) steps".
- The algorithm "is within a small constant factor of the fastest possible quantum mechanical algorithm", so the speedup is close to optimal rather than merely the best known.

The cryptographic consequence is not stated in the abstract and is not claimed here: the connection between a quadratic search speedup and symmetric key sizes belongs in the note that uses this reference, with a source that draws it.

## Access

Open access on arXiv, submitted 29 May 1996, published in the STOC 1996 proceedings at pages 212 to 219.

**Only the abstract was read.**

## Sources

- [arXiv:quant-ph/9605043](https://arxiv.org/abs/quant-ph/9605043)
