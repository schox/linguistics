---
type: Type
aliases:
  - "MOC"
_icon: map
_color: blue
_sidebar_label: Maps
_order: 10
_pinned_properties:
  - area
  - updated
area:
updated:
---

# MOC

A map-of-content (index) note for an area or folder. Lists and links the files and subfolders inside it, and embeds any images that originated there.

Every folder holding files has one, named `_index.md`, including `types/`, `scripts/`, `people/`, `places/` and `references/`.

An area `_index.md` does double duty: it is also the **controlled vocabulary** for the `subfield` field of notes in that area. If you need a subfield value that is not listed, add it to the index in the same change.

MOC notes do not need `belongs_to`, `subfield` or `cites`.
