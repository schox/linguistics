---
type: Doc
aliases:
  - "Conventions"
status: living
---

# Conventions

The rules of the Linguistics vault. Andrew and any AI assistant read this first. Living document: when a convention changes, change it here, then update the type documents in `types/` to match.

## What the vault is

An Obsidian vault for linguistics and related matters, human languages, computer languages, cryptography, and decipherment. The source of truth is the filesystem: plain Markdown with YAML frontmatter, plus attachments (PDF, docx, images). The app is a lens; `scripts/check-vault.py`, not the app, is the authority on the schema. (The vault began life in Tolaria; `DECISIONS.md` 2026-08-12 records the move and what it changed.)

The vault serves **personal and academic research**. That has one consequence which runs through everything below: claims carry references, and references carry links wherever a link exists. A note without sources is a draft, not a finished note.

## Folder layout

Folders are deliberately shallow. The schema organizes by `type`, and the taxonomy lives in frontmatter (see "Taxonomy and subfields"), so folders exist only to keep the vault navigable in Finder, the terminal and on GitHub.

```
Linguistics/
  README.md                orientation
  CONVENTIONS.md            this document
  AGENTS.md                 AI onramp
  _junctions.md             index of cross-cutting notes
  types/                    type definitions
  views/                    saved Bases (.base table views)
  attachments/              images referenced from notes
  references/               the bibliography, one note per source
  people/                   seminal figures, one note each
  places/                   seminal institutions and sites
  General-Linguistics/      the theory
  Human-Languages/          particular languages, organized genealogically
  Computer-Languages/       programming, markup, query and formal languages
  Cryptography/             ciphers, algorithms, cryptanalysis, crypto history
  Decipherment/             reading lost scripts and unknown languages
```

**One level per area is the rule.** A second level is allowed only where a body of attachments needs its own home (a language's course materials, a script's plate scans). Do not build the taxonomy as nested folders: a note belongs to one folder but often to several subfields, and folders cannot express that. Put it in frontmatter instead.

## Types

**The schema lives in `types/`, not here.** Each type file declares the frontmatter template, the allowed values for every field, and a worked example. This document gives rules and rationale; it deliberately does not restate field lists, because maintaining a schema in two places guarantees drift.

Entity types: `Language`, `Script`, `ComputerLanguage`, `Cipher`, `Person`, `Place`.
Content types: `Concept`, `Method`, `Note`, `Media`, `Reference`.
Structural types: `MOC`, `Doc`, `Type`.

Every content note carries `subfield`, `belongs_to` and `status`, usually `related_to` and `cites`, and ends with a `## Sources` section. `MOC`, `Doc` and `Type` notes are exempt.

### Wikilinks must be quoted

```yaml
belongs_to: "[[Cryptography]]"    # correct, a string
belongs_to: [[Cryptography]]      # wrong, YAML reads a nested list, silently
```

This is the easiest mistake to make and the hardest to notice, because nothing looks broken. The checker catches it.

### Script is not Language

Scripts and languages are many-to-many, joined by `writes` and `written_in`. Cuneiform wrote five unrelated languages. Linear A is a script whose language is unknown. Etruscan is a language readable in a script we can pronounce but do not fully understand. "Is X deciphered?" is always two questions.

### Unverified facts, and facts that are absent

The vault serves research, so it confines itself to the facts as found. Inference is not evidence, and your own reasoning is not a source.

Three situations, three treatments, and collapsing them loses information:

**You cannot verify it.** Do not write it. Mark the note `status: draft` and state in prose what is missing and what would settle it. Do not invent a placeholder format; `status: draft` plus a sentence is the convention.

**It is genuinely disputed.** Write it, with both sides attributed to their proponents and both sets of sources. See "References and citations" below.

**It appears not to exist, or you looked and could not find it.** Record the absence in an `## Open questions` section at the foot of the note, saying what you looked for and where. This is the case most easily lost, because an omission reads as completeness. A stated gap is a finding: it tells the next reader that the search has been done, and it is often the honest answer for a corpus that has never been fully published.

