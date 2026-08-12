---
type: Type
aliases:
  - "Method"
_icon: git-branch
_color: cyan
_sidebar_label: Methods
_order: 55
_pinned_properties:
  - category
  - origin
  - applies_to
category:
origin:
applies_to:
subfield:
belongs_to:
related_to:
cites:
status: open
---

# Method

A technique, manual or computational, that transfers between areas: frequency analysis, Kober's triplets, the index of coincidence, minimum-cost flow alignment.

- `category`: `statistical` | `combinatorial` | `structural` | `contextual` | `computational`.
- `origin`: the field it came from, free text.
- `applies_to`: wikilinks to the areas or problems it is used on.

These are the notes most likely to belong in several areas at once, which is why they are typed rather than filed. Targets of a `Cipher`'s `broken_by` are usually Method notes.

Worked example: `Decipherment/frequency-analysis.md`.

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
