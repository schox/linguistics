---
type: Doc
status: living
---

# Decisions

Why the vault is shaped the way it is, and what was considered and rejected. Append-only, newest last. Do not rewrite history here; add a superseding entry instead.

**This is not an activity log.** Git records what changed and when, and does it better. This file records *why*, and in particular records the alternatives that were rejected, because that is the thing a future reader cannot reconstruct from a diff. If you are about to reverse one of these decisions, read the entry first: several look like obvious improvements until you see what they were chosen against.

---

## 2026-08-09: Five areas, with Decipherment as a peer

**Decided.** General Linguistics, Human Languages, Computer Languages, Cryptography, and Decipherment as a fifth top-level area.

**Rejected.** Decipherment as a subfolder of Cryptography, and Decipherment as cross-cutting notes with no folder.

**Why.** Cryptography is the backdrop to decipherment, so nesting the subject inside its own background is upside down. Decipherment is the integrative area: it takes method from Cryptography, constraint from General Linguistics, candidate relatives from Human Languages, and technique from Computer Languages.

## 2026-08-09: Taxonomy lives in frontmatter, not folders

**Decided.** Folders stay one level deep per area. The taxonomy is the `subfield` field, with the permitted values listed explicitly in each area's `_index.md`.

**Rejected.** Nested folders mirroring the taxonomy.

**Why.** Folders are single-inheritance and the most valuable material here belongs in several places at once. Frequency analysis is cryptanalysis, statistics, and decipherment method simultaneously. Expressed as folders it gets one home and two lies. Frontmatter also means a branch can be re-cut without moving a file, which matters because the first cut will be wrong somewhere.

**Do not** deepen the folder tree. If a note seems to need a new folder, it needs a `subfield` value.

## 2026-08-09: Genealogy as the spine of Human Languages

**Decided.** Languages are organized genealogically, `family` then `branch`.

**Why.** Glottolog already maintains the tree, versioned and CC BY 4.0, so the vault leans on it rather than curating a worse copy. It is also the organization that makes decipherment material navigable, since knowing a language's relatives is exactly what lets you read it or fail to.

## 2026-08-09: Adopt external identifiers, do not mirror external data

**Decided.** Entity notes carry `glottocode`, `iso639_3`, `iso15924`, `hopl_id`, `wikidata`, `pleiades`, `ror` and similar. The vault links out and does not copy.

**Rejected.** Mirroring Glottolog or WALS subsets into the repository.

**Why.** This is the CLLD lesson: shared stable identifiers are what make datasets joinable, and a local copy silently goes stale. Exception if a snapshot is ever genuinely needed: record the version DOI, store it as CLDF, mark it dated. WALS is safer to mirror than Glottolog because it is complete and frozen.

## 2026-08-09: Script and Language are separate types

**Decided.** `Script` and `Language` are distinct note types joined by `writes` / `written_in`.

**Why.** They are many-to-many. Cuneiform wrote five unrelated languages; Japanese uses four scripts; Linear A is a script whose language is unknown; Etruscan is a language readable in a script we can pronounce but do not fully understand. Collapse them and "has Linear A been deciphered?" becomes unanswerable, because it is two questions.

**Consequence.** `Script` notes live in `Decipherment/` regardless of decipherment status. This is a filing convenience, not a claim that every script is undeciphered.

## 2026-08-09: References are notes, not trailing links

**Decided.** One `Reference` note per source in `references/`, keyed `author-year`, cited from content notes via `cites`.

**Why.** The vault serves academic research. A work used in six places should be one node with six backlinks, so the graph can answer "what have I read on this" and "what depends on this source". Also lets reading status be tracked.

## 2026-08-09: Person and Place types, with inclusion tests

**Decided.** Both exist, both have written inclusion tests, both live in cross-cutting folders.

**Why.** People and places are the strongest cross-area joins, because method transfer usually happens through a person or an institution rather than through literature. The inclusion tests exist because "seminal figures only" erodes without one: authorship of a cited paper does not earn a note.

