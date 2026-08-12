---
type: Doc
aliases:
  - "Decisions"
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

## 2026-08-10: The push check is conversational, not mechanical

**Decided.** `git push` stays allowed in local settings so no dialog appears, and the rule is restated in all four places it is written: ask Andrew in conversation before pushing, every time, and say so where the reader can see that the permission layer will not enforce it.

**Rejected.** Removing the permission so the dialog returns as a hard gate.

**Why.** The two were inconsistent, which is the failure this file exists to prevent. Four documents said "ask before pushing" while the configuration allowed it silently, so the rule's protection rested entirely on an agent remembering to ask. That is precisely the pattern the earlier entry on the checker rejects: an assertion the tooling does not back should either be enforced or softened.

Softening was the better trade here. The conversational check has worked without exception, it happens earlier than a dialog would, and it carries context a yes/no prompt cannot. A dialog would add a click and displace a judgement onto a moment when the decision has already been made.

**Consequence.** Rule 15 now says out loud that nothing will stop you mechanically. That is deliberate: a rule which admits it is unenforced is more likely to be followed than one which implies a safety net that is not there.

## 2026-08-10: The checker verifies STATUS.md's own note count

**Decided.** `scripts/check-vault.py` reads the "The vault currently holds N notes" line in `STATUS.md` and fails if N does not match the number of files it checked.

**Why.** That number was wrong for eight batches. It read 107 while the vault held 132, because every edit meant to update it was a string replacement that matched nothing and returned silently. Nothing noticed, because nothing was looking.

The failure mode is worth naming precisely, since it will recur. An unasserted `str.replace` on a moving target is not an edit, it is a request that may be declined without telling you. The batches that carried these updates asserted on some replacements and not on this one.

`STATUS.md` is the first file an incoming agent reads after `AGENTS.md`. A wrong headline figure there is worse than no figure, because it is quoted onward.

**Rejected.** Removing the number, and generating the whole file. The count earns its place, and generating `STATUS.md` would destroy the judgement in the rest of it.

**Consequence.** Adding a note now fails the build until `STATUS.md` is updated, which is the intended coupling. This is the same principle as the entry on the checker enforcing rather than advising: a figure the vault asserts should be one the vault can check.

## 2026-08-11: Breadth before depth, and what a starter note is

**Decided.** Andrew's instruction: the vault "needs to start as a general reference and then be amplified". The batching plan is re-ordered accordingly. Every discipline gets a hierarchical taxonomy and a set of starter notes across it before any more interpretation is written anywhere.

**Why.** The audit on 2026-08-10 measured the problem rather than guessing at it. Nine batches in, Decipherment held a worked argument about why scripts stay unread, and General Linguistics, the area that argument leans on hardest, held two notes and neither was about linguistics. It had no phonology note. Eight of its ten subfields were empty. The same picture held elsewhere: Cryptography's index promised roughly eighty topics against three notes and had received no commits at all.

The failure mode is specific and worth naming, because it is the natural one for an agent working batch by batch. Depth-first work always has an obvious next step, so it never runs out of things to do, and it produces notes that are individually good and collectively unbalanced. Nothing in the process notices that a vault about linguistics has no note on syntax, because no single batch is responsible for that.

**Rejected.** A separate lower evidentiary tier for survey material, marked `status: draft`. It was the obvious way to buy breadth cheaply and it was the wrong trade twice over. `draft` already means something precise in `CONVENTIONS.md` (a fact could not be verified), so overloading it would blunt the one signal that flags unreliability. And a two-tier standard would put the burden on every future reader to work out which tier they were looking at.

**What a starter note is instead.** Narrower scope, same standard.

- Sourced like any other note, with `## Sources` and `cites`.
- The vault's own reasoning marked as the vault's own, as everywhere else.
- Gaps recorded in `## Open questions` rather than papered over, and a starter note is expected to have many.
- **It must connect.** A starter note that only restates a textbook does not earn a place; each carries a section relating its subject to work the vault has already done.

That last point turned out to be the argument for the whole approach rather than a stylistic requirement. Writing six notes on the levels of analysis surfaced three problems the Decipherment area had been walking past: the minimal-pair test presupposes meanings a decipherer does not have, grammaticality judgements presuppose an informant no dead language has, and signs per document measures writing rather than language. None of those came from the decipherment literature. They came from writing down the elementary material the vault had skipped.

**Consequence.** Breadth is cheaper per note but not cheap, since sourcing dominates. It also means General Linguistics and Cryptography, which have been neglected, now come before more Decipherment work.

