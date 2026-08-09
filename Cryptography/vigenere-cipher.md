---
type: Cipher
category: classical
era: early modern
first_described: 1553
status: historical
broken_by:
  - "[[Kasiski examination]]"
  - "[[Index of coincidence]]"
subfield:
  - Classical ciphers
  - Cryptanalysis
belongs_to: "[[Cryptography]]"
related_to:
  - "[[Frequency analysis]]"
  - "[[Adversarial versus accidental encipherment]]"
cites:
  - "[[Kasiski 1863]]"
wikidata:
---

# Vigenère cipher

A polyalphabetic substitution cipher in which a repeating keyword selects, letter by letter, which shifted alphabet encrypts the next character. Because a given plaintext letter maps to different ciphertext letters depending on its position under the key, the flat single-alphabet frequency signature is smeared out and simple [frequency analysis](../Decipherment/frequency-analysis.md) fails.

## Attribution, which is wrong

The cipher was described by **Giovan Battista Bellaso** in *La cifra del Sig. Giovan Battista Bellaso* (1553), building on Trithemius's tabula recta by adding a repeating key. Blaise de Vigenère published a different construction, an autokey cipher, in 1586. The misattribution to Vigenère happened in the nineteenth century and stuck.

Worth keeping because it is a cheap standing reminder that eponyms record reputation rather than priority, which is a pattern this vault meets repeatedly. Compare [Alice Kober](../people/alice-kober.md), whose contribution ran the other way: the work was hers and the name attached elsewhere.

## Breaking it

It held its reputation as *le chiffre indéchiffrable* for roughly three centuries.

Charles Babbage broke a variant by 1854 and never published. **Friedrich Kasiski** published the first general method in 1863: repeated ciphertext sequences betray the key period, because a repeated plaintext fragment encrypted at the same key offset produces an identical ciphertext fragment, and the spacings between repetitions are multiples of the key length. **William Friedman** later added the index of coincidence, estimating the period statistically rather than from coincidental repeats.

The shape of the attack is the interesting part. Neither method attacks the cipher directly. Both recover the period and thereby *reduce* one polyalphabetic problem to several monoalphabetic ones, each then solvable by ordinary frequency analysis.

## Why it sits at the boundary

That reduction is exactly what does not transfer to decipherment. Here you know the plaintext language, so you know the distribution you are trying to match, and you are attacking a system somebody built to resist you. On an undeciphered corpus you know neither the language nor its expected frequencies, and there is no adversary and no key. See [Adversarial versus accidental encipherment](../Decipherment/adversarial-versus-accidental.md).

No key material or worked example key is stored here, per the intake rules.

## Sources

- [Vigenère cipher, Wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
- [Kasiski 1863](../references/kasiski-1863.md)
