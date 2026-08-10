---
type: Doc
status: living
---

# Roadmap

What to do next, in what order, and what is stuck. `STATUS.md` says where the project is; this says where it is going. `DECISIONS.md` says why the shape is what it is.

**This file holds judgement, not inventory.** The vault accumulates an `## Open questions` section on most notes, and there are dozens of them. Do not copy them here; a hand-maintained list of that size is stale the first time a note is edited. Get the live list instead:

```sh
python3 scripts/check-vault.py --questions
```

That harvests every open question in the vault, grouped by note. This file records only the ones that need a decision, an external resource, or an ordering choice.

## The audit, deferred on purpose

**Agreed with Andrew on 2026-08-10: there will be a full audit of the whole corpus, and it happens when the vault is much closer to complete, not before.** Nothing in the harvested list needs chasing in the meantime.

That is a deliberate trade. The alternative, resolving every open question as it arises, would mean each batch spends more effort on the tail of the previous one than on new material, and a note written today may be superseded by a source read next month anyway. Recording gaps honestly and moving on is cheaper than closing them one at a time, which is the whole reason `## Open questions` exists as a convention.

**What the audit should cover when it comes:**

1. Every item from `--questions`, triaged: closeable now, blocked, or not worth pursuing.
2. Bibliographic details marked provisional, especially `Olivier 2007` and `Montecchi 2019`.
3. Every figure the vault computed rather than quoted, re-derived. The convention requires the working to be shown, so this is checkable.
4. Facts taken at second hand where the primary source exists, notably everything reaching the vault through Farmer, Sproat and Witzel, Petrolito and colleagues, or a review rather than the book reviewed.
5. Content retrieved through the Tavily extraction service rather than seen directly. Those notes say so; the audit should confirm the pages still say what was extracted.
6. Empty identifier fields, distinguishing "not looked up" from "searched and probably absent". The vault has been careful about this distinction and it should be verified.
7. Andrew's standing questions, at the foot of `STATUS.md`.

## Blocked on Andrew

Nothing here can be moved by more searching.

- **Cambridge Core access.** Three volumes in *Elements in Writing in the Ancient World* cover three of the vault's seven undeciphered scripts, and all are paywalled: [Salgarella 2025](references/salgarella-2025.md) on Linear A, [Kelley 2026](references/kelley-2026.md) on Proto-Elamite, [Donnelly 2025](references/donnelly-2025.md) on Cypro-Minoan. An institutional login or the three eBooks would close roughly a dozen open questions. Salgarella's sections 3 and 5 alone would settle the per-site distribution of the Linear A corpus, the longest-standing gap in the vault.
- **Grammatology's home**: wholly into Decipherment, or split with General Linguistics. Deferred twice now. `Script` notes currently live in `Decipherment/` as a filing convenience, which `DECISIONS.md` records as a convenience and not a claim.
- **Whether Chomsky and Knuth get `Person` notes.** Chomsky was deliberately left unwritten because his status could not be verified and false death reports circulated in 2024. See the living-people rule in `types/person.md`.

## Blocked on external sources

- **Montecchi 2019**, the study of record for the Hagia Triada archive. The Bologna repository returns 403 and failed again through Tavily; the CNR eprints server has a TLS error. This is what would settle the contested tablet count, 147 against Rutter's 168.
- **Younger's Linear A transcriptions.** The University of Kansas site is gone. A 53-page deposit under his name exists on Academia.edu, last updated 8 April 2024. The vault's Linear A corpus figures descend from the dead site, so confirming they are traceable into the surviving document is the single most valuable outstanding check.
- **Mahadevan 1977**, an 829-page print memoir, for the per-site distribution of the Indus corpus.
- **The Cuneiform Digital Library Initiative**, for the Proto-Elamite corpus and its per-site breakdown. Not blocked, simply not yet consulted.

## Next work, in order

**Phase 2, the solved decipherments.** ~~Egyptian hieroglyphs~~ done 2026-08-10; then cuneiform, Maya glyphs, Ugaritic. One batch each, each on *what actually broke it*, which is usually a bilingual, a proper name, or a structural regularity rather than cleverness. Older sources, far more likely to be open access than phase 1's were. Ugarit is needed as a `Place` note here and is already overdue as the sole provenance of the CM3 texts.

**Phase 3, people.** Driven by `check-vault.py --report`, which lists names recurring across two or more notes, that being the inclusion test in `types/person.md` stated mechanically. It currently surfaces Champollion, Rawlinson, Knorozov, Proskouriakoff, Turing, Saussure, al-Kindi and Michael Ventris. Let the vault say who it needs rather than working from a wishlist.

**Phase 4, the thin areas.** General Linguistics and Computer Languages, one note each. `chomsky-hierarchy.md` is load-bearing for an entire junction on its own.

## Standalone items, not tied to a phase

- **Linear Elamite** deserves a note. It is not Proto-Elamite, and `Decipherment/proto-elamite.md` states the distinction. Its 21 or 22 inscriptions, most longer than the longest of 4,000 to 5,000 Indus texts, are the cleanest demonstration in the vault that corpus volume and text length are independent variables. No ISO 15924 code, no Unicode block.
- **A `Language` note for Rapanui.** A real, living, attested language currently mentioned only as an appendage to a script, and the vault's first Austronesian entry.
- **Thomas Young now clearly earns a `Person` note.** He meets two limbs of the inclusion test: discussed in two or more notes, and bridging areas, since the same man worked on optics and physiology. The credit dispute with Champollion is recorded in `people/champollion.md` and would be better balanced by a note of his own.
- **Coptic, and the Coptic alphabet.** `Copt` 204, blocks U+2C80-U+2CFF and U+102E0-U+102FF, both verified. Whether Coptic is a stage of Egyptian or a language in its own right decides whether that is one note or two.
- **Hieratic (`Egyh` 060) and demotic (`Egyd` 070)** have codes and no notes, and demotic is a third of the Rosetta Stone.
- **Cretan Hieroglyphic**, the third Aegean script of the period and the natural comparison for both Linear A and the Phaistos Disc. Mnamon covers it.
- **The `wikidata` sweep.** High value as the universal join key, and **not** the cheap job it looks: a Q-number is the most fabricable string in the vault, so it needs real lookups rather than recall.
- **Two junction notes** still unwritten at the foot of `_junctions.md`, plus a third added after batch 4: corpus destruction as a historical event rather than an accident, which rongorongo showed the existing framing does not cover.
- **Test the vault against Tolaria's actual rendering.** Icons and colors in `types/*.md` are guesses at Tolaria's icon set and have never been checked in the app.

## Sources

This is a planning document rather than a research note, so it carries no citations of its own. Every claim above about a source's status is recorded, with its evidence, in the relevant `Reference` note or in `STATUS.md`.
