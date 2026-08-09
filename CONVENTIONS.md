---
type: Doc
status: living
---

# Conventions

The rules of the Linguistics vault. Andrew and any AI assistant read this first. Living document: when a convention changes, change it here, then update the type documents in `types/` to match.

## What the vault is

A Tolaria vault for linguistics and related matters, human languages, computer languages, cryptography, and decipherment. The source of truth is the filesystem: plain Markdown with YAML frontmatter, plus attachments (PDF, docx, images).

The vault serves **personal and academic research**. That has one consequence which runs through everything below: claims carry references, and references carry links wherever a link exists. A note without sources is a draft, not a finished note.

## Folder layout

Folders are deliberately shallow. Tolaria organises by `type`, and the taxonomy lives in frontmatter (see "Taxonomy and subfields"), so folders exist only to keep the vault navigable in Finder, the terminal and on GitHub.

```
Linguistics/
  README.md                orientation
  CONVENTIONS.md            this document
  AGENTS.md                 AI onramp
  _junctions.md             index of cross-cutting notes
  types/                    type definitions
  views/                    saved sidebar views
  attachments/              images referenced from notes
  references/               the bibliography, one note per source
  people/                   seminal figures, one note each
  places/                   seminal institutions and sites
  General-Linguistics/      the theory
  Human-Languages/          particular languages, organised genealogically
  Computer-Languages/       programming, markup, query and formal languages
  Cryptography/             ciphers, algorithms, cryptanalysis, crypto history
  Decipherment/             reading lost scripts and unknown languages
```

**One level per area is the rule.** A second level is allowed only where a body of attachments needs its own home (a language's course materials, a script's plate scans). Do not build the taxonomy as nested folders: a note belongs to one folder but often to several subfields, and folders cannot express that. Put it in frontmatter instead.

## Types

Every Markdown note declares a `type` in frontmatter. Supported types (defined in `types/`):

- `MOC`: a map-of-content / index note for an area or subfolder.
- `Language`: a specific human language. Fields: `family`, `script`, `status`, `era`.
- `Script`: a writing system, which is **not** the same thing as a language (see below). Fields: `class`, `period`, `decipherment_status`, `writes`.
- `ComputerLanguage`: a programming, markup, query or formal language. Fields: `paradigm`, `first_appeared`, `lineage`, `status`.
- `Cipher`: a cipher, cryptographic algorithm or system. Fields: `era`, `category`.
- `Method`: a technique, manual or computational, that transfers between areas. Fields: `category`, `origin`, `applies_to`.
- `Concept`: a term or idea worth its own note, from any area. Field: `subfield`.
- `Person`: a seminal figure in one of the areas. Fields: `born`, `died`, `field`, `known_for`, `key_works`, `worked_at`.
- `Place`: an institution where expertise concentrated, or a site that produced the evidence. Fields: `kind`, `country`, `flourished`.
- `Reference`: a bibliographic entry, one per source. Fields: `authors`, `year`, `container`, `doi`, `url`, `ref_type`, `status`.
- `Note`: a general working note that doesn't yet belong under a more specific type.
- `Media`: a photo, diagram, plate or image kept for reference.
- `Doc`: utility/meta documents like this one, the README, AGENTS.

Attachments (PDF, docx, images) carry no frontmatter. They are referenced from MOC or content notes.

### Script is not Language

Scripts and languages are many-to-many, and conflating them makes the decipherment material incoherent. Cuneiform wrote Sumerian, Akkadian, Hittite, Elamite and Old Persian, which are unrelated languages. Japanese uses four scripts at once. Linear A is a script whose underlying language is unknown. Etruscan is a language we can pronounce but not understand.

So "is X deciphered?" is always two questions: do we have the script, and do we have the language? Keep them in separate notes, joined by `writes` / `written_in`.

## Taxonomy and subfields

Each area's `_index.md` carries the controlled vocabulary of subfields for that area. Content notes declare one or more via `subfield:`. This is what makes the taxonomy re-cuttable: to reorganise a branch, change the vocabulary and the frontmatter, and no file moves.

```yaml
subfield:
  - Historical and comparative
  - Writing systems
```

