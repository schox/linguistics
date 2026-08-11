---
type: MOC
area: General-Linguistics
updated: 2026-08-09
---

# General Linguistics

The theory. Supplies the constraints that make every other area tractable, and in particular supplies decipherment with its notion of what a possible human language looks like.

## Subfields

Controlled vocabulary for the `subfield` field on notes in this area.

1. **Levels of analysis**: phonetics (articulatory, acoustic, auditory), phonology, morphology, syntax, semantics, pragmatics, discourse.
2. **Historical and comparative**: the comparative method, regular sound change, internal reconstruction, proto-language reconstruction, glottochronology and its critics, contact, substrate and superstrate, borrowing versus inheritance.
3. **Typology and universals**: word order, morphosyntactic alignment (nominative-accusative, ergative-absolutive, split systems), Greenbergian universals, WALS, areal features and Sprachbund.
4. **Sociolinguistics**: variation and change, dialectology and isoglosses, register and code-switching, pidgins and creoles, standardization and language policy, endangerment, documentation and revival.
5. **Psycholinguistics and acquisition**: first and second language acquisition, processing, aphasia and neurolinguistics, the critical period, sign language acquisition.
6. **Writing systems**: typology of scripts, the history of the alphabet, literacy and orthographic depth, script reform, transliteration and romanization standards. Junction with Decipherment.
7. **Computational linguistics**: corpus methods, distributional semantics and embeddings, parsing, machine translation, LLMs as linguistic objects and as linguistic evidence. Junction with Computer Languages and Decipherment.
8. **Formal foundations**: generative grammar, the Chomsky hierarchy, formal semantics, dependency versus constituency. Junction with Computer Languages.
9. **Semiotics and philosophy of language**: Saussure, Peirce, sense and reference, speech acts, linguistic relativity and its defensible versions.
10. **Etymology and lexicography**: dictionary-making, corpora, false friends and folk etymology, loanword strata.

## Subfield vocabulary

The exact permitted values for the `subfield` field on notes in this area. `scripts/check-vault.py` reads this list verbatim. To add a value, add it here in the same change.

- Levels of analysis
- Historical and comparative
- Typology and universals
- Sociolinguistics
- Psycholinguistics and acquisition
- Writing systems
- Computational linguistics
- Formal foundations
- Semiotics and philosophy of language
- Etymology and lexicography

## Notes

Each subfield gets a `MOC` note as its hub. Content notes `belongs_to` that hub rather than this one, and child topics `belongs_to` their parent note, so the tree is the computed `has` relation rather than a list maintained by hand. See `CONVENTIONS.md`.

- **[Levels of analysis](levels-of-analysis.md)** (MOC)
  - [Phonetics](phonetics.md), the physical signal
  - [Phonology](phonology.md), the system of contrasts
  - [Morphology](morphology.md), word structure
  - [Syntax](syntax.md), phrase and sentence structure
  - [Semantics](semantics.md), meaning independent of context
  - [Pragmatics](pragmatics.md), meaning in context
  - Discourse, unwritten
- **Formal foundations**, no MOC yet
  - [The Chomsky hierarchy](chomsky-hierarchy.md)
- **Computational linguistics**, no MOC yet
  - [Redundancy](redundancy.md)

The six notes under Levels of analysis are entries rather than treatments: each defines its subject, describes it with examples, names the child topics that should become notes of their own, and records what it does not cover. None of the child topics is written.

**Still empty:** Historical and comparative, Typology and universals, Sociolinguistics, Psycholinguistics and acquisition, Writing systems, Semiotics and philosophy of language, Etymology and lexicography.

**Writing systems is the most urgent.** The `class` value carried by every `Script` note in the vault (alphabet, abjad, abugida, syllabary, logographic, mixed) is a claim this area is supposed to define and does not.

## Documents

(none yet)

## Images

(none yet)
