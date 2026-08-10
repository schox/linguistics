---
type: Concept
subfield:
  - Infrastructure
  - Epistemics
belongs_to: "[[Decipherment]]"
related_to:
  - "[[The evidentiary threshold and unicity distance]]"
  - "[[Is it writing at all? The Indus entropy debate]]"
  - "[[Computational decipherment: three distinct tasks]]"
  - "[[Indus script]]"
  - "[[Rongorongo]]"
  - "[[Linear A]]"
  - "[[Cypro-Minoan]]"
  - "[[Voynich manuscript]]"
cites:
  - "[[Farmer, Sproat and Witzel 2004]]"
  - "[[Yadav et al. 2009]]"
  - "[[Berthin 2024]]"
  - "[[Ferrara 2013]]"
  - "[[Salgarella and Castellan 2020]]"
  - "[[Petrolito et al. 2015]]"
  - "[[Mnamon]]"
status: open
---

# What counts as one sign

Every statistic about an undeciphered script begins with a decision that is almost never presented as one: where does a sign end and the next begin, and which marks are the same sign.

Sign counts and token counts look like observations. They are outputs of that decision. Change it and the inventory changes, the token count changes, and every entropy value, Zipf fit and n-gram model computed downstream changes with them. This note collects the evidence, which is scattered across the vault as an open question on five separate notes, and states the consequence once.

## The same corpus, different numbers

**The [Indus script](indus-script.md) is the clearest case, because the spread is enormous.** All of these are counts of the sign inventory of one corpus:

| Count | Whose, and on what basis |
| --- | --- |
| 417 | Mahadevan's concordance, the figure both sides of the entropy debate use |
| 300-400 | the range Farmer, Sproat and Witzel report for most counts since the 1960s |
| over 600 (676) | Wells, who treats far more variants as separate signs |
| about 20 | S. R. Rao, decomposing signs into strokes; no serious support |

A factor of thirty separates the extremes. Farmer, Sproat and Witzel note what Wells's finer splitting does to the data: about half his signs then occur exactly once. That is not a discovery about the Indus civilization. It is a mechanical consequence of the splitting rule, and it would look like evidence of a non-linguistic system to anyone who took the inventory as given.

**[Linear A](linear-a.md) shows the same effect in a milder form**, and here the numbers are not even in conflict:

- some 180 simple signs, some 164 complex signs formed by combining simple ones, and some 30 fractional signs (Salgarella and Castellan, from the standard list in GORILA volume 5)
- some 85 distinct signs (Rutter, describing it as a syllabary)
- 81 signs shared with [Linear B](linear-b.md) and assumed to carry syllabic values (Petrolito and colleagues)

These count different things: the full inventory of simple signs, an estimate of the syllabic subset, and the shared subset. Quoting any one as "the number of Linear A signs" produces an argument that does not survive contact with the others.

**[Rongorongo](rongorongo.md) has the problem built into the script.** Berthin gives about 120 unique base characters which, citing Barthel, fuse into hundreds of compound forms. Whether a fused pair is one sign or two is a segmentation judgement made hundreds of times over a corpus of roughly 14,000 signs, and the token count is not independent of it.

**[Cypro-Minoan](cypro-minoan.md) has it one level up.** The question there is not where a sign ends but where the *corpus* ends: whether CM1, CM2 and CM3 are three scripts or one. Ferrara's treatment of the repertory as 83 graphemes of a single writing system is an answer to that, and the answer determines whether the material is one corpus of 243 inscriptions or three of a few dozen each.

**The [Voynich manuscript](voynich-manuscript.md) has it in the purest form.** There is no archaeological sign list at all, so every statistical claim rests on a transcription alphabet, and different transcriptions segment the script differently. The statistics are properties of a transcription as much as of the manuscript.

## A second decision: which texts count

Segmentation has a companion that behaves the same way. [Yadav and colleagues](../references/yadav-et-al-2009.md) build their Indus working set by removing damaged, illegible, duplicate and multi-line texts. That takes 2,906 texts down to 1,548, and 40 of the 417 signs disappear from the data entirely.

Every one of those exclusions is defensible on its own terms. Together they nearly halve the corpus and remove a tenth of the inventory before any analysis begins. A corpus is not what was excavated; it is what survives the decisions made to render it analyzable.

## Why this matters for the vault's central claim

