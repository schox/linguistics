---
type: Doc
status: living
---

# Conventions

The rules of the Linguistics vault. Andrew and any AI assistant read this first. Living document: when a convention changes, change it here, then update the type documents in `types/` to match.

## What the vault is

A Tolaria vault for linguistics and related matters, human languages, computer languages, and cryptography. The source of truth is the filesystem: plain Markdown with YAML frontmatter, plus attachments (PDF, docx, images).

This is a reference and archive vault, not primarily an authoring vault. Content is a mix of original notes (concepts, comparisons, worked examples) and reference material collected from elsewhere (dictionaries, grammars, papers, specs, RFCs, books). Markdown notes are the concept notes, language and cipher hubs, reference wrappers, and the per-area index notes (MOCs) that make the archive navigable.

## Folder layout

Folders are not load-bearing for Tolaria (it organises by `type`), but they keep the vault sane in Finder, the terminal and on GitHub.

```
Linguistics/
  README.md               orientation
  CONVENTIONS.md           this document
  AGENTS.md                AI onramp
  types/                   type definitions
  views/                   saved sidebar views
  attachments/             images referenced from notes
  General-Linguistics/     linguistics theory: phonetics, phonology, morphology, syntax, semantics,
                            pragmatics, historical/comparative linguistics, sociolinguistics, etymology
  Human-Languages/          specific human languages: grammar, vocabulary, courses, dictionaries
  Computer-Languages/       programming, markup, query and formal languages
  Cryptography/             ciphers, cryptographic algorithms, cryptanalysis, crypto history
```

