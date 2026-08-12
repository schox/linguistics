---
type: Script
aliases:
  - "Voynich manuscript"
class: undetermined
period: parchment radiocarbon dated 1404-1438 CE
decipherment_status: undeciphered
status: open
writes:
found_at:
corpus_size: one manuscript, Beinecke MS 408; 102 folios plus folding leaves
subfield:
  - Unsolved, partial and contested
  - Epistemics
belongs_to: "[[Decipherment]]"
related_to:
  - "[[Is it writing at all? The Indus entropy debate]]"
  - "[[The evidentiary threshold and unicity distance]]"
  - "[[Phaistos Disc]]"
  - "[[Adversarial versus accidental encipherment]]"
cites:
  - "[[Beinecke MS 408]]"
iso15924:
iso15924_num:
unicode_block:
wikidata: Q179492
---

# Voynich manuscript

An illustrated codex in an unidentified script, held at Yale as Beinecke MS 408. It is the vault's hardest case to classify, and the reason it has a `Script` note is that the alternative is worse: leaving out the one corpus where every hypothesis in the area is live at once.

`found_at` is empty and that is correct rather than missing. The Voynich has a provenance, not a findspot. It was not excavated, and the chain of custody is documentary: Rudolph II, who paid 600 gold ducats and may have acquired it from John Dee; Jacobus Horcicky de Tepenecz; Johannes Marcus Marci, who sent it to Athanasius Kircher in 1666; Wilfrid Voynich, who bought it from the Jesuit College at Frascati in 1912; and H. P. Kraus, who gave it to the Beinecke in 1969.

## The object

The Beinecke catalog gives 102 folios, including five double, three triple, one quadruple and one sextuple folding leaves, on parchment, 225 by 160 mm, in an eighteenth or nineteenth century vellum case. Almost every page carries drawings in ink with colored washes. The library describes the text as "in cipher, apparently based on Roman minuscule characters", the language as unidentified, and the content as a "Scientific or magical text".

## Two dates that do not agree

Radiocarbon dating of the parchment at the University of Arizona in 2009, on four samples taken from folios 8, 26, 47 and 68, put it at 1404-1438 with 95% probability, refined on combined analysis to 1404-1435.

The Beinecke catalog record gives "Central Europe [?], s. XV ex-XVI [?]", late fifteenth to sixteenth century, and reports the argument that identifying New World plants among the drawings would mean the manuscript could not predate 1493.

Those cannot both be right. The likely explanation is dull, that the catalog record predates the 2009 test, and the vault records the conflict rather than silently preferring one. It matters because the New World plant argument is load-bearing for several hoax and later-composition theories, and radiocarbon at 1404-1435 removes its foundation. What radiocarbon dates is the parchment and not the writing, so it sets a floor rather than settling the question.

## Why it belongs in Decipherment rather than Cryptography

The Voynich is where the vault's own distinction gets tested. [Adversarial versus accidental encipherment](adversarial-versus-accidental.md) argues that cryptanalysis faces a system built to resist you while decipherment faces obscurity that is an accident of loss, and that the statistical apparatus transfers between them while the adversarial apparatus does not.

The Voynich might be either. The live hypotheses, as [is it writing at all?](is-it-writing-at-all.md) already sets out, are a natural language in an unknown script, an enciphered natural language, a constructed language, and an elaborate hoax carrying no information. Only the second is a cryptographic problem. The first is decipherment, the third is something else again, and the fourth means there is nothing to find. The Beinecke states the position dryly: "Cryptographic approaches have failed to decipher the text, if it is indeed encoded."

Choosing between those four is prior to any attempt at reading, and no method chooses for you. That is why the note sits here.

## What makes it different from every other script in this area

**The corpus is large and still singular.** Unlike the [Phaistos Disc](phaistos-disc.md), the Voynich has plenty of text: 102 folios of continuous writing, far more than [Linear A](linear-a.md) or the Indus corpus in running length. Quantity is not the constraint. What it lacks is any second source: no other document in this script exists, no bilingual, no proper names identifiable from outside, no archaeological context, no known reading community.

That combination is unique here. Every other undeciphered script in the vault is under-resourced in text. The Voynich is under-resourced in everything except text, which is why statistical work on it is abundant and inconclusive.

**Nothing about it is registered.** No ISO 15924 code, no Unicode block, no Unicode script property value, all verified on 2026-08-10. In this it resembles the [Phaistos Disc](phaistos-disc.md), which at least has a block, and differs from every other script here.

## Open questions

- **No sourced count of glyphs or word-tokens.** This is a real gap and an odd one. Decades of statistical analysis rest on transcriptions, and the vault has no figure from a source it has read for how many characters or words the manuscript contains, nor for the size of the glyph inventory. Commonly cited figures exist; none was verified. Until that is fixed, `corpus_size` records the object and not the text.
- **The transcription systems have not been examined.** Any statistical claim about the Voynich depends on a transcription alphabet, EVA being the usual one, and different transcriptions segment the script differently. This is the same segmentation problem that afflicts [rongorongo](rongorongo.md) and the [Indus script](indus-script.md), now collected in [what counts as one sign](segmentation-and-transcription.md).
- **The hoax hypothesis is stated but not assessed.** Arguments from the statistical properties of the text have been made in both directions and none has been read.
- **The illustrations are untouched here.** The botanical, astronomical and balneological sections are a large body of non-textual evidence, and identification of the plants is one of the few external constraints available.

## Sources

- [Beinecke MS 408](../references/beinecke-ms-408.md), the library's catalog record, for the physical description, dating and provenance
- [Radio-carbon dating of the Voynich MS](https://voynich.nu/extra/carbon.html), maintained by René Zandbergen, for the 2009 Arizona results
- [Voynich manuscript, Beinecke collection highlights](https://beinecke.library.yale.edu/collections/highlights/voynich-manuscript)
- [ISO 15924](../references/iso15924.md), checked and containing no Voynich entry
- [Unicode block data](https://www.unicode.org/Public/UNIDATA/Blocks.txt), checked and containing no Voynich block
- [Wikidata Q179492](https://www.wikidata.org/wiki/Q179492)
