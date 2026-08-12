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
