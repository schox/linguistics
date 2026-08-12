---
type: Type
aliases:
  - "ComputerLanguage"
_icon: terminal
_color: indigo
_sidebar_label: Computer Languages
_order: 50
_pinned_properties:
  - paradigm
  - first_appeared
  - status
paradigm:
lineage:
first_appeared:
status: reference
influenced_by:
implemented_in:
subfield:
belongs_to:
related_to:
cites:
hopl_id:
wikidata:
---

# ComputerLanguage

A programming, markup, query or formal language. Lives in `Computer-Languages/`.

## Fields

- `paradigm`: free text, may be several, e.g. `functional, procedural, reflective`.
- `lineage`: the descent group, e.g. `Lisp`, `ALGOL`, `ML`, `C`, `Smalltalk`.
- `first_appeared`: year.
- `status`: `using` | `reference` | `historical` | `learning`.
- `influenced_by`: wikilinks to other `ComputerLanguage` notes. The computed inverse gives the influence graph, mirroring what HOPL records.
- `implemented_in`: wikilinks for compiler bootstrapping, the relation languagelineage.org records. Distinct from influence.

## Identifiers

- `hopl_id`: entry in the Online Historical Encyclopaedia of Programming Languages.
- `wikidata`.

Worked example: `Computer-Languages/lisp.md`.

## Body

A `ComputerLanguage` note answers: what the language is for, what it looks like, where it came from, and what it changed.

```markdown
# <Language name>

<What it is, when it appeared, and who designed it.>

## Design
   The model of computation, the type discipline, and the
   syntax in a short example.

## Lineage
   What it descends from and what descends from it.
   `lineage` and `influenced_by` carry the same relation in
   frontmatter; the prose says what was actually inherited.

## Implementation
   Compilation or interpretation, and notable implementations.

## Reception and use
   What it was adopted for, and what it displaced.

## Child topics
## Open questions
## Sources
```

The comparison with human language is a topic to be argued in its own note, not a metaphor to reach for in this one.

## Fields required on every content note

These are mandatory and are checked by `scripts/check-vault.py`:

```yaml
subfield:                  # one or more values from the owning area's _index.md
  - Some Subfield
belongs_to: "[[Area Hub]]" # exactly one area hub, quoted
status: open               # open | draft | settled
```

Optional but usual: `related_to` (lateral links), `cites` (Reference notes this note draws on).

**Wikilink values must be quoted.** `belongs_to: "[[Cryptography]]"` is a string; `belongs_to: [[Cryptography]]` is a nested YAML list and silently fails. Always use double quotes.
