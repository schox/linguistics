---
type: Type
_icon: pen-tool
_color: orange
_sidebar_label: Scripts
_order: 45
_pinned_properties:
  - class
  - decipherment_status
  - writes
class:
period:
decipherment_status: undeciphered
writes:
found_at:
corpus_size:
subfield:
belongs_to:
related_to:
cites:
iso15924:
iso15924_num:
unicode_block:
wikidata:
---

# Script

A writing system, which is not the same thing as a language. Cuneiform wrote five unrelated languages; Linear A is a script whose language is unknown; Etruscan is a language readable in a script we can pronounce but do not fully understand.

**Script notes live in `Decipherment/`**, whatever their status, because the script-versus-language argument lives there. This is a filing decision, not a claim that every script is undeciphered.

## Fields

- `class`: `alphabet` | `abjad` | `abugida` | `syllabary` | `logographic` | `mixed` | `undetermined`.
- `decipherment_status`: `deciphered` | `partial` | `contested` | `undeciphered`.
- `writes`: wikilinks to the `Language` notes it records, where known. Inverse of `written_in`.
- `found_at`: wikilinks to `Place` notes for the sites the corpus came from.
- `corpus_size`: free text, e.g. `c. 6,058 inscriptions`. **Record this wherever known.** Corpus size is the variable that decides decipherability, so it is a first-class fact here rather than trivia.

## Identifiers

- `iso15924`: four-letter code, e.g. `Linb` (Linear B), `Lina` (Linear A), `Ital` (Old Italic).
- `iso15924_num`: numeric code. The ranges are a typology in themselves, and 600-699 is reserved for undeciphered scripts.
- `unicode_block`: e.g. `U+10000-U+1007F`.
- `wikidata`.

Worked example: `Decipherment/linear-b.md`.

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
