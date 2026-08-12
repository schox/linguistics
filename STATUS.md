---
type: Doc
aliases:
  - "Status"
status: living
---

# Status

Where the project is up to, as at 2026-08-12. Update this when the picture changes; it is the first thing an incoming agent should read after `AGENTS.md`.

This file is the present tense: what exists, what is thin, what has been established, what is known to be wrong or missing. For what happens next and what is blocked, see `ROADMAP.md`.

## What exists

The structure is complete and enforced. Five areas, thirteen note types plus `Type` itself, a stated subfield vocabulary per area, an external-identifier scheme, a bibliography, and a checker that fails the build on schema violations. Every type has at least one worked example, named in its type file.

**The vault is an Obsidian vault as of 2026-08-12**, migrated from Tolaria; `DECISIONS.md` records why and what changed. **The migration is complete and the vault has been seen in the app.** Every note aliases its H1 title (checker-enforced, so title-style wikilinks resolve), every subfield has a `MOC` hub so the whole taxonomy shows in the graph, the eleven Bases in `views/*.base` render and are confirmed against observed rather than documented behavior, the Tolaria `views/*.yml` are gone, `.obsidian/` is committed, and `scripts/check-vault.py` runs in CI on every push. Andrew judged the stub taxonomy in the graph and found it sound: it needs amplification, not re-cutting. The one loose end is Breadcrumbs, installed but not yet pointed at `belongs_to`; see `ROADMAP.md`.

The vault currently holds 223 notes, of which 51 are subfield hub stubs and 13 are topic stubs so the whole taxonomy is visible in the graph. Decipherment is no longer a skeleton; every other area's content still is, though its shape now shows.

**This figure is now checked.** `scripts/check-vault.py` fails if it drifts from the actual count, which it had, silently, from 107 to 132 across eight batches.

## What is deliberately thin

Content. The areas hold their taxonomy and a handful of exemplars, nothing more:

- **General Linguistics**: 10 content notes across 21 files. The **Levels of analysis** subfield has a `MOC` and six entries (phonetics, phonology, morphology, syntax, semantics, pragmatics); the Chomsky hierarchy and redundancy sit under Formal foundations and Computational linguistics. **Writing systems** has two entries as of 2026-08-12, `script-typology.md` and `orthographic-depth.md`, and is the first subfield worked under the drafting policy. Ten subfields, six still empty. None of the child topics the six levels entries name is written.
- **Human Languages**: 7 notes (Akkadian, Classic Maya, Egyptian, Etruscan, Mycenaean Greek, Sumerian, Ugaritic). The genealogy is mapped to branch level and almost entirely unpopulated.
- **Computer Languages**: 1 note (Lisp).
- **Cryptography**: 3 written notes and 13 topic stubs, across 34 files. The subfield vocabulary was rebuilt on 2026-08-12 against three published classifications (see the area index); 14 subfields, of which **Cryptanalysis** is the first to be stubbed out in full. The other 13 hold no content note at all.
- **Decipherment**: 21 notes, plus the 15 places, 11 people and 51 references that overwhelmingly serve it. The only area worked properly, though the Writing systems entries are the first material in General Linguistics that Decipherment can lean on rather than the reverse.

The Human Languages notes are worth a caveat: all seven exist because a deciphered script needed a language to point at. The area is currently a by-product of Decipherment rather than a treatment of its own subject.

## How the content was built

Content is added in **batches**: one commit per closure set, meaning an anchor note plus every note it must link for the checker to pass, plus the index updates and this file. Argument-first rather than coverage-first, so notes that make the vault's central claim checkable come before even coverage across areas.

**Phase 1, the undeciphered scripts, is complete** as at 2026-08-10, in four batches:

1. Linear A, with Hagia Triada.
2. The Indus script, with Mohenjo-daro and Harappa.
3. Cypro-Minoan and the Phaistos Disc, with Enkomi and Phaistos.
4. Rongorongo, Proto-Elamite and the Voynich, with Rapa Nui and Susa.

