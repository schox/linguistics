---
type: Concept
subfield:
  - Epistemics
belongs_to: "[[Decipherment]]"
related_to:
  - "[[The evidentiary threshold and unicity distance]]"
  - "[[Cryptography]]"
cites:
  - "[[Rao et al. 2009]]"
  - "[[Farmer, Sproat and Witzel 2004]]"
  - "[[Sproat 2010]]"
  - "[[Rao et al. 2010]]"
  - "[[Yadav et al. 2009]]"
status: open
---

# Is it writing at all? The Indus entropy debate

The prior question, which most decipherment discussion skips: before asking what a corpus says, establish that it says anything.

## The dispute

Farmer, Sproat and Witzel (2004) argue that the Indus corpus is **not writing**. Their case rests on the extreme brevity of the inscriptions (typically around five signs), the behavior of the sign inventory, the high proportion of signs occurring only once, and the complete absence of long texts, which they read as positive evidence of a non-linguistic symbol system rather than as an accident of preservation. They note that a literate civilization that left no long texts anywhere would be unique.

Rao and colleagues (2009) reply with an information-theoretic argument. Measuring conditional entropy over Indus sign sequences, they find the values fall within the range of known linguistic systems and outside the range of the non-linguistic control systems they tested, and conclude that a linguistic interpretation remains the better supported one.

The exchange that followed was sharp, and both the statistical methodology and the choice of control corpora were contested. It has a published form, which is the one to cite: [Sproat 2010](../references/sproat-2010.md) in *Computational Linguistics* 36(3), answered by [Rao et al. 2010](../references/rao-2010.md) in 36(4). Both are worth reading in full before forming a view, and neither has been read here.

**What is not in dispute.** Both sides work from [Mahadevan's concordance](../references/mahadevan-1977.md) and report compatible corpus statistics; Rao and colleagues contest the interpretation, not the counts. The material facts are set out in [Indus script](indus-script.md), and keeping them in a separate note from this one is deliberate: the numbers are common ground and the argument is not.

Worth noting too that [Yadav et al. 2009](../references/yadav-et-al-2009.md), from the same group, states a narrower conclusion than the press coverage of the Science paper suggested. It finds the script "is a structured sign system showing features of a formal language" while saying explicitly that this "cannot conclusively establish that it encodes natural language". The distinction between structure and language is the whole of the dispute.

## Why it belongs in this vault

It is the cleanest demonstration that decipherment has a well-posedness problem that cryptanalysis does not. A cryptanalyst knows the ciphertext encodes a message, because somebody encrypted one. A decipherer has to establish it, and the tools for doing so are statistical, which means they inherit every weakness of a small corpus.

It also generalizes. The same question applies to [Rongorongo](rongorongo.md), to the [Phaistos Disc](phaistos-disc.md), and most sharply to the [Voynich manuscript](voynich-manuscript.md), where the live hypotheses include natural language in an unknown script, an enciphered natural language, a constructed language, and an elaborate hoax containing no information at all. Those four require entirely different methods, and choosing between them is a prior step to any attempt at reading.

## Sources

- [Farmer, Sproat and Witzel 2004](../references/farmer-sproat-witzel-2004.md), *The Collapse of the Indus-Script Thesis*, EJVS 11(2). [Author copy](https://safarmer.com/fsw2.pdf)
- [Rao et al. 2009](../references/rao-2009.md), *Entropic Evidence for Linguistic Structure in the Indus Script*, Science 324(5931), 1165. [DOI](https://www.science.org/doi/10.1126/science.1170391)
- [Sproat 2010](../references/sproat-2010.md), *Computational Linguistics* 36(3), 585-594, the published critique
- [Rao et al. 2010](../references/rao-2010.md), *Computational Linguistics* 36(4), 795-805, the published reply
- [Yadav et al. 2009](../references/yadav-et-al-2009.md), for the narrower stated conclusion
- [Indus script](indus-script.md), for the corpus statistics both sides accept
- [Language Log commentary on the Science paper](https://languagelog.ldc.upenn.edu/nll/?p=4652)
