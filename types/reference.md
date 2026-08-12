---
type: Type
aliases:
  - "Reference"
_icon: book-open
_color: teal
_sidebar_label: Reference
_order: 90
_pinned_properties:
  - authors
  - year
  - status
authors:
year:
title:
container:
ref_type: paper
doi:
url:
open_access:
license:
accessed:
status: unread
subfield:
belongs_to:
related_to:
---

# Reference

A bibliographic entry: one note per source, cited from many. Lives in `references/`. Filename and title use a citation key of author and year (`barber-1974.md`, titled `Barber 1974`); disambiguate with a letter (`rao-2009a`).

## Fields

- `authors`: `Surname, Initials; Surname, Initials`. A plain string, not wikilinks. Only seminal authors get a `Person` note, and the link runs the other way via `key_works`.
- `ref_type`: `paper` | `book` | `chapter` | `website` | `dataset` | `course` | `thesis` | `corpus`.
- `status`: the reading list. `unread` | `in-progress` | `read`. Do not mark something read that you have skimmed.
- `doi` / `url`: prefer a DOI or stable publisher URL.
- `open_access`: a free copy, where one exists alongside a paywalled version of record. Give both.
- `license`: for datasets. Matters because the repository is public; see `_data-sources.md`.

Reference notes do not need `cites` (they are the thing cited) but do carry `belongs_to` and `subfield`.