Use values from the area index where one fits. If nothing fits, add the value to the area index in the same commit, so the vocabulary stays closed and discoverable.

## Relationships

Tolaria turns the vault into a graph via wikilink fields in frontmatter. `belongs_to` and `has` are computed inverses of each other, and `related_to` is lateral. They show in the Properties panel, backlinks, and Neighborhood view.

Model used here:

- Each area's `_index.md` is the hub for that area, titled `General Linguistics`, `Human Languages`, `Computer Languages`, `Cryptography`, `Decipherment`.
- Content notes set `belongs_to` the relevant area hub. The hub shows them under the computed `has`; do not write the reverse by hand.
- `related_to` carries lateral links, including across areas.
- `cites` on a content note points at `Reference` notes. The inverse tells you every note that draws on a given source.
- `writes` on a `Script` note points at the `Language` notes it records.
- `applies_to` on a `Method` note points at the areas or problems it is used on.

Wikilink targets resolve by note title or filename, so prefer the note's exact H1 title.

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

**Distinguish what you have read from what you have merely found.** The `status` field on a `Reference` is the reading list. Do not mark something `read` that you have skimmed.

**Attribute contested claims to their proponents.** Much of the decipherment material is disputed, sometimes bitterly. Write "Rao and colleagues argue" and "Farmer, Sproat and Witzel reply", not "the Indus script is writing". Where a debate is live, the note should carry both sides and their sources.

## People

`Person` notes cover seminal figures, linked from documents as they are mentioned. They live in `people/` because the interesting ones belong to more than one area, and `field` taking multiple values is the marker of a genuine cross-area figure.

**Inclusion test.** Not every author of every cited paper. A person earns a note if at least one holds: they are cited or discussed in two or more notes; their name is the standard label for a method, result or principle; or they bridge two or more areas. Otherwise they remain an author string on the `Reference` note.

**Living people.** Stick to documented professional contribution, sourced. No unsourced biographical claim, no health or personal-life detail, no political characterisation, and nothing written from memory. This is not squeamishness: false reports of Noam Chomsky's death circulated widely in 2024, so a note written casually from recall could enshrine an error that looks perfectly plausible. If a fact cannot be verified now, leave it out and say so.

**Credit is part of the record.** Where a contribution has been historically misattributed or overlooked, say so with sources. Alice Kober's relationship to the Linear B decipherment is the standing example.

## Places

`Place` notes cover institutions and sites. They live in `places/` alongside `people/` because they are cross-cutting entities rather than subject matter.

The two kinds sit at opposite ends of the same process. **Institutions** are where interpretation happens and are linked from `Person` notes via `worked_at`. **Sites** are where the material comes from and are linked from `Script` notes via `found_at`.

Sites are not background colour. The size of a surviving corpus decides whether a script can be read, and corpus size is set by excavation, so provenance is causally upstream of the central argument in Decipherment. Knossos is why Linear B was decipherable.

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

Licensing matters here because the repository has a public remote. Glottolog and WALS are CC BY 4.0 and may be reused with attribution. Ethnologue is proprietary, and most of the programming-language projects state no licence at all, so those are link-only. Never copy data whose licence you have not checked.

If a subset must be held locally, record the exact version and DOI, store it in CLDF rather than an invented schema, and mark it as a dated snapshot.

## Linking attachments to notes

Attachments should not sit orphaned. Three rules:

1. **Images live in `attachments/`** with clean, space-free names prefixed by area (e.g. `decipherment-linear-b-tablet-py-ta-641.png`). Tolaria does not preview paths containing spaces or angle brackets, so embeds use plain markdown with a clean relative path: `![Pylos tablet Ta 641](../attachments/decipherment-linear-b-tablet-py-ta-641.png)`. Never use angle-bracket URLs in embeds.
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

## Style

Australian English. No em-dashes (use commas, parentheses, semicolons). Extinct or dead languages are marked with a dagger in prose lists. Give dates as BCE/CE.

## Git

The vault is a git repository. Remote: `https://github.com/schox/linguistics.git`. Commit with descriptive messages; ask Andrew before pushing unless he has said otherwise.
