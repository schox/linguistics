---
type: Doc
aliases:
  - "Roadmap"
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
3. Every figure the vault computed rather than quoted, re-derived. The convention requires the working to be shown, so this is checkable. **Extend this to figures the vault states about itself**: the STATUS note count drifted silently for eight batches before a check was added for it, and other stated counts (per-area figures, the reference total) are still unchecked.
4. Facts taken at second hand where the primary source exists, notably everything reaching the vault through Farmer, Sproat and Witzel, Petrolito and colleagues, or a review rather than the book reviewed.
5. Content retrieved through the Tavily extraction service rather than seen directly. Those notes say so; the audit should confirm the pages still say what was extracted.
6. Empty identifier fields, distinguishing "not looked up" from "searched and probably absent". The vault has been careful about this distinction and it should be verified.
7. Andrew's standing questions, at the foot of `STATUS.md`.
8. **The argument-framed section headings in the older notes.** A survey on 2026-08-12 found 208 distinct H2 headings across roughly ninety content notes, of which only four are structural. About thirty are named for a subject's relevance to the vault rather than for the subject: "Why this matters for the vault's central claim", "Why it belongs in a linguistics vault", "Why she matters here", "Why this reframes the whole area". They are the 2026-08-11 thesis-voice failure surviving in structural form, in the Decipherment, people and places notes written before that decision. The drafting policy now forbids them going forward; carrying it back is audit work, not a reason to stop the breadth program.

   Worst first when it comes: `Decipherment/linear-b.md`, which is 430 words with a single content section, and that section is an argument. `Cryptography/kasiski-examination.md` (176 words) and `Cryptography/index-of-coincidence.md` (213) have no content sections at all, and `ROADMAP.md` already schedules their repair with the Cryptography batch.

9. **Self-reference in the content notes.** 261 instances of "this vault" and "the vault's" across 88 files, counted 2026-08-12. The drafting policy of that date rules them out: notes do not refer to the collection they sit in, and absences are written impersonally instead. Concentrated in `Decipherment/why-scripts-stay-unread.md` (15), `General-Linguistics/redundancy.md` (12), `Decipherment/ugaritic-script.md` (12), `Decipherment/is-it-writing-at-all.md` (10).

   **Not a find-and-replace.** Each instance needs rewording in context, and about a dozen are load-bearing rather than stylistic. `General-Linguistics/redundancy.md` carries "This is the vault's own reasoning and is not drawn from a source", which was the marker for unsourced analysis and now has to become the labeling convention set out in `CONVENTIONS.md` under `### Analysis, opinion and theory`.

   **Do this in the same pass as item 8**, note by note. Both are the same job, retrofitting policy written on 2026-08-12 onto prose written before it, and they touch overwhelmingly the same files. Two passes over 88 notes to fix two things in each is the expensive way round.

   The cost of deferring, recorded so it is a decision rather than an oversight: until the sweep runs, 88 notes carry a voice the policy forbids, and anything learning the house style by reading the corpus will learn the wrong one. That is the trade against spending the effort now, while the areas that are actually short of material stay short.

## Blocked on Andrew

Nothing here can be moved by more searching.

- **The Ethnologue 200 list**, which is sold rather than published. Without it the popularity half of the Human Languages selection rests on the four languages its free pages name in prose, and the other 47 are coverage judgements. A purchase or an institutional route would convert the largest unsourced judgement in the area into a sourced one. Added 2026-08-13.
- **Cambridge Core access.** Three volumes in *Elements in Writing in the Ancient World* cover three of the vault's seven undeciphered scripts, and all are paywalled: [Salgarella 2025](references/salgarella-2025.md) on Linear A, [Kelley 2026](references/kelley-2026.md) on Proto-Elamite, [Donnelly 2025](references/donnelly-2025.md) on Cypro-Minoan. An institutional login or the three eBooks would close roughly a dozen open questions. Salgarella's sections 3 and 5 alone would settle the per-site distribution of the Linear A corpus, the longest-standing gap in the vault.
- **Grammatology's home**: wholly into Decipherment, or split with General Linguistics. Deferred twice now. `Script` notes currently live in `Decipherment/` as a filing convenience, which `DECISIONS.md` records as a convenience and not a claim.
- **Whether Chomsky and Knuth get `Person` notes.** Chomsky was deliberately left unwritten because his status could not be verified and false death reports circulated in 2024. See the living-people rule in `types/person.md`.
- ~~**The `class` enum, now that the typology is written.**~~ **Settled 2026-08-12**, see `DECISIONS.md`. `logographic` became `logosyllabary` while the value had no users; `mixed` and `undetermined` stay and are documented in `types/script.md` as local terms with their standard equivalents named; `featural` stays out until a note needs it. The per-note reconciliation below is what remains.

