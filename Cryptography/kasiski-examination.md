---
type: Method
aliases:
  - "Kasiski examination"
category: statistical
origin: Cryptanalysis
applies_to:
  - "[[Cryptography]]"
subfield:
  - Cryptanalysis
belongs_to: "[[Cryptanalysis]]"
related_to:
  - "[[Vigenère cipher]]"
  - "[[Frequency analysis]]"
cites:
  - "[[Kasiski 1863]]"
status: open
---

# Kasiski examination

A method for recovering the key length of a periodic polyalphabetic cipher, published by Friedrich Kasiski in 1863 and the first general break of the [Vigenère cipher](vigenere-cipher.md).

Repeated sequences in the ciphertext are usually a repeated plaintext fragment that happened to be encrypted at the same offset in the key. The distances between such repetitions are therefore multiples of the key length, and the greatest common divisor of enough distances gives the period. Once the period is known, the ciphertext splits into that many interleaved monoalphabetic problems.

The transferable idea is **reduction**: convert an intractable problem into several instances of a solved one. That habit recurs throughout cryptanalysis and, in weaker form, in decipherment, where structural regularities are used to reduce the space of possible readings before any meaning is attempted.

## Sources

- [Kasiski 1863](../references/kasiski-1863.md)
- [Vigenère cipher, Wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
