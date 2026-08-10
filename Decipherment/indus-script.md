---
type: Script
class: undetermined
period: c. 2600-1900 BCE (Mature Harappan)
decipherment_status: undeciphered
status: open
writes:
found_at:
  - "[[Mohenjo-daro]]"
  - "[[Harappa]]"
corpus_size: c. 4,000-5,000 inscribed objects; 2,906 texts and 13,372 sign occurrences in Mahadevan's concordance
subfield:
  - Unsolved, partial and contested
  - Epistemics
belongs_to: "[[Decipherment]]"
related_to:
  - "[[Is it writing at all? The Indus entropy debate]]"
  - "[[Linear A]]"
  - "[[Script versus language]]"
  - "[[The evidentiary threshold and unicity distance]]"
cites:
  - "[[Mahadevan 1977]]"
  - "[[Farmer, Sproat and Witzel 2004]]"
  - "[[Rao et al. 2009]]"
  - "[[Yadav et al. 2009]]"
  - "[[Sproat 2010]]"
  - "[[Rao et al. 2010]]"
  - "[[UNESCO, Archaeological Site of Harappa]]"
iso15924: Inds
iso15924_num: 610
unicode_block:
wikidata: Q601388
---

# Indus script

The sign system of the Indus civilization, found on seals, sealings, pottery, copper tablets and other durable objects from sites across present-day Pakistan and northwest India. Undeciphered, and unusual among the vault's scripts in that whether it is a script at all is a live scholarly question.

`class` is `undetermined` and `writes` is empty. Both are the honest values rather than placeholders: no underlying language has been identified, and the sign system's type cannot be assigned while its status as writing is disputed. See [Is it writing at all?](is-it-writing-at-all.md), which carries the debate itself; this note carries the material facts it turns on.

## What both camps agree on

This is the most useful thing to establish first, because the dispute is loud enough to obscure it.

