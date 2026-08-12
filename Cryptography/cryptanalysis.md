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

Thirteen of these are stubs, added 2026-08-12. Each names the section of a published source that establishes it as a topic; none makes a claim beyond that.

**Attack models**

- [Classes of attack](classes-of-attack.md), stub
- [Attacks on protocols](attacks-on-protocols.md), stub
- [Attacks on hash functions](attacks-on-hash-functions.md), stub
- [Attacks on identification protocols](attacks-on-identification-protocols.md), stub

**Classical and statistical**

- [Cryptanalysis of classical ciphers](cryptanalysis-of-classical-ciphers.md), stub
- [Kasiski examination](kasiski-examination.md), written, and thin
- [Index of coincidence](index-of-coincidence.md), written, and thin
- [Birthday attacks](birthday-attacks.md), stub

**Against modern symmetric ciphers**

- [Differential cryptanalysis](differential-cryptanalysis.md), stub
- [Linear cryptanalysis](linear-cryptanalysis.md), stub

**Against the hard problems**

- [Integer factorization algorithms](integer-factorization-algorithms.md), stub
- [Discrete logarithm algorithms](discrete-logarithm-algorithms.md), stub
- [Quantum cryptanalysis](quantum-cryptanalysis.md), stub

**Against the implementation**

- [Side-channel attacks](side-channel-attacks.md), stub

**Historical**

- [Cryptanalysis of the Lorenz cipher](cryptanalysis-of-the-lorenz-cipher.md), stub

Related and filed elsewhere: [Frequency analysis](../Decipherment/frequency-analysis.md), which sits in Decipherment because it is the technique that crosses between the two areas, and the [Vigenère cipher](vigenere-cipher.md), which carries this subfield as its second value.

## Topics owed, with no source yet held

Named in the area index and deliberately not stubbed, because nothing held establishes them as topics and a placeholder with no citation would be a guess:

- **The bombe, and the cryptanalysis of Enigma.** [Good, Michie and Timms 1945](../references/good-michie-timms-1945.md) covers Tunny and not Enigma, so the Lorenz break is stubbed and the Enigma break is not. The Polish work of Rejewski and the later Bletchley Park machine both need a source.
- **Known-plaintext attack and crib-dragging** as techniques in their own right, as against the attack *model* covered by [Classes of attack](classes-of-attack.md).
- **Meet-in-the-middle attacks**, and the reason double encryption buys less than it appears to.

## What the existing notes need

[Kasiski examination](kasiski-examination.md) is 176 words and [Index of coincidence](index-of-coincidence.md) is 213, the two thinnest notes anywhere in the corpus, and both are load-bearing: the Decipherment area divides by them. Repairing them is scheduled with this area's content work in `ROADMAP.md`, and [Kasiski 1863](../references/kasiski-1863.md) is already held and unread.
