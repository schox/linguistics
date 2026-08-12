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
- `ref_type`: `paper` | `book` | `chapter` | `website` | `dataset` | `course` | `thesis` | `corpus` | `news` | `preprint`.
- `claim_status`: **required when `ref_type` is `news` or `preprint`.** `peer-reviewed` | `preprint` | `press-release` | `press-coverage` | `self-published` | `unpublished`.
- `peer_reviewed`: **required with the same two types.** `true` | `false` | `unknown`. Use `unknown` where it could not be established, not `false`.
- `status`: the reading list. `unread` | `in-progress` | `read`. Do not mark something read that you have skimmed.
- `doi` / `url`: prefer a DOI or stable publisher URL.
- `open_access`: a free copy, where one exists alongside a paywalled version of record. Give both.
- `license`: for datasets. Matters because the repository is public; see `_data-sources.md`.

Reference notes do not need `cites` (they are the thing cited) but do carry `belongs_to` and `subfield`.

## Body

A `Reference` note answers: what the work is, what it establishes, and how to get at it.

```markdown
# <Author Year>

<The work in a sentence: what it is and what it argues.>

## What it establishes
   The findings the vault actually draws on, with page or
   section references where a specific figure comes from it.
   Distinguish what the work claims from what the vault takes
   from it, since those are rarely the same extent.

## Access
   Where it was read, whether the copy was open access, and any
   retrieval caveat: a paywall, a dead host, or content reached
   through the extraction service rather than seen directly.

## Sources
```

No `## Child topics`. Where a bibliographic detail could not be verified, say so here rather than guessing: a wrong citation is worse than a missing one, because a reader cannot tell it from a right one. `references/rutter-aegean-prehistory.md` is the worked example of a required field taking a stated proxy.

### Announcements

A `Reference` of `ref_type: news` or `preprint` records a **claim**, not a finding, and its body says so:

```markdown
# <Author Year>

<Who claimed what, where, and when.>

## The claim
   What was actually asserted, in the claimant's terms.
   Which of the three tasks in
   Decipherment/computational-decipherment-three-tasks.md the
   work performs: restoration, decipherment proper, or cognate
   search. Misreporting almost always happens at that seam.

## Standing
   Published, reviewed, or neither. `claim_status` and
   `peer_reviewed` carry the same in frontmatter; the prose
   says how that was established.

## Response
   What specialists said, cited. Where a claim has simply been
   ignored by the field, record that: silence is evidence of a
   kind, and is often the whole of what can be said.

## Sources
```

Write it flatly, with neither derision nor credulity. The purpose is to know what is being claimed and by whom, so that a correct announcement is not missed among the incorrect ones. See `CONVENTIONS.md`.
