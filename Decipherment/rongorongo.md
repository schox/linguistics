---
type: Script
class: undetermined
period: attested from the 19th century CE; date of origin disputed
decipherment_status: undeciphered
status: open
writes:
found_at:
  - "[[Rapa Nui]]"
corpus_size: 25 or 26 authentic objects; c. 14,000 signs; c. 120 base glyphs
subfield:
  - Unsolved, partial and contested
  - Epistemics
belongs_to: "[[Decipherment]]"
related_to:
  - "[[Script versus language]]"
  - "[[The evidentiary threshold and unicity distance]]"
  - "[[Is it writing at all? The Indus entropy debate]]"
cites:
  - "[[Berthin 2024]]"
iso15924: Roro
iso15924_num: 620
unicode_block:
wikidata: Q209764
---

# Rongorongo

The undeciphered sign system of [Rapa Nui](../places/rapa-nui.md), incised on wooden objects. Properly *kohau rongorongo*.

It is the case that should have been solvable and is not, and understanding why is more instructive than the corpus figures alone suggest.

## The corpus

Berthin gives about 120 unique base characters, which combine into hundreds of compound forms, on 25 or 26 authentic wooden slabs and objects, comprising approximately 14,000 signs in total. The surviving objects are tablets, a tablet fragment, an inscribed statuette, a staff, a snuff box and two *rei miro*, the crescent-shaped gorgets.

Set against the vault's other scripts by sign count, rongorongo is not the smallest corpus:

| Script | Sign occurrences |
| --- | --- |
| [Linear B](linear-b.md) | 57,398 |
| Rongorongo | c. 14,000 |
| [Indus](indus-script.md) | 13,372 |
| [Linear A](linear-a.md) | 7,362-7,396 |
| [Phaistos Disc](phaistos-disc.md) | 241 |

**Each figure is its own source's, and they are not strictly commensurable**; treat the ranking as approximate. Even so it makes the point: rongorongo has roughly twice Linear A's text and slightly more than the Indus corpus, and is no closer to being read.

## Why the extra text does not help

Three obstacles, none of which is quantity.

**The corpus boundary is unsettled, because forgery is a live industry.** Objects carrying rongorongo-like glyphs have been produced for sale to visitors since the nineteenth century and still are. Berthin's paper exists to test six objects for authenticity, and he makes an observation that has no parallel elsewhere in the vault: portions of imitations that quote directly from authentic but now-lost texts ought to be *added* to the validated corpus rather than discarded. So the corpus can in principle both shrink and grow under scrutiny, and "how many signs are there" has no settled answer.

**The sign inventory resists counting for a structural reason.** About 120 base glyphs is a plausible syllabary-sized inventory. But the bases fuse into compound forms in the hundreds, and whether a compound is one sign or two is a segmentation decision that changes the inventory, the token count and every frequency statistic computed from them. This is the same problem the [Indus script](indus-script.md) has with variant-splitting, where counts run from 417 to 676 depending on the analyst. See [what counts as one sign](segmentation-and-transcription.md).

**The language is probably known, and that still is not enough.** Unlike Linear A or the Indus corpus, there is a strong candidate: Old Rapanui, an Eastern Polynesian language with living descendants and recorded nineteenth-century texts. Berthin cites Pozdniakov's work treating rongorongo as a glyph syllabary and comparing rank-frequency distributions against the traditional Rapanui poem *Apai*.

That last point deserves emphasis, because it inverts the vault's usual story. Linear B fell because the language beneath turned out to be Greek. Rongorongo has a candidate language of the same order of availability and remains unread, which shows that a known language is necessary and not sufficient. What Linear B also had, and rongorongo does not, was 57,398 signs of administrative text with repeated formulaic structure, and a bilingual-adjacent constraint in the form of place names.

## The reading community was destroyed within the documentary record

This is what separates rongorongo from every other script in this area, and it should be stated plainly rather than gestured at.

Berthin, citing Fischer, records that most rongorongo scribes and cantors were kidnapped or died in the genocide and disease that accompanied the colonization of Rapa Nui, and that by June 1869, when Bishop Tepano Jaussen brought the script to outside notice, few people who could interpret it are presumed to have remained alive.

Elsewhere the vault describes decipherment as facing obscurity that is "an accident of cultural loss", in [adversarial versus accidental encipherment](adversarial-versus-accidental.md). Rongorongo is the case where that phrasing is inadequate. The loss was recent, documented, and caused by identifiable human action, and it happened while European observers were present. The knowledge did not fade; it was destroyed, and the destruction is inside the historical record rather than behind it.

## Reading order

Inverse boustrophedon: reading starts at the lower left, and at the end of each line the object is turned 180 degrees so the next line is read the right way up. Berthin notes that forgers have been known to imitate the layout in reverse, which is one of the tells his method uses.

## Encoding

`iso15924` is `Roro`, numeric 620, assigned 2004-05-01, within the 600-699 range the registry reserves for undeciphered scripts.

**There is no Unicode block**, verified against `Blocks.txt`. As with the Indus script, encoding presupposes a settled sign list, and here the segmentation of compound glyphs is exactly what is unsettled.

## Open questions

- **`period` is weakly founded.** The frontmatter records attestation rather than origin, because no source read here dates the invention of the script. Whether rongorongo predates European contact in 1722 or was stimulated by it is a genuine and consequential dispute, and the vault currently has nothing on it. This is the most important gap in the note.
- **Barthel's and Fischer's corpus editions have not been consulted.** Barthel 1958 established the classification whose numbers run 1 to 799, and Fischer 1997 is the other standard reference. Everything here reaches the vault through Berthin citing them.
- **`class: undetermined`.** Pozdniakov's syllabary hypothesis is reported by Berthin and is not adopted here, on the same reasoning as the Phaistos Disc: an inference from inventory size is not a demonstration.
- **No `Language` note for Rapanui.** Unlike Minoan and Harappan, this is a real, attested, living language, and it belongs in `Human-Languages/` on its own merits rather than as an appendage to a script. It would also give the vault its first Austronesian entry.

## Sources

- [Berthin 2024](../references/berthin-2024.md), for the corpus figures, the authenticity problem, the reading order and the fate of the reading community
- [ISO 15924](../references/iso15924.md), for `Roro` 620, verified against the Unicode Consortium code list
- [Unicode block data](https://www.unicode.org/Public/UNIDATA/Blocks.txt), checked and containing no rongorongo block
- [Wikidata Q209764](https://www.wikidata.org/wiki/Q209764)
