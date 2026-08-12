---
type: Type
aliases:
  - "Concept"
_icon: lightbulb
_color: purple
_sidebar_label: Concepts
_order: 30
_pinned_properties:
  - subfield
  - related_to
subfield:
belongs_to:
related_to:
cites:
status: open
---

# Concept

A term or idea worth its own note: a linguistic concept (phoneme, isogloss), a computing concept (type system, parser), a cryptographic concept (unicity distance, nonce), or a decipherment concept (evidentiary threshold, quasi-bilingual).

Lives in the area folder it most belongs to. Cross-cutting concepts are additionally listed in `_junctions.md`.

Worked example: `Decipherment/evidentiary-threshold-and-unicity-distance.md`.

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