**Also decided.** Living people get sourced professional contribution only, never written from memory. False reports of Noam Chomsky's death circulated widely in 2024, and a plausible-looking note written from recall could enshrine an error.

## 2026-08-09: International English, with titles exempt

**Decided.** US spelling in this vault, a deliberate exception to Andrew's usual Australian English. Locale can be changed if a derived work is produced.

**Critical exception.** Quoted titles, proper nouns and quotations keep their own spelling, always. Tamburini's paper really is titled "combinatorial optimisation"; Barber's book really is *Archaeological Decipherment*. Normalizing a title breaks the citation. `scripts/check-vault.py` holds the allowlist in `PROTECTED`.

## 2026-08-09: The type definitions are the authoritative schema

**Decided.** `types/*.md` is the single source of truth for field names and allowed values. `CONVENTIONS.md` describes rules and rationale but does not restate schemas.

**Why.** An independent cold-read audit found the two had already drifted: `types/language.md` declared a `script:` field while three other documents said `written_in`, with no way to be right. Maintaining a schema in two prose locations guarantees drift. `scripts/check-vault.py` now enforces the schema so drift is caught rather than discovered.

## 2026-08-09: The checker enforces, it does not merely advise

**Decided.** `scripts/check-vault.py` validates required fields per type, enum values, subfield membership, wikilink quoting, `## Sources` presence, link resolution and house style.

**Why.** The earlier version checked far less than the documentation claimed it did, which is worse than not having it: an agent trusting a green run would ship broken notes. Anything the docs assert should either be enforced or the assertion should be softened.

**Known limit.** It does not resolve wikilink targets, so a `belongs_to` pointing at a note that does not exist passes. Worth adding. **Superseded**, see below.

## 2026-08-09: The checker resolves wikilink targets

**Decided.** `scripts/check-vault.py` now resolves every wikilink against the set of H1 titles and bare filenames in the vault, and fails on a dangling target. Examples inside fenced code blocks are exempt; examples in inline code spans are not, so an illustrative link in prose must point at a note that exists.

This supersedes the known limit recorded in the entry above.

**Why.** An unresolvable `belongs_to` is exactly the failure the quoting rule exists to prevent, one step later: the YAML parses, the field looks right, and the relationship still does not exist. Catching the quoting error but not the dangling target left half the hole open.

**Consequence.** A note cannot be committed pointing at an entity that has not been written yet. Where a new `Script` note needs a `found_at` site, the `Place` note is part of the same change rather than a follow-up.

## 2026-08-09: Absent facts are recorded, not omitted

**Decided.** The vault's evidentiary standard is stated in `AGENTS.md` and covers three cases rather than one. A claim that cannot be verified is not written. A claim that is disputed is written with both sides attributed. A fact that would have been useful but cannot be found is **written down as absent**, under `## Open questions`, with what was looked for.

**Rejected.** Silently omitting what could not be found, which was the previous default.

**Why.** Andrew's framing: this is for research and academic use, personal now and shared later, so there is no room for inference dressed as fact. The first two cases were already covered. The third was not, and it is the one that degrades quietly, because an omission is indistinguishable from completeness on the page. Recording the gap converts a dead end into a result and stops the next reader repeating the search. It also removes the incentive that produces fabrication in the first place, which is the felt need to fill a hole.

**Consequence.** Notes on thinly published corpora will carry visible gaps. That is the intended outcome, not a defect. `## Open questions` is optional and unenforced by the checker, because the checker cannot tell a genuine absence from an unasked question.

**Known limit.** `scripts/check-vault.py` verifies that a `## Sources` section exists and that its relative links resolve. It cannot tell a real citation from a plausible fabrication, and it does not check that a DOI or external identifier resolves. The standard above is therefore a discipline, not something the tooling enforces. Andrew has a separate service that does fact and link checking periodically, so the checker deliberately stays offline and structural rather than growing a network mode.

## 2026-08-09: Wikipedia is a source, not a Reference

