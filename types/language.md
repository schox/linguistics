---
type: Type
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
script:
era: living
status: interested
glottocode:
iso639_3:
wals_code:
wikidata:
---

# Language

A specific human language. `family` and `branch` place it genealogically, which is the canonical spine of the Human Languages area.

Era: living | historical | extinct | reconstructed.
Status: interested | learning | reference | reading | fluent.
Use `written_in` to link the `Script` notes that record it.

## Identifiers

Fill these wherever they exist. They are what join a note to the external catalogs rather than duplicating them.

- `glottocode`: Glottolog's stable identifier for the languoid, e.g. `stan1293`. Resolves at `https://glottolog.org/resource/languoid/id/<code>`.
- `iso639_3`: the three-letter ISO code, e.g. `deu`.
- `wals_code`: WALS language code, where the language is covered.
- `wikidata`: Q-number, the universal join key across everything else.