## Blocked on external sources

- **Montecchi 2019**, the study of record for the Hagia Triada archive. The Bologna repository returns 403 and failed again through Tavily; the CNR eprints server has a TLS error. This is what would settle the contested tablet count, 147 against Rutter's 168.
- **Younger's Linear A transcriptions.** The University of Kansas site is gone. A 53-page deposit under his name exists on Academia.edu, last updated 8 April 2024. The vault's Linear A corpus figures descend from the dead site, so confirming they are traceable into the surviving document is the single most valuable outstanding check.
- **Mahadevan 1977**, an 829-page print memoir, for the per-site distribution of the Indus corpus.
- **The Cuneiform Digital Library Initiative catalog**, for a per-site breakdown of the proto-Elamite tablets. Its publications have now been used; the searchable catalog has not.

## The Obsidian migration

**Complete as at 2026-08-12.** The vault moved from Tolaria to Obsidian; `DECISIONS.md` has the reasoning and what the app turned out to do in practice. All seven steps are done: the vault was opened on Andrew's Mac, the Bases render, Omnisearch and Breadcrumbs are installed, the taxonomy was judged in the graph and found sound (Andrew: "heading in the right direction, it just needs amplification"), `.obsidian/` is committed, the Tolaria `views/*.yml` are deleted, and the checker runs in CI.

What the app verified, as against what was written to documentation:

- **The view-level `sort:` key is real**, which the Bases syntax reference does not document. Obsidian rewrote `direction: ASC` to `DESC` in place, preserving the structure, so all eleven bases were correct as written.
- **Obsidian normalizes what it opens.** It unquotes filter and formula strings (`'type == "Person"'` becomes `type == "Person"`). Its form is now the house form; expect a base to show as modified in git after you merely open it.
- **Every base leads with a `Title` column**, a formula (`file.asLink(aliases[0])`) rather than `file.name`, because filenames are kebab-case stable keys and unreadable in a table. `references.base` labels it `Citation`, since `Reference` notes already carry a `title` property.

**Still outstanding, small:**

- **Breadcrumbs is installed but not configured.** It looks for a property named `up`; this vault uses `belongs_to`, so `belongs_to` must be added under the plugin's Edge Fields settings and assigned the up direction. Until then the plugin does nothing. No current documentation for the settings UI was found; the published wiki 404s.
- **Smart Connections**, the deferred third plugin (semantic similarity; purely additive, and check its indexing settings before letting it embed on every edit).

**Deliberately deferred:**

- ~~**Re-parenting existing notes onto their subfield hubs.**~~ **Done 2026-08-12**, as its own batch rather than per area, after the structural review found that 48 of 51 subfield hubs had no children at all. See `DECISIONS.md`.
- Pruning or repurposing the Tolaria legacy fields in `types/*.md` (`_icon`, `_color`, `_sidebar_label`, `_order`, `_pinned_properties`). At the audit.

## Next work, in order

**The plan below is superseded from 2026-08-11.** Andrew's instruction is that the vault starts as a general reference and is amplified afterward, so breadth across every discipline comes before any more interpretation. `DECISIONS.md` records the reasoning and what a starter note is. Phases 3 and 4 as scoped below are not cancelled, only re-ordered behind the breadth work; the items in them are still owed and are still accurate.

### The breadth program

One subfield per batch, taxonomy already in place from each area's `_index.md`. Order is by how much the rest of the vault is already leaning on the missing material.

**These are reference entries, not arguments.** See `DECISIONS.md`: describe the subject, give examples, name the child topics, record the gaps. Analysis goes in separate notes.