Within an area, a note with a lot of accompanying attachments (a language's course materials, say) can get its own subfolder with its own `_index.md`; a note with little else around it can sit directly in the area folder. Either way, every folder that holds files needs an `_index.md`.

## Types

Every Markdown note declares a `type` in frontmatter. Supported types (defined in `types/`):

- `MOC`: a map-of-content / index note for an area or subfolder. Lists and links the files and subfolders inside it, and embeds any images that originated there.
- `Language`: a specific human language (e.g. French, Japanese, Latin). Fields: `family`, `script`, `status` (interested | learning | reference | fluent).
- `ComputerLanguage`: a programming, markup, query or formal language (e.g. Python, SQL, Lisp). Fields: `paradigm`, `first_appeared`, `status` (using | reference | historical | learning).
- `Cipher`: a specific cipher, cryptographic algorithm or system (e.g. Caesar cipher, Enigma, RSA, AES). Fields: `era`, `category` (classical | symmetric | asymmetric | hash | protocol).
- `Concept`: a term or idea worth its own note, from any of the four areas (a linguistic concept like phoneme or isogloss, a computing concept like a type system, a cryptographic concept like a nonce). Field: `category`, free text.
- `Reference`: an external reference kept for the record: a dictionary, grammar, paper, RFC, spec, book, or course. Usually wraps an attachment. Fields: `topic`, `status` (unread | in-progress | read).
- `Note`: a general working note or observation that doesn't yet belong under a more specific type.
- `Media`: a photo, diagram, screenshot or image kept for reference.
- `Doc`: utility/meta documents like this one, the README, AGENTS.

Attachments (PDF, docx, images) carry no frontmatter. They are referenced from MOC or content notes.

## Relationships

Tolaria turns the vault into a graph via wikilink fields in frontmatter. Defaults: `belongs_to` and `has` are computed inverses of each other, and `related_to` is lateral. They show in the Properties panel, backlinks, and Neighborhood view.

Model used here:

- Each area's `_index.md` (type `MOC`) acts as the hub for that area, titled `General Linguistics`, `Human Languages`, `Computer Languages`, or `Cryptography`.
- A content note (`Language`, `ComputerLanguage`, `Cipher`, `Concept`, `Reference`) sets `belongs_to` the relevant area hub, e.g. `belongs_to: "[[Human Languages]]"`. The hub then shows those notes under the computed `has` relationship; you do not write the reverse by hand.
- Use `related_to` for lateral links across areas or types, e.g. a `Concept` note on substitution ciphers `related_to` the `Cipher` notes that use the technique, or a `Language` note on French `related_to` a `Concept` note on Romance languages.

Wikilink targets resolve by note title or filename, so prefer the note's exact H1 title (e.g. `"[[Human Languages]]"`, not the folder name).

## Linking attachments to notes

Attachments should not sit orphaned. Three rules:

1. **Images live in `attachments/`.** All image files are stored in the root `attachments/` folder with clean, space-free names, prefixed by area (e.g. `cryptography-enigma-rotor-wiring.png`). Tolaria does not preview paths that contain spaces or angle brackets, so embeds use plain markdown with a clean relative path: `![Enigma rotor wiring](../attachments/cryptography-enigma-rotor-wiring.png)`. Never use angle-bracket URLs in embeds.
2. **Folder index.** Every folder that holds files has an `_index.md` (type `MOC`) that embeds the images which originated in that folder, links the documents still in the folder, and links subfolders to their own `_index.md`.
3. **Content notes.** Where an attachment belongs to a concept covered by a note, embed or link it from that note too, not just the MOC. Example: a scan of an Enigma wiring diagram is embedded in `Cryptography/enigma.md`, not just listed in `Cryptography/_index.md`.

## Frontmatter

Minimal and consistent. Examples:

```yaml
---
type: MOC
area: Human-Languages
updated: 2026-08-09
---
```

```yaml
---
type: Language
family: Romance
script: Latin
status: learning
belongs_to: "[[Human Languages]]"
---
```

```yaml
---
type: ComputerLanguage
paradigm: functional
first_appeared: 1958
status: reference
belongs_to: "[[Computer Languages]]"
---
```

```yaml
---
type: Cipher
era: WWII
category: electromechanical
belongs_to: "[[Cryptography]]"
related_to:
  - "[[Rotor Cipher]]"
---
```

```yaml
---
type: Reference
topic: Historical linguistics
status: unread
belongs_to: "[[General Linguistics]]"
---
```

Use Tolaria's built-in relationships (`belongs_to`, `has`, `related_to`) where they fit; any frontmatter field containing `[[wikilinks]]` is treated as a relationship.

## Intake rules (what belongs here)

A file or note belongs in this vault if it concerns linguistics, a specific human language, a computer/programming/formal language, or cryptography:

- Linguistic theory, historical/comparative linguistics, sociolinguistics, etymology → `General-Linguistics/`
- A specific human language: grammar, vocabulary, courses, dictionaries → `Human-Languages/`
- A specific programming, markup, query or formal language: specs, references, notes → `Computer-Languages/`
- Ciphers, cryptographic algorithms, cryptanalysis, crypto history → `Cryptography/`

**Never bring into this vault:**

- **Real secrets, keys or credentials.** A `Cipher` or `Concept` note can discuss RSA or AES as cryptography; it must never hold an actual private key, password, API token or seed phrase. Those stay in secured storage and are never mirrored here, even as an example.
- **Clinical or patient data.** Never.
- **Other vaults' material.** Andrew's personal/professional life belongs in the `Andrew` vault, Novansa OÜ material belongs in the `Novansa` vault, the novel belongs in the `Spoonbill` vault.

If a file's status is unclear, leave it out and flag it rather than guess.

## Naming

- Keep original filenames for document attachments (PDF, docx); they carry dates and context.
- Images are renamed into `attachments/` with clean, space-free, area-prefixed names.
- New Markdown notes: kebab-case filename, descriptive H1 title.
- MOC notes: `_index.md` inside the folder they describe.

## Git

The vault is a git repository. Remote: `https://github.com/schox/linguistics.git`. Commit with descriptive messages; ask Andrew before pushing unless he has said otherwise.
