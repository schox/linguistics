---
type: Doc
status: living
---

# AGENTS.md

If you are an AI assistant working in this vault: read this file first, then `CONVENTIONS.md`.

## What this vault is

A Tolaria vault for linguistics, human languages, computer languages, cryptography and decipherment, serving personal and academic research. Markdown with YAML frontmatter plus attachments, in a git repository with a GitHub remote.

## What to read, in order

1. This file, for the operating model.
2. `CONVENTIONS.md`, for layout, types, the taxonomy model, referencing and intake rules. This is the contract.
3. `STATUS.md` for where the project is, then `ROADMAP.md` for what to do next and what is blocked.
4. `_junctions.md`, for the argument the vault is organized around.
5. The relevant area's `_index.md`, which holds the controlled `subfield` vocabulary for that area.

`DECISIONS.md` records why the vault is shaped as it is, and what was rejected. Read the relevant entry before reversing anything that looks like an obvious improvement.

## The model in one paragraph

Five areas: `General-Linguistics/`, `Human-Languages/`, `Computer-Languages/`, `Cryptography/`, `Decipherment/`, plus `references/` for the bibliography. Folders are shallow and are not the taxonomy; the taxonomy is the `subfield` field, drawn from each area index. Notes carry a `type` (`MOC`, `Language`, `Script`, `ComputerLanguage`, `Cipher`, `Method`, `Concept`, `Person`, `Place`, `Reference`, `Note`, `Media`, `Doc`) and `belongs_to` an area hub. Decipherment is the integrative area, taking method from Cryptography, constraint from General Linguistics, candidate relatives from Human Languages, and technique from Computer Languages.

## The evidentiary standard

This vault is for research and academic use: Andrew's own first, shared with others later. Everything below follows from that. **Confine yourself to the facts as you find them.**

- **No inference presented as fact.** If a claim is not carried by a source you have actually consulted, it does not go in. Not a plausible reconstruction, not a reasonable interpolation, not something that is very probably true. Your own reasoning is not a source.
- **Say when a matter is contested**, and attribute the sides.
- **Say when something is missing.** If a fact would have been useful and you could not find it, record that in the note, with what you looked for. A stated gap is a finding and saves the next reader the same search. A silent omission looks like completeness and is not.
- **A wrong fact is worse than no fact**, because a reader cannot tell it apart from a right one. That asymmetry is the reason the vault carries references at all.

Three failure modes, three different treatments, and they must not be collapsed into each other:

| Situation | What to do |
| --- | --- |
| You cannot verify a claim | Do not write it. Mark the note `status: draft` and say in prose what would settle it. |
| The matter is genuinely disputed | Write it, with both sides and their sources, attributed to their proponents. |
| The fact appears not to exist, or you could not find it | Write the absence, under `## Open questions`, saying what you looked for. |

This applies to a note's whole content, not only to its citations. It applies with particular force to numbers (corpus sizes, dates, sign counts) and to external identifiers, both of which look authoritative on the page and are easy to produce from recall rather than from a source.

### How to verify

**Order.** Registries and primary documents first; search engines only to locate them, never to answer. Resolve every identifier for a batch before writing any prose: ISO 15924 from the Unicode Consortium code list, Unicode blocks from `Blocks.txt`, Q-numbers from the Wikidata API, `glottocode` from Glottolog. This is fast, it is authoritative, and it usually turns up facts for later batches at no extra cost.

**A search-result summary is not a source.** No number reaches frontmatter from one. Get to the paper, the registry or the database record. If a PDF resists fetching it is still saved to disk and can be read directly, which is the reliable route for papers and should be the first attempt rather than the fallback.

**Repetition is not corroboration.** A figure appearing in five search results is usually one tertiary source quoted five times. Count distinct primary sources, not distinct URLs, and say which one you actually read.

**When a page refuses a direct fetch**, use the Tavily extraction service as a retrieval fallback. Many institutional and reference sites (UNESCO, Britannica, museum and project sites) return HTTP 403 to any non-browser client, and those are exactly the sources archaeological provenance depends on. Two conditions: it is a fallback and not the default path, because an extract is one step further from the primary document than the document is; and where the extracted content carries a load-bearing fact, the note says it was retrieved that way, so a reader knows the page itself was not seen. Do not attempt to defeat a block by other means.

**Tertiary encyclopedias are sources, not references.** Britannica, Wikipedia and their like may be cited under a note's `## Sources` and are often the honest answer for an outline. They never get a `Reference` note. See `CONVENTIONS.md`.

**Derived numbers must show their working.** A ratio, percentage, average, unit conversion or absolute date computed from sourced inputs is *your* claim, not the source's, and it carries the source's authority without having earned it. State the inputs and their origin in the note so the arithmetic is checkable and not merely the citation. This is where errors actually happen: verification instinctively points at quotations, and quotations are the part already under control.

**A required field with no verifiable value** takes the nearest verifiable proxy and says in the note that it is a proxy, with what it does and does not establish. It never takes a plausible guess. `references/rutter-aegean-prehistory.md` is the worked example: an undated web resource whose `year` is its copyright notice, stated as dating the access rather than the work. A schema slot is not evidence that a fact exists.

## Rules

