---
type: Type
aliases:
  - "Script"
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

- `class`: `alphabet` | `abjad` | `abugida` | `syllabary` | `logosyllabary` | `mixed` | `undetermined`. The standard categories are defined in [Script typology](../General-Linguistics/script-typology.md), from three classifications that do not fully agree; the note says where they diverge. Two of the values below are local terms and are marked as such, because no source consulted uses either as a category name.
  - `alphabet`, `abjad`, `abugida`, `syllabary`: standard, and defined in that note.
  - `logosyllabary`: signs write words or morphemes, with subsidiary use for syllabic sound. This is the Unicode Standard's term, adopted here in preference to `logographic` because pure logography is not attested at scale: every system so labeled also writes sound.
  - `mixed`: **local term.** One script whose signs are of more than one kind, where no single standard category fits. Do not reach for it first. Where the script writes words or morphemes alongside phonetic signs, `logosyllabary` is the standard answer and is preferred. Note also that Unicode's "composite system" is *not* the equivalent: that describes one language's writing using several scripts, as Japanese uses Han, two kana and Latin, which is a different claim.
  - `undetermined`: **local term.** The type has not been established. This is **not** the same as `decipherment_status: undeciphered`, and the two vary independently: Cypro-Minoan is recorded as a syllabary that nobody can read. Use `undetermined` where sign inventory and structure do not settle the type, and say in the note what would.

  **`featural` is deliberately absent.** It is a standard category in both sources, applied to Hangul, and no note here needs it. Add the value with the first note that does, rather than carrying a value nothing uses.
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

## Body

A `Script` note answers: what the signs are, what they wrote, how much survives, and how far it can be read.

```markdown
# <Script name>

<What kind of writing system it is, its period, and its status.>

## The signs
   Inventory size, sign classes, direction of writing, and what
   a sign is taken to be. Say who segmented the corpus: that is
   a decision taken before any statistic, not an observation.

## The corpus
   How much survives, on what, from where. `corpus_size` and
   `found_at` carry the same facts in frontmatter; the prose
   says what the figures are counts of and which are derived.

## The language, or the question of it
   What it writes, or why that is unknown. Link the `Language`
   notes named in `writes`.

## Decipherment
   What is read, what is not, and on what evidence. Attribute
   contested readings to their proponents.

## Encoding
   ISO 15924, Unicode block, or the recorded absence of either.

## Child topics
## Open questions
## Sources
```

Do not name a section for the script's relevance to the vault. "Why it was solvable" is a heading for a synthesis note; in a `Script` note that material is described under `## Decipherment`.

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
