---
type: Type
_icon: lock
_color: rose
_sidebar_label: Ciphers
_order: 60
_pinned_properties:
  - era
  - category
era:
category:
first_described:
status: reference
broken_by:
subfield:
belongs_to:
related_to:
cites:
wikidata:
---

# Cipher

A cipher, cryptographic algorithm or system. Lives in `Cryptography/`.

## Fields

- `category`: `classical` | `mechanical` | `symmetric` | `asymmetric` | `hash` | `protocol`.
- `era`: broad period, from this list: `ancient` | `medieval` | `early modern` | `industrial` | `mechanical` | `computer` | `post-quantum`. Use `first_described` for the actual year.
- `first_described`: year or approximate year, e.g. `1553`.
- `status`: `reference` (studied here) | `historical` (obsolete) | `current` (in live use) | `broken`.
- `broken_by`: wikilinks to the `Method` or `Person` notes that defeated it. No external catalog supplies this, so it is original structuring work. See `_data-sources.md`.

## Identifiers

- `wikidata` only. There is no domain-specific identifier scheme for ciphers.

Worked example: `Cryptography/vigenere-cipher.md`.

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
