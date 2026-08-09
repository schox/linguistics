---
type: Type
_icon: user
_color: violet
_sidebar_label: People
_order: 35
_pinned_properties:
  - field
  - known_for
  - born
born:
died:
field:
known_for:
key_works:
worked_at:
viaf:
orcid:
wikidata:
---

# Person

A seminal figure in one of the vault's areas: a brief biography, what they are known for, their key works, and links out.

People are the strongest cross-area join in this vault. Method transfer between cryptanalysis and decipherment, or between linguistics and computer science, is often a matter of biography rather than analogy, and `field` taking more than one value is the signal that a person is doing that work.

## Inclusion test

Not every author of every cited paper. A person earns a note if **at least one** of these holds:

1. They are cited or discussed in two or more notes.
2. Their name is the standard label for a method, result or principle (Kasiski examination, Kober's triplets, Kerckhoffs's principle, the Chomsky hierarchy).
3. They bridge two or more areas of the vault.

Otherwise they stay as an author string in the `authors` field of a `Reference` note. Authorship alone does not earn a note.

## Identifiers

- `viaf`: Virtual International Authority File, the library-standard identifier, best for historical figures.
- `orcid`: for living researchers.
- `wikidata`: Q-number, the universal fallback.

Use `worked_at` to link the `Place` notes where they did the relevant work.

## Living people

Notes on living people stick to documented professional contribution, sourced. No unsourced biographical claim, no health or personal-life detail, no political characterisation. If a fact cannot be verified now, leave it out and say so in the note rather than reproducing what you remember.