`## Open questions` sits after `## Sources`. It is optional, and it is not a to-do list for the note's prose; it is for questions the sources themselves do not answer.

**Phrase an open question as an actionable lookup.** Distinguish what is unknown from what was merely unreachable, and say which source would settle it. "The Pleiades ID was not confirmed because the site was behind bot detection on 2026-08-09" can be picked up and closed by someone with access; "no Pleiades ID" cannot. Andrew runs a separate fact and link checking service periodically, and a well-phrased gap is work it can do.

### Derived numbers

A ratio, percentage, average, unit conversion or absolute date that you computed is your own claim, however well sourced its inputs. It inherits the appearance of authority from the citation beside it without inheriting the authority itself.

State the inputs and where they came from, so the arithmetic is checkable and not just the reference. `Decipherment/linear-a.md` does this: the corpus percentages and the signs-per-document averages are given alongside the raw counts they derive from and the paper those counts come from, and the note says which figures are lower bounds.

This is where mistakes actually occur. Verification instinct points at quotations, and quotations are the part already under control.

### Required fields with no verifiable value

Some schema fields are mandatory for a type and some facts simply do not exist: an undated web resource still needs `year`. The field takes the nearest verifiable proxy, and the note says in prose that it is a proxy and what it does and does not establish.

Never a plausible guess. A schema slot is not evidence that a fact exists, and a required field is the most reliable way to talk yourself into inventing one. Worked example: `references/rutter-aegean-prehistory.md`.

## Taxonomy and subfields

Each area's `_index.md` carries the controlled vocabulary of subfields for that area. Content notes declare one or more via `subfield:`. This is what makes the taxonomy re-cuttable: to reorganize a branch, change the vocabulary and the frontmatter, and no file moves.

```yaml
subfield:
  - Historical and comparative
  - Writing systems
```

Use values from the area index where one fits. If nothing fits, add the value to the area index in the same commit, so the vocabulary stays closed and discoverable.

## Relationships

Wikilink fields in frontmatter turn the vault into a graph. Obsidian treats frontmatter wikilinks as real links: they appear in the graph view and the backlinks pane. There is no computed inverse; a parent's children are read from its backlinks (or rendered as a tree by the Breadcrumbs plugin, which understands `belongs_to`-style fields). `related_to` is lateral.

Model used here:

- Each area's `_index.md` is the hub for that area, titled `General Linguistics`, `Human Languages`, `Computer Languages`, `Cryptography`, `Decipherment`.
- **`belongs_to` chains, and carries the topic hierarchy.** A note sets `belongs_to` its immediate parent, which may be the area hub, a subfield `MOC`, or a broader `Concept`. The parent's children are its backlinks; do not maintain a reverse list by hand. Every chain terminates at an area hub.
- **Every subfield has a `MOC` hub**, titled with the subfield's exact vocabulary value, for example `Levels of analysis`. It sits between the area hub and that subfield's notes. Since 2026-08-12 the hubs exist for the whole taxonomy, most of them as stubs; existing notes still pointing directly at an area hub move under their subfield hub when that subfield is next worked on.
- **Two subfield values are shared between vocabularies** and have one hub each rather than two same-titled notes: `Formal foundations` (General Linguistics and Computer Languages) and `Writing systems` (General Linguistics and Decipherment). Both live in `General-Linguistics/` and belong to both area hubs. See `DECISIONS.md` 2026-08-12.
- Chain depth is not limited, but keep it shallow enough to state: area, subfield, topic, subtopic is the expected shape. `subfield` stays on every note in the chain regardless of depth, because it is the taxonomy and `belongs_to` is the graph.
- `related_to` carries lateral links, including across areas. Siblings link to each other with `related_to`, not `belongs_to`.
- `cites` on a content note points at `Reference` notes. The inverse tells you every note that draws on a given source.
- `writes` on a `Script` note points at the `Language` notes it records.
- `applies_to` on a `Method` note points at the areas or problems it is used on.

### Wikilink resolution, and the alias rule