## 2026-08-11: A knowledge base first, an argument second

**Decided.** Andrew's instruction, given after the first attempt at the breadth batch was rejected: "think of it more like a database than a thesis". Entries describe their subject. Analysis, interpretation and cross-area synthesis go in separate notes that link to the entries.

**This supersedes the entry above it in one respect**, and only one. The reasoning for breadth before depth stands. The claim that a starter note "must connect" to existing vault work, and the six notes written on that basis, do not.

**Why the first attempt failed.** It produced entries that were structurally sound and wrong in kind. Each defined its level in a few paragraphs and then spent as much space again arguing from that level back into the Decipherment area: what Kober was really doing, why a decipherer cannot use minimal pairs, why signs per document overstates the evidence. Individually those are defensible. Collectively they meant a reader looking up what a phoneme is got an argument about undeciphered scripts, and the reference layer the vault had set out to build did not exist at the end of it.

The generalization worth keeping: **a note that answers a question nobody asked it is not a reference note**, however well sourced. Argument attracts argument, and an area written argument-first stays argument-first because every new note is written to fit the existing case.

**What an entry looks like now.** Definition, description, examples, child topics named, `## Open questions` for what is not covered, `## Sources`. No section relating the subject to other areas beyond a link.

**Rejected.** Deleting the analysis. Several of those observations are worth notes of their own, written as such and linking to both sides rather than embedded in a definition. They are parked in `ROADMAP.md`.

**Consequence.** Coverage is now the measure of progress for the reference layer, not depth. The vault will look thinner and less interesting for a while, which is the intended trade.

## 2026-08-11: `belongs_to` chains, and subfields get MOC hubs

**Decided.** `belongs_to` carries the topic hierarchy, not just membership of an area. A note points at its immediate parent; the chain runs topic to subfield `MOC` to area hub. `related_to` links siblings. Each subfield gets a `MOC` note when it acquires content.

**Why.** The vault needed a hierarchical taxonomy per discipline, and Tolaria already supplies the machinery: `has` is the computed inverse of `belongs_to`, so a chained `belongs_to` renders as a tree in the Properties panel and the Neighborhood view with nothing written by hand. The previous rule, that every content note points at its area hub, made all 145 notes siblings in the graph and left any hierarchy to be maintained as prose in an `_index.md`, which is exactly the sort of hand-maintained list this vault has already been burned by.

**Rejected.** A separate `parent` field. It would have duplicated what `belongs_to` already means and would not have been picked up by Tolaria's computed inverse, so the graph would have stayed flat while the frontmatter claimed otherwise.

Also rejected: dropping `subfield` once a `MOC` exists for it. `subfield` is the controlled taxonomy and is checked against each area's stated vocabulary; `belongs_to` is the graph. They answer different questions and both stay on every note.

**Consequence.** `CONVENTIONS.md` is amended. Existing notes are not being migrated wholesale: they point at their area hub, which remains valid as a chain of length one, and they move under a subfield `MOC` when that subfield is next worked on.

## 2026-08-12: Obsidian replaces Tolaria as the vault application

**Decided.** The vault is an Obsidian vault from here. The files do not change in kind: plain Markdown with YAML frontmatter, the schema in `types/`, the taxonomy in `subfield`, the graph in wikilink fields, `scripts/check-vault.py` as the authority on all of it. What changes is the lens, and three mechanical consequences below.

**Why.** The first iteration of this project is a knowledge base for learning, and the tools that matter for that are navigation, discovery and iteration: the graph, database-style views over frontmatter (Bases), full-text and fuzzy search (Omnisearch), semantic similarity (Smart Connections), and freeform argument-mapping (Canvas). Obsidian has all five, mature. Tolaria's genuine advantage, typed relations with computed inverses, is not worth the gap on the other four; the hierarchy also lives in `subfield` and the `belongs_to` chain, so dropping the computed `has` loses a rendering, not information. Portability was the deciding argument: the vault was already app-agnostic by design, which makes the move nearly free, and a future migration into a database (Convex is the likely target) leans on exactly the parts that stay: schema'd frontmatter, kebab-case filenames as stable keys, and a checker that guarantees the frontmatter parses rather than merely resembling a schema.

**The three mechanical consequences.**