1. ~~**General Linguistics, Levels of analysis, parent entries.**~~ **Done 2026-08-11**, batch 9: a `MOC` plus phonetics, phonology, morphology, syntax, semantics, pragmatics, from [Anderson et al. 2022](references/anderson-et-al-2022.md). Discourse is named in the index and was not written, because the source does not treat it as a level.
2. **Levels of analysis, child topics.** Roughly forty-five notes, named at the foot of each of the six entries. One parent per batch. Phonology and morphology first, since the Decipherment area leans on both. A source beyond an introductory textbook is needed for several, particularly acoustic and auditory phonetics.
3. **General Linguistics, Writing systems.** ~~The most urgent thing in the vault.~~ **Anchored 2026-08-12** by `General-Linguistics/script-typology.md`, which defines the vocabulary the `class` field draws on, from [Baroni 2011](references/baroni-2011.md), [the Unicode Standard](references/unicode-standard-17.md) chapter 6 with its Table 6-1, and the numeric ranges of [ISO 15924](references/iso15924.md). The three do not fully agree, and the note says where.

   **Orthographic depth followed on the same day**, from [Frost 2005](references/frost-2005.md), which is the hypothesis stated by one of its own authors and is free, and [Seymour et al. 2003](references/seymour-et-al-2003.md) for the acquisition evidence.

   **Still owed to the hub**, each its own batch: the history of the alphabet, transliteration and romanization standards, script reform, literacy, and a note on the grapheme. The two entries name further child topics at their feet.

   **Two pieces of follow-up work it generated**, both mechanical rather than research:

   - **Reconcile the 13 `Script` notes against Table 6-1.** Several disagree with the Unicode classification, sometimes defensibly. Ugaritic is `abjad` here and an alphabet in Table 6-1; Linear A is `mixed` here and a logosyllabary there, though it is undeciphered; cuneiform and Egyptian hieroglyphs are `mixed` here and logosyllabaries there. Linear B is `mixed` on a considered decision recorded in `DECISIONS.md` 2026-08-09. Each note should state which classification it follows and why, rather than carrying a bare value.

     `types/script.md` now says `logosyllabary` is preferred to `mixed` wherever it applies, so the likely outcome is that cuneiform, Egyptian hieroglyphs, Linear A and Maya move off `mixed` and Linear B stays on it. Do this per note as each area is worked, not as a sweep: each move is a claim about a script and needs a source in the note, which is precisely what a bulk edit would skip.
4. **Cryptography, the whole area, treated as an area in its own right.** Andrew's decision of 2026-08-12: the same coverage ambition as General Linguistics, including the modern applied material, rather than only the parts Decipherment leans on. Thinness here is a real gap in the project's declared scope, not a consequence of it.

   **The vocabulary was rebuilt on 2026-08-12** against three published classifications, so the cut of the field is citable rather than invented: [Menezes et al. 1996](references/menezes-et-al-1996.md) as the primary instrument, [Boneh and Shoup 2023](references/boneh-shoup-2023.md) for what a 1996 handbook cannot cover, and NIST's activity areas for what is standardized. Ten values became fourteen. See `DECISIONS.md` for what the instruments turned up and the two deliberate deviations from them.

   Three of the fourteen have any content: Cryptanalysis 3, Classical ciphers 1, Theory 1. **Eleven hold no content note at all.**

   **The stub inventory follows, one batch per subfield**, on the model of the Levels of analysis child topics. Each stub cites the source section that names the topic, which is what makes it a placeholder for a real subject rather than a guess. Andrew's rule: an obvious placeholder should carry at least one reference, because otherwise there is no evidence the topic is a topic.

   **Cryptanalysis is done**, 2026-08-12: 13 stubs, plus four new references to cover what the two handbooks do not (Shor, Grover, Kocher on timing attacks, and the Bletchley Park report on Tunny). Three topics named in the area index were deliberately left unstubbed for want of a source, and are listed on the hub: the bombe and the Enigma break, known-plaintext and crib-dragging as techniques, and meet-in-the-middle attacks.

   **The remaining thirteen subfields, in suggested order:** Classical ciphers and Symmetric cryptography first, since they are what Cryptanalysis attacks and the existing thin notes sit between them; then Public-key cryptography, Digital signatures and authentication, Hashes and integrity; then Randomness and key generation, Key management and establishment, Protocols and deployment; then Theory, which is the Decipherment junction and deserves care; then Post-quantum cryptography, Mechanical and electromechanical, History and politics. **Quantum cryptography last**, because it is the one subfield whose topic list is not drawn from any held source and needs one first.

   The three existing notes are also the oldest and thinnest anywhere: `index-of-coincidence` is 213 words and `kasiski-examination` is 176, and both are load-bearing for the Decipherment area, which divides by them. Repair them in the same batch rather than adding around them.

   Sourcing is more favorable here than anywhere else in the project, since the classical literature is out of copyright: [Kasiski 1863](references/kasiski-1863.md) is already held and unread, and Shannon 1949 and 1951 are both held.
