---
type: Script
aliases:
  - "Egyptian hieroglyphs"
class: mixed
period: in use until 394 CE; start date not sourced here
decipherment_status: deciphered
status: open
writes:
  - "[[Egyptian]]"
found_at:
  - "[[Rosetta]]"
corpus_size: vast and not usefully counted; see the note below on why that matters
subfield:
  - Solved decipherments
  - The problem space
belongs_to: "[[Decipherment]]"
related_to:
  - "[[Script versus language]]"
  - "[[The evidentiary threshold and unicity distance]]"
  - "[[Linear B]]"
  - "[[Jean-François Champollion]]"
cites:
  - "[[Dalby 2019]]"
iso15924: Egyp
iso15924_num: 050
unicode_block: U+13000-U+1342F
wikidata: Q132659
---

# Egyptian hieroglyphs

The monumental script of ancient Egypt, deciphered by Jean-François Champollion in the 1820s, and the case every later decipherment is measured against. It is also the case most often misdescribed, because the popular story compresses twenty-three years of work into one object.

## What actually broke it

Not the Rosetta Stone alone. Dalby's account gives the sequence, and the useful thing about it is the dates.

| Year | Step |
| --- | --- |
| 1761 | Barthélemy suggests that cartouches enclose proper names |
| 1797 | Zoëga suggests foreign names in hieroglyphic might be written phonetically |
| 1799 | The stone is recognized as carrying three versions of one text |
| 1802 | Silvestre de Sacy and Åkerblad show the **demotic** spells foreign names phonetically; Åkerblad publishes 29 demotic letters, more than half correct |
| 1803 | First full translation of the Greek text |
| 1814-1819 | [Thomas Young](../people/young.md) shows the **hieroglyphic** does the same, reads `p t o l m e s` in a cartouche, and finds as many as 80 similarities between hieroglyphic and demotic |
| 1822 | Champollion reads `k l e o p a t r a` from the Philae obelisk and publishes an alphabet of phonetic hieroglyphs in the *Lettre à M. Dacier* |
| 1823 | Champollion confirms that phonetic signs also spell **native** Egyptian names, identifying Ramesses and Thutmose at Abu Simbel |

Twenty years separate the Greek translation from the announcement, and a further year from the step that mattered most.

**The decisive move was 1823, not 1822.** Up to that point the phonetic principle could be dismissed as a Ptolemaic device for writing Greek names that Egyptian had no signs for, leaving the native script symbolic as tradition held. Ramesses and Thutmose are Egyptian names, spelled phonetically, on monuments centuries older than any Greek in Egypt. That killed the symbolic reading and made the script a writing system rather than a code of ideas.

## The bilingual is not what people think

The Rosetta Stone is a bilingual in the sense that matters, and it was still not a key in the sense the phrase implies.

Dalby: "The fact that the three versions cannot be matched word for word helps to explain why the decipherment has been more difficult than originally expected, especially for those original scholars who were expecting an exact bilingual key to Egyptian hieroglyphs."

Which of the three is the original is itself disputed. Letronne argued in 1841 for the Greek. John Ray holds that "the hieroglyphs were the most important of the scripts on the stone: they were there for the gods to read, and the more learned of their priesthood". Derchain and Thissen argue all three were composed simultaneously; Quirke sees "an intricate coalescence of three vital textual traditions". None of that is settled here, and the vault should not describe the Stone as a translation with a known direction.

The lesson for the rest of this area is that a bilingual supplies constraint, not a dictionary. What it gave was a bounded set of places where known names had to occur, which is why cartouches did the work.

## The three things it had that the unread scripts do not

Set against [Linear A](linear-a.md), the [Indus script](indus-script.md), [rongorongo](rongorongo.md) and the rest, Egyptian had all three of the conditions the vault keeps identifying as necessary, and this is the only script here that had them together.