[The evidentiary threshold](evidentiary-threshold-and-unicity-distance.md) is stated in terms of quantity: below some amount of surviving text, a proposed reading can be neither proved nor disproved.

**Segmentation determines what the quantity is.** So the threshold cannot be measured independently of a decision that is itself unsettled, and comparisons of corpus size across scripts, including the tables in this vault, are only as commensurable as their underlying segmentations. That is the reason those tables carry a warning that the figures are each their own source's and the comparison is order-of-magnitude.

It also bears directly on the [Indus entropy debate](is-it-writing-at-all.md), and in an unexpected direction. Conditional entropy over a sign sequence is computed on tokens, so it inherits the segmentation completely. What makes that dispute a real dispute rather than an artifact is that **both camps use Mahadevan's segmentation**: Farmer, Sproat and Witzel draw their frequency case from it while arguing the corpus is not writing, and Rao and colleagues build on the electronic version of the same concordance while arguing the opposite. Shared tokenization is what allows them to disagree about interpretation rather than past each other. Where two analyses do not share a segmentation, an apparent disagreement about a script may be a disagreement about a rule.

## The one script with no segmentation problem

The [Phaistos Disc](phaistos-disc.md) is the exception, and it is instructive.

Its signs were stamped into fresh clay using pre-prepared forms. Every occurrence of a sign is therefore physically identical to every other occurrence, and sign identity is a manufacturing fact rather than an analytic judgement. There are 45 distinct signs and 241 impressions, and nobody disputes either number.

It is also the least decipherable corpus in the vault. Removing the segmentation problem entirely does not help when there are 241 tokens, which is a useful reminder that segmentation is a distinct constraint from quantity and neither substitutes for the other.

## An observation about encoding, offered as inference

The vault has verified which of these scripts have Unicode blocks. Setting that beside the state of their sign lists produces a pattern:

| Script | Unicode block | Standard sign list |
| --- | --- | --- |
| Linear A | yes | GORILA volume 5 |
| Cypro-Minoan | yes | HoChyMin, then Ferrara |
| Phaistos Disc | yes | fixed by the physical stamps |
| Indus | **no** | Mahadevan 1977, used by all sides |
| Rongorongo | **no** | Barthel 1958, with compounds unresolved |
| [Proto-Elamite](proto-elamite.md) | **no** | several hundred signs, not settled here |
| Voynich | **no** | transcription alphabets only |

**This is the vault's own inference and not a sourced claim.** The tempting reading is that encoding requires a settled sign list, and the Indus script is the counterexample that makes it interesting: Mahadevan's 417 signs are a de facto standard that both camps in a bitter dispute rely on, and there is still no block. What that suggests is that a standards body needs more than agreement among researchers about the inventory; it needs the corpus's status as writing not to be in dispute. Encoding is a claim about what a thing is, not only about how to count it.

## Open questions

- **No source read here treats segmentation as a general problem.** Every observation above is assembled from sources discussing one script. A methodological literature on this almost certainly exists, in grapholinguistics and in the digital-epigraphy community, and none of it has been consulted. Until it is, this note is a synthesis of the vault's own material rather than a summary of a field.
- **No worked demonstration.** The claim that entropy is sensitive to segmentation is stated and not shown. Computing conditional entropy over the Indus corpus under Mahadevan's 417-sign and Wells's 676-sign segmentations would demonstrate it directly, and both segmentations are published.
- **Transcription systems have not been surveyed.** EVA for the Voynich, the Raison-Pope and GORILA systems for Linear A, and Barthel's numbering for rongorongo are all mentioned in the vault without any account of how they differ or what they commit their users to.

## Sources

- [Farmer, Sproat and Witzel 2004](../references/farmer-sproat-witzel-2004.md), for the Indus sign-count range and the effect of Wells's splitting
- [Yadav et al. 2009](../references/yadav-et-al-2009.md), for the EBUDS pruning and the shared use of Mahadevan's concordance
- [Berthin 2024](../references/berthin-2024.md), for rongorongo base glyphs and compound forms
- [Ferrara 2013](../references/ferrara-2013.md), for the single-writing-system treatment of Cypro-Minoan
- [Salgarella and Castellan 2020](../references/salgarella-castellan-2020.md) and [Petrolito et al. 2015](../references/petrolito-et-al-2015.md), for the Linear A inventories
- [Mnamon](../references/mnamon.md), Phaistos Disc entry, for the stamped production method
