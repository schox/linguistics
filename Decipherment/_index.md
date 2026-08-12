---
type: MOC
aliases:
  - "Decipherment"
area: Decipherment
updated: 2026-08-12
---

# Decipherment

Reading lost scripts and unknown languages. The integrative area: it takes method from Cryptography, constraint from General Linguistics, candidate relatives from Human Languages, and technique from Computer Languages.

The organizing fact of this area is that the binding constraint is usually **corpus size, not cleverness**. Below a certain quantity of surviving text a proposed reading can be neither proved nor disproved, however good the method. See [The evidentiary threshold and unicity distance](evidentiary-threshold-and-unicity-distance.md).

## Subfields

Controlled vocabulary for the `subfield` field on notes in this area.

1. **The problem space**. Decipherment problems are classified by what is known, and the computational literature's three named cases are a better spine than an informal grid:
   - *Different script, same language*: Linear B to Mycenaean Greek; the Cypriot syllabary to Arcadocypriot Greek. The tractable case.
   - *Different script, different language*: [Ugaritic](ugaritic-script.md) to Old Hebrew; Phoenician to Ugaritic. Tractable where a related known language exists.
   - *Same script, different language*: Luvian and Hittite.
   - *Neither known*: Indus, [Rongorongo](rongorongo.md). No established method exists for this case.