[Farmer, Sproat and Witzel](../references/farmer-sproat-witzel-2004.md), arguing the corpus is not writing, and [Yadav and colleagues](../references/yadav-et-al-2009.md), arguing it is a structured sign system, both work from [Mahadevan's 1977 concordance](../references/mahadevan-1977.md) and report compatible counts. Farmer, Sproat and Witzel give 2,905 cataloged objects and 13,372 sign occurrences across 417 signs; Yadav and colleagues give "417 unique signs in 3573 lines of 2906 texts". The one-object difference is rounding or a cataloging decision, not a disagreement.

[Rao and colleagues' 2010 reply](../references/rao-2010.md) disputes the interpretation of these statistics and not the statistics themselves. So the numbers below are common ground, and the argument is entirely about what follows from them.

## Brevity is the central fact

Farmer, Sproat and Witzel: "The longest on one surface has 17 symbols; less than 1/100 carry as many as 10." They give the mean as "4.6 signs long" over the 2,905 objects in the concordance, which is consistent with the 13,372 occurrences they report (13,372 divided by 2,905 is 4.60). Yadav and colleagues describe texts of "not more than 14 signs in a single line", a lower ceiling because it counts lines rather than whole object surfaces.

Set against the vault's other scripts, using each source's own totals:

| Script | Documents | Sign occurrences | Mean signs per document |
| --- | --- | --- | --- |
| Indus | 2,905 | 13,372 | 4.6 |
| [Linear A](linear-a.md) | 1,427 | 7,362-7,396 | c. 5.2 |
| [Linear B](linear-b.md) | more than 4,600 | 57,398 | at most c. 12.5 |

**The Indus and Linear A means are sourced; the Linear B mean is not.** Farmer, Sproat and Witzel state 4.6 directly. The Linear A and Linear B figures are divisions performed here on the counts in [Petrolito et al. 2015](../references/petrolito-et-al-2015.md), and the Linear B figure is an upper bound because its document count is given as "more than 4,600". Treat the column as an order-of-magnitude comparison, not as three equally solid numbers.

The pattern it shows is worth the caveats. The two undeciphered scripts have texts averaging around five signs; the deciphered one has texts more than twice as long. Corpus size alone does not separate them, since the Indus corpus has nearly twice Linear A's sign occurrences and is still unread.

Farmer, Sproat and Witzel press this further with a comparison the vault should keep: only 21 or possibly 22 Linear Elamite inscriptions are known, "most of them are longer than the longest of the known 4-5,000 Indus inscriptions". A corpus two hundred times smaller can contain longer texts. Length and volume are independent variables, and the evidentiary threshold depends on both. (Linear Elamite is not [Proto-Elamite](proto-elamite.md); they are distinct scripts and the vault should not merge them when Proto-Elamite is written.)

## The sign inventory, and why counts differ

Estimates depend almost entirely on how variants are split, which is a decision rather than an observation.

- **417** distinct signs in Mahadevan's concordance, the figure both camps use.
- **300-400** is the range Farmer, Sproat and Witzel report for most counts since the 1960s, citing Parpola, Fairservis, Possehl and others.
- **676** in Wells, who treats far more variants as separate signs. Farmer, Sproat and Witzel note the consequence: about half of Wells's signs then occur exactly once.
- **20** in S. R. Rao (1982), who decomposed signs into strokes. Farmer, Sproat and Witzel record that this has no serious support.

Frequency is heavily skewed. Farmer, Sproat and Witzel: "Just four of 417 signs account for 21% of the 13,372 sign occurrences in Mahadevan's concordance; eight signs make up 31%; and twenty signs over 50%." Yadav and colleagues fit the rank-frequency distribution with a Zipf-Mandelbrot law and note that word frequencies in natural languages follow the same law. The same skew is read by one side as evidence of a small functional emblem repertoire and by the other as a property Indus signs share with words.

## What the corpus loses when it is made analyzable

Yadav and colleagues' working set is a good measure of how thin the evidence really is. Removing damaged, illegible, duplicate and multi-line texts from the 2,906 leaves 1,548, and 40 of the 417 signs disappear from the data entirely.

That is the evidentiary threshold operating mechanically rather than in principle. A corpus is not the number of objects excavated; it is the number of usable sequences left after everything unreadable is set aside.

## Encoding

`iso15924` is `Inds`, numeric 610, and 610 sits inside the 600-699 block the registry reserves for undeciphered scripts.

**There is no Unicode block.** `unicode_block` is empty because none exists, not because it was not looked up: the Unicode block list contains no block whose name refers to the Indus or Harappan script. Encoding presupposes an agreed sign list, and for the Indus corpus the sign list is exactly what is in dispute.

The [Phaistos Disc](phaistos-disc.md) is the mirror image: no ISO 15924 code and no Unicode script value, but a Unicode block all the same. Between them the two show that the registries are not one system. A corpus can be encoded as characters without being recognized as a script, or recognized as a script without being encoded, and neither status implies anything about whether it is writing.

## Open questions

- **Per-site distribution of the corpus was not established.** Mahadevan's concordance is reported to include tables of sign distribution by archaeological site, which is precisely what would let the provenance argument in [Mohenjo-daro](../places/mohenjo-daro.md) and [Harappa](../places/harappa.md) be made quantitatively rather than by assertion. Reading M77 Table 1 would settle it. No source read here gives per-site inscription counts.
- **Neither the Sproat nor the Rao article of the published exchange has been read.** Both are recorded with their DOIs, and open-access copies exist for both. The characterization of the Rao reply currently rests on the authors' own summary page, which is a partisan source for a dispute about that very argument.
- **The dating range is the civilization's, not the script's.** `period` gives the Mature Harappan phase, c. 2600-1900 BCE, which is corroborated by Farmer, Sproat and Witzel and by the excavators' phase chronology in [UNESCO's Harappa documentation](../references/unesco-harappa-tentative.md). Farmer, Sproat and Witzel separately refer to the symbols being in use for "at least 600 years", which is consistent with that span. What is still missing is a first-and-last-attestation range for the signs themselves, which need not coincide with the mature phase: the Harappa sequence has Early Harappan levels from c. 2800 BCE and Late Harappan down to c. 1300 BCE, and whether inscribed objects occur in either was not established.
- **Whether the vault should hold a `Language` note for Harappan.** Wikidata has Q3428279, "unknown language or languages of the Harappan civilization". No note was created, on the same reasoning as Minoan for Linear A: an unattested language identified only as the referent of an undeciphered script is not a language note, it is a gap in a script note.

## Sources

- [Farmer, Sproat and Witzel 2004](../references/farmer-sproat-witzel-2004.md), for brevity, sign frequency and the Linear Elamite comparison
- [Yadav et al. 2009](../references/yadav-et-al-2009.md), for the concordance figures, the Zipf-Mandelbrot fit and the EBUDS pruning
- [Mahadevan 1977](../references/mahadevan-1977.md), the concordance both camps use
- [Rao et al. 2009](../references/rao-2009.md) and [Rao et al. 2010](../references/rao-2010.md), for the entropy argument and the published reply
- [Sproat 2010](../references/sproat-2010.md), for the critique
- [UNESCO, Archaeological Site of Harappa](../references/unesco-harappa-tentative.md), for the excavators' phase chronology
- [ISO 15924](../references/iso15924.md), for `Inds` and 610, verified against the Unicode Consortium code list
- [Unicode block data](https://www.unicode.org/Public/UNIDATA/Blocks.txt), checked and containing no Indus block
- [Wikidata Q601388](https://www.wikidata.org/wiki/Q601388)