5. **General Linguistics, Historical and comparative.** The comparative method, regular sound change, reconstruction. Decipherment uses candidate relatives constantly (Ventris against Greek, Bauer against Semitic) and the vault has never written down what a relative is or how one is established.
6. **General Linguistics, Typology and universals.** [WALS 2013](references/wals-2013.md) is already held as a Reference and has never been used. This is where word order, alignment and the morphological typology belong; three starter notes from batch 9 defer to it.
7. **Computer Languages.** Stubbed out on 2026-08-12: 49 topic stubs across all eight subfields. `DECISIONS.md` previously recommended leaving this area thin, a recommendation made under argument-first batching that did not survive the change to breadth-first.

   **The language layer is settled**, 2026-08-12, on Andrew's criterion: the most popular languages plus one or two from each paradigm. 32 selected, 22 by rank from [TIOBE index, August 2026](references/tiobe-2026-08.md) and 10 added for coverage, since popularity alone leaves no functional, logic or concatenative language and misses four of the six lineages. [GEN 2024](references/gen-2024.md) supplies the forty-year view that a current snapshot cannot, and is held for the set of languages it names and never for its self-described best-guess figures.

   **Two paradigms still have no member**: dataflow has none and declarative has only SQL. Neither instrument names a candidate for dataflow and the gap is recorded on the hub rather than filled by guessing.

   **The same question was settled for Human Languages** on 2026-08-13, on the same criterion in its genealogical form. See item 8.
8. **Human Languages.** The genealogical spine was stubbed on 2026-08-12: 88 notes covering the families and branches named in the area index, plus the topics of the four non-genealogical groupings.

   ~~**The language layer is blocked on a selection principle.**~~ **Settled 2026-08-13**, see `DECISIONS.md`. Andrew's criterion, the most spoken languages plus one or two from each family, is the same one applied to Computer Languages the day before. 51 languages across 24 families, plus nine isolates retyped from `Concept` to `Language`. The taxonomy program now has no open selection questions.

   **Only four of the 51 rest on sourced speaker numbers.** [Ethnologue 2026](references/ethnologue-2026.md) sells its ranked list, and its free pages name the top four in prose: Mandarin Chinese, Spanish, English and Hindi. The other 47 are coverage judgements made from the area index, and every stub says which of the two it is. Buying the list, or reaching it through an institution, would let the popularity half be done properly, and is the cheapest unblocking purchase in the vault.

   **WALS was passed over here** and is not gone: it optimizes for typological diversity rather than prominence, so it answers a different question, and its sample list was not retrievable in usable form on 2026-08-12. It is still owed as the instrument for item 6 above, which is what it was built for. The CLDF release is the likely retrieval route; see `_data-sources.md`.

   ~~Four `Language` notes are owed because the corpus already refers to them: Rapanui, Coptic, Old Persian and Hittite.~~ **Stubbed 2026-08-13** with the rest. They still need writing, and the standalone items below say why each matters.

   **What the area needs next is writing, not more structure.** 139 of its 161 files are stubs, and the seven written notes are all Decipherment by-products.

Remaining General Linguistics subfields (Sociolinguistics, Psycholinguistics and acquisition, Computational linguistics, Semiotics and philosophy of language, Etymology and lexicography) follow. Computational linguistics should absorb the statistical-language-model note described at the foot of this section.

### Analysis notes, unblocked 2026-08-12

Written while drafting batch 9, then removed from it because an entry describes rather than argues. Each is a note in its own right, typed `Note`, linking to both sides rather than living inside a definition.

**These were parked pending a prior published proponent for each. That bar was dropped on 2026-08-12**: original analysis is permitted, subject to the four conditions in `CONVENTIONS.md` under `## Drafting` (typed `Note`, labeled as analysis in its opening, every premise sourced, and what would settle it stated). A literature search is still expected first, and finding a proponent is recorded where one exists. Finding none is a fact about the search, not a reason to withhold the argument.

They remain scheduled behind the breadth program, since the reference layer is what they link into. The ordering is unchanged; only the permission is.

