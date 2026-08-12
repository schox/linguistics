---
type: Reference
aliases:
  - "Menezes et al. 1996"
authors: "Menezes, A. J.; van Oorschot, P. C.; Vanstone, S. A."
year: 1996
title: "Handbook of Applied Cryptography"
container: "CRC Press. ISBN 0-8493-8523-7"
ref_type: book
url: "https://cacr.uwaterloo.ca/hac/"
accessed: 2026-08-12
status: in-progress
subfield:
  - Theory
belongs_to: "[[Cryptography]]"
related_to:
  - "[[Decipherment]]"
---

# Menezes et al. 1996

The standard reference handbook of applied cryptography, and the source of the topic map this area's subfield vocabulary is checked against. All fifteen chapters are free from the authors' site with the publisher's permission.

## What it establishes

Used here as a **classification instrument** rather than for its contents: the chapter and section structure is a published, citable answer to what the field contains, which is what a taxonomy needs and what an invented list cannot supply.

The fifteen chapters: Overview of Cryptography; Mathematical Background; Number-Theoretic Reference Problems; Public-Key Parameters; Pseudorandom Bits and Sequences; Stream Ciphers; Block Ciphers; Public-Key Encryption; Hash Functions and Data Integrity; Identification and Entity Authentication; Digital Signatures; Key Establishment Protocols; Key Management Techniques; Efficient Implementation; Patents and Standards.

Roughly ninety numbered sections sit beneath those, and the detailed table of contents is public on the same site.

Four divisions it draws that a casual list of cryptographic topics tends not to:

- **Digital signatures are their own chapter** (11), separate from public-key encryption (8). Signing and encrypting are different operations with different security goals.
- **Key establishment** (12) and **key management** (13) are two chapters, not a footnote to public-key cryptography.
- **Pseudorandom bits and sequences** is a chapter of its own (5). Generation of randomness is treated as a primitive, not an implementation detail.
- **Identification and entity authentication** (10) is separate from both signatures and protocols.

**It is a 1996 book**, and the date shows in what is absent rather than in what is wrong: no authenticated encryption as a named primitive, no post-quantum cryptography, no treatment of side-channel attacks, and its block-cipher chapter predates AES. [Boneh and Shoup 2023](boneh-shoup-2023.md) is held alongside it for that reason.

## Access

Free from the Centre for Applied Cryptographic Research at the University of Waterloo, chapter by chapter as PDFs, with CRC Press's permission.

**The license is restrictive and matters for this repository.** The copyright notice permits retrieving, printing and storing *a single copy for personal use*, and explicitly forbids binding chapters together, photocopying, copies beyond personal use, and making electronic copies available to others without written permission. **No chapter of this book goes into `attachments/`**, which has a public remote. Cite and link only.

The tables of contents and front matter were read; the chapters themselves were not, which is why `status` is `in-progress` and why nothing here rests on the book's substance.

**The year and ISBN are not on the publisher's free site.** Both were taken from an Open Library catalog record, which gives 1996 as first publication, CRC Press, ISBN 9780849385230, the thirteen-digit form of 0-8493-8523-7. A printed copyright page would confirm them at first hand.

## Sources

- [Handbook of Applied Cryptography, free chapters](https://cacr.uwaterloo.ca/hac/)
- [Detailed table of contents](https://cacr.uwaterloo.ca/hac/about/table_of_contents.html)
- [Copyright notice](https://cacr.uwaterloo.ca/hac/about/copyright-notice.html)
- [Open Library catalog record](https://openlibrary.org/search?q=Handbook+of+applied+cryptography), for the year and ISBN
