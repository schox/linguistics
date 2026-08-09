---
type: MOC
area: Decipherment
updated: 2026-08-09
---

# Decipherment

Reading lost scripts and unknown languages. The integrative area: it takes method from Cryptography, constraint from General Linguistics, candidate relatives from Human Languages, and technique from Computer Languages.

The organizing fact of this area is that the binding constraint is usually **corpus size, not cleverness**. Below a certain quantity of surviving text a proposed reading can be neither proved nor disproved, however good the method. See [The evidentiary threshold and unicity distance](evidentiary-threshold-and-unicity-distance.md).

## Subfields

Controlled vocabulary for the `subfield` field on notes in this area.

1. **The problem space**. Decipherment problems are classified by what is known, and the computational literature's three named cases are a better spine than an informal grid:
   - *Different script, same language*: Linear B to Mycenaean Greek; the Cypriot syllabary to Arcadocypriot Greek. The tractable case.
   - *Different script, different language*: Ugaritic to Old Hebrew; Phoenician to Ugaritic. Tractable where a related known language exists.
   - *Same script, different language*: Luvian and Hittite.
   - *Neither known*: Indus, Rongorongo. No established method exists for this case.
2. **Solved decipherments**: Egyptian hieroglyphs (Young, Champollion, the Rosetta Stone), cuneiform (Grotefend, Rawlinson, Behistun), Old Persian, Linear B (Kober's triplets, Ventris, Chadwick), Maya glyphs (Knorozov, Proskouriakoff, and the long resistance to a phonetic reading), Hittite, Ugaritic, Carian. Each worth a note on what actually broke it, which is usually a bilingual, a proper name, or a structural regularity rather than raw cleverness.
3. **Unsolved, partial and contested**: Linear A, the Indus script, Rongorongo, Proto-Elamite, Cypro-Minoan, the Phaistos Disc, Isthmian and Olmec, the Rohonc Codex, the Voynich manuscript. Also Etruscan, readable but not understood, which demonstrates that script and language are genuinely separate problems.
4. **Manual method**: frequency and positional analysis, sign inventories and how you count them, Kober's triplets and the detection of inflection, Ventris's grid, name-hunting (cartouches, royal names, toponyms), archaeological and iconographic context, bilinguals and quasi-bilinguals, and the fact that most early writing is administrative, which constrains the content you can expect to find.
5. **Computational method**, which splits three ways. Popular coverage collapses them, so hold the distinction firmly:
   - *Restoration and attribution*, where script and language are known and the text is damaged: Pythia, Ithaca, Aeneas. These decipher nothing.
   - *Decipherment proper*, mapping an unknown script onto a known language: minimum-cost flow models, phonetic-prior models for undersegmented scripts, combinatorial optimisation with coupled simulated annealing.
   - *Cognate and related-language search*, which is where Linear A actually sits: testing candidate relatives rather than producing a reading.
6. **Epistemics**: what counts as a decipherment, evidentiary thresholds, falsification criteria, overfitting and pareidolia, the fact that a model always outputs something, why undeciphered scripts attract cranks, and the question of whether a given corpus is writing at all.
7. **Practitioners**: Champollion, Rawlinson, Kober, Ventris, Chadwick, Knorozov, Proskouriakoff, Barber, and the cryptanalysts who crossed over in both directions.
8. **Infrastructure**: sign lists and their disputes, transliteration conventions, Unicode encoding of ancient scripts, digital corpora and their gaps, dating and provenance, forgeries.

## Notes

- [The evidentiary threshold and unicity distance](evidentiary-threshold-and-unicity-distance.md)
- [Adversarial versus accidental encipherment](adversarial-versus-accidental.md)
- [Script versus language](script-versus-language.md)
- [Frequency analysis](frequency-analysis.md)
- [Is it writing at all? The Indus entropy debate](is-it-writing-at-all.md)
- [Computational decipherment: three distinct tasks](computational-decipherment-three-tasks.md)

## Documents

(none yet)

## Images

(none yet)
