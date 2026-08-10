---
type: Doc
status: living
---

# Linguistics

Tolaria vault for linguistics, human languages, computer languages, cryptography, and decipherment. Built for personal and academic research, which means claims carry references and references carry links.

## Start here

1. Read `CONVENTIONS.md`. Layout, types, the taxonomy model, the referencing rules and the intake rules all live there.
2. If you are an AI assistant, read `AGENTS.md` first. It is the canonical onramp.
3. Read `_junctions.md` for the argument the vault is organized around, and `_data-sources.md` for what already exists externally.

## Layout

```
General-Linguistics/   the theory: phonology through to computational linguistics
Human-Languages/       particular languages, organized genealogically
Computer-Languages/    programming, markup, query and formal languages
Cryptography/          ciphers, algorithms, cryptanalysis, crypto history
Decipherment/          reading lost scripts and unknown languages
references/            the bibliography, one note per source
people/                seminal figures, one note each
places/                seminal institutions and sites
types/                 Tolaria type definitions
views/                 saved sidebar views
attachments/           images referenced from notes
scripts/               check-vault.py, the consistency checker
_junctions.md          index of cross-cutting notes
_data-sources.md       what external data exists, and how the vault relates to it
DECISIONS.md           why the vault is shaped this way, and what was rejected
STATUS.md              where the project is up to
ROADMAP.md             what to do next, and what is blocked on what
```

Folders are shallow and stay that way. The taxonomy lives in the `subfield` frontmatter field, with the controlled vocabulary held in each area's `_index.md`, so a branch can be re-cut without moving files.

## The idea

Cryptography is the backdrop to decipherment, not its parent. The two share a statistical apparatus and almost nothing else: cryptography assumes an adversary who designed the system to resist you, while decipherment faces obscurity that is an accident of cultural loss. The sharpest expression of the overlap is that Shannon's unicity distance and Barber's evidentiary threshold are the same underdetermination result reached independently in two literatures, which is why the binding constraint on Linear A is corpus size rather than method.

## Checking

```sh
python3 scripts/check-vault.py
```

Checks required fields per type, enum values, `subfield` membership against each area's stated vocabulary, wikilink quoting, wikilink resolution, presence of a `## Sources` section, relative link resolution, and house style.

```sh
python3 scripts/check-vault.py --report
```

The advisory sweep, which never fails. The checks above resolve every link that exists but cannot see a link that is missing, so this lists unlinked mentions of existing notes, and recurring names that have no note yet. Run it after adding an entity note.

```sh
python3 scripts/check-vault.py --questions
```

Every `## Open questions` bullet in the vault, harvested live so that `ROADMAP.md` does not have to keep a copy.

## Git

Git repository, remote `https://github.com/schox/linguistics.git`. Commit with descriptive messages; ask Andrew before pushing unless he has said otherwise.
