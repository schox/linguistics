---
type: MOC
aliases:
  - "Types"
area: types
updated: 2026-08-09
---

# Types

**The type definitions are the authoritative schema.** Where this folder and prose elsewhere disagree, these files win, and the disagreement is a bug to fix.

Each file declares the type's frontmatter template, plus the allowed values for each field, plus a **`## Body` skeleton** for the note's prose. Read the one for the type you are writing before you write it. The underscore-prefixed fields (`_icon`, `_color`, `_sidebar_label`, `_order`, `_pinned_properties`) are Tolaria legacy that Obsidian ignores; they stay as harmless metadata until the audit prunes or repurposes them.

**The skeletons are guidance, not enforcement.** `scripts/check-vault.py` validates frontmatter and the presence of `## Sources`; it does not read prose. A skeleton is the shape a note of that type should take unless the subject gives a reason to differ, and the general rules behind them are in `CONVENTIONS.md` under `## Drafting`.

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

Every content note opens with a definition, names its sections for its subject rather than for its relevance to the vault, and ends with `## Sources`. `Doc` is exempt from the drafting policy entirely; see `CONVENTIONS.md`.

Wikilink values must be quoted: `"[[Cryptography]]"`. Unquoted, YAML reads `[[Cryptography]]` as a nested list and the relationship silently fails.
