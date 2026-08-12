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

Record `credit` and `license` for anything not your own. The repository is public, so an unlicensed scan of an in-copyright plate does not belong here; link to it instead.

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