1. **Aliases.** Tolaria resolved wikilinks by H1 title or filename; Obsidian resolves by filename or alias only. Every note therefore carries its H1 title in `aliases`, the checker enforces it, and title-style wikilinks keep working. Filenames were not renamed to titles, deliberately: they are the stable keys.
2. **Bases replace the sidebar views.** `views/*.base` are the Obsidian equivalents of the Tolaria `views/*.yml`, which stay until the bases are confirmed rendering and then get deleted.
3. **No computed `has`.** The `belongs_to` chain still carries the hierarchy, but its inverse is now read from the backlinks pane or rendered by the Breadcrumbs plugin rather than computed by the app. The 2026-08-11 entry on `belongs_to` chains stands with that one amendment.

**Rejected.** Renaming files to their titles, which would have made Obsidian resolution work without aliases at the cost of churning every stable key. Also rejected: letting Obsidian's flexibility soften the schema. Obsidian enforces nothing, so the checker matters more after this move, not less; it should go into CI so the enforcement survives the app change.

**Consequence.** The `_icon`, `_color`, `_sidebar_label`, `_order` and `_pinned_properties` fields in `types/*.md` are Tolaria legacy. Obsidian ignores them. They stay for now as harmless metadata and get pruned or repurposed at the audit. The in-app git caveat in `AGENTS.md` now describes Obsidian (with the git community plugin, if installed) rather than Tolaria.

## 2026-08-12: The taxonomy is stubbed with MOC hubs before content

**Decided.** Every subfield vocabulary value in every area gets a `MOC` hub note immediately, as a stub: scope in a sentence or two, the topics owed to it, and a scanned list of the existing notes that carry its subfield value. 48 hubs were added on this decision.

**Why.** Andrew's instruction: see the whole starting structure in the graph first, judge whether it is sufficient, then backfill content in batches. A taxonomy that lives only in `_index.md` prose cannot be looked at as a shape; hubs make it nodes and edges. This is the breadth-before-depth decision of 2026-08-11 taken one step further: the reference layer now has a visible skeleton before any of its flesh.

**Two vocabularies share a value, so two hubs are shared.** Formal foundations appears in both the General Linguistics and Computer Languages vocabularies, Writing systems in both General Linguistics and Decipherment, and in both cases the two entries name the same subject and are described in the indexes as junctions with each other. One hub each, living in `General-Linguistics/`, with `belongs_to` both area hubs. Two same-titled notes would have resolved ambiguously and said less.

**Rejected.** Stubbing the child topics (roughly forty-five under Levels of analysis alone, hundreds across the vault). A stub hub is structural and carries no claims, so it needs no sources; a stub *entry* on phonology's child topics would be a content note with nothing verified in it, which the evidentiary standard exists to prevent. The taxonomy is the subfield vocabulary; the child topics are content, and content arrives sourced, in batches.

Also rejected: re-parenting the existing notes onto their new hubs in the same change. They still point at their area hubs, which remains a valid chain of length one. Moving them is mechanical but judgement-bearing (several notes carry two subfields), so it happens per-area as each area is next worked on, recorded in `ROADMAP.md`.

**Consequence.** The note count jumps by 48 with no new content, and the per-area figures in `STATUS.md` now measure structure and content mixed. The stubs make the vault look more finished than it is; each one says "Stub hub" in its body so the graph cannot be mistaken for coverage.

## 2026-08-12: A drafting policy, and a body skeleton per type

**Decided.** `CONVENTIONS.md` gains a `## Drafting` section, and every type file in `types/` gains a `## Body` skeleton beside its frontmatter template. Guidance, not enforcement: `scripts/check-vault.py` continues to validate frontmatter and the presence of `## Sources`, and continues not to read prose.

**Why.** The vault specified its schema completely and its prose not at all, and it showed. A survey found **208 distinct H2 headings across roughly ninety content notes**, of which four are structural (`## Sources`, `## Open questions`, and the two stub-hub headings). Every note was inventing its own shape. Worse, about thirty of those headings are named for a subject's relevance to the vault rather than for the subject: "Why this matters for the vault's central claim", "Why she matters here", "Why it belongs in a linguistics vault".

That is the 2026-08-11 decision's failure mode surviving in structural form. That decision changed the prose and never touched the headings, and a heading is not decoration: **a section named "Why this matters here" will be filled with an argument about why it matters here.** `Decipherment/linear-b.md` is the demonstration. The vault's flagship solved script gets 430 words under one content heading, "Why it was solvable", and describes almost nothing about the script itself.

Meanwhile the good shape already existed and had never been written down. The six batch 9 entries had converged on subject-named sections, then `## Child topics`, `## Open questions`, `## Sources`. The skeletons codify what those notes do.

