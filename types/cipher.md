---
type: Type
aliases:
  - "Cipher"
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

## Body

A `Cipher` note answers: what the algorithm does, what breaks it, and where it sits historically.

```markdown
# <Cipher name>

<What kind of cipher it is, and when it appeared.>

## How it works
   The mechanism, with a worked example on a short plaintext.

## Cryptanalysis
   What defeats it, and what that costs in text or computation.
   Link the `Method` notes named in `broken_by`.

## History and use
   Who used it, when, and what displaced it.

## Open questions
## Sources
```

**Worked examples use obviously fictitious keys and plaintexts.** Real keys, passwords, tokens and seed phrases never enter this vault, in any note, in any form, however illustrative. See the intake rules in `CONVENTIONS.md`.

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
