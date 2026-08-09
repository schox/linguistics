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
3. `_junctions.md`, for the argument the vault is organized around.
4. The relevant area's `_index.md`, which holds the controlled `subfield` vocabulary for that area.

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

Commit with descriptive messages. Ask Andrew before pushing unless he has said otherwise.

### If you are running in Cowork rather than locally

Cowork reaches the vault through a device bridge, which has two quirks worth knowing. Files appear under a session mount path rather than the real one, so translate paths. More importantly the bridge cannot delete files, so `git` leaves `.git/index.lock` behind after every `git add` and the next command fails with "another git process seems to be running". The workaround is to rename the lock in place (`mv .git/index.lock .git/index.lock.stale`) between git commands. Running locally, none of this applies.
