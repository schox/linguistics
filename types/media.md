---
type: Type
aliases:
  - "Media"
_icon: image
_color: pink
_sidebar_label: Media
_order: 80
_pinned_properties:
  - date
  - credit
date:
credit:
license:
subfield:
belongs_to:
related_to:
status: open
---

# Media

A photo, diagram, plate or image kept for reference, where the image itself warrants a note rather than a bare embed in a MOC.

## Fields

All four are **required and checked**, because an image with no recorded origin cannot be verified by a reader and is worth no more than an unsourced sentence:

- `credit`: who made it. Own work says so explicitly.
- `license`: the terms. Own work still states them.
- `source_url`: where it came from. For own work, state that there is no external source.
- `retrieved`: the date it was obtained.

The repository is public, so an unlicensed scan of an in-copyright plate does not belong here whatever its attribution; link to it instead.

**Every file in `attachments/` must be traceable**, not only those with a `Media` note. The checker fails an artifact that no note references, and an artifact whose referencing notes record no origin. A `## Provenance` section in the note that uses the file satisfies this where a full `Media` note would be overkill.

The image file itself goes in `attachments/` with a clean, space-free, area-prefixed name.

## Body

```markdown
# <What the image shows>

<What it is, and what it is evidence of.>

<The embed itself: plain markdown, relative path into
 attachments/, area-prefixed space-free filename.>

## Provenance
   Where the image came from, who made it, and when.

## Credit and license
   Required for anything not your own.

## Sources
```

Embeds use plain markdown with a relative path, never angle-bracket URLs or wikilink embeds, so they render on GitHub as well as in Obsidian. See `CONVENTIONS.md`.
