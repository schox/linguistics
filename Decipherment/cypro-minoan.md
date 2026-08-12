---
type: Script
aliases:
  - "Cypro-Minoan"
class: syllabary
period: late 16th to 11th century BCE
decipherment_status: undeciphered
status: open
writes:
found_at:
  - "[[Enkomi]]"
corpus_size: 243 inscriptions in Ferrara's catalog, most very short; 83 graphemes
subfield:
  - Unsolved, partial and contested
  - The problem space
belongs_to: "[[Unsolved, partial and contested]]"
related_to:
  - "[[Linear A]]"
  - "[[Linear B]]"
  - "[[Script versus language]]"
  - "[[The evidentiary threshold and unicity distance]]"
cites:
  - "[[Ferrara 2013]]"
  - "[[Olivier 2007]]"
  - "[[Mnamon]]"
  - "[[Donnelly 2025]]"
iso15924: Cpmn
iso15924_num: 402
unicode_block: U+12F90-U+12FFF
wikidata: Q1751985
---

# Cypro-Minoan

The undeciphered script of Late Bronze Age Cyprus, in use from the late 16th to the 11th century BCE. Descended from or influenced by [Linear A](linear-a.md), and ancestral to the Cypriot syllabary that was later read because it wrote Greek.

That last point makes Cypro-Minoan the most tantalizing case in the vault. It sits between a script we cannot read and a script we can, in a direct line of descent, and it is still not readable.

## The corpus, and an argument about how to count it

[Ferrara's 2013 corpus](../references/ferrara-2013.md) catalogs 243 inscriptions, numbered ##001-243, of which 27 are additions to [Olivier's *HoChyMin*](../references/olivier-2007.md), the 2007 edition whose numbering the field still uses. Cannavò, writing the Mnamon entry, describes the corpus as "little more than two hundred" inscriptions, mostly very short.

The conventional classification, devised by Masson and kept by Olivier, splits these into subgroups:

| Subgroup | Content |
| --- | --- |
| CM0 | a single tablet from [Enkomi](../places/enkomi.md), late 16th century BCE, 23 signs |
| CM1 | the bulk of the material, across the Late Bronze Age on varied media |
| CM2 | three fragmentary tablets from Enkomi, 13th-12th century BCE |
| CM3 | texts from Ugarit, 13th century BCE |

**Whether those are one script or several is the live question, and it is not a taxonomic quibble.** Ferrara's Appendix 2 treats the repertory as "83 different graphemes of a single writing system", which cuts against reading CM1, CM2 and CM3 as separate scripts.

The consequence is arithmetical. A single corpus of 243 short inscriptions is already far below the threshold at which a decipherment could be tested. Split three ways it becomes three corpora of a few dozen each, and each of those is closer to the [Phaistos Disc](phaistos-disc.md) than to [Linear A](linear-a.md). How you classify the material determines whether there is anything to work on, which is an unusually direct case of a methodological decision setting the evidentiary limit. It is the corpus-level form of the problem set out in [what counts as one sign](segmentation-and-transcription.md). See [the evidentiary threshold](evidentiary-threshold-and-unicity-distance.md).

## Why a readable descendant does not help

The Cypriot syllabary, ISO 15924 `Cprt`, is deciphered: it wrote Arcadocypriot Greek, and bilinguals with Phoenician made it readable. It is the *different script, same language* case that also describes [Linear B](linear-b.md), and it is the tractable one.

Cypro-Minoan is its ancestor and remains unread, because descent supplies sign shapes and not sound values, and because the language underneath is unknown. `writes` is empty for that reason. Eteocypriot, attested later in the readable Cypriot syllabary but itself not understood, is the usual candidate, and the vault does not assert it.

This is the same structure as Linear A against Linear B, one generation removed and in the opposite direction: there, a descendant script supplies probable values for an unread ancestor; here, the descendant is readable and still does not deliver the ancestor. Two attempts at the same trick, both failing for the same reason, which is that a script is not a language.

## A possible explanation for the shortness, not yet adopted

[Donnelly 2025](../references/donnelly-2025.md), a current single-volume treatment that this vault has not been able to read, offers a causal account of the corpus's character rather than a description of it. Her abstract states that Cypro-Minoan has "few clay tablets, characteristic of neighboring scribal-based, administrative writing traditions", and that "Cypro-Minoan writers wrote on mercantile objects, outside of scribal schools".

If that holds, the corpus is short and scattered because of who was writing and why, not because of what happened to survive. That would make Cypro-Minoan different in kind from [Linear A](linear-a.md) and the [Indus script](indus-script.md), where the vault treats the constraint as preservation and excavation: here the evidentiary limit would have been set at the moment of inscription, by a writing practice that produced portable mercantile objects rather than palatial archives.

It is recorded as a reported position and not adopted, because the volume is paywalled and only the abstract has been read.

## Findspots

Principally Cyprus, and Enkomi above all: CM0 is a single tablet from there and CM2 is three tablets from there. CM3 comes entirely from [Ugarit](../places/ugarit.md) on the Syrian coast, which places the script in the eastern Mediterranean trade network rather than on Cyprus alone. Reviews of Ferrara also mention material from Maroni, Palaepaphos and Tiryns.

## Open questions

- **No per-site breakdown of the 243.** As with the [Indus script](indus-script.md), the corpus is described in aggregate and by subgroup rather than by findspot, so `found_at` lists only Enkomi, where the tablets are securely attributed. Maroni, Palaepaphos and Tiryns would all deserve entries under a fuller accounting. [Ugarit](../places/ugarit.md) now has one.
- **The single-system claim is taken at second hand.** Neither volume of Ferrara has been read; the 243, the 27 additions and the 83 graphemes all come from Petrakis's review. The claim that these are variants of one writing system is the most consequential thing in this note and it deserves to rest on the book.
- **HoChyMin's bibliographic details are provisional.** See the caveat in [Olivier 2007](../references/olivier-2007.md); no catalog record was reached.
- **`class: syllabary` follows Mnamon and Wikidata**, and the ISO 15924 French name is *syllabaire chypro-minoen*. It has not been demonstrated by decipherment, and the same caution applies as to the Phaistos Disc, though here the descent from Linear A and to the Cypriot syllabary makes the classification considerably better founded.

## Sources

- [Ferrara 2013](../references/ferrara-2013.md), the current corpus, via Petrakis's review
- [Olivier 2007](../references/olivier-2007.md), *HoChyMin*, the reference numbering
- [Mnamon](../references/mnamon.md), Cypro-Minoan entry edited by Anna Cannavò, for the subgroups, dating and corpus size
- [ISO 15924](../references/iso15924.md), for `Cpmn` 402 and `Cprt` 403, verified against the Unicode Consortium code list
- [Unicode block data](https://www.unicode.org/Public/UNIDATA/Blocks.txt), for U+12F90-U+12FFF
- [Wikidata Q1751985](https://www.wikidata.org/wiki/Q1751985)