All seven carry their ISO 15924 code, Unicode block, `corpus_size` and `found_at`, which was the point: corpus size is the variable the whole Decipherment argument turns on, and it is now checkable across the set rather than asserted. A cross-cutting note, `Decipherment/segmentation-and-transcription.md`, followed from what all four batches turned up independently.

**Phase 2, the solved decipherments, is under way.** Batch 5 covered Egyptian hieroglyphs; batch 6 covered cuneiform, with Behistun, Rawlinson, Hincks, Akkadian and Sumerian; batch 7 covered Mayan hieroglyphs, with Piedras Negras, Knorozov, Proskouriakoff and Classic Maya; batch 8 covered Ugaritic, with Ugarit. **Phase 2 is complete**, and produced `Decipherment/why-scripts-stay-unread.md`, the synthesis the area was building toward. That note now also diagnoses all seven unread scripts, and finds that only one of them is cleanly explained by the corpus-size thesis phase 1 established. Both batches needed `Language` notes, because a deciphered script has to have something to point at.

**The plan then changed, on Andrew's instruction.** Phases 3 and 4 as originally scoped (people, then thin areas) are superseded. The vault was going deep before it went wide, producing analysis and interpretation on a base that had no general reference under it: eight notes into the Decipherment argument, General Linguistics still had no note on phonology. The instruction is that the vault **starts as a general reference and is amplified afterward**, which means a hierarchical taxonomy per discipline and starter notes across it before any more interpretation.

**Batch 9 is the first of these**, and it establishes the shape. A `MOC` note for the **Levels of analysis** subfield of General Linguistics, plus six entries under it (phonetics, phonology, morphology, syntax, semantics, pragmatics), written from one open-access textbook ([Anderson et al. 2022](references/anderson-et-al-2022.md), CC BY-NC-SA).

**The vault is a knowledge base first and an argument second.** That ordering is Andrew's and it is the governing instruction for every batch from here. In practice:

- **An entry describes; it does not argue.** Define the subject, describe it, give examples, name the child topics, record what is not covered. Interpretation, cross-area synthesis and the vault's own reasoning belong in separate notes that link to the entries, not inside them.
- **Structure is carried by the graph, not by prose.** `belongs_to` chains from a note to its parent, up through a subfield `MOC` to the area hub, so the tree is read from the links and backlinks rather than maintained as prose. `related_to` links siblings. See `CONVENTIONS.md`.
- **Breadth changed the scope, not the evidentiary standard.** Each entry is sourced, cites its Reference, and records its gaps under `## Open questions`.

Batch 9 was written twice. The first attempt produced six essays that argued from each level back into the Decipherment area, which is the failure mode this ordering exists to prevent: it read as a thesis with a textbook attached, and it was rewritten as reference entries. The observations it generated were not discarded; they are parked in `ROADMAP.md` as notes to be written on their own once the reference layer exists.

**Everything still to do is in `ROADMAP.md`**, including what is blocked and on whom. Do not duplicate it here.

## Useful facts already established

Verified while writing batch 1, so later batches need not re-derive them:

- ISO 15924, from the Unicode Consortium code list: Linear A `Lina` 400, Linear B `Linb` 401, Cypro-Minoan `Cpmn` 402, Indus `Inds` 610, Rongorongo `Roro` 620, Proto-Elamite `Pelm` 016.
- **The Phaistos Disc has no ISO 15924 code, but does have a Unicode block** (`101D0..101FF`) and no Unicode script property value. Verified against all three registry files. Encoded as characters, unregistered as a script.
- Unicode blocks: Linear A U+10600-U+1077F, Linear B Syllabary U+10000-U+1007F, Linear B Ideograms U+10080-U+100FF, Aegean Numbers U+10100-U+1013F, Cypro-Minoan U+12F90-U+12FFF.
- **The Indus script has no Unicode block**, checked against `Blocks.txt`. Encoding presupposes an agreed sign list, which is the thing in dispute.
- Mean signs per document, for the comparison the vault's argument rests on: Indus 4.6 (sourced), Linear A c. 5.2 and Linear B at most c. 12.5 (both computed here, and the Linear B figure is an upper bound). Later batches should extend this table and keep marking which figures are sourced and which are derived.
- Total sign occurrences, the other axis: Linear B 57,398; Indus 13,372; Linear A 7,362-7,396; Phaistos Disc 241. Each is its own source's total and the four are not perfectly commensurable, so treat the comparison as order-of-magnitude.
- Cypriot syllabary is `Cprt` 403, block U+10800-U+1083F. It is **deciphered** and is the descendant of Cypro-Minoan, so do not confuse the two.

