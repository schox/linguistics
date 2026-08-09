---
type: MOC
area: Cryptography
updated: 2026-08-09
---

# Cryptography

Historical and current, algorithms included. Also the methodological backdrop to Decipherment: the statistical apparatus transfers, the adversarial apparatus does not. See [Adversarial versus accidental encipherment](../Decipherment/adversarial-versus-accidental.md).

Discussion and reference only. This area never stores real keys, secrets or credentials (see `CONVENTIONS.md`).

## Subfields

Controlled vocabulary for the `subfield` field on notes in this area.

1. **Classical ciphers**: substitution (Caesar, Atbash, keyword), polyalphabetic (Alberti, Vigenère, Porta), transposition, nomenclators and the chancery ciphers, book and running-key ciphers, steganography as a distinct thing.
2. **Mechanical and electromechanical**: rotor machines, Enigma and its variants, Lorenz SZ40/42, Purple, Hagelin, the one-time pad and its operational failures (Venona).
3. **Cryptanalysis**: frequency analysis and al-Kindi, Kasiski examination, the index of coincidence and Friedman, known-plaintext and crib-dragging, Bletchley Park (the Polish work of Rejewski, Turing, Welchman, the bombe, Tunny and Colossus), differential and linear cryptanalysis, side channels.
4. **Modern symmetric**: DES and its politics, AES, block ciphers and modes of operation, stream ciphers, authenticated encryption.
5. **Asymmetric**: Diffie-Hellman, RSA, elliptic curve, the factoring and discrete log assumptions, digital signatures, PKI and the trust problem.
6. **Hashes and integrity**: the MD and SHA families, collisions in practice, HMAC, Merkle trees, proof of work.
7. **Protocols and deployment**: TLS, PGP and the web of trust, Signal and the double ratchet, Tor, cryptocurrencies as applied cryptography.
8. **Theory**: Shannon's information theory, entropy and redundancy, perfect secrecy, unicity distance, Kerckhoffs's principle, computational hardness, provable security and its limits, zero-knowledge proofs. Junction with Decipherment.
9. **Post-quantum**: Shor and Grover, lattice-based schemes, the NIST process, harvest-now-decrypt-later.
10. **History and politics**: black chambers, the NSA and GCHQ, the crypto wars, export control, Clipper, Snowden, the current lawful-access argument.

## Subfield vocabulary

The exact permitted values for the `subfield` field on notes in this area. `scripts/check-vault.py` reads this list verbatim. To add a value, add it here in the same change.

- Classical ciphers
- Mechanical and electromechanical
- Cryptanalysis
- Modern symmetric
- Asymmetric
- Hashes and integrity
- Protocols and deployment
- Theory
- Post-quantum
- History and politics

## Notes

- [Vigenère cipher](vigenere-cipher.md), classical
- [Kasiski examination](kasiski-examination.md), method
- [Index of coincidence](index-of-coincidence.md), method

## Documents

(none yet)

## Images

(none yet)
