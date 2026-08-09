---
type: MOC
area: types
updated: 2026-08-09
---

# Types

**The type definitions are the authoritative schema.** Where this folder and prose elsewhere disagree, these files win, and the disagreement is a bug to fix.

Each file declares the frontmatter template Tolaria reads, plus the allowed values for each field. Read the one for the type you are writing before you write it.

## Entity types

- [Language](language.md), a human language. Worked example: `Human-Languages/etruscan.md`
- [Script](script.md), a writing system, not the same thing as a language. Worked example: `Decipherment/linear-b.md`
- [ComputerLanguage](computer-language.md), a programming or formal language. Worked example: `Computer-Languages/lisp.md`
- [Cipher](cipher.md), a cipher or cryptographic algorithm. Worked example: `Cryptography/vigenere-cipher.md`
- [Person](person.md), a seminal figure. Worked example: `people/alice-kober.md`
- [Place](place.md), an institution or site. Worked example: `places/bletchley-park.md`

## Content types

- [Concept](concept.md), a term or idea
- [Method](method.md), a technique that transfers between areas
- [Note](note.md), a general working note
- [Media](media.md), an image warranting its own note
- [Reference](reference.md), a bibliographic entry

## Structural types

- [MOC](moc.md), a folder index and subfield vocabulary
- [Doc](doc.md), a meta document
- `Type`, this folder's own type. Each file here declares `type: Type`.

## Common rules

Every content note carries `subfield`, `belongs_to` and `status`, and usually `related_to` and `cites`. `MOC`, `Doc` and `Type` notes are exempt.

Wikilink values must be quoted: `"[[Cryptography]]"`. Unquoted, YAML reads `[[Cryptography]]` as a nested list and the relationship silently fails.
