---
type: MOC
aliases:
  - "Cryptanalysis"
area: Cryptography
subfield:
  - Cryptanalysis
belongs_to: "[[Cryptography]]"
updated: 2026-08-12
---
# Cryptanalysis

Breaking ciphers, and the study of what breaking one means. The subfield covers the classes of attack a system is judged against, the statistical and algebraic techniques used against symmetric ciphers, the algorithms that threaten the hard problems behind public-key cryptography, and the attacks that bypass the mathematics entirely by measuring the machine.

It is also the formal junction with Decipherment. The statistical apparatus is shared, and the difference is the adversary: a cipher was designed to resist analysis, while a lost script was not. See [Adversarial versus accidental encipherment](../Decipherment/adversarial-versus-accidental.md).

## Notes in this subfield

Forty-two of these are stubs, added 2026-08-12, at two levels of depth. Each names the section of a published source that establishes it as a topic; none makes a claim beyond that.

**Attack models**

- [Classes of attack](classes-of-attack.md), stub, with four children
- [Attacks on protocols](attacks-on-protocols.md), stub
- [Attacks on hash functions](attacks-on-hash-functions.md), stub, with three children
- [Attacks on identification protocols](attacks-on-identification-protocols.md), stub

**Classical and statistical**

- [Cryptanalysis of classical ciphers](cryptanalysis-of-classical-ciphers.md), stub, with two children
- [Kasiski examination](kasiski-examination.md), written, and thin
- [Index of coincidence](index-of-coincidence.md), written, and thin
- [Birthday attacks](birthday-attacks.md), stub
- [Meet-in-the-middle attacks](meet-in-the-middle-attacks.md), stub
- [Crib-dragging](crib-dragging.md), stub

**Against modern symmetric ciphers**

- [Differential cryptanalysis](differential-cryptanalysis.md), stub
- [Linear cryptanalysis](linear-cryptanalysis.md), stub

**Against the hard problems**

- [Integer factorization algorithms](integer-factorization-algorithms.md), stub, with seven children
- [Discrete logarithm algorithms](discrete-logarithm-algorithms.md), stub
- [Quantum cryptanalysis](quantum-cryptanalysis.md), stub, with two children

**Against the implementation**

- [Side-channel attacks](side-channel-attacks.md), stub, with five children

**Historical**

- [Cryptanalysis of the Lorenz cipher](cryptanalysis-of-the-lorenz-cipher.md), stub, with four children
- [Enigma cryptanalysis and the bombe](enigma-cryptanalysis-and-the-bombe.md), stub

Related and filed elsewhere: [Frequency analysis](../Decipherment/frequency-analysis.md), which sits in Decipherment because it is the technique that crosses between the two areas, and the [Vigenère cipher](vigenere-cipher.md), which carries this subfield as its second value.

## How deep the stubs go

Two levels below this hub: topic, then subtopic, which is the shape `CONVENTIONS.md` names as expected.

Depth follows the subject rather than the bibliography. Until 2026-08-12 a stub needed a source that named it, and the effect was that [Integer factorization algorithms](integer-factorization-algorithms.md) got seven children because one handbook itemizes them, while attacks on hash functions got none, which said something about a 1996 table of contents and nothing about cryptography. The rule was relaxed for stubs; see `DECISIONS.md`.

Stubs that already have a source cite it. The rest carry **To be researched** and are listed by `python3 scripts/check-vault.py --stubs`, which is the worklist for closing them.

## Still owed to this subfield

Named in the area index or in the sources, and not yet stubbed:

- **The Polish contribution in its own right**, as against the Bletchley Park work that followed it, which [Enigma cryptanalysis and the bombe](enigma-cryptanalysis-and-the-bombe.md) currently covers together.
- **Differential-linear cryptanalysis**, which [Menezes et al. 1996](../references/menezes-et-al-1996.md) attributes to Langford and Hellman in section 7.8 and which sits between two stubs here.
- **Related-key attacks**, and **truncated differentials**, both named in the same section.
- **al-Kindi**, the earliest known frequency analysis, which is a `Person` note owed rather than a topic.

## What the existing notes need

[Kasiski examination](kasiski-examination.md) is 176 words and [Index of coincidence](index-of-coincidence.md) is 213, the two thinnest notes anywhere in the corpus, and both are load-bearing: the Decipherment area divides by them. Repairing them is scheduled with this area's content work in `ROADMAP.md`, and [Kasiski 1863](../references/kasiski-1863.md) is already held and unread.
