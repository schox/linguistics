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

**Stub hub.** This note exists so the taxonomy is visible in the graph before the subfield has content; the breadth program in `ROADMAP.md` fills it in. Notes in this subfield set `belongs_to` here once it has an owner below the area hub.

## Topics owed to this hub

Lattice-based cryptography, ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205), hash-based signatures, code-based cryptography, the NIST standardization process, harvest-now-decrypt-later, cryptographic agility and migration.

From [Boneh and Shoup 2023](../references/boneh-shoup-2023.md) chapter 17 and NIST's post-quantum project, which standardized the first three in August 2024.

**Shor and Grover are not here.** They are attacks, and sit under [Cryptanalysis](cryptanalysis.md) with the other attacks. Most treatments put them in this chapter instead, because the threat is what motivates the remedy; filing them with attacks is the more consistent choice here and is a deliberate deviation.

## Notes in this subfield

(none yet)