1. **A vast corpus**, on monuments, papyri and tomb walls, over three thousand years. `corpus_size` is recorded as uncountable rather than given a number, and that is the point: the variable that binds every other script in this area stops binding here.
2. **A known language underneath.** [Egyptian](../Human-Languages/egyptian.md) survived as Coptic, in liturgical use and readable. Dalby records that medieval Arab scholars, Dhul-Nun al-Misri and Ibn Wahshiyya in the ninth and tenth centuries, had already tried comparing hieroglyphs with the Coptic spoken by priests around them.
3. **Proper names locatable in the text.** Cartouches marked them typographically, and the Greek said which names to expect.

Linear B had the first and second and no third, and took until 1952. Linear A has none of them.

## The obstacle was a theory

Worth recording because it is not a shortage of evidence, which is what this area usually diagnoses.

Hieroglyphs kept their pictorial appearance, and classical authors emphasized it. Horapollo's *Hieroglyphica*, from the fifth century, explained almost 200 glyphs symbolically and was believed authoritative. Dalby's judgment is that it "was misleading in many ways, and this and other works were a lasting impediment to the understanding of Egyptian writing". Kircher in the seventeenth century worked within the same tradition and got nowhere; he called the problem the riddle of the Sphinx.

So the script was unread for roughly fourteen centuries with an abundant corpus, a surviving descendant language and no shortage of scholars. What was missing was the idea that the signs might spell sounds. That is a different failure mode from the [evidentiary threshold](evidentiary-threshold-and-unicity-distance.md), and the vault should hold both: a decipherment can be blocked by too little evidence or by a wrong theory, and only the first is a property of the corpus.

## When it stopped being read

Use of hieroglyphs narrowed through the later Pharaonic period, and by the fourth century CE few Egyptians could read them. Monumental use ceased after Theodosius I ordered the closing of all non-Christian temples in 391. The last known inscription is dated 24 August 394, found at Philae and known as the Graffito of Esmet-Akhom.

## Encoding

`iso15924` is `Egyp`, numeric 050, Unicode alias `Egyptian_Hieroglyphs`, dated 2009-06-01. The related scripts have their own codes: `Egyh` 060 for hieratic, `Egyd` 070 for demotic, `Copt` 204 for Coptic.

Unicode blocks, all verified against `Blocks.txt`: Egyptian Hieroglyphs U+13000-U+1342F, Egyptian Hieroglyph Format Controls U+13430-U+1345F, and Egyptian Hieroglyphs Extended-A U+13460-U+143FF. The frontmatter records the first only, since the schema has one field.

The contrast with phase 1 is stark. Three blocks and four script codes for the Egyptian complex, against no block at all for the Indus script or rongorongo. Encoding follows a settled sign list, and a settled sign list follows decipherment. See [what counts as one sign](segmentation-and-transcription.md).

## Open questions

- **No start date.** `period` records only the end, because no source read here dates the earliest hieroglyphs. This is a large gap for a script whose antiquity is part of its significance.
- **Hieratic and demotic have no notes**, though both have ISO 15924 codes and demotic is on the Rosetta Stone. The relationship between the three, and Young's finding of 80 shared signs between hieroglyphic and demotic, would be better carried by a note that covers the complex rather than by this one.
- **Champollion's own publications have not been read.** The *Lettre à M. Dacier* (1822) and the posthumous grammar and dictionary are the primary record, and everything here is Dalby's account of them.
- **The corpus is described as uncountable and never bounded.** Some estimate of surviving inscribed material would let the comparison with the unread scripts be quantitative rather than rhetorical, which is what the vault does everywhere else.
- **The British Museum record was not reachable**, returning 403, so the object description in [Rosetta](../places/rosetta.md) comes from Dalby rather than from the holding institution.

## Sources

- [Dalby 2019](../references/dalby-2019.md), for the decipherment sequence, the credit dispute, the Horapollo tradition and the end of hieroglyphic use
- [ISO 15924](../references/iso15924.md), for `Egyp` 050 and the related codes, verified against the Unicode Consortium code list
- [Unicode block data](https://www.unicode.org/Public/UNIDATA/Blocks.txt), for the three Egyptian blocks
- [Wikidata Q132659](https://www.wikidata.org/wiki/Q132659)
