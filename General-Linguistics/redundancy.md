---
type: Concept
aliases:
  - "Redundancy"
subfield:
  - Computational linguistics
  - Formal foundations
belongs_to: "[[Computational linguistics]]"
related_to:
  - "[[The evidentiary threshold and unicity distance]]"
  - "[[Is it writing at all? The Indus entropy debate]]"
  - "[[Frequency analysis]]"
  - "[[Why a script stays unread]]"
cites:
  - "[[Shannon 1951]]"
  - "[[Shannon 1949]]"
  - "[[Rao et al. 2009]]"
  - "[[Farmer, Sproat and Witzel 2004]]"
status: open
---

# Redundancy

Language is repetitive, and that is what makes it readable by anyone who does not already know it.

This note exists because the vault has been leaning on redundancy for months without defining it. [The evidentiary threshold](../Decipherment/evidentiary-threshold-and-unicity-distance.md) divides by it. [Is it writing at all?](../Decipherment/is-it-writing-at-all.md) argues that the whole Indus dispute is an attempt to measure it. [Frequency analysis](../Decipherment/frequency-analysis.md) works because of it. None of those says what it is.

## What Shannon measured

[Shannon 1951](../references/shannon-1951.md) defines redundancy as "the amount of constraint imposed on a text in the language due to its statistical structure", and estimates it for printed English by asking people to guess the next letter from the preceding text.

His figures, which are the ones this vault should quote:

| Context | Entropy | Redundancy |
| --- | --- | --- |
| short-range, up to 8 letters | roughly 2.5 bits per letter | roughly 50 per cent |
| long-range, up to 100 letters | of the order of one bit per letter | roughly 75 per cent |

With 100 letters of context and a 27-character alphabet including the space, his experimental bounds were 1.3 bits per letter as an upper estimate and 0.6 as a lower one.

A 27-character alphabet could in principle carry about 4.75 bits per character if every character were equally likely and independent. English carries a fraction of that. **The rest of the channel is spent on constraint**, and constraint is what a decipherer has to work with.

## Why it is the thing decipherment runs on

If every sign sequence were equally probable, no proposed reading could ever be preferred to any other. There would be nothing to be wrong about.

Redundancy is what makes a wrong reading *look* wrong. It shows up as uneven sign frequencies, which is what [frequency analysis](../Decipherment/frequency-analysis.md) exploits and what al-Kindi noticed in the ninth century. It shows up as constrained sequences, which is what n-gram and Markov models exploit. It shows up as formulaic repetition, which is what let [Kober](../people/alice-kober.md) detect inflection in Linear B and [Proskouriakoff](../people/proskouriakoff.md) detect biography in Maya dates, in both cases without knowing a single sound value.

Every method in this vault's Decipherment area is a way of turning redundancy into a constraint on hypotheses.

## The denominator problem

In Shannon's cryptographic setting, redundancy is the divisor: the more redundant the plaintext language, the less ciphertext you need before the key is determined. High redundancy is the cryptanalyst's friend.

**Decipherment cannot use the formula, because it does not know the value.** The plaintext language is unattested, and its redundancy is exactly what is unknown. That is the qualification the vault records in [the evidentiary threshold](../Decipherment/evidentiary-threshold-and-unicity-distance.md) and develops in [is it writing at all?](../Decipherment/is-it-writing-at-all.md): you cannot compute how much text you need without knowing how redundant the language is, and you cannot know that until you can read it.

So the Indus entropy dispute is not a side-argument. [Rao and colleagues](../references/rao-2009.md) are estimating redundancy from the corpus alone and arguing the value falls in the linguistic range; [Farmer, Sproat and Witzel](../references/farmer-sproat-witzel-2004.md) argue there is no linguistic redundancy there to measure. Both are arguing about the denominator.

## A tension the vault should not smooth over

**This is the vault's own reasoning and is not drawn from a source.**

Most early corpora are administrative, and administrative text is formulaic. Formulaic text is highly redundant, which by the argument above should make it easier to work with.

But the vault's own figures point the other way. [Linear A](../Decipherment/linear-a.md) documents average about five signs; the [Indus](../Decipherment/indus-script.md) corpus averages 4.6. Highly formulaic, highly redundant, and unread. Meanwhile [Linear B](../Decipherment/linear-b.md), also administrative, fell.

The resolution is probably that redundancy and *quantity of distinct context* are different things, and that a corpus can be repetitive without being informative: a thousand near-identical five-sign entries constrain the hypothesis space far less than their sign count suggests, because they are close to one observation repeated. If that is right, then raw sign totals overstate the evidence in exactly the corpora this vault cares about, and the comparisons in [why a script stays unread](../Decipherment/why-scripts-stay-unread.md) are more generous to the short corpora than they should be.

The vault does not have the means to settle this, and it is stated here as a problem rather than a finding.

## Open questions

- **The tension above is unresolved and possibly important.** If repetitive corpora carry less information than their token counts imply, several of this vault's cross-script comparisons are optimistic. Someone will have formalized this; nothing has been read on it.
- **Shannon 1949 has still not been read**, only 1951 and only in part. The vault cites the unicity distance result throughout and has never seen it stated.
- **Redundancy figures for languages other than English are not recorded here**, and the vault's argument implicitly assumes the English figures are representative. Whether redundancy varies much across languages, and by how much, matters directly to the threshold argument.
- **Nothing here covers redundancy in speech**, or the phonological and morphological sources of it, which is what a General Linguistics note on this ought eventually to do. The note is currently written entirely from the decipherment end.

## Sources

- [Shannon 1951](../references/shannon-1951.md), for the definition and the entropy and redundancy figures for printed English
- [Shannon 1949](../references/shannon-1949.md), for unicity distance, unread
- [Rao et al. 2009](../references/rao-2009.md) and [Farmer, Sproat and Witzel 2004](../references/farmer-sproat-witzel-2004.md), for the dispute about whether the Indus corpus has linguistic redundancy at all
