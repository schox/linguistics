---
type: Type
aliases:
  - "Place"
_icon: map-pin
_color: amber
_sidebar_label: Places
_order: 37
_pinned_properties:
  - kind
  - flourished
  - country
kind: institution
country:
region:
flourished:
coordinates:
wikidata:
geonames:
pleiades:
ror:
---

# Place

A seminal place: an institution where expertise concentrated, or a site that produced the evidence.

Two kinds matter here and they sit at opposite ends of the same process.

- **Institutions** are where interpretation happens: Bletchley Park, the Max Planck Institute at Leipzig, a university department. Linked from `Person` notes via `worked_at`.
- **Sites** are where the material comes from: Knossos, Ugarit, Behistun, Mohenjo-daro. Linked from `Script` and corpus notes via `found_at`.

The distinction matters more than it looks. In this vault the size of a surviving corpus is the variable that decides whether a script can be read at all, and corpus size is set by excavation. Sites are therefore causally upstream of the central argument in Decipherment, not background color.

`kind`: institution | site | region | facility.
`flourished`: the period when the place mattered, which is usually narrower than its existence.

## Inclusion test

As with `Person`, not everywhere. A place earns a note if at least one holds:

1. Expertise concentrated there in a way that explains a breakthrough.
2. It is the provenance of a significant corpus.
3. It is referenced from two or more notes.

Not every university anyone attended, and not every find-spot.

## Identifiers

- `wikidata`: Q-number, universal fallback.
- `geonames`: modern geographic identifier.
- `pleiades`: the community gazetteer of ancient places, the right identifier for archaeological sites.
- `ror`: Research Organization Registry, the standard identifier for research institutions.
