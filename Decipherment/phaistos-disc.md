---
type: Script
aliases:
  - "Phaistos Disc"
class: undetermined
period: 18th-17th centuries BCE, from a disturbed context
decipherment_status: undeciphered
status: open
writes:
found_at:
  - "[[Phaistos]]"
corpus_size: one object; 241 sign-impressions, 45 distinct signs, 61 sign-groups
subfield:
  - Unsolved, partial and contested
  - Epistemics
belongs_to: "[[Unsolved, partial and contested]]"
related_to:
  - "[[The evidentiary threshold and unicity distance]]"
  - "[[Linear A]]"
  - "[[Is it writing at all? The Indus entropy debate]]"
cites:
  - "[[Mnamon]]"
  - "[[Heraklion Archaeological Museum, the Phaistos Disc]]"
iso15924:
iso15924_num:
unicode_block: U+101D0-U+101FF
wikidata: Q465338
---

# Phaistos Disc

A single fired clay disc, impressed on both faces with signs arranged in a spiral, found at the palace of [Phaistos](../places/phaistos.md) on 3 July 1908. It is the limiting case of everything this area argues, and the reason to hold a `Script` note for one object.

## The whole corpus is one object

241 sign-impressions. 45 distinct signs. 61 sign-groups, thirty on one face and thirty-one on the other, separated by incised lines and presumed to be words.

Against the vault's other scripts, this is not a small corpus but a different order of thing:

| Script | Sign occurrences |
| --- | --- |
| [Linear B](linear-b.md) | 57,398 |
| [Indus](indus-script.md) | 13,372 |
| [Linear A](linear-a.md) | 7,362-7,396 |
| Phaistos Disc | 241 |

**These are each source's own totals and are not perfectly comparable**, since the Linear A and Linear B figures come from [Petrolito et al. 2015](../references/petrolito-et-al-2015.md), the Indus figure counts occurrences in Mahadevan's concordance, and 241 is the count of impressions on this object from the museum that holds it. The comparison is an order-of-magnitude one. At that resolution it still holds: the Disc has roughly one thirtieth of Linear A's text and one two-hundredth of Linear B's.

With 45 distinct signs over 241 tokens, most signs appear a handful of times and the longest repeated sequence is short. There is no quantity of internal structure to work with, and no second document to test a hypothesis against.

## Why it cannot be deciphered, as opposed to has not been

Most undeciphered scripts are open problems. This one is closed by argument, and the specialist statement of that is worth quoting exactly. Del Freo, writing the Mnamon entry, notes that many decipherment attempts have been made "but none can be considered conclusively valid, since in the absence of similar inscriptions, no proposed decipherment can be verified."

That is [the evidentiary threshold](evidentiary-threshold-and-unicity-distance.md) reached independently, in a specialist reference work, without invoking Shannon. A proposed reading of 241 signs cannot be falsified because there is nothing to falsify it against. Barber's threshold and Shannon's unicity distance both say that below a certain quantity of text, multiple mutually inconsistent readings fit the evidence equally well and no method distinguishes them. The Disc is the cleanest empirical instance of that in the vault, and its steady supply of confident decipherments is the predicted consequence rather than a curiosity.

The contrast with [Linear A](linear-a.md) is instructive. Linear A is undeciphered and might not stay that way, because 1,427 documents leave room for the corpus to grow or for a related script to supply values. The Disc has no such route unless a second inscribed object turns up.

## What the signs are, and what they are not

**Made with types, not drawn.** The signs were stamped into fresh clay using pre-prepared forms before firing. Each occurrence of a sign is therefore identical to every other, which is a manufacturing fact with two consequences: it makes sign identification unusually secure, and it means whoever made the Disc had a set of reusable stamps and so presumably more than one thing to write with them. That second implication is not evidence of anything on its own, but it is the strongest reason to think this was not a one-off.

**Class is `undetermined`.** Del Freo reports the standard inference: 45 signs are too many for an alphabet and too few for a logographic system, so a syllabary is the natural reading, in line with Cretan Hieroglyphic, Linear A and Linear B. That is an argument from inventory size, not a demonstration, so the frontmatter does not record it as fact. Mnamon is equally clear that similarities with other Cretan sign systems "are very uncertain and do not show any definite relationship with these graphic systems".

**Direction.** A vertical line with five dots at the outer edge of each face marks the start, and reading runs from the rim inward. Del Freo gives the sequence as right to left.

## Encoded but not recognized as a script

The registry situation is a small oddity worth recording precisely, because it says something about how the standards bodies treat a corpus of one.

- **Unicode has a block**: `101D0..101FF; Phaistos Disc`, verified in `Blocks.txt`.
- **Unicode has no script property value** for it. `PropertyValueAliases.txt` lists `Cpmn` for Cypro_Minoan and `Cprt` for Cypriot, and nothing for Phaistos.
- **ISO 15924 has no code**, verified against the Unicode Consortium's code list.

So the characters are encoded, and the writing system is not registered as one. `iso15924` and `iso15924_num` are empty here because no code exists, not because none was looked up. Q2493875 is the Wikidata item for the Unicode block; Q465338, in the frontmatter, is the object.

## Open questions

- **Dating rests on a disturbed context.** Del Freo gives 18th-17th centuries BCE while noting the Disc "comes from a disturbed context and is therefore very difficult to date stratigraphically", and the Mnamon heading carries an explicit question mark over the second millennium attribution. Pernier's own excavation report is the document that would establish what was actually found with it.
- **Authenticity has been questioned and is not examined here.** The suggestion that the Disc is a modern forgery has been raised periodically and is generally rejected, but no source read here argues the case either way. Given that the vault's whole treatment rests on a single object, this deserves a sourced paragraph rather than a sentence.
- **The "hymn or incantation" reading is the museum's**, offered on the strength of repeated sign-groups. It is recorded in the reference note and not adopted, and no scholarly assessment of it was read.
- **Cretan Hieroglyphic has no note yet.** It is the third Aegean script of the period and the natural comparison for both this and [Linear A](linear-a.md). Mnamon covers it.

## Sources

- [Mnamon](../references/mnamon.md), Phaistos Disc entry edited by Maurizio Del Freo, for the sign count, dating, production method and the unverifiability argument
- [Heraklion Archaeological Museum](../references/heraklion-museum-phaistos-disc.md), for the discovery, the 241 impressions and the 61 groups
- [Unicode block data](https://www.unicode.org/Public/UNIDATA/Blocks.txt) and [script property aliases](https://www.unicode.org/Public/UNIDATA/PropertyValueAliases.txt), for the block and the absent script value
- [ISO 15924](../references/iso15924.md), checked and containing no Phaistos entry
- [Wikidata Q465338](https://www.wikidata.org/wiki/Q465338)
