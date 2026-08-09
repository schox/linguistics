---
type: Script
class: mixed
period: c. 1450-1200 BCE
decipherment_status: deciphered
status: open
writes:
  - "[[Mycenaean Greek]]"
found_at:
  - "[[Knossos]]"
corpus_size: c. 6,058 inscriptions, of which some 5,000 tablets
subfield:
  - Solved decipherments
  - The problem space
belongs_to: "[[Decipherment]]"
related_to:
  - "[[Linear A]]"
  - "[[Script versus language]]"
  - "[[The evidentiary threshold and unicity distance]]"
cites:
  - "[[Ventris and Chadwick 1953]]"
  - "[[Chadwick 1958]]"
  - "[[Salgarella and Castellan 2020]]"
iso15924: Linb
iso15924_num: 401
unicode_block: U+10000-U+1007F (syllabary), U+10080-U+100FF (ideograms)
wikidata:
---

# Linear B

The script of Mycenaean administration, about 87 syllabic signs and over 100 ideographic signs, used from roughly 1450 to 1200 BCE. Deciphered by Michael Ventris in 1952, with [John Chadwick](../people/john-chadwick.md).

`class` is `mixed`, not `syllabary`. Salgarella and Castellan state that "both Linear A and Linear B are logo-syllabic writing systems", consisting of syllabograms for open syllables and logograms standing for whole words or concepts. The sign counts in the first sentence say the same thing: a script with more ideographic signs than syllabic ones is not a syllabary. This note previously said `syllabary` and so contradicted its own opening line while disagreeing with [Linear A](linear-a.md), which is classified from the same source.

Both remain syllabaries in ordinary speech, and the vault's enum has no `logo-syllabic` value. `mixed` is the closest available and the distinction that matters (phonetic signs plus semantic signs, in one system) is preserved in prose.

## Why it was solvable

Three conditions held simultaneously, and their conjunction is rare.

**Corpus.** Around 6,058 inscriptions survive, some 5,000 of them tablets, from Knossos, Pylos, Thebes, Mycenae, Kydonia and elsewhere. That is enough text for distributional argument to bite.

**Structure recoverable without meaning.** [Alice Kober](../people/alice-kober.md) demonstrated inflection from the distribution alone, without assigning a single sound value, building the sign relationships that became Ventris's grid. See [frequency analysis](frequency-analysis.md).

**A known language underneath.** The language turned out to be Greek, which meant an entire comparative apparatus was waiting once the identification was granted. This is the *different script, same language* case.

Compare [Linear A](linear-a.md), which shares the second condition partly (Linear B supplies probable values for many signs) and fails the other two. Around 1,427 documents and no identified language. The contrast is the cleanest available illustration of [the evidentiary threshold](evidentiary-threshold-and-unicity-distance.md): the same scholars, the same island, the same script family, and one is read while the other is not, largely because of what survived.

## Sources

- [Linear B, Wikipedia](https://en.wikipedia.org/wiki/Linear_B)
- [Chadwick 1958](../references/chadwick-1958.md), *The Decipherment of Linear B*
- [Salgarella and Castellan 2020](../references/salgarella-castellan-2020.md), for the logo-syllabic classification
- [ISO 15924](../references/iso15924.md) for the script code
