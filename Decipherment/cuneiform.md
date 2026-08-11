---
type: Script
class: mixed
period: c. 2350 BCE to c. 100 CE for Akkadian cuneiform; earlier for Sumerian
decipherment_status: deciphered
status: open
writes:
  - "[[Akkadian]]"
  - "[[Sumerian]]"
found_at:
  - "[[Behistun]]"
corpus_size: very large; tens of thousands of tablets from Ashurbanipal's library alone
subfield:
  - Solved decipherments
  - Epistemics
belongs_to: "[[Decipherment]]"
related_to:
  - "[[Script versus language]]"
  - "[[The evidentiary threshold and unicity distance]]"
  - "[[Egyptian hieroglyphs]]"
  - "[[What counts as one sign]]"
cites:
  - "[[Torres Torres 2007]]"
  - "[[Mnamon]]"
iso15924: Xsux
iso15924_num: 020
unicode_block: U+12000-U+123FF
wikidata: Q401
---
# Cuneiform

The wedge-shaped script of Mesopotamia, invented for [Sumerian](../Human-Languages/sumerian.md) and adapted for [Akkadian](../Human-Languages/akkadian.md) and many other languages. Deciphered across the nineteenth century, and formally accepted as deciphered on 29 May 1857 by a procedure this vault should care about more than the decipherment itself.

`writes` lists two languages and understates the case. Cuneiform is the standing example in `CONVENTIONS.md` for why `Script` and `Language` are separate types, because one script carried Sumerian, Akkadian, Elamite, Hittite, Old Persian and others across three thousand years. The two notes here are the ones the vault has written, not the full list.

## What actually broke it: names first, again

The pattern from [Egyptian hieroglyphs](egyptian-hieroglyphs.md), the script of the [Egyptian](../Human-Languages/egyptian.md) language, repeats with different materials, and the repetition is the point.