**Rejected: enforcing the skeleton in the checker.** It would fail roughly forty existing notes on day one and hold the build red until legacy prose was rewritten, which inverts the priority: breadth is the program, and the legacy headings are audit work. It would also push the checker toward being a prose linter, which is a different tool with a much worse false-positive rate.

**Rejected: a minimum word count.** The obvious lever, and wrong. It is gameable by padding, which is the exact failure mode the evidentiary standard exists to prevent, and it is wrong for short subjects. The test is instead stated as a question: **does the note answer its own title for a reader who arrived cold?** `Cryptography/kasiski-examination.md` fails that test at 176 words because you cannot perform a Kasiski examination from it; a short identifier note passes at the same length.

**Rejected: rewriting the legacy now.** Recorded as item 8 of the deferred audit in `ROADMAP.md`, with the worst offenders named. Those notes are sourced and accurate; they are shaped wrongly, which is a real but lesser defect than the areas that have no notes at all.

**Consequence.** `Doc` notes are explicitly exempt: `README.md`, `ROADMAP.md`, `STATUS.md` and this file are working documents and are allowed to argue and to address the reader. Everything else opens with a definition, names sections for the subject, attributes claims in the sentence, and marks the vault's own reasoning as the vault's own.

## 2026-08-12: The checker runs in CI, and the app is not trusted to preserve the vault

**Decided.** `scripts/check-vault.py` runs as a GitHub Action on every push to `main` and on every pull request. The advisory sweeps (`--report`, `--questions`) run in the same job and never fail the build; they are printed so the run log carries the worklist.

**Why.** This was already recorded as owed when Obsidian replaced Tolaria, on the general ground that Obsidian enforces nothing. Opening the vault for the first time supplied a specific ground, which is stronger. Ordinary use of the app created two files nobody asked for: an empty `Untitled.canvas`, and an empty `Decipherment.md` at the vault root. The second is the instructive one. The vault contains 91 wikilinks to `[[Decipherment]]`, all resolving through the alias on `Decipherment/_index.md`, and a root-level file of that exact name gives every one of them a second candidate. Obsidian's documentation does not state how it breaks such a tie, and the failure would have been silent, graph-wide, and invisible in the app.

Two stray keystrokes also landed in note bodies (a tab in `linear-b.md`, a `d` in `rongorongo.md`) simply from clicking around. Neither the app nor the checker objected.

The generalization: **the editor is now a source of unreviewed writes to the vault.** Tolaria was not, because the vault was only ever edited deliberately. Enforcement that depends on a person remembering to run a script does not survive that change.

**Rejected.** Extending the checker to catch stray characters between frontmatter and the H1. The class of accidental edit is unbounded and `git diff` already shows it perfectly well; the answer is to read diffs before committing, not to grow the checker toward a linter.

**Also decided: plugin code is not committed.** `.obsidian/plugins/` is gitignored. It is 2.6 MB of bundled JavaScript that turns over with every plugin update, against 24 KB of actual settings, and `community-plugins.json` already records which plugins a new machine should install. The settings files (`app`, `appearance`, `graph`, `types`, and the plugin lists) are committed so vault behavior travels; `workspace.json` stays ignored as per-machine state.

**Consequence.** Enforcement no longer depends on anyone remembering. A push that breaks the schema fails visibly, including a push made from Obsidian's own git plugin, which is the path least likely to have run the checker first.

## 2026-08-12: Obsidian's normalization is the house form for `.base` files

**Decided.** Where Obsidian rewrites a `.base` file, its output is canonical and the vault does not rewrite it back.

**Why.** The eleven bases were written to the documented Bases schema without the app to test against. Opening them settled two things that documentation could not. The view-level `sort:` key, which the syntax reference does not document at all, is real: changing a sort in the UI rewrote `direction: ASC` to `DESC` in place and left the structure alone, which confirms the whole set was correct as written. And Obsidian unquotes filter and formula strings, turning `'type == "Person"'` into `type == "Person"`. Both forms are valid YAML, the app plainly prefers one, and fighting it would mean a spurious diff every time a base is opened.

**Consequence.** New bases are written unquoted. A base showing as modified in `git status` after merely being opened is expected and not a defect. Every base also now leads with a `Title` formula column (`file.asLink(aliases[0])`) instead of `file.name`, because filenames are deliberately kebab-case stable keys and are unreadable in a table; `references.base` names that column `Citation`, because `Reference` notes already carry a `title` property and two columns headed "Title" would be worse than the problem being solved.
