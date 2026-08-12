---
type: MOC
aliases:
  - "Cryptography"
area: Cryptography
updated: 2026-08-12
---

# Cryptography

Historical and current, algorithms included. Also the methodological backdrop to Decipherment: the statistical apparatus transfers, the adversarial apparatus does not. See [Adversarial versus accidental encipherment](../Decipherment/adversarial-versus-accidental.md).

Discussion and reference only. This area never stores real keys, secrets or credentials (see `CONVENTIONS.md`).

## Where the vocabulary comes from

The subfield list below was revised on 2026-08-12 against three published classifications, so that the cut of the field is citable rather than invented:

- [Menezes et al. 1996](../references/menezes-et-al-1996.md), the *Handbook of Applied Cryptography*, whose fifteen chapters and roughly ninety numbered sections are the primary instrument.
- [Boneh and Shoup 2023](../references/boneh-shoup-2023.md), for the material a 1996 handbook could not cover: authenticated encryption, security definitions as organizing principle, lattices, and the advanced protocols.
- NIST's cryptographic activity areas, for what is standardized and what the standards body treats as a distinct subject.

**Two deviations from the instruments, both deliberate.** *Mechanical and electromechanical* appears in none of the three, which are all modern applied texts; it is kept because Enigma, Lorenz and Bletchley Park are where this area meets Decipherment. And *Shor and Grover* are filed under Cryptanalysis rather than under Post-quantum cryptography, on the ground that they are attacks; most treatments place them with the remedy they motivate.

## Subfields

Controlled vocabulary for the `subfield` field on notes in this area.

1. **Classical ciphers**: substitution (Caesar, Atbash, keyword), polyalphabetic (Alberti, Vigenère, Porta), transposition, nomenclators and the chancery ciphers, book and running-key ciphers, steganography as a distinct thing.
2. **Mechanical and electromechanical**: rotor machines, Enigma and its variants, Lorenz SZ40/42, Purple, Hagelin, the one-time pad and its operational failures (Venona).
3. **Cryptanalysis**: frequency analysis and al-Kindi, Kasiski examination, the index of coincidence and Friedman, known-plaintext and crib-dragging, Bletchley Park (the Polish work of Rejewski, Turing, Welchman, the bombe, Tunny and Colossus), differential and linear cryptanalysis, side-channel attacks, quantum cryptanalysis (Shor, Grover).
4. **Symmetric cryptography**: block ciphers, stream ciphers, modes of operation, authenticated encryption, DES and its politics, AES.
5. **Public-key cryptography**: RSA, Diffie-Hellman, ElGamal, elliptic curves and pairings, the factoring and discrete logarithm assumptions, chosen ciphertext security.
6. **Digital signatures and authentication**: signature schemes, DSA and ECDSA, one-time and blind signatures, entity authentication, challenge-response, sigma protocols, PKI and certificates.
7. **Hashes and integrity**: the MD and SHA families, collisions in practice, MACs and HMAC, Merkle trees, proof of work.
8. **Randomness and key generation**: random and pseudorandom bit generation, statistical tests, entropy sources and seeding, prime generation, randomness failures in deployed systems.
9. **Key management and establishment**: key transport and agreement, authenticated key exchange, secret sharing, certificate authorities, key life cycle and revocation.
10. **Protocols and deployment**: TLS, PGP and the web of trust, Signal and the double ratchet, Tor, cryptocurrencies as applied cryptography, and the advanced protocols (zero-knowledge, threshold cryptography, secure multi-party computation).
11. **Theory**: Shannon's information theory, entropy and redundancy, perfect secrecy, unicity distance, Kerckhoffs's principle, computational hardness, provable security and its limits, and the mathematical background the field rests on. Junction with Decipherment.
12. **Post-quantum cryptography**: lattice-based schemes, ML-KEM, ML-DSA, SLH-DSA, hash-based and code-based schemes, the NIST process, harvest-now-decrypt-later.
13. **Quantum cryptography**: quantum key distribution, BB84, quantum random number generation. Distinct from the above; NIST's own contrast is that post-quantum cryptography is a defense against quantum computers built on classical mathematics, while quantum cryptography is based on quantum physics.
14. **History and politics**: black chambers, the NSA and GCHQ, the crypto wars, export control, Clipper, Snowden, the current lawful-access argument.

## Subfield vocabulary

The exact permitted values for the `subfield` field on notes in this area. `scripts/check-vault.py` reads this list verbatim. To add a value, add it here in the same change.

- Classical ciphers
- Mechanical and electromechanical
- Cryptanalysis
- Symmetric cryptography
- Public-key cryptography
- Digital signatures and authentication
- Hashes and integrity
- Randomness and key generation
- Key management and establishment
- Protocols and deployment
- Theory
- Post-quantum cryptography
- Quantum cryptography
- History and politics

## Subfield hubs

Every subfield has a `MOC` hub, so the taxonomy is visible in the graph. Six are stubbed out in full: [Cryptanalysis](cryptanalysis.md), [Classical ciphers](classical-ciphers.md), [Symmetric cryptography](symmetric-cryptography.md), [Public-key cryptography](public-key-cryptography.md), [Digital signatures and authentication](digital-signatures-and-authentication.md) and [Hashes and integrity](hashes-and-integrity.md). The other eight are stub hubs awaiting the breadth program in `ROADMAP.md`.

- [Classical ciphers](classical-ciphers.md)
- [Mechanical and electromechanical](mechanical-and-electromechanical.md)
- [Cryptanalysis](cryptanalysis.md)
- [Symmetric cryptography](symmetric-cryptography.md)
- [Public-key cryptography](public-key-cryptography.md)
- [Digital signatures and authentication](digital-signatures-and-authentication.md)
- [Hashes and integrity](hashes-and-integrity.md)
- [Randomness and key generation](randomness-and-key-generation.md)
- [Key management and establishment](key-management-and-establishment.md)
- [Protocols and deployment](protocols-and-deployment.md)
- [Theory](theory.md)
- [Post-quantum cryptography](post-quantum-cryptography.md)
- [Quantum cryptography](quantum-cryptography.md)
- [History and politics](history-and-politics.md)

## Notes

Written:

- [Vigenère cipher](vigenere-cipher.md), classical
- [Kasiski examination](kasiski-examination.md), method
- [Index of coincidence](index-of-coincidence.md), method

**125 taxonomy stubs**, added 2026-08-12 across six subfields, at two levels of depth. See each hub for its list: [Cryptanalysis](cryptanalysis.md) 42, [Classical ciphers](classical-ciphers.md) 21, [Symmetric cryptography](symmetric-cryptography.md) 18, [Public-key cryptography](public-key-cryptography.md) 16, [Digital signatures and authentication](digital-signatures-and-authentication.md) 15, [Hashes and integrity](hashes-and-integrity.md) 13.

A stub says so in its body and asserts nothing about its subject. 66 cite a source naming the topic; the other 59 read **To be researched** and are listed by `python3 scripts/check-vault.py --stubs`, which is the worklist for closing them. `DECISIONS.md` records why that relaxation exists and when it expires.

## Documents

(none yet)

## Images

(none yet)