Obsidian resolves a wikilink by **filename or alias**, never by H1 title. The vault links by title (`"[[Linear B]]"`, not `"[[linear-b]]"`), so **every note whose H1 title differs from its filename carries that title in `aliases`**:

```yaml
type: Script
aliases:
  - "Linear B"
```

The checker enforces this. Keep linking by exact H1 title; the alias makes it resolve. Filenames stay kebab-case and are never casually renamed, because they are the vault's stable keys, including for any future database import.

## References and citations

This is a research vault. Referencing is not optional.

**One `Reference` note per source.** A paper cited by six notes is one note with six backlinks, not six copies of a URL. Filename and title use a citation key of author and year: `barber-1974.md`, titled `Barber 1974`. Disambiguate with a letter (`rao-2009a`) where needed.

```yaml
---
type: Reference
authors: "Shannon, C. E."
year: 1949
title: "Communication Theory of Secrecy Systems"
container: "Bell System Technical Journal 28(4), 656-715"
ref_type: paper          # paper | book | chapter | website | dataset | course | thesis | corpus
doi: "10.1002/j.1538-7305.1949.tb00928.x"
url: "https://onlinelibrary.wiley.com/doi/10.1002/j.1538-7305.1949.tb00928.x"
accessed: 2026-08-09
status: read             # unread | in-progress | read
subfield:
  - Theory
belongs_to: "[[Cryptography]]"
---
```

**Every substantive note ends with a `## Sources` section**, listing the works it draws on as markdown links, and declares them in `cites:` frontmatter so the graph knows. Prefer a DOI or a stable publisher URL over a general web page. Where an open-access copy exists alongside a paywalled version of record, give both.

**Wikipedia is a source in a note, never a `Reference` note.** Listing a Wikipedia article under a note's `## Sources`, or linking it in prose, is fine and often the most useful orientation available. What it must not become is its own file in `references/`, because `references/` is the authoritative bibliography: papers, books, chapters, datasets, corpora. Wikipedia is a finding aid pointing at those, so cite it where it helped and follow it to the work of record. `scripts/check-vault.py` fails a `Reference` note whose `url` is a Wikipedia article.

**The same applies to Britannica and other tertiary encyclopedias**, which the checker does not enforce because the list is open-ended. The test is not the publisher's reputation but the kind of document: a work of record gets a `Reference` note, a summary of works of record gets a line under `## Sources`. Institutional documentation is different again and can earn a note where it is the primary record of something, as UNESCO's World Heritage entries are for a site's extent and protection status.

**Distinguish what you have read from what you have merely found.** The `status` field on a `Reference` is the reading list. Do not mark something `read` that you have skimmed.

**Attribute contested claims to their proponents.** Much of the decipherment material is disputed, sometimes bitterly. Write "Rao and colleagues argue" and "Farmer, Sproat and Witzel reply", not "the Indus script is writing". Where a debate is live, the note should carry both sides and their sources.

## People

`Person` notes cover seminal figures, linked from documents as they are mentioned. They live in `people/` because the interesting ones belong to more than one area, and `field` taking multiple values is the marker of a genuine cross-area figure.

**Inclusion test.** Not every author of every cited paper. A person earns a note if at least one holds: they are cited or discussed in two or more notes; their name is the standard label for a method, result or principle; or they bridge two or more areas. Otherwise they remain an author string on the `Reference` note.

**Living people.** Stick to documented professional contribution, sourced. No unsourced biographical claim, no health or personal-life detail, no political characterization, and nothing written from memory. This is not squeamishness: false reports of Noam Chomsky's death circulated widely in 2024, so a note written casually from recall could enshrine an error that looks perfectly plausible. If a fact cannot be verified now, leave it out and say so.

**Credit is part of the record.** Where a contribution has been historically misattributed or overlooked, say so with sources. Alice Kober's relationship to the Linear B decipherment is the standing example.

## Places

`Place` notes cover institutions and sites. They live in `places/` alongside `people/` because they are cross-cutting entities rather than subject matter.

