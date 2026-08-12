---
type: Method
aliases:
  - "Index of coincidence"
category: statistical
origin: Cryptanalysis
applies_to:
  - "[[Cryptography]]"
  - "[[Decipherment]]"
subfield:
  - Cryptanalysis
  - Theory
belongs_to: "[[Cryptanalysis]]"
related_to:
  - "[[Vigenère cipher]]"
  - "[[Frequency analysis]]"
  - "[[Is it writing at all? The Indus entropy debate]]"
status: open
---

# Index of coincidence

A statistic introduced by William Friedman in 1922: the probability that two letters drawn at random from a text are identical. Natural language has a characteristically high value because its letter distribution is uneven; a uniform random string has a low one.

Applied to a periodic polyalphabetic cipher, it estimates the key length statistically rather than relying on the coincidental repeats that [Kasiski examination](kasiski-examination.md) needs, which makes it work on shorter texts.

## Why it reaches beyond cryptanalysis

The index measures how far a symbol distribution departs from uniformity, which is a general question about a corpus and not a question about ciphers. That is the same measurement, in a different dress, that the [Indus entropy debate](../Decipherment/is-it-writing-at-all.md) turns on: whether a set of symbol sequences behaves statistically like a linguistic system.

A genuine cross-area method, which is why it is typed `Method` and not filed as a cryptographic footnote.

## Sources

- Friedman, W. F. (1922), *The Index of Coincidence and Its Applications in Cryptography*, Riverbank Publication 22. [Scan (NSA)](https://www.nsa.gov/portals/75/documents/news-features/declassified-documents/friedman-documents/publications/FOLDER_269/41784779082379.pdf)
