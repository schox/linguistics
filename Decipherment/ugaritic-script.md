---
type: Script
aliases:
  - "Ugaritic script"
class: abjad
period: Late Bronze Age, to c. 1190 BCE
decipherment_status: deciphered
status: open
writes:
  - "[[Ugaritic]]"
found_at:
  - "[[Ugarit]]"
corpus_size: thousands of tablets from Ugarit; the decipherment used the 1929 and 1930 finds only
subfield:
  - Solved decipherments
  - The problem space
belongs_to: "[[Solved decipherments]]"
related_to:
  - "[[Cuneiform]]"
  - "[[Frequency analysis]]"
  - "[[Adversarial versus accidental encipherment]]"
  - "[[The evidentiary threshold and unicity distance]]"
cites:
  - "[[Day 2002]]"
iso15924: Ugar
iso15924_num: 040
unicode_block: U+10380-U+1039F
wikidata: Q332652
---

# Ugaritic script

A consonantal alphabet of thirty letters, written with a cuneiform stylus, used at [Ugarit](../places/ugarit.md) in the Late Bronze Age. Deciphered in about a year, which makes it the fastest in the record and the reason it belongs in this vault.

It is the first `abjad` here. Every other script in the Decipherment area is a syllabary, a logo-syllabic mixture or undetermined.

## Why it fell so fast

Not corpus size. The corpus was tiny when the work was done: the 1929 season's tablets, then the 1930 season's. Two things decided it, and neither is the variable phase 1 of this vault spent four batches on.

**Thirty signs.** The CREWS Project's account is that the excavators saw immediately that there were far too few signs for a logosyllabic system like the Akkadian cuneiform found across the Near East, and rightly concluded it had to be alphabetic. Thirty is a number that tells you what kind of thing you are looking at before you know anything else.

**A correct guess at the language.** They supposed it was closely related to Hebrew and Phoenician, which it is. With those two deductions, CREWS notes, "decipherment was able to progress extremely quickly, being accomplished essentially within a year by three men working more or less separately".

## Sign inventory is a variable in its own right

This is the note's contribution to the vault's argument.

Everything in phase 1 turns on **how much text** survives. Ugaritic shows that **how many signs** there are is independently decisive, and that the two can pull in opposite directions.

| Script | Signs | Outcome |
| --- | --- | --- |
| Ugaritic | 30 | read in about a year |
| [Linear B](linear-b.md) | c. 87 syllabic plus over 100 ideographic | read after decades |
| [Cuneiform](cuneiform.md) | c. 600 | read over a century |
| [Mayan hieroglyphs](maya-script.md) | several hundred | read over a century, and blocked politically |
| [Indus](indus-script.md) | 417, disputed | unread |

The mechanism is the size of the hypothesis space. A thirty-sign consonantal alphabet writing a language whose family you have guessed correctly is very close to a **monoalphabetic substitution cipher**, and the vault already has a note on how those are broken. See [frequency analysis](frequency-analysis.md).

That is the sharpest instance in the vault of what [adversarial versus accidental encipherment](adversarial-versus-accidental.md) claims: the statistical apparatus of cryptanalysis transfers to decipherment even though the adversarial apparatus does not. Ugaritic is the case where an archaeological decipherment problem was, in its formal structure, a cipher of a kind cryptanalysis had solved routinely for a thousand years.

**A caution the vault should keep.** The resemblance holds only because the language family was guessed right. Get that wrong and thirty signs buys you nothing, because a substitution cipher is only tractable against a known plaintext language model. That is exactly the qualification [the evidentiary threshold](evidentiary-threshold-and-unicity-distance.md) makes about applying unicity distance to decipherment.

## A prediction, satisfied

Day records a confirmation worth keeping beside the [1857 cuneiform test](cuneiform.md).

Virolleaud suggested looking for a four-consonant word meaning "axe". Bauer's system, applied to the texts, yielded `grzn`, which has a Hebrew cognate of that meaning. Dussaud reported this to the Académie as verification.

That is a prediction made in advance and satisfied by the reading, which is a stronger form of evidence than a reading that merely produces plausible words. The vault's recurring complaint about decipherment claims is that a method always outputs something; the answer, in 1857 and again here, is to fix the target before you look.

## Three men, one year, and a press release

The decipherment was accomplished between 1929 and 1930 by Hans Bauer at Halle, Paul Dhorme at Jerusalem and Charles Virolleaud, working, in the CREWS phrasing, "more or less separately".

It produced the third credit dispute in as many solved decipherments the vault has covered. Day's article exists to sort it out, and reports that after the Académie meeting of 24 October the French press presented Virolleaud's success as though no one else had made any progress at all; Dhorme, who had learned of Virolleaud's work only from those releases, knew that to be untrue, and by 8 December 1930 had published a revised alphabet crediting Bauer.

Set beside Young and Champollion, and Rawlinson and Hincks, the pattern is hard to miss: **every solved decipherment in this vault came with a quarrel about who solved it.** That is worth stating as an observation and not explained here. It may say something about how credit works in a field where the result is a single announcement, or only that fast public results attract disputes.

## Encoding

`iso15924` is `Ugar`, numeric 040, Unicode alias `Ugaritic`, dated 2004-05-01. The Unicode block is U+10380-U+1039F, immediately below Old Persian at U+103A0-U+103DF and verified against `Blocks.txt`.

Both scripts are cuneiform in technique and neither is Sumero-Akkadian [cuneiform](cuneiform.md), which has its own code `Xsux` 020. Three separate script codes for three writing systems sharing a stylus is the registry treating technique and system correctly.

## Open questions

- **Hans Bauer's method is not established here, and the interesting claim about it is unverified.** Accounts circulate that he had done cryptanalysis for German military intelligence in the First World War and applied statistical methods learned there. If true, it is the most direct link between Cryptography and Decipherment anywhere in this vault. It is **not asserted**: it appeared only in a search summary, the Wikipedia article on Bauer does not mention any war service or codebreaking, and the passages of Day retrieved here do not cover it. Bauer's own *Entzifferung* would settle it.
- **No `Person` notes for Bauer, Dhorme or Virolleaud**, though all three plausibly meet the inclusion test. Deferred because the most substantive thing the vault would say about Bauer is the unverified claim above.
- **Day 2002 was read in fragments, not continuously**, because the host refuses direct fetches. The sequence of who established what, which is the article's whole point, is therefore not fully followed here.
- **`corpus_size` is not a number.** Thousands of tablets are reported from Ugarit; the decipherment used only the 1929 and 1930 finds, and neither figure is given.
- **The relationship to the alphabet's origins is untouched.** A thirty-letter consonantal alphabet in the Late Bronze Age Levant sits directly on the question of where alphabets come from, and CREWS says the Ugarit tablets revolutionized understanding of the early history of the alphabet. The vault has nothing on that.

## Sources

- [Day 2002](../references/day-2002.md), for the roles of the three decipherers, the `grzn` confirmation and the priority dispute
- [Ninety years of Ugaritic Studies, CREWS Project](https://crewsproject.wordpress.com/2019/05/14/ninety-years-of-ugaritic-studies/), Cambridge, for the thirty signs, the alphabetic deduction and the guess at the language family
- [ISO 15924](../references/iso15924.md), for `Ugar` 040, verified against the Unicode Consortium code list
- [Unicode block data](https://www.unicode.org/Public/UNIDATA/Blocks.txt), for U+10380-U+1039F
- [Wikidata Q332652](https://www.wikidata.org/wiki/Q332652)