## Sources that were unreachable

Recorded so the fact-checking service can retry them rather than each batch rediscovering the block. All as at 2026-08-09/10.

- ~~Britannica, UNESCO World Heritage, harappa.com: HTTP 403~~ **resolved 2026-08-10** through Tavily. See `DECISIONS.md` for when that is appropriate and how retrieved content is marked.
- ~~`people.ku.edu` (Younger's Linear A transcriptions)~~ **explained 2026-08-10.** The site is gone, not moved: reportedly taken down by the University of Kansas after Younger's retirement, with the contents deposited on Academia.edu (last update 8 April 2024). The vault's Linear A corpus figures descend from it, so tracing them into the surviving document is the outstanding check. See the open questions in `Decipherment/linear-a.md`.
- ~~Pleiades~~ **partly resolved 2026-08-10.** Knossos is 589872, now recorded. Hagia Triada returned no record, and probably has none: Pleiades is scoped to the Greek and Roman world and a purely Minoan site may fall outside it.
- **Still blocked:** the University of Bologna repository record for Montecchi 2019, which failed again through Tavily. The CNR eprints TLS error was not retried. This is the one that would settle the contested Hagia Triada tablet count, 147 against Rutter's 168.

## Known limitations

- `wikidata` is empty nearly everywhere. It is the universal join key, so filling it is high value, but see the warning above about doing it from recall.
- **The checker cannot detect a fabricated citation.** It verifies that `## Sources` exists and that relative links resolve; a plausible-looking invented DOI passes. Fact and link checking is handled by a separate service Andrew runs. The evidentiary standard in `AGENTS.md` is therefore a discipline, not something the tooling enforces.
- Two sources reached during batch 1 were unavailable and their absence is recorded in the notes rather than papered over: John G. Younger's Linear A transcriptions at `people.ku.edu`, which did not resolve and which the corpus figures ultimately descend from, and Pleiades, which was behind bot detection so no site identifier could be confirmed.
- No `Media` notes and nothing in `attachments/` yet.
- No automated intake routine, unlike the Andrew and Novansa vaults. Material is added deliberately.
- **Obsidian creates files as a byproduct of ordinary use**, which Tolaria did not. Opening the vault for the first time produced an empty `Untitled.canvas` and, more dangerously, an empty `Decipherment.md` at the root, which would have competed with `Decipherment/_index.md` for all 91 `[[Decipherment]]` wikilinks in the vault. The checker caught both; this is the concrete argument for it running in CI. The underscore-prefixed fields in `types/*.md` are Tolaria legacy that Obsidian ignores.

## Open questions for Andrew

These two have been open since the vault was built and are restated in `ROADMAP.md` under what is blocked on him.

- Whether grammatology should move wholesale into Decipherment, or stay split between there and General Linguistics. `Script` notes currently live in `Decipherment/` regardless of status.
- Whether Noam Chomsky and Donald Knuth should get `Person` notes. Chomsky was deliberately not written because his current status could not be verified and false death reports circulated in 2024; see the living-people rule in `types/person.md`.

**The 59 open questions on individual notes are not listed anywhere by hand.** Run `python3 scripts/check-vault.py --questions` for the live set. They are deliberately not being chased: see the deferred audit in `ROADMAP.md`.
