---
type: Reference
aliases:
  - "Boneh and Shoup 2023"
authors: "Boneh, D.; Shoup, V."
year: 2023
title: "A Graduate Course in Applied Cryptography"
container: "Version 0.6, 14 January 2023. Self-published online"
ref_type: book
url: "https://toc.cryptobook.us/"
accessed: 2026-08-12
status: in-progress
subfield:
  - Theory
belongs_to: "[[Cryptography]]"
---

# Boneh and Shoup 2023

A free graduate textbook on applied cryptography, held alongside [Menezes et al. 1996](menezes-et-al-1996.md) as the second classification instrument for this area, and covering the material a handbook from 1996 could not.

## What it establishes

Used, like the handbook, for its structure rather than its contents. Twenty-three chapters in three parts:

- **Part I, Secret Key Cryptography**: introduction; encryption; stream ciphers; block ciphers; chosen plaintext attacks; message integrity; message integrity from universal hashing; message integrity from collision resistant hashing; authenticated encryption.
- **Part II, Public Key Cryptography**: public key tools; public key encryption; chosen ciphertext secure public-key encryption; digital signatures; fast signatures from one-way functions; elliptic curve cryptography and pairings; attacks on number theoretic assumptions; post-quantum cryptography from lattices.
- **Part III, Protocols**: protocols for identification and login; identification and signatures from sigma protocols; proving properties in zero-knowledge; authenticated key exchange; threshold cryptography; secure multi-party computation.

Four appendices cover number theory, probability, complexity and probabilistic algorithms.

**What it adds over the 1996 handbook**, and the reason both are held:

- **Authenticated encryption** as a named primitive with its own chapter, rather than as a construction.
- **Security definitions as organizing principle**: chosen plaintext attack and chosen ciphertext security are chapters, not remarks. The handbook organizes by mechanism, this by what is being proved.
- **Post-quantum cryptography from lattices**, a subject that did not exist as a research program when the handbook was written.
- **Advanced protocols**: zero-knowledge, threshold cryptography and secure multi-party computation each get a chapter. The handbook has none of the three.

It confirms the handbook's division of signatures from public-key encryption, and of identification from both.

## Access

Free from the authors, as a full PDF and chapter by chapter. Version 0.6, dated 14 January 2023, is the version consulted; the book is a work in progress and the version number should be recorded with any citation of its contents.

The table of contents was read; the chapters were not.

## Sources

- [A Graduate Course in Applied Cryptography](https://toc.cryptobook.us/)