1. **International English (US spelling)** in this vault: organize, standardize, center, color, license, program, catalog, paleographic. This is a deliberate exception to Andrew's usual Australian English, set for this project. No em-dashes (use commas, parentheses, semicolons).
2. **Never normalize a quoted title, proper noun or quotation.** Tamburini's paper really is titled "combinatorial optimisation"; Barber's book really is *Archaeological Decipherment*. Changing a title breaks the citation. `scripts/check-vault.py` holds the allowlist.
3. **Reference everything.** This is a research vault. Every substantive note ends with a `## Sources` section of markdown links and declares `cites:` in frontmatter. One `Reference` note per source, in `references/`, keyed `author-year`. Prefer a DOI or stable publisher URL, and give an open-access copy alongside a paywalled one where it exists. Wikipedia may be listed under a note's `## Sources` and linked in prose, but never gets its own `Reference` note; `references/` is the authoritative bibliography, and Wikipedia is a finding aid pointing into it.
4. **Do not invent citations.** If you cannot verify a bibliographic detail, say so in the note rather than guessing. A wrong citation is worse than a missing one.
5. **Record what you could not find.** Where a fact would have been useful and is missing, unlocatable or does not appear to exist, say so in an `## Open questions` section rather than passing over it. See the evidentiary standard above.
6. **Attribute contested claims.** Much of the decipherment material is disputed. Write "Rao and colleagues argue", not "the Indus script is writing", and give both sides with sources where a debate is live.
7. **Person notes have an inclusion test** (see `types/person.md`); authorship of a cited paper is not by itself grounds for one. For living people, write only sourced professional contribution, never from memory.
8. **Place notes have an inclusion test too** (see `types/place.md`). Sites matter because corpus size decides decipherability, so record provenance via `found_at` rather than treating it as trivia.
9. Keep `Script` and `Language` as separate notes joined by `writes` / `written_in`. They are many-to-many and conflating them breaks the decipherment material.
10. **Fill external identifiers** on entity notes wherever they exist (`glottocode`, `iso15924`, `hopl_id`, `wikidata`). They are the join to real datasets. Look each one up; never write an identifier from recall. Do not mirror external data into the vault; link to it. Check the license before copying anything, and see `_data-sources.md`.
11. Do not deepen the folder tree. If a note seems to need a new folder, it almost certainly needs a `subfield` value instead.
12. Use `subfield` values from the area `_index.md`. If none fits, add it to the index in the same change so the vocabulary stays closed.
13. Never store real keys, secrets or credentials, even as examples in a cryptography note.
14. When you add or move files, update the relevant `_index.md` and, for cross-cutting notes, `_junctions.md`.
15. Commit with descriptive messages. Ask Andrew before pushing unless he has said otherwise.

## Care with claims

The computational decipherment literature is widely misreported, including by reputable outlets. Before writing that a script has been deciphered by a model, check which of the three tasks in `Decipherment/computational-decipherment-three-tasks.md` the work actually performs. Restoration is not decipherment, and cognate search is not decipherment.

## Environment

The vault root is the git repository root. All paths in this document are relative to it. Work from the repo root and use relative paths; do not hard-code an absolute path, because this vault is worked on from more than one environment.

**Before you start**, always:

```sh
git status
python3 scripts/check-vault.py
```

Tolaria is a desktop app that reads and writes these same files while Andrew has the vault open, and it has its own in-app git client. Assume the working tree may have changed under you, and never assume your last-known state is current.

**Before you finish**, run the checker again and make sure it exits clean. It checks required fields per type, enum values, subfield membership against each area's stated vocabulary, wikilink quoting, wikilink resolution, `## Sources` presence, relative link resolution, and house style.

**After adding an entity note**, run the sweep:

```sh
python3 scripts/check-vault.py --report
```

The checks above are enforcement and they resolve every link that exists. They are blind in one direction: nothing detects a link that is *missing*, which is how the graph decays quietly. `--report` covers that direction and never fails, listing notes that name an existing note in prose without linking it, and capitalized names recurring across two or more notes with no note of their own. The second list feeds the `Person` and `Place` inclusion tests. It is a heuristic worklist with false positives, not a to-do list: judge each entry against the inclusion test rather than writing a note for everything it prints. Link on first mention per note only.

**To see what the vault knows it does not know:**

```sh
python3 scripts/check-vault.py --questions
```

This harvests every `## Open questions` bullet in the vault. It exists so that `ROADMAP.md` does not have to list them by hand, since a copied list of that size goes stale immediately. **Do not chase these as you go.** A full audit is planned for when the vault is closer to complete; recording a gap honestly and moving on is the intended behavior, and `ROADMAP.md` explains the trade.

Commit with descriptive messages. Ask Andrew before pushing unless he has said otherwise.

### If you are running in Cowork rather than locally

Cowork reaches the vault through a device bridge, which has two quirks worth knowing. Files appear under a session mount path rather than the real one, so translate paths. More importantly the bridge cannot delete files, so `git` leaves `.git/index.lock` behind after every `git add` and the next command fails with "another git process seems to be running". The workaround is to rename the lock in place (`mv .git/index.lock .git/index.lock.stale`) between git commands. Running locally, none of this applies.
