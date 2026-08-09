---
type: Doc
status: living
---

# Status

Where the project is up to, as at 2026-08-09. Update this when the picture changes; it is the first thing an incoming agent should read after `AGENTS.md`.

## What exists

The structure is complete and enforced. Five areas, thirteen note types plus `Type` itself, a stated subfield vocabulary per area, an external-identifier scheme, a bibliography, and a checker that fails the build on schema violations. Every type has at least one worked example, named in its type file.

The vault currently holds 79 notes. That is a skeleton with a good spine, not a body of research.

Content is now being added in **batches**, one commit per closure set: an anchor note plus every note it must link for the checker to pass, plus the index updates and this file. See the batching plan below and the entry on sweeps in `DECISIONS.md`.

## What is deliberately thin

Content. The areas hold their taxonomy and a handful of exemplars, nothing more:

- **General Linguistics**: 1 note (the Chomsky hierarchy). Ten subfields, nine empty.
- **Human Languages**: 2 notes (Etruscan, Mycenaean Greek). The genealogy is mapped to branch level and almost entirely unpopulated.
- **Computer Languages**: 1 note (Lisp).
- **Cryptography**: 3 notes (Vigenère, and two methods).
- **Decipherment**: the most developed area, 9 notes, because it carries the vault's argument.

## The batching plan

Agreed with Andrew on 2026-08-09. Argument-first rather than coverage-first: notes that make the vault's central claim checkable are worth more than even coverage across areas.

**Phase 1, the undeciphered scripts.** Each with ISO 15924 code, Unicode block, `corpus_size` and `found_at`. Corpus size is the variable the whole Decipherment argument turns on.

1. ~~Linear A, with Hagia Triada~~ **done**, 2026-08-09.
2. The Indus script, with Mohenjo-daro and Harappa. Two references already exist and it feeds `is-it-writing-at-all.md`.
3. Cypro-Minoan (`Cpmn`, 402) and the Phaistos Disc, with Enkomi and Phaistos.
4. Rongorongo (`Roro`, 620), Proto-Elamite (`Pelm`, 016) and the Voynich, with Rapa Nui and Susa.

**Phase 2, the solved decipherments.** Egyptian hieroglyphs, cuneiform, Maya glyphs, Ugaritic. One batch each, each worth a note on *what actually broke it*, usually a bilingual, a proper name, or a structural regularity.

**Phase 3, people.** Driven by `--report`, not by a wishlist: the sweep lists names recurring across two or more notes, which is the inclusion test in `types/person.md` stated mechanically. As at this commit it surfaces Champollion, Rawlinson, Knorozov, Proskouriakoff, Turing, Saussure, al-Kindi and Michael Ventris.

**Phase 4, the thin areas.** General Linguistics and Computer Languages, one note each. `chomsky-hierarchy.md` is currently load-bearing for an entire junction on its own.

Running alongside: the two unwritten junction notes at the foot of `_junctions.md`, and the `wikidata` sweep. The identifier sweep is **not** the cheap job it looks: a Q-number is the most fabricable string in the vault, so it needs real lookups, and it is deliberately scheduled after phase 1 rather than done from recall.

## Useful facts already established

Verified while writing batch 1, so later batches need not re-derive them:

- ISO 15924, from the Unicode Consortium code list: Linear A `Lina` 400, Linear B `Linb` 401, Cypro-Minoan `Cpmn` 402, Indus `Inds` 610, Rongorongo `Roro` 620, Proto-Elamite `Pelm` 016.
- **The Phaistos Disc has no ISO 15924 code at all.** That is a genuine gap in the registry, not an oversight in this vault, and batch 3 has to say so rather than leave the field looking unfilled.
- Unicode blocks: Linear A U+10600-U+1077F, Linear B Syllabary U+10000-U+1007F, Linear B Ideograms U+10080-U+100FF, Aegean Numbers U+10100-U+1013F, Cypro-Minoan U+12F90-U+12FFF.

## Known limitations

- `wikidata` is empty nearly everywhere. It is the universal join key, so filling it is high value, but see the warning above about doing it from recall.
- **The checker cannot detect a fabricated citation.** It verifies that `## Sources` exists and that relative links resolve; a plausible-looking invented DOI passes. Fact and link checking is handled by a separate service Andrew runs. The evidentiary standard in `AGENTS.md` is therefore a discipline, not something the tooling enforces.
- Two sources reached during batch 1 were unavailable and their absence is recorded in the notes rather than papered over: John G. Younger's Linear A transcriptions at `people.ku.edu`, which did not resolve and which the corpus figures ultimately descend from, and Pleiades, which was behind bot detection so no site identifier could be confirmed.
- No `Media` notes and nothing in `attachments/` yet.
- No automated intake routine, unlike the Andrew and Novansa vaults. Material is added deliberately.
- The vault has never been tested against Tolaria's actual rendering of the newer types (`Script`, `Method`, `Person`, `Place`). Icons and colors in `types/*.md` are guesses at Tolaria's icon set and may need correcting in the app.

## Open questions for Andrew

- Whether grammatology should move wholesale into Decipherment, or stay split between there and General Linguistics. Deferred once already; `Script` notes currently live in `Decipherment/` regardless of status.
- Whether Noam Chomsky and Donald Knuth should get `Person` notes. Chomsky was deliberately not written because his current status could not be verified and false death reports circulated in 2024; see the living-people rule in `types/person.md`.
