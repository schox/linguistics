---
type: Doc
status: living
---

# Status

Where the project is up to, as at 2026-08-09. Update this when the picture changes; it is the first thing an incoming agent should read after `AGENTS.md`.

## What exists

The structure is complete and enforced. Five areas, thirteen note types plus `Type` itself, a stated subfield vocabulary per area, an external-identifier scheme, a bibliography, and a checker that fails the build on schema violations. Every type has at least one worked example, named in its type file.

The vault currently holds 96 notes. That is a skeleton with a good spine, not a body of research.

Content is now being added in **batches**, one commit per closure set: an anchor note plus every note it must link for the checker to pass, plus the index updates and this file. See the batching plan below and the entry on sweeps in `DECISIONS.md`.

## What is deliberately thin

Content. The areas hold their taxonomy and a handful of exemplars, nothing more:

- **General Linguistics**: 1 note (the Chomsky hierarchy). Ten subfields, nine empty.
- **Human Languages**: 2 notes (Etruscan, Mycenaean Greek). The genealogy is mapped to branch level and almost entirely unpopulated.
- **Computer Languages**: 1 note (Lisp).
- **Cryptography**: 3 notes (Vigenère, and two methods).
- **Decipherment**: the most developed area, 12 notes, because it carries the vault's argument.

## The batching plan

Agreed with Andrew on 2026-08-09. Argument-first rather than coverage-first: notes that make the vault's central claim checkable are worth more than even coverage across areas.

**Phase 1, the undeciphered scripts.** Each with ISO 15924 code, Unicode block, `corpus_size` and `found_at`. Corpus size is the variable the whole Decipherment argument turns on.

1. ~~Linear A, with Hagia Triada~~ **done**, 2026-08-09.
2. ~~The Indus script, with Mohenjo-daro and Harappa~~ **done**, 2026-08-10.
3. ~~Cypro-Minoan and the Phaistos Disc, with Enkomi and Phaistos~~ **done**, 2026-08-10.
4. Rongorongo (`Roro`, 620), Proto-Elamite (`Pelm`, 016) and the Voynich, with Rapa Nui and Susa.

Note for batch 4: **Linear Elamite is not Proto-Elamite.** They are distinct scripts and the vault must not merge them. Farmer, Sproat and Witzel use Linear Elamite as a comparison case for the Indus corpus, and it is worth a note of its own: 21 or 22 known inscriptions, most longer than the longest Indus text, which is the cleanest demonstration that corpus volume and text length are independent variables.

**Phase 2, the solved decipherments.** Egyptian hieroglyphs, cuneiform, Maya glyphs, Ugaritic. One batch each, each worth a note on *what actually broke it*, usually a bilingual, a proper name, or a structural regularity.

**Phase 3, people.** Driven by `--report`, not by a wishlist: the sweep lists names recurring across two or more notes, which is the inclusion test in `types/person.md` stated mechanically. As at this commit it surfaces Champollion, Rawlinson, Knorozov, Proskouriakoff, Turing, Saussure, al-Kindi and Michael Ventris.

**Phase 4, the thin areas.** General Linguistics and Computer Languages, one note each. `chomsky-hierarchy.md` is currently load-bearing for an entire junction on its own.

Running alongside: the two unwritten junction notes at the foot of `_junctions.md`, and the `wikidata` sweep. The identifier sweep is **not** the cheap job it looks: a Q-number is the most fabricable string in the vault, so it needs real lookups, and it is deliberately scheduled after phase 1 rather than done from recall.

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

## Resources found but not yet used

- **Salgarella, *Writing in Bronze Age Crete: Linear A*** (Cambridge Elements, "Writing the World" series). A recent single-volume overview of Linear A signs and inscribed objects in archaeological context, by the author of SigLA. The obvious next reference for Linear A; bibliographic details not yet verified.
- **Mnamon**, Scuola Normale Superiore, "Ancient writing systems in the Mediterranean: a critical guide to electronic resources" (`mnamon.sns.it`), with a DOI and ISBN. A curated scholarly guide covering Linear A, Cypro-Minoan and others. Likely useful for batch 3.

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
