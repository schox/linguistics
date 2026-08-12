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

A map-of-content (index) note. Two kinds share the type:

**Folder indexes.** Every folder holding files has one, named `_index.md`, including `types/`, `scripts/`, `people/`, `places/` and `references/`. It lists and links the files and subfolders inside the folder, and embeds any images that originated there. An area `_index.md` does double duty: it is also the **controlled vocabulary** for the `subfield` field of notes in that area. If you need a subfield value that is not listed, add it to the index in the same change.

**Subfield hubs.** One per subfield vocabulary value, kebab-case filename, titled with the value exactly (`levels-of-analysis.md`, titled `Levels of analysis`). A hub sits between the area hub and its subfield's notes in the `belongs_to` chain, carries `subfield` naming itself and `belongs_to` the area hub, and lists its member notes. Most are stubs until the breadth program reaches them; a stub says so in its body.

MOC notes do not need `belongs_to`, `subfield` or `cites`, though subfield hubs carry the first two.

## Body

**Subfield hubs** take a fixed shape, already used by the 49 existing hubs:

```markdown
# <Subfield value, spelled exactly as the area index spells it>

<Scope in a sentence or two: what belongs under this hub.>

## Topics owed to this hub
   The topics that should become notes, from the area index.

## Notes in this subfield
   The notes carrying this subfield value. A stub says "Stub
   hub" here, so the graph cannot be mistaken for coverage.
```

**Folder indexes** list and link the files and subfolders in their folder, and embed the images that originated there. Area indexes additionally carry the controlled `subfield` vocabulary, which is the one part of any MOC that other files depend on: `scripts/check-vault.py` reads that list verbatim.

MOC notes carry no `## Sources`, because they assert nothing. A hub that finds itself arguing has content in it, and the content belongs in a note.
