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
status: open
---

# Is it writing at all? The Indus entropy debate

The prior question, which most decipherment discussion skips: before asking what a corpus says, establish that it says anything.

## The dispute

Farmer, Sproat and Witzel (2004) argue that the Indus corpus is **not writing**. Their case rests on the extreme brevity of the inscriptions (typically around five signs), the behavior of the sign inventory, the high proportion of signs occurring only once, and the complete absence of long texts, which they read as positive evidence of a non-linguistic symbol system rather than as an accident of preservation. They note that a literate civilisation that left no long texts anywhere would be unique.

Rao and colleagues (2009) reply with an information-theoretic argument. Measuring conditional entropy over Indus sign sequences, they find the values fall within the range of known linguistic systems and outside the range of the non-linguistic control systems they tested, and conclude that a linguistic interpretation remains the better supported one.

The exchange that followed was sharp, and both the statistical methodology and the choice of control corpora were contested. Sproat's critiques and Rao's published rebuttal are both worth reading in full before forming a view.

## Why it belongs in this vault

It is the cleanest demonstration that decipherment has a well-posedness problem that cryptanalysis does not. A cryptanalyst knows the ciphertext encodes a message, because somebody encrypted one. A decipherer has to establish it, and the tools for doing so are statistical, which means they inherit every weakness of a small corpus.

It also generalizes. The same question applies to Rongorongo, to the Phaistos Disc, and most sharply to the Voynich manuscript, where the live hypotheses include natural language in an unknown script, an enciphered natural language, a constructed language, and an elaborate hoax containing no information at all. Those four require entirely different methods, and choosing between them is a prior step to any attempt at reading.

## Sources

- [Farmer, Sproat and Witzel 2004](../references/farmer-sproat-witzel-2004.md), *The Collapse of the Indus-Script Thesis*, EJVS 11(2). [Author copy](https://safarmer.com/fsw2.pdf)
- [Rao et al. 2009](../references/rao-2009.md), *Entropic Evidence for Linguistic Structure in the Indus Script*, Science 324(5931), 1165. [DOI](https://www.science.org/doi/10.1126/science.1170391)
- [Rao's rebuttal](https://homes.cs.washington.edu/~rao/IndusResponse.html)
- [Language Log commentary on the Science paper](https://languagelog.ldc.upenn.edu/nll/?p=4652)
