---
type: Concept
aliases:
  - "Is it writing at all? The Indus entropy debate"
subfield:
  - Epistemics
belongs_to: "[[Decipherment]]"
related_to:
  - "[[The evidentiary threshold and unicity distance]]"
  - "[[Why a script stays unread]]"
  - "[[Voynich manuscript]]"
  - "[[Indus script]]"
  - "[[Cryptography]]"
cites:
  - "[[Shannon 1949]]"
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

## This is the same question as the evidentiary threshold

The vault has treated well-posedness and corpus size as two separate problems. They are two terms of one expression, and seeing that explains several things at once.

**The vault's own reading, stated as such.** Shannon's unicity distance is, informally, the quantity of ciphertext needed before the key is uniquely determined, and it scales with the size of the key space divided by the [redundancy](../General-Linguistics/redundancy.md) of the plaintext language. Two quantities, one on top and one underneath.

[The evidentiary threshold](evidentiary-threshold-and-unicity-distance.md) is the vault's version of the first question: **is there enough text?** That note's own Caution flags the second, and files it as a limitation of the analogy: unicity distance assumes a defined key space and a known plaintext language model, and "decipherment has neither".

That caution is not a footnote. It is the other half of the argument. A corpus can fail to determine an answer in two ways:

- **Not enough text**, against a threshold that is in principle finite. This is [Linear A](linear-a.md), the [Phaistos Disc](phaistos-disc.md), [Cypro-Minoan](cypro-minoan.md). Excavation can move it.
- **No finite threshold to reach**, because the space of candidate answers is unbounded or the plaintext model does not exist. No quantity of text fixes this.

The second is what "is it writing at all?" asks. If the corpus encodes no language, there is no redundancy to divide by and the expression has no value; the question was malformed rather than hard.

### Why entropy, specifically

This also explains the shape of the Indus dispute, which otherwise looks like an odd choice of tool.

Rao and colleagues measure conditional entropy over sign sequences. That is an attempt to **estimate the denominator empirically**: to decide, from the corpus alone, whether it behaves like something carrying linguistic redundancy. Farmer, Sproat and Witzel argue that it does not and that the expression therefore has no value at all.

So the entropy debate is not a side-argument about statistics. It is the two camps trying to establish whether the vault's central inequality can even be written down for the Indus corpus. That is why it is prior to everything else, and why [the vault cannot diagnose the Indus script](why-scripts-stay-unread.md) until it is settled.

### Where this puts the Voynich

The [Voynich manuscript](voynich-manuscript.md) is the case that forced the point. It has 102 folios of continuous writing, so it cannot be short of text, and it is still undecidable, because its candidate set spans natural language in an unknown script, an enciphered natural language, a constructed language, and a hoax containing nothing.

Those four do not merely require different methods. They imply different denominators, and one of them implies no denominator at all. Until the set is narrowed, more text is not evidence, because there is nothing for it to be evidence *about*.

**The practical consequence is an ordering.** For any unread corpus, the well-posedness question comes first, the quantity question second, and running them in the other order produces the confident-decipherment pattern this vault keeps documenting. A method applied to a corpus of unknown status will always output something.

**A caution on the caution.** None of this is a derivation. Shannon's result is defined for a cipher with a stated key space and known language statistics; applying its shape to an undeciphered corpus is analogy, and the vault should not pretend a number falls out of it. What the analogy earns is the structure of the problem, not a value.

## Why it belongs in this vault

It is the cleanest demonstration that decipherment has a well-posedness problem that cryptanalysis does not. A cryptanalyst knows the ciphertext encodes a message, because somebody encrypted one. A decipherer has to establish it, and the tools for doing so are statistical, which means they inherit every weakness of a small corpus.

It also generalizes beyond the Indus corpus, to [Rongorongo](rongorongo.md), the [Phaistos Disc](phaistos-disc.md) and above all the [Voynich manuscript](voynich-manuscript.md), as set out above.

## Open questions

- **The reading above is the vault's own and rests on an informal statement of unicity distance.** Shannon's result is not quoted here, and the numerator-and-denominator framing is a paraphrase of a paraphrase. Reading Shannon 1949 directly would either firm it up or show it does not carry the weight put on it.
- **Neither published article of the Sproat and Rao exchange has been read**, though both are recorded with DOIs and open-access copies exist.
- **Whether "structure" and "language" can be separated statistically at all** is the live technical question underneath the dispute, and Yadav et al.'s own careful phrasing suggests the group thinks not. The vault has no note on it.
- **The ordering claim is untested.** That well-posedness should be settled before quantity is stated here as a practical consequence, and no case in the vault has actually been worked in that order.

## Sources

- [Farmer, Sproat and Witzel 2004](../references/farmer-sproat-witzel-2004.md), *The Collapse of the Indus-Script Thesis*, EJVS 11(2). [Author copy](https://safarmer.com/fsw2.pdf)
- [Rao et al. 2009](../references/rao-2009.md), *Entropic Evidence for Linguistic Structure in the Indus Script*, Science 324(5931), 1165. [DOI](https://www.science.org/doi/10.1126/science.1170391)
- [Sproat 2010](../references/sproat-2010.md), *Computational Linguistics* 36(3), 585-594, the published critique
- [Rao et al. 2010](../references/rao-2010.md), *Computational Linguistics* 36(4), 795-805, the published reply
- [Yadav et al. 2009](../references/yadav-et-al-2009.md), for the narrower stated conclusion
- [Indus script](indus-script.md), for the corpus statistics both sides accept
- [Language Log commentary on the Science paper](https://languagelog.ldc.upenn.edu/nll/?p=4652)