- **What Kober did was morphology and phonology without meanings.** Her triplets are inflectional paradigm detection; her grid is a system of contrasts with no values attached. Links [Alice Kober](people/alice-kober.md), [Morphology](General-Linguistics/morphology.md), [Phonology](General-Linguistics/phonology.md), [Linear B](Decipherment/linear-b.md).
- **The field's standard methods presuppose an informant.** The minimal pair needs to know that two forms mean different things; the grammaticality judgment can only be obtained from an individual speaker. No language in the Decipherment area has one, so all negative evidence is unavailable and corpus-only linguistics works under a strictly weaker evidence base. The exception is Classic Maya, where speakers of related languages existed, and it is also the case that broke.
- **Signs per document measures writing, not language.** One language's word is another's sentence, so a five-sign document could be five items or one inflected clause. Compounds the tension already open in [redundancy](General-Linguistics/redundancy.md); both suggest the vault's cross-script comparisons are optimistic.
- **Conditional entropy over sign sequences is a weak proxy for grammar.** Constrained ordering is consistent with syntax and is not the same claim, since heraldic sequences, accounting formats and calendars are all strongly ordered. Bears on [is it writing at all?](Decipherment/is-it-writing-at-all.md). Whether anyone has attempted a hierarchy-sensitive test on the Indus corpus is unknown.
- **Administrative corpora are pragmatically flat.** Almost everything the vault reads is inventory and accounts, which is a survival bias rather than a fact about those societies. A decipherment of such a corpus recovers a register rather than a language.

None of these is sourced beyond the reasoning that produced it, which is why none was left in an entry and why each carries the labeling requirement when written. The premises they rest on are sourced in the notes they link to, and any that are not must be sourced before the argument can stand on them.

### The superseded plan, still owed

**Phase 2, the solved decipherments, is complete**, 2026-08-10: Egyptian hieroglyphs, cuneiform, Maya glyphs and Ugaritic, the last bringing Ugarit with it.

What phase 2 produced, beyond the notes, is a second axis for the whole area, now written up as `Decipherment/why-scripts-stay-unread.md`. Phase 1 established that corpus size is the binding constraint on the unread scripts. Phase 2 shows that among the *solved* ones the decisive variables were different every time, and none of them was a shortage of text.

~~The obvious next use of that note is to apply it.~~ **Done**, 2026-08-10. All seven unread scripts are now diagnosed in that note, and the result was not what phase 1 implied: **only one of the seven, the Phaistos Disc, is cleanly explained by corpus size.** Applying the taxonomy also broke it in three places and it now carries the repairs, including two new family-two mechanisms (insufficient attention, and an interpretive tradition destroyed rather than faded) each resting on a single case.

**What follows from the diagnosis, in rough order of value:**

- **Carry the diagnosis back into the seven script notes.** Each still describes its obstacle in its own terms and none says which family it is in. Deliberately deferred while the taxonomy was still moving; it should be reconciled at the audit.
- ~~Proto-Elamite is the tractable one.~~ **Acted on**, 2026-08-10. Englund 2004, free from the CDLI, is now the note's main source and confirms the diagnosis in the author's own words. Still outstanding on it: the chapter was read only to page 103 of 149, and the CDLI catalog itself has not been queried for a per-site breakdown.
- ~~The Voynich needs its hypothesis space narrowed, and the two notes should be joined.~~ **Joined**, 2026-08-10. `is-it-writing-at-all.md` now argues that well-posedness and corpus size are the two terms of one expression, which makes it load-bearing rather than a side-debate and explains why entropy is the tool in the Indus dispute. The Voynich itself still needs its candidate set narrowed, and nothing in the vault does that. One batch each, each on *what actually broke it*, which is usually a bilingual, a proper name, or a structural regularity rather than cleverness. Older sources, far more likely to be open access than phase 1's were. Ugarit is needed as a `Place` note here and is already overdue as the sole provenance of the CM3 texts.

**Phase 3, people.** Driven by `check-vault.py --report`. Ventris, Young and Grotefend written 2026-08-10, the first because the sweep made plain that the vault held Kober and Chadwick and not the man who read Linear B.

The sweep now surfaces, in rough order of how strongly: **Horapollo** and **Kircher**, who would be the vault's first notes for people who *blocked* a decipherment rather than achieving one, and who are the standard labels for the wrong-theory obstacle; **Diego de Landa**, whose alphabet nobody recognized for four centuries; **J. Eric S. Thompson**, still the least defensible characterization in the area; **Claude Schaeffer**, who bridges Ugarit and Enkomi; and **Barthel**, for the rongorongo corpus. Bauer, Dhorme and Virolleaud remain owed from batch 8.

Horapollo and Kircher are the interesting ones. A `Person` note for an obstacle would test whether `types/person.md`'s inclusion test means what it says, since both are standard labels for a result, and the result is an error.

