---
type: MOC
aliases:
  - "Key management and establishment"
area: Cryptography
subfield:
  - Key management and establishment
belongs_to: "[[Cryptography]]"
updated: 2026-08-12
---
# Key management and establishment

Getting a shared key to two parties who do not have one, and looking after keys once they exist. Two chapters of the handbook, and the part of applied cryptography that fails most often in practice.

Stubbed out on 2026-08-12, one level. Nothing here is written yet.

## Notes in this subfield

Establishment:

- [Key transport](key-transport.md)
- [Key agreement](key-agreement.md)
- [Diffie-Hellman key agreement](diffie-hellman-key-agreement.md)
- [Authenticated key exchange](authenticated-key-exchange.md)
- [Secret sharing](secret-sharing.md)
- [Conference keying](conference-keying.md)

Management:

- [Distributing public keys](distributing-public-keys.md)
- [Controlling key usage](controlling-key-usage.md)
- [Key life cycle](key-life-cycle.md)

Diffie-Hellman sits here rather than under [Public-key cryptography](public-key-cryptography.md) because it agrees a key rather than encrypting a message. The assumption beneath it is [The Diffie-Hellman problem](diffie-hellman-problem.md).
