---
type: Reference
aliases:
  - "Kocher 1996"
authors: "Kocher, P. C."
year: 1996
title: "Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems"
container: "Lecture Notes in Computer Science, 104-113. Springer"
ref_type: paper
doi: "10.1007/3-540-68697-5_9"
url: "https://www.paulkocher.com/doc/TimingAttacks.pdf"
accessed: 2026-08-12
status: in-progress
subfield:
  - Cryptanalysis
belongs_to: "[[Cryptography]]"
---

# Kocher 1996

The paper that opened side-channel cryptanalysis: a secret key can be recovered by measuring how long an implementation takes to use it, without any weakness in the algorithm itself.

## What it establishes

The abstract states the attack and its reach:

> "By carefully measuring the amount of time required to perform private key operations, attackers may be able to find fixed Diffie-Hellman exponents, factor RSA keys, and break other cryptosystems. Against a vulnerable system, the attack is computationally inexpensive and often requires only known ciphertext. Actual systems are potentially at risk, including cryptographic tokens, network-based cryptosystems, and other applications where attackers can make reasonably accurate timing measurements."

The mechanism, from the introduction and section 2: cryptosystems take different amounts of time on different inputs, for reasons including "performance optimizations to bypass unnecessary operations, branching and conditional statements, RAM cache hits, processor instructions (such as multiplication and division) that run in non-fixed time". Against a modular exponentiator the attack recovers the exponent one bit at a time, each guess verified by whether the total operation time behaves as that bit value predicts.

**Why it matters for a taxonomy of cryptanalysis:** the attack targets the implementation rather than the algorithm, so it sits outside the classes of attack that [Menezes et al. 1996](menezes-et-al-1996.md) enumerates. The handbook, published the same year, has no treatment of it.

The paper also proposes defenses, and notes that "some cryptosystems will need to be revised to protect against the attack".

## Access

Open access as an author copy. Bibliographic details were taken from Crossref, which gives Lecture Notes in Computer Science, pages 104 to 113, Springer, 1996, DOI 10.1007/3-540-68697-5_9.

**The proceedings volume is not confirmed.** Crossref returns no volume number, and the author copy carries no venue line, so the LNCS volume and the conference it belongs to are unrecorded rather than guessed.

Read to page 2 of the author copy, covering the abstract, the introduction and the attack on a simple modular exponentiator.

## Sources

- [Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems (author copy, PDF)](https://www.paulkocher.com/doc/TimingAttacks.pdf)
- [Crossref record, DOI 10.1007/3-540-68697-5_9](https://doi.org/10.1007/3-540-68697-5_9)