**Decided.** A Wikipedia article may be listed under a note's `## Sources` and linked in prose. It never gets its own note in `references/`. `scripts/check-vault.py` fails a `Reference` whose `url` or `doi` points at Wikipedia.

**Rejected.** Two stricter readings, both considered and both wrong. Banning Wikipedia from `## Sources` as well, which would have stripped citations from eleven existing notes and left several with nothing, replacing a useful pointer with a hole. And the status quo of saying nothing, which leaves the line undrawn until someone files `references/wikipedia-linear-a.md` and it looks like precedent.

**Why.** The two roles are different. `## Sources` records what a note actually drew on, and for orientation on a script or a site Wikipedia frequently is that, honestly. `references/` is the authoritative bibliography, the thing the vault's academic use rests on, and it holds works of record: papers, books, chapters, datasets, corpora. Wikipedia is a finding aid pointing into that literature, so the correct move on encountering it is to follow its citations to the work of record and reference that.

**Consequence.** Where a fact is available only from Wikipedia, cite Wikipedia in `## Sources` and say in the note that the primary source has not been located. That is the absent-fact case from the entry above, not a license to skip the search.

## 2026-08-09: Sweeps are advisory, and separate from enforcement

**Decided.** `scripts/check-vault.py --report` lists unlinked mentions of existing notes, and capitalized names recurring across two or more notes with no note of their own. It exits 0 whatever it finds and prints nothing during a normal run.

**Rejected.** Folding these into the enforcing checks, and running them as a periodic manual reread of the vault.

**Why.** The enforcing checks resolve every link that exists. They are blind in exactly one direction: nothing detects a link that is *missing*, because a missing link is indistinguishable from a deliberate silence. That is the direction in which a graph decays quietly, and it gets worse as the vault grows, since each new entity note creates unlinked mentions in every note written before it.

Enforcement and advice are kept apart because they behave differently under doubt. An enforcing check must have no false positives or it gets ignored, and being ignored is how the earlier permissive checker did damage. An advisory sweep should over-report, because a false positive costs a glance and a miss costs a broken join. Mixing them would force one standard on both.

**Consequence.** The second list is a worklist, not a to-do list. It is a heuristic over capitalization and it says so in its own output. Entries are judged against the inclusion tests in `types/person.md` and `types/place.md`, which is the point: it lets the vault say who it already needs rather than working from a wishlist.

**House style it assumes.** Link on first mention per note. A note that already links a target is treated as satisfied however often the name recurs, because linking every mention is noise and is harder to undo than to not do.

## 2026-08-09: Derived numbers are claims, and required fields are not evidence

**Decided.** Two additions to the evidentiary standard, both from reviewing what nearly went wrong in the first content batch.

A number computed rather than quoted (ratio, percentage, average, unit conversion, absolute date from a relative phase) must state its inputs and their source in the note. A required schema field with no verifiable value takes the nearest verifiable proxy and says so; never a plausible guess.

**Why.** Both failure modes were caught in batch 1 and neither was a citation problem, which is the point. Every quotation and identifier verified clean, because that is where the discipline was aimed.

The first draft of `Decipherment/linear-a.md` stated that Linear A has 13 percent of Linear B's documents and 13 percent of its signs. The document ratio is about 31 percent. The two numbers came from a correctly cited source and the arithmetic in between was mine, so the error sat inside a properly referenced sentence. Worse, the corrected version is a better note: the gap between 31 and 13 percent is average document length, which is the substantive point about why Linear A resists distributional attack.

The second: `places/hagia-triada.md` was drafted with `flourished: c. 1600-1450 BCE`, converted by me from the ceramic phases the sources actually give. Aegean High and Low chronologies put LM IB about a century apart, so that conversion silently took a side in a live dispute. It now records the phase.

And `references/rutter-aegean-prehistory.md` was first written with `year: 2000`, invented purely to fill a required field on an undated web resource. It now carries the site's copyright year with a statement that this dates the access rather than the work.