The two kinds sit at opposite ends of the same process. **Institutions** are where interpretation happens and are linked from `Person` notes via `worked_at`. **Sites** are where the material comes from and are linked from `Script` notes via `found_at`.

Sites are not background color. The size of a surviving corpus decides whether a script can be read, and corpus size is set by excavation, so provenance is causally upstream of the central argument in Decipherment. Knossos is why Linear B was decipherable.

**Inclusion test.** Expertise concentrated there in a way that explains a breakthrough, or it is the provenance of a significant corpus, or it is referenced from two or more notes. Not every university anyone attended, and not every find-spot.

## External data sources and identifiers

Mature curated datasets already exist for some of this material, unevenly across the areas. The vault's stance is **adopt their identifiers, link out, do not mirror**. See `_data-sources.md` for the survey and the reasoning.

Every entity note carries the external identifiers that exist for it, because those are what make the note joinable to real data rather than a paraphrase of it:

- `Language`: `glottocode` (Glottolog), `iso639_3`, `wals_code`, `wikidata`
- `Script`: `iso15924`, `iso15924_num`, `unicode_block`, `wikidata`
- `ComputerLanguage`: `hopl_id`, `wikidata`
- `Cipher`: `wikidata` only, since no domain scheme exists
- `Person`: `viaf` (library standard, best for historical figures), `orcid` (living researchers), `wikidata`
- `Place`: `geonames`, `pleiades` (ancient sites), `ror` (research institutions), `wikidata`

Wikidata Q-numbers are the universal fallback.

Licensing matters here because the repository has a public remote. Glottolog and WALS are CC BY 4.0 and may be reused with attribution. Ethnologue is proprietary, and most of the programming-language projects state no license at all, so those are link-only. Never copy data whose license you have not checked.

If a subset must be held locally, record the exact version and DOI, store it in CLDF rather than an invented schema, and mark it as a dated snapshot.

## Linking attachments to notes

Attachments should not sit orphaned. Three rules:

1. **Images live in `attachments/`** with clean, space-free names prefixed by area (e.g. `decipherment-linear-b-tablet-py-ta-641.png`). Embeds use plain markdown with a clean relative path, `![Pylos tablet Ta 641](../attachments/decipherment-linear-b-tablet-py-ta-641.png)`, never angle-bracket URLs: space-free paths and plain syntax render everywhere, including GitHub, which wikilink embeds do not.
2. **Folder index.** Every folder holding files has an `_index.md` (type `MOC`) embedding the images which originated there, linking the documents still in the folder, and linking subfolders to their own `_index.md`.
3. **Content notes.** Where an attachment belongs to a concept covered by a note, embed or link it from that note too, not only from the MOC.

Respect copyright. Scans of in-copyright books belong in personal storage, not in a vault with a public remote. Prefer a `Reference` note with a link over a copied PDF.

## Intake rules

A note belongs here if it concerns linguistics, a particular human language, a computer or formal language, cryptography, or decipherment.

**Never bring into this vault:**

- **Real secrets, keys or credentials.** A `Cipher` note can discuss RSA or AES; it must never hold an actual private key, password, API token or seed phrase, even as an example.
- **Clinical or patient data.** Never.
- **Other vaults' material.** Personal and professional life belongs in `Andrew`, Novansa OÜ material in `Novansa`, the novel in `Spoonbill`.

If a file's status is unclear, leave it out and flag it rather than guess.

## Naming

- Keep original filenames for document attachments; they carry dates and context.
- Images are renamed into `attachments/` with clean, space-free, area-prefixed names.
- New Markdown notes: kebab-case filename, descriptive H1 title.
- `Reference` notes: citation key, `author-year`.
- MOC notes: `_index.md` inside the folder they describe.

## Drafting

The schema in `types/` says what a note must carry. This says what a note should read like, and each type file now carries a **body skeleton** under `## Body` alongside its frontmatter template.

Both are conventions, not checks. `scripts/check-vault.py` validates frontmatter and the presence of `## Sources`; it does not read prose and is not going to. Drafting is a discipline, like the evidentiary standard it serves.

