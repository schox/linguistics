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

## Body

A `Concept` note answers: what the term means, how it is used, and where its edges are.

```markdown
# <Concept name>

<The definition, in one or two sentences.>

## <Sections named for parts of the subject>
   Phonology's are "Phonemes and allophones", "Notation",
   "Phonotactics". Never "Why this matters here".

## Child topics
   The concepts under this one that should become notes of
   their own. Naming them is how breadth stays visible before
   it is written, and it is where the next batch comes from.

## Open questions
## Sources
```

The six notes under `General-Linguistics/levels-of-analysis.md` are the worked examples; `General-Linguistics/phonology.md` is closest to the intended shape.

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
