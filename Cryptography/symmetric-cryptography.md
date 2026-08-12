---
type: MOC
aliases:
  - "Symmetric cryptography"
area: Cryptography
subfield:
  - Symmetric cryptography
belongs_to: "[[Cryptography]]"
updated: 2026-08-12
---
# Symmetric cryptography

Cryptography in which the same key encrypts and decrypts. Block ciphers, stream ciphers, the modes that turn a block cipher into a usable system, and authenticated encryption.

Stubbed out in full on 2026-08-12: four topics with fourteen children. Nothing here is written yet.

## Notes in this subfield

- [Block ciphers](block-ciphers.md), with two structures and five ciphers under it
- [Stream ciphers](stream-ciphers.md), with three
- [Modes of operation](modes-of-operation.md), with four
- [Authenticated encryption](authenticated-encryption.md)

Drawn from [Menezes et al. 1996](../references/menezes-et-al-1996.md) chapters 6 and 7, and [Boneh and Shoup 2023](../references/boneh-shoup-2023.md) part I. Authenticated encryption is in the second and not the first, which is a difference of date rather than of opinion, and AES is in neither: the handbook predates it.

## Still owed to this subfield

- **FEAL and SAFER**, both of which the handbook gives sections (7.5, 7.7) and which are omitted here as minor. They matter mainly as cryptanalytic targets, and the [Cryptanalysis](cryptanalysis.md) stubs reference attacks on both.
- **Key schedules** as a topic in their own right, which several attacks turn on.
- **Message authentication codes** are not here: they are filed under Hashes and integrity.
- **Chosen plaintext attacks**, named in the old topic list, are filed under [Classes of attack](classes-of-attack.md) with the other attack models.
