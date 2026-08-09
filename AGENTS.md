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

## Rules

1. **International English (US spelling)** in this vault: organize, standardize, center, color, license, program, catalog, paleographic. This is a deliberate exception to Andrew's usual Australian English, set for this project. No em-dashes (use commas, parentheses, semicolons).
2. **Never normalize a quoted title, proper noun or quotation.** Tamburini's paper really is titled "combinatorial optimisation"; Barber's book really is *Archaeological Decipherment*. Changing a title breaks the citation. `scripts/check-vault.py` holds the allowlist.
3. **Reference everything.** This is a research vault. Every substantive note ends with a `## Sources` section of markdown links and declares `cites:` in frontmatter. One `Reference` note per source, in `references/`, keyed `author-year`. Prefer a DOI or stable publisher URL, and give an open-access copy alongside a paywalled one where it exists.
4. **Do not invent citations.** If you cannot verify a bibliographic detail, say so in the note rather than guessing. A wrong citation is worse than a missing one.
5. **Attribute contested claims.** Much of the decipherment material is disputed. Write "Rao and colleagues argue", not "the Indus script is writing", and give both sides with sources where a debate is live.
6. **Person notes have an inclusion test** (see `types/person.md`); authorship of a cited paper is not by itself grounds for one. For living people, write only sourced professional contribution, never from memory.
7. **Place notes have an inclusion test too** (see `types/place.md`). Sites matter because corpus size decides decipherability, so record provenance via `found_at` rather than treating it as trivia.
8. Keep `Script` and `Language` as separate notes joined by `writes` / `written_in`. They are many-to-many and conflating them breaks the decipherment material.
9. **Fill external identifiers** on entity notes wherever they exist (`glottocode`, `iso15924`, `hopl_id`, `wikidata`). They are the join to real datasets. Do not mirror external data into the vault; link to it. Check the license before copying anything, and see `_data-sources.md`.
10. Do not deepen the folder tree. If a note seems to need a new folder, it almost certainly needs a `subfield` value instead.
11. Use `subfield` values from the area `_index.md`. If none fits, add it to the index in the same change so the vocabulary stays closed.
12. Never store real keys, secrets or credentials, even as examples in a cryptography note.
13. When you add or move files, update the relevant `_index.md` and, for cross-cutting notes, `_junctions.md`.
14. Commit with descriptive messages. Ask Andrew before pushing unless he has said otherwise.

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
