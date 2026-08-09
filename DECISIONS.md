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
