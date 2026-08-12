---
type: MOC
aliases:
  - "General Linguistics"
area: General-Linguistics
updated: 2026-08-12
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

## Subfield hubs

Every subfield has a `MOC` hub, so the taxonomy is visible in the graph. Two have content, Levels of analysis and Writing systems; the other eight are stubs awaiting the breadth program in `ROADMAP.md`.

- [Levels of analysis](levels-of-analysis.md), with content
- [Historical and comparative](historical-and-comparative.md)
- [Typology and universals](typology-and-universals.md)
- [Sociolinguistics](sociolinguistics.md)
- [Psycholinguistics and acquisition](psycholinguistics-and-acquisition.md)
- [Writing systems](writing-systems.md), shared with Decipherment
- [Computational linguistics](computational-linguistics.md)
- [Formal foundations](formal-foundations.md), shared with Computer Languages
- [Semiotics and philosophy of language](semiotics-and-philosophy-of-language.md)
- [Etymology and lexicography](etymology-and-lexicography.md)

## Notes

Each subfield gets a `MOC` note as its hub. Content notes `belongs_to` that hub rather than this one, and child topics `belongs_to` their parent note, so the tree hangs off the `belongs_to` chain rather than a list maintained by hand. See `CONVENTIONS.md`.

- **[Levels of analysis](levels-of-analysis.md)** (MOC)
  - [Phonetics](phonetics.md), the physical signal
  - [Phonology](phonology.md), the system of contrasts
  - [Morphology](morphology.md), word structure
  - [Syntax](syntax.md), phrase and sentence structure
  - [Semantics](semantics.md), meaning independent of context
  - [Pragmatics](pragmatics.md), meaning in context
  - Discourse, unwritten
- **[Writing systems](writing-systems.md)** (MOC), shared with Decipherment
  - [Script typology](script-typology.md), what the signs stand for, and the source of the `class` vocabulary
  - [Orthographic depth](orthographic-depth.md), how directly an orthography maps signs to sounds
- **[Formal foundations](formal-foundations.md)** (MOC), shared with Computer Languages
  - [The Chomsky hierarchy](chomsky-hierarchy.md)
- **[Computational linguistics](computational-linguistics.md)** (MOC)
  - [Redundancy](redundancy.md)

The six notes under Levels of analysis are entries rather than treatments: each defines its subject, describes it with examples, names the child topics that should become notes of their own, and records what it does not cover.

**All 75 child topics were stubbed on 2026-08-12**, each citing the chapter of [Anderson et al. 2022](../references/anderson-et-al-2022.md) its parent entry draws on. None is written. See [Levels of analysis](levels-of-analysis.md).

**Still empty:** Historical and comparative, Typology and universals, Sociolinguistics, Psycholinguistics and acquisition, Semiotics and philosophy of language, Etymology and lexicography.

**Writing systems has two entries written**, [Script typology](script-typology.md) and [Orthographic depth](orthographic-depth.md). The history of the alphabet, transliteration and romanization standards, script reform, literacy and the grapheme are still owed to the hub.

## Documents

(none yet)

## Images

(none yet)