**Rejected.** Relaxing the required fields so the second case cannot arise. The fields earn their place; the fix is a stated convention for the empty case, not a weaker schema.

## 2026-08-09: Linear B is `mixed`, not `syllabary`

**Decided.** `Decipherment/linear-b.md` carries `class: mixed`, matching `Decipherment/linear-a.md`, on the authority of Salgarella and Castellan, who classify both together as logo-syllabic.

**Why.** The note already contained the evidence against its own classification: its first sentence gives about 87 syllabic signs and over 100 ideographic signs, and a script with more semantic signs than phonetic ones is not a syllabary. The two notes also disagreed with each other while describing one script family.

**Known limit.** The `class` enum has no `logo-syllabic` value, which is the standard term in the Aegean literature. `mixed` is the closest available and the distinction is carried in prose instead. Adding a vocabulary value for one script family was judged a poor trade, but it is open.

## 2026-08-10: Tavily as a retrieval fallback, and how retrieved content is marked

**Decided.** Where a page refuses a direct fetch, the Tavily extraction service is used to retrieve it. It is a fallback, not the default research path, and a note whose load-bearing fact came through it says so.

**Rejected.** Two alternatives. Leaving the gaps, which is what batch 2 did and which produced the two weakest notes in the vault. And defeating the block directly by spoofing a browser client, which was tested only far enough to establish that plain `curl` is refused too, and then dropped: these sites are choosing to refuse automated clients, and working around that is not a research method the vault should adopt.

**Why.** Six of the eight source failures across the first two batches were HTTP 403 bot-blocks, and they clustered on exactly the institutional and reference sites that archaeological provenance depends on: UNESCO, Britannica, harappa.com. On the first attempt Tavily retrieved all three, and immediately closed an open question that `places/mohenjo-daro.md` had recorded as unanswerable: UNESCO gives the property as 240 hectares with about one third excavated since 1922, which is the quantity the argument from absence in the Indus dispute actually rests on.

**The constraint that comes with it.** An extraction service returns a rendering of a page, not the page. That is one step further from the primary document than the vault's own verification rule wants, and the risk is that it quietly becomes the default because it is easier. So it is scoped to pages that refuse direct access, and `references/unesco-moenjodaro.md` and `references/unesco-harappa-tentative.md` both carry an explicit statement that their content was retrieved this way and the page itself was not seen.

**Also decided, arising from the same batch.** Britannica and other tertiary encyclopedias are treated as Wikipedia is: citable under `## Sources`, never a `Reference` note. Institutional documentation such as a UNESCO World Heritage entry is treated differently and can earn a note, because for a site's extent, protection status and excavated fraction it is the primary record rather than a summary of one.

## 2026-08-10: Open questions accumulate; the audit is deferred and deliberate

**Decided.** Gaps are recorded on the note where they arise and left there. A full audit of the whole corpus happens when the vault is much closer to complete. `ROADMAP.md` is created to hold what is blocked, on whom, and in what order work should proceed, and `STATUS.md` is trimmed to the present tense so the two do not drift.

**Rejected.** Resolving each open question as it arises, and keeping a hand-written to-do list of them.

**Why.** Phase 1 produced 59 open questions across 17 notes in two days. Chasing them as they appeared would have meant each batch spending more effort on the tail of the previous one than on new material, and much of it wasted: a note written today may be superseded by a source read next month, and several questions that looked permanent were closed incidentally by later batches. Recording a gap honestly is cheap, which is the whole point of the `## Open questions` convention; closing them one at a time is not.

The hand-written list was rejected for the reason the vault rejects any duplicated inventory. A copied list of 59 items is stale the first time a note is edited, and the vault already had one drift of exactly this kind between `CONVENTIONS.md` and `types/`. `scripts/check-vault.py --questions` harvests them instead, so `ROADMAP.md` can hold judgement and ordering without holding data.

**Consequence.** An agent finding a gap mid-batch should record it and move on, not chase it. That is now stated in `AGENTS.md`, because the natural instinct is the opposite and the instinct is wrong here.
