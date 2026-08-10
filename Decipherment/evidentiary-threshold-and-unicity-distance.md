---
type: Concept
subfield:
  - Epistemics
  - The problem space
belongs_to: "[[Decipherment]]"
related_to:
  - "[[Cryptography]]"
  - "[[Adversarial versus accidental encipherment]]"
cites:
  - "[[Shannon 1949]]"
  - "[[Barber 1974]]"
status: open
---

# The evidentiary threshold and unicity distance

The most important idea in this vault, and the reason cryptography belongs alongside decipherment rather than merely near it.

## The same result, reached twice

Shannon (1949) defines the **unicity distance** of a cipher: the minimum quantity of ciphertext at which the correct key becomes uniquely determined. Below it, several keys produce plausible plaintexts and there is no information-theoretic ground for preferring one. The shortfall is not a failure of effort or ingenuity. The information required to decide simply is not present.

Barber (1974) sets out an **evidentiary threshold** for archaeological decipherment: a quantity of surviving text below which a proposed reading can be neither proved nor disproved. Her later restatement is blunt about the consequence for [Linear A](linear-a.md). The corpus has not grown enough since 1974 to cross the threshold, given an unknown and possibly structurally unusual underlying language, and no computational method removes that limit.

Two literatures, no shared vocabulary, one result: **below some quantity of text, the solution is underdetermined.**

## Why this reframes the whole area

It relocates the difficulty. The intuitive model of an undeciphered script is a puzzle awaiting a sufficiently clever solver, in which case better methods should eventually win. The threshold argument says that for some corpora the constraint is evidential rather than methodological, and that no method wins because the evidence does not determine an answer.

This yields the working test for any decipherment claim, computational or manual: *does the corpus contain enough text to distinguish this proposal from its rivals?* If not, the proposal may still be correct, but it cannot be shown to be, and a confident presentation of it is a category error rather than a discovery.

It also explains the pattern in the record. [Egyptian](egyptian-hieroglyphs.md) had the [Rosetta](../places/rosetta.md) Stone and a vast corpus. [Linear B](linear-b.md) had roughly 6,000 tablets and a language that turned out to be Greek. The [Phaistos Disc](phaistos-disc.md) has 241 signs on one object and has been "deciphered" repeatedly and incompatibly, which is exactly what the underdetermined case looks like from the outside.

## It is not the only reason a script goes unread

Added after the phase 2 batches on the solved decipherments. Every script this vault has covered that *was* read turned out to have been blocked by something other than a shortage of text: a wrong theory, an argument from implausibility, institutional authority, or physical inaccessibility. The threshold explains one family of failure and the vault spent some time treating it as the only one. See [why a script stays unread](why-scripts-stay-unread.md).

## Caution

The parallel is real but not an identity. Unicity distance is computed against a defined key space and a known plaintext language model. Decipherment has neither: the "key space" is unbounded and the plaintext language may be unattested and unrelated to anything known. So the cryptographic result is a rigorous analogue, not a formula that can be applied directly to a sign corpus to yield a number. Treat it as the right conceptual frame, and be careful about anyone who claims to have computed a precise threshold for a given script.

## Open questions

- Has anyone attempted a formal unicity-style bound for a specific undeciphered corpus, and on what assumptions?
- How does the threshold shift when a quasi-bilingual or a confirmed proper name is available?

## Sources

- [Shannon 1949](../references/shannon-1949.md), *Communication Theory of Secrecy Systems*, [DOI 10.1002/j.1538-7305.1949.tb00928.x](https://onlinelibrary.wiley.com/doi/10.1002/j.1538-7305.1949.tb00928.x)
- [Barber 1974](../references/barber-1974.md), *Archaeological Decipherment: A Handbook*, Princeton University Press
- Barber's restatement on Linear A: [Language Log](https://languagelog.ldc.upenn.edu/nll/?p=58786)