**A note answers its own title.** This is the test for whether a note is finished, and it is deliberately not a word count. A reader who arrives cold at `Phonology` should leave knowing what phonology is. A reader who arrives at `Kasiski examination` should be able to perform one. Length follows the subject and the sources: 176 words is too thin for a method the Decipherment area runs on, and about right for a minor identifier note. Where the sources will not support an answer, that is an `## Open questions` entry, never a reason to pad.

**Open with the definition.** The first sentence says what the subject is. No throat-clearing, no announcement of what the note will cover, no restatement of the vault's purpose. Then a short orientation: when, where, how big, who.

**Name a section for its subject, not for its relevance.** `## Phonotactics`, not `## Why phonotactics matters here`. This is the 2026-08-11 decision on entries, applied to structure: a heading that frames content as an argument for the vault will be filled with an argument for the vault, and the reference layer does not get built. About thirty legacy sections in the older Decipherment, people and places notes are named this way; they are recorded against the audit in `ROADMAP.md` rather than repaired piecemeal.

**Prose by default.** Lists are for genuine enumerations: sign inventories, sound changes, code lists, child topics, the sides of a dispute. A list of full sentences is usually a paragraph that has lost its connective tissue.

**Attribute in the sentence, not only in `## Sources`.** A reader should know whose claim it is without scrolling. "Rao and colleagues argue", "Farmer, Sproat and Witzel reply", "Englund's own diagnosis is". `## Sources` records where it came from; the sentence records whose it is.

**Mark the vault's own reasoning as the vault's own.** Where a note computes, compares or infers, say so in the prose: "computed here", "the figure is derived from", "no source states this directly". Derived numbers additionally show their inputs, per the rule above.

**Hedge to the evidence, and only to the evidence.** Say which of three things is true: established, contested, or unknown. "Probably", "arguably" and "it seems" are not calibration, they are a way of writing an unsourced claim without owning it. Contested means attributed to its sides; unknown means `## Open questions`.

**Tense.** Present for what is the case, including for dead systems, since the system still has the properties it had: "Linear B has about 87 syllabic signs". Past for events: "Ventris announced the decipherment in 1952". A script or language that is no longer used is extinct in the past tense and describable in the present.

**Voice.** The vault does not address the reader as "you" and does not write as "I". Where the vault itself is doing something, name it: "this vault holds", "the comparison here is". Dagger for extinct languages in prose lists, per `## Style`.

**Link on first mention per note, then stop.** Repeated wikilinks to the same note add nothing to the graph and clutter the sentence. `check-vault.py --report` lists notes that name an existing note without linking it once.

**`Doc` notes are exempt** from all of the above. `README.md`, `ROADMAP.md` and this file are working documents, not reference entries.

## Style

The mechanical layer under `## Drafting`.

**International English (US spelling) in this vault.** Use `-ize` and `-ization` (organize, standardize, industrialization), `center`, `color`, `license`, `program`, `catalog`, `paleographic`. This is a deliberate exception to Andrew's usual Australian English: the vault's subject matter and its sources are overwhelmingly international, and locale can be changed at the point any derived work is produced.

**Quoted titles keep their own spelling, always.** Tamburini's paper is titled "...combinatorial optimisation and coupled simulated annealing" and Barber's book is *Archaeological Decipherment*. Never normalize a title, a proper noun, or quoted matter. The Research Organization Registry is named that way; the Association for Computational Linguistics is named that way. Altering a title breaks the citation.

No em-dashes (use commas, parentheses, semicolons). Extinct or dead languages are marked with a dagger in prose lists. Give dates as BCE/CE.

Run `python3 scripts/check-vault.py` before committing. It validates frontmatter, resolves relative links, and checks style, with an allowlist for protected titles.

## Git

The vault is a git repository. Remote: `https://github.com/schox/linguistics.git`. Commit freely with descriptive messages. **Ask Andrew in conversation before pushing**, every time, unless he has said otherwise for that piece of work.
