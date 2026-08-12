---
type: Method
aliases:
  - "Frequency analysis"
category: statistical
subfield:
  - Manual method
  - Computational method
origin: Cryptanalysis
applies_to:
  - "[[Cryptography]]"
  - "[[Decipherment]]"
  - "[[General Linguistics]]"
belongs_to: "[[Decipherment]]"
related_to:
  - "[[Adversarial versus accidental encipherment]]"
status: open
---

# Frequency analysis

One technique, three literatures. The oldest method that still works, and the clearest case of transfer between cryptanalysis and decipherment.

## Origin

Al-Kindi, in ninth-century Baghdad, set out the counting of letter frequencies to break monoalphabetic substitution, in *Risalah fi Istikhraj al-Mu'amma* (A Manuscript on Deciphering Cryptographic Messages). It rests on the observation that a language has a stable statistical fingerprint which substitution permutes but does not destroy.

## The three applications

**Cryptanalysis.** Break substitution ciphers by matching observed symbol frequencies to expected plaintext frequencies. Extended by Kasiski examination and Friedman's index of coincidence to handle polyalphabetic ciphers, where the trick is first to determine the key length and then to reduce the problem to several monoalphabetic ones.

**Decipherment.** The same counting, with a critical difference: you do not know which language's fingerprint to match against. Frequency analysis on an undeciphered script therefore tells you about *structure* before it tells you about *content*: how many distinct signs there are (which distinguishes an alphabet from a syllabary from a logographic system), whether signs cluster positionally (which suggests affixes and therefore inflection), and whether the distribution looks linguistic at all.

Alice Kober's work on Linear B is the model. Counting sign groups that varied only in their final signs, she identified her "triplets", demonstrating that the language inflected and building the grid of relationships that Ventris later used to assign sound values. She was not guessing at meaning; she was extracting structure from distribution.

**Linguistics.** The same counting underlies corpus linguistics, Zipf's law, and ultimately the distributional hypothesis that produces modern word embeddings, which is the mechanism behind neural decipherment. See [Computational decipherment: three distinct tasks](computational-decipherment-three-tasks.md).

## Limits

Frequency analysis needs volume. On a short corpus the counts are noise, which is the point at which this method runs into [the evidentiary threshold](evidentiary-threshold-and-unicity-distance.md). It is also weak against a corpus of proper names or numerals, and administrative tablets, which is most of what survives, are full of both.

## Sources

- Al-Kindi (c. 850), *Risalah fi Istikhraj al-Mu'amma*. Discussed in Singh, S. (1999), *The Code Book*, Doubleday
- Friedman, W. F. (1922), *The Index of Coincidence and Its Applications in Cryptography*, Riverbank Publication 22. [Text](https://www.nsa.gov/portals/75/documents/news-features/declassified-documents/friedman-documents/publications/FOLDER_269/41784779082379.pdf)
- Fox, M. (2013), *The Riddle of the Labyrinth: The Quest to Crack an Ancient Code*, Ecco. On Kober's method
- Chadwick, J. (1958), *The Decipherment of Linear B*, Cambridge University Press
