---
type: MOC
aliases:
  - "Post-quantum cryptography"
area: Cryptography
subfield:
  - Post-quantum cryptography
belongs_to: "[[Cryptography]]"
updated: 2026-08-12
---
# Post-quantum cryptography

Classical algorithms chosen to resist attack by a quantum computer. NIST's distinction is the governing one: post-quantum cryptography is "a defense against potential cyberattacks from quantum computers", built on mathematics that is often very old, and is a different subject from [quantum cryptography](quantum-cryptography.md), which is "based fundamentally on quantum physics".

Stubbed out on 2026-08-12, one level. Nothing here is written yet.

## Notes in this subfield

- [Lattice-based cryptography](lattice-based-cryptography.md)
- [ML-KEM](ml-kem.md), FIPS 203
- [ML-DSA](ml-dsa.md), FIPS 204
- [SLH-DSA](slh-dsa.md), FIPS 205
- [Hash-based signatures](hash-based-signatures.md)
- [Code-based cryptography](code-based-cryptography.md)
- [The NIST standardization process](the-nist-standardization-process.md)
- [Harvest-now-decrypt-later](harvest-now-decrypt-later.md)

The quantum attacks that motivate all of this are filed under [Quantum cryptanalysis](quantum-cryptanalysis.md) in Cryptanalysis, with [Shor's algorithm](shors-algorithm.md) and [Grover's algorithm](grovers-algorithm.md) beneath it. [McEliece](mceliece-cryptosystem.md), the long-standing code-based scheme, sits under public-key encryption because it predates the term by decades.
