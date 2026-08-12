---
type: Type
aliases:
  - "Language"
_icon: languages
_color: green
_sidebar_label: Languages
_order: 40
_pinned_properties:
  - family
  - status
  - glottocode
family:
branch:
written_in:
era: living
status: interested
subfield:
belongs_to:
related_to:
cites:
glottocode:
iso639_3:
wals_code:
wikidata:
---

# Language

A specific human language. Lives in `Human-Languages/`.

## Fields

- `family`: top-level genealogical family, from the **Family vocabulary** in `Human-Languages/_index.md` (e.g. `Indo-European`, `Tyrsenian`, `Afro-Asiatic`).
- `branch`: the branch within that family (e.g. `Germanic`, `Semitic`). Leave empty for an isolate or a single-member family.
- `era`: `living` | `historical` | `extinct` | `reconstructed`.
- `status`: your relationship to it. `interested` | `learning` | `reference` | `reading` | `fluent`.
- `written_in`: wikilinks to the `Script` notes that record it. **This is the join field.** There is no `script:` field; scripts are notes, not strings.
- `subfield`: from the **Subfield vocabulary** in `Human-Languages/_index.md`, which is a separate list from the family vocabulary.

## Identifiers

Fill wherever they exist; they join the note to external catalogs rather than duplicating them. Leave the key present and empty if you have checked and none exists.

- `glottocode`: Glottolog identifier, e.g. `etru1241`. Resolves at `https://glottolog.org/resource/languoid/id/<code>`.
- `iso639_3`: three-letter code, e.g. `ett`.
- `wals_code`, `wikidata`.

Worked example: `Human-Languages/etruscan.md`.

## Body

A `Language` note answers: whose language it is, where it sits in the family tree, how it is attested, and what it looks like.

```markdown
# <Language name>

<What it is, where and when spoken, living or extinct.>

## Classification
   Family and branch. Contested placements are attributed to
   their proponents, not resolved silently.

## Attestation
   For a corpus language: what survives, from when, in what
   script, and how much. Link the `Script` notes named in
   `written_in`.

## Structure
   A sketch across the levels of analysis: sound system,
   morphology, syntax. Enough to characterize the language,
   not a grammar of it.

## Child topics
## Open questions
## Sources
```

Speaker numbers for a living language carry a date and a source, because the figure moves. Extinct languages take the dagger in prose lists.

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