**Phase 4, the thin areas.** Started 2026-08-10 with `General-Linguistics/redundancy.md`, which was the highest-value gap anywhere in the vault: the Decipherment area had been dividing by redundancy for months without a note saying what it is.

**Computer Languages is being left thin deliberately, and that is a recommendation rather than a deferral.** The area holds one note, on Lisp. Nothing in nine batches of Decipherment work has needed it, and writing notes there now would be filling a quota rather than following the argument, which is what `DECISIONS.md` says this vault does not do. The one thing that would genuinely serve is a note on statistical language models, n-grams and Markov chains, since `computational-decipherment-three-tasks.md`, `Yadav et al. 2009` and `redundancy.md` all lean on them; but that belongs under Computational linguistics in General Linguistics, not here.

Leave Computer Languages until Andrew wants it for its own sake. It is the one area whose thinness is not a defect in the vault's coverage but a consequence of what the vault is about.

## Standalone items, not tied to a phase

- **Linear Elamite** deserves a note. It is not Proto-Elamite, and `Decipherment/proto-elamite.md` states the distinction. Its 21 or 22 inscriptions, most longer than the longest of 4,000 to 5,000 Indus texts, are the cleanest demonstration in the vault that corpus volume and text length are independent variables. No ISO 15924 code, no Unicode block.
- **A `Language` note for Rapanui.** A real, living, attested language currently mentioned only as an appendage to a script, and the vault's first Austronesian entry. **Stubbed 2026-08-13**; it is now one of six Austronesian stubs and still needs writing.
- **Thomas Young now clearly earns a `Person` note.** He meets two limbs of the inclusion test: discussed in two or more notes, and bridging areas, since the same man worked on optics and physiology. The credit dispute with Champollion is recorded in `people/champollion.md` and would be better balanced by a note of his own.
- **Coptic, and the Coptic alphabet.** `Copt` 204, blocks U+2C80-U+2CFF and U+102E0-U+102FF, both verified. Whether Coptic is a stage of Egyptian or a language in its own right decides whether that is one note or two. **The language is stubbed as at 2026-08-13**, filed under Afro-Asiatic / Egyptian, which anticipates that question rather than settling it; the script has no note.
- **Hieratic (`Egyh` 060) and demotic (`Egyd` 070)** have codes and no notes, and demotic is a third of the Rosetta Stone.
- **Hans Bauer's cryptanalytic background.** Accounts circulate that he did codebreaking for German military intelligence in the First World War and applied statistical method to Ugaritic. If true it is the most direct Cryptography-to-Decipherment link in the vault. It is currently unverified: only a search summary asserts it, Wikipedia's article on Bauer does not mention it, and the retrieved parts of Day 2002 do not cover it. Bauer's *Entzifferung* would settle it.
- **`Person` notes for Bauer, Dhorme and Virolleaud**, deferred from batch 8 because the most substantive claim about Bauer is the unverified one above.
- **J. Eric S. Thompson.** The vault now characterizes him at second hand, through his opponents, including the phrase "communist propaganda". He led Maya studies for decades and nothing of his has been read. Under the rule on contested claims this is the least defensible thing in the Decipherment area.
- **Old Persian** (`Xpeo` 030, block U+103A0-U+103DF) and **Elamite**. Old Persian was the wedge that opened cuneiform; Behistun is trilingual and the corpus covers one of the three languages. This was the most obvious hole left by batch 6. **Both are stubbed as at 2026-08-13**, Old Persian with the language layer and Elamite by the isolate retyping, so what is owed is now the writing and the Old Persian script note.
- **Cretan Hieroglyphic**, the third Aegean script of the period and the natural comparison for both Linear A and the Phaistos Disc. Mnamon covers it.
- **The `wikidata` sweep.** High value as the universal join key, and **not** the cheap job it looks: a Q-number is the most fabricable string in the vault, so it needs real lookups rather than recall.
- **Two junction notes** still unwritten at the foot of `_junctions.md`, plus a third added after batch 4: corpus destruction as a historical event rather than an accident, which rongorongo showed the existing framing does not cover.
- ~~**Test the vault against Tolaria's actual rendering.**~~ **Superseded 2026-08-12** by the move to Obsidian; the equivalent check (Bases, graph, aliases as observed rather than documented behavior) is step 2 and 4 of the migration section above.

## Sources

This is a planning document rather than a research note, so it carries no citations of its own. Every claim above about a source's status is recorded, with its evidence, in the relevant `Reference` note or in `STATUS.md`.