[Grotefend's](../people/grotefend.md) work bore fruit in **1802**, twenty years before Champollion's *Lettre*, and it started from royal names with no bilingual at all. Working on two Old Persian inscriptions from Persepolis, he identified a recurring sign group as "king" and a longer one as "king of kings", inferred from the pattern that the author of one text was the son of the author of the other, and matched the pair against Darius and Xerxes because Greek historians said Persepolis was built by kings Herodotus named.

He then assigned sound values from Greek, Hebrew and Avestan forms of those names, reading `d a r h e u s h` for Darius and `kh sh h e r sh e` for Xerxes, and used the royal title *khscheio* from Duperron's 1771 edition of the Avesta to recover vowels and transliterate Hystaspes as `g o sh t a s p`.

Several of those values were wrong, and Torres Torres notes he never realized the signs were not purely alphabetic. It did not matter. The principle was right, and the principle was the same one that would work at Rosetta: **proper names are where a known thing and an unknown script are forced to touch.**

## Behistun, and access as a constraint

Grotefend had short palace inscriptions. Real progress needed long texts, and the long text was on a cliff.

Rawlinson began copying Darius's inscription at [Behistun](../places/behistun.md) in 1835, lowering himself down a vertical rock face and staying there for hours at a time. He had already reached results comparable to Grotefend's from trilingual inscriptions at Mount Elwend near Hamadan, twenty lines in Old Persian, Elamite and Babylonian on two rocks about two metres high.

This introduces a variable the vault has not had. Every other constraint in this area is about how much text survives. Here a large trilingual text survived intact and was simply **out of reach**, and the decipherment waited on someone willing to hang off a mountain. Corpus size was not the binding constraint at Behistun; physical access was.

## The 1857 test, which is why this note exists

The decipherment was resisted, and the objection was a good one.

Cuneiform is polyvalent. Mnamon's Akkadian entry, edited by Salvatore Gaspa, defines the two properties that make it hard: homophony, where the same sound may be written with different signs, and polyphony, where the same sign may stand for different sequences of sounds. Modern sign lists carry around 600 signs, and not all were used in every period.

Torres Torres reports the sceptical argument plainly: that a system in which one sign might be several syllables was so dysfunctional, so open to uncertainty, that the ancient Assyrians could not themselves have read it, and therefore the proposed decipherment and everything derived from it must be false.

That is an argument from plausibility, and it was answered with an experiment.

**William Henry Fox Talbot proposed the test.** The same Fox Talbot who invented the calotype, which is a fair sample of how many of this vault's decipherers arrived from somewhere else entirely. He had a prepublication copy of an inscription of Tiglath-Pileser I, found by Hormuzd Rassam at Qalat Shergat, and he sent his translation to the Royal Asiatic Society under seal, proposing that others do the same independently and that the results be compared. Four took part with no contact between them: Talbot, the Reverend Edward Hincks, Julius Oppert and Sir Henry Rawlinson. On **29 May 1857** the Society compared the four versions and pronounced the decipherment sound; Rawlinson's and Hincks's were closest.

Talbot's own case for why this could work is worth keeping, in translation from the Spanish: many cuneiform groups have only one value, and others always have the same value in the same word or phrase, so the remaining difficulties and uncertainties of reading are reduced to moderate limits.

**This is the vault's answer to a question it keeps asking.** [The evidentiary threshold](evidentiary-threshold-and-unicity-distance.md) says a proposed reading is worth nothing unless it can be distinguished from its rivals. The 1857 test is what distinguishing looks like in practice: independent readers, no communication, a text none had published on, and agreement as the evidence. It is a falsification procedure invented ninety years before information theory gave the underlying reason it works.

It also cuts against a modern habit. A computational decipherment claim that cannot be put through something like the 1857 test, because there is no second independent reader and no held-out text, is not being held to a standard the field met in the middle of the nineteenth century.

**One caution.** The 1857 test defeated an argument from implausibility, and the vault elsewhere entertains arguments of that shape: [Farmer, Sproat and Witzel](../references/farmer-sproat-witzel-2004.md) reason partly from what a literate civilization would plausibly have left behind. The precedent does not settle that dispute, but it is a reminder that "no real writing system could work like this" has been wrong before, and spectacularly.

## Encoding

`iso15924` is `Xsux`, numeric 020, Unicode alias `Cuneiform`, dated 2006-10-10. The related scripts have their own codes: `Xpeo` 030 for Old Persian and `Ugar` 040 for Ugaritic.

Unicode blocks verified against `Blocks.txt`: Cuneiform U+12000-U+123FF, Cuneiform Numbers and Punctuation U+12400-U+1247F, Early Dynastic Cuneiform U+12480-U+1254F. Old Persian is separately encoded at U+103A0-U+103DF and Ugaritic at U+10380-U+1039F.

Those last two ranges are worth stating precisely, because a summary consulted while writing this note gave both scripts the same range. They are adjacent and distinct.

## Open questions

- **Old Persian has no note**, despite being the wedge that opened everything here and having its own script code and Unicode block. It should be the next thing written in this area.
- **Elamite likewise**, and the vault already holds a warning about Linear Elamite in `ROADMAP.md`. Behistun is trilingual and the vault covers one of the three.
- `period` **is uneven.** The range given is Mnamon's for Akkadian cuneiform. Sumerian cuneiform is earlier and the note does not date it, so the field describes part of its subject.
- `corpus_size` **is not a number.** Torres Torres mentions tens of thousands of tablets in Ashurbanipal's library alone, and the total across all sites and periods is far larger. As with Egyptian, the variable that binds the undeciphered scripts stops binding here, but the vault should still find a figure rather than gesture.
- **Nothing from the primary literature has been read.** Rawlinson's *The Persian Cuneiform Inscription at Behistun* (1846-1851), the 1857 comparison itself, and Hincks's papers in the *Transactions of the Royal Irish Academy* are all out of copyright and all reach this note through Torres Torres.
- **The Cuneiform Digital Library Initiative** remains unconsulted, and is the obvious source for corpus figures.

## Sources

- [Torres Torres 2007](../references/torres-torres-2007.md), for Grotefend, Behistun, the sceptical objection and the 1857 test
- [Mnamon](../references/mnamon.md), Akkadian cuneiform entry edited by Salvatore Gaspa, for the sign count, the mixed system and the definitions of homophony and polyphony
- [ISO 15924](../references/iso15924.md), for `Xsux` 020, `Xpeo` 030 and `Ugar` 040, verified against the Unicode Consortium code list
- [Unicode block data](https://www.unicode.org/Public/UNIDATA/Blocks.txt), for the cuneiform, Old Persian and Ugaritic ranges
- [Wikidata Q401](https://www.wikidata.org/wiki/Q401)