2. **Solved decipherments**: [Egyptian hieroglyphs](egyptian-hieroglyphs.md) (Young, [Champollion](../people/champollion.md), the [Rosetta](../places/rosetta.md) Stone), [cuneiform](cuneiform.md) (Grotefend, [Rawlinson](../people/rawlinson.md), [Behistun](../places/behistun.md)), Old Persian, Linear B (Kober's triplets, Ventris, Chadwick), [Maya glyphs](maya-script.md) ([Knorozov](../people/knorozov.md), [Proskouriakoff](../people/proskouriakoff.md), and the long resistance to a phonetic reading), Hittite, [Ugaritic](ugaritic-script.md), Carian. Each worth a note on what actually broke it, which is usually a bilingual, a proper name, or a structural regularity rather than raw cleverness.
3. **Unsolved, partial and contested**: Linear A, the Indus script, Rongorongo, [Proto-Elamite](proto-elamite.md), Cypro-Minoan, the Phaistos Disc, Isthmian and Olmec, the Rohonc Codex, the [Voynich manuscript](voynich-manuscript.md). Also Etruscan, readable but not understood, which demonstrates that script and language are genuinely separate problems.
4. **Manual method**: frequency and positional analysis, sign inventories and how you count them, Kober's triplets and the detection of inflection, Ventris's grid, name-hunting (cartouches, royal names, toponyms), archaeological and iconographic context, bilinguals and quasi-bilinguals, and the fact that most early writing is administrative, which constrains the content you can expect to find.
5. **Computational method**, which splits three ways. Popular coverage collapses them, so hold the distinction firmly:
   - *Restoration and attribution*, where script and language are known and the text is damaged: Pythia, Ithaca, Aeneas. These decipher nothing.
   - *Decipherment proper*, mapping an unknown script onto a known language: minimum-cost flow models, phonetic-prior models for undersegmented scripts, combinatorial optimisation with coupled simulated annealing.
   - *Cognate and related-language search*, which is where Linear A actually sits: testing candidate relatives rather than producing a reading.
6. **Epistemics**: what counts as a decipherment, evidentiary thresholds, falsification criteria, overfitting and pareidolia, the fact that a model always outputs something, why undeciphered scripts attract cranks, and the question of whether a given corpus is writing at all.
7. **Practitioners**: Champollion, Rawlinson, Kober, Ventris, Chadwick, Knorozov, Proskouriakoff, Barber, and the cryptanalysts who crossed over in both directions.
8. **Infrastructure**: sign lists and their disputes, transliteration conventions, Unicode encoding of ancient scripts, digital corpora and their gaps, dating and provenance, forgeries.

## Subfield vocabulary

The exact permitted values for the `subfield` field on notes in this area. `scripts/check-vault.py` reads this list verbatim. To add a value, add it here in the same change.

- The problem space
- Solved decipherments
- Unsolved, partial and contested
- Manual method
- Computational method
- Epistemics
- Practitioners
- Infrastructure
- Writing systems

## Subfield hubs

Every subfield has a `MOC` hub, so the taxonomy is visible in the graph. The hubs are stubs; the area's existing notes still `belongs_to` this hub directly, and re-parenting them is recorded in `ROADMAP.md`.

- [The problem space](the-problem-space.md)
- [Solved decipherments](solved-decipherments.md)
- [Unsolved, partial and contested](unsolved-partial-and-contested.md)
- [Manual method](manual-method.md)
- [Computational method](computational-method.md)
- [Epistemics](epistemics.md)
- [Practitioners](practitioners.md)
- [Infrastructure](infrastructure.md)
- [Writing systems](../General-Linguistics/writing-systems.md), the shared hub with General Linguistics, now holding [Script typology](../General-Linguistics/script-typology.md)

## What is stubbed

**52 topic stubs, added 2026-08-12**, completing the last of the five areas. This area is the reverse of the others: content came first, 21 notes written across nine batches before any taxonomy existed, so the stubbing is filling in around finished work rather than mapping an empty discipline.

The topics come from this index's own subfield descriptions, which already named them, and from the items `ROADMAP.md` records as owed. By subfield: The problem space 4, Solved decipherments 8, Unsolved, partial and contested 4, Manual method 8, Computational method 6, Epistemics 5, Infrastructure 6, Practitioners 11.

**The computational stubs are the best sourced anywhere in the corpus**: five of six cite the paper that introduced the method, all already held. The eleven practitioner stubs needed no selection principle, since every one is already named as owed.

**Twelve `Script` stubs carry `class: undetermined`.** A stub asserts nothing about its subject and the typology in [Script typology](../General-Linguistics/script-typology.md) has not been applied to them. `decipherment_status` is set, because that is the claim which files each one as solved or unsolved.

## Notes

- [The evidentiary threshold and unicity distance](evidentiary-threshold-and-unicity-distance.md)
- [Adversarial versus accidental encipherment](adversarial-versus-accidental.md)
- [Script versus language](script-versus-language.md)
- [Frequency analysis](frequency-analysis.md)
- [Is it writing at all? The Indus entropy debate](is-it-writing-at-all.md)
- [Computational decipherment: three distinct tasks](computational-decipherment-three-tasks.md)
- [What counts as one sign](segmentation-and-transcription.md), segmentation and transcription as prior decisions
- [Why a script stays unread](why-scripts-stay-unread.md), the taxonomy of obstacles, evidential and otherwise

## Scripts

- [Egyptian hieroglyphs](egyptian-hieroglyphs.md), deciphered, and the case every later decipherment is measured against
- [Cuneiform](cuneiform.md), deciphered, and the one that invented a verification procedure
- [Mayan hieroglyphs](maya-script.md), deciphered, and blocked for years by authority rather than by evidence
- [Ugaritic script](ugaritic-script.md), deciphered in about a year, the fastest in the record
- [Linear B](linear-b.md), deciphered
- [Linear A](linear-a.md), undeciphered, and the corpus-size case in its clearest form
- [Indus script](indus-script.md), undeciphered, and disputed as to whether it is writing at all
- [Cypro-Minoan](cypro-minoan.md), undeciphered, between a script we cannot read and one we can
- [Phaistos Disc](phaistos-disc.md), undeciphered, and the limiting case: a corpus of one object
- [Rongorongo](rongorongo.md), undeciphered, where the reading community was destroyed inside the record
- [Proto-Elamite](proto-elamite.md), partial, and partial in an unexpected direction
- [Voynich manuscript](voynich-manuscript.md), undeciphered, and not certainly a decipherment problem at all
- [Etruscan alphabet](etruscan-alphabet.md), deciphered script, partly understood language

## Documents

(none yet)

## Images

(none yet)
