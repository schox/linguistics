---
type: Concept
subfield:
  - Levels of analysis
belongs_to: "[[General Linguistics]]"
related_to:
  - "[[Morphology]]"
  - "[[Semantics]]"
  - "[[The Chomsky hierarchy]]"
  - "[[Is it writing at all? The Indus entropy debate]]"
cites:
  - "[[Anderson et al. 2022]]"
status: open
---

# Syntax

The study of how words are organized into phrases and sentences. [Anderson et al.](../references/anderson-et-al-2022.md) make the central claim immediately: a sentence is not a string of words but a **hierarchical structure**, and every phrase has an element that is its **head**.

That claim, not the details of any particular theory, is what connects this area to [the Chomsky hierarchy](chomsky-hierarchy.md) and through it to Computer Languages. Hierarchy is the thing a regular grammar cannot produce and a context-free one can.

## Generativity, shown with nonsense

Their demonstration is two invented sentences. *All grypnos are tichek* is the right shape for English even though two of its words mean nothing. *Grypnos tichek all are* is not, and would still not be even if you knew what a grypno was.

Nobody has encountered either sentence before, which is the point: an internal grammar generalizes to new cases. They call this **generativity**.

**Shape is separable from meaning.** The vault has been relying on this for its entire Decipherment area, since every distributional method assumes that structure is detectable without content, and it has not previously had a note saying so.

## Grammaticality judgments, and why the vault cannot have any

A sentence matching the patterns of a user's internal grammar is **grammatical**; one that does not is **ungrammatical**, conventionally marked with an asterisk. A sentence that is well formed but makes no sense takes a hash mark instead: their example is *#The book pedalled the ladder harmoniously*, which is the right shape and semantically absurd.

The evidence base of the field is the **grammaticality judgment**, and Anderson et al. are careful about what it is. It is an evaluation by an individual language user. There is no way to obtain one for "English" as a whole, only from particular English speakers, and describing something as ungrammatical in a language is shorthand for saying that its users generally agree. Where they disagree, that disagreement is itself data about syntactic variation.

They are also clear that ungrammatical examples are the more interesting ones, because they show the limits.

**This is the vault's own reasoning and is not drawn from the source.** Every language in this vault's Decipherment area is dead, and several are unidentified. There is nobody to ask. The consequence is that **the primary evidence of syntax, and specifically all negative evidence, is unavailable for the languages the vault studies.** A corpus shows what was written. It never shows what could not have been written, and the asterisk cannot be assigned.

This is a structural limit rather than a shortage of data, and it belongs beside the constraint recorded in [phonology](phonology.md), where minimal pairs turned out to require meanings a decipherer does not have. In both cases the field's standard method presupposes an informant. Corpus-only linguistics is a different discipline working under a strictly weaker evidence base, and the vault should say so wherever it treats a distributional result as equivalent to a grammatical one.

## Constituents, heads and selection

Words group into **constituents**. Anderson et al. define a **phrase** as a set of words acting together as a unit, and demonstrate it by substitution: in *All kittens are very cute*, the opening can be replaced by *puppies*, or *the ducklings that I saw earlier*, or *these videos of a baby panda sneezing*, but not by *that I saw earlier* or *of a baby panda*.

What the working substitutions share is not merely containing a noun. They are noun phrases, in which the noun is the **head**: it fixes the category of the whole phrase, and therefore where the phrase can go. This is the same headedness found inside compound words, applied to words in a phrase instead of morphemes in a word, which is why [morphology](morphology.md) and syntax are usually taught as one continuous argument.

Heads also **select**. A verb has, in their phrasing, an opinion about how many objects it takes, which is transitivity; no verb has an opinion about whether it is modified by an adverb.

## Where this touches the Indus dispute

[Is it writing at all?](../Decipherment/is-it-writing-at-all.md) records an argument conducted almost entirely in terms of conditional entropy over sign sequences. Both sides are measuring how constrained the ordering is.

The vault should be careful about what that measures. Constrained ordering is consistent with syntax and is not the same claim. Heraldic sequences, accounting formats and calendrical notations are all strongly ordered and none is a sentence. The hierarchical structure that Anderson et al. put at the center of syntax is exactly what a bigram or Markov statistic does not test for, and the vault's existing note says the dispute is about redundancy without saying that redundancy at that order of statistic is a weak proxy for grammar.

**Stated as a caution, not as a finding.** Whether anyone has attempted a hierarchy-sensitive test on the Indus corpus is unknown here and is worth finding out.

## Open questions

- **No syntactic theory is presented.** The source's treatment is X-bar and movement, one framework among several, and this note has deliberately taken only the parts that are common ground. Dependency versus constituency is named in this area's index under **Formal foundations** and is unwritten.
- **Word order typology is absent.** It is the most immediately useful part of syntax for this vault, since a decipherer wants to know what orders are possible at all, and it belongs under **Typology and universals** sourced from [WALS 2013](../references/wals-2013.md), which the vault holds as a Reference and has not used for this.
- **The claim that entropy over sign sequences is a weak proxy for syntax is the vault's own** and is not attributed. It is the kind of claim that ought to exist in the computational literature already.
- **Nothing here covers the syntax of dead languages as a practiced discipline.** Classicists and Assyriologists do describe the syntax of languages with no speakers, and how they establish anything without negative evidence is exactly the question this note raises and does not answer.
- **Thematic roles, argument structure, and the passive are all in the source and unused**, and argument structure is where syntax hands off to [semantics](semantics.md).

## Sources

- [Anderson et al. 2022](../references/anderson-et-al-2022.md), section 6.1 for the definition of syntax, the *grypnos* examples, generativity, grammaticality judgments and the asterisk and hash conventions; section 6.3 for constituents, phrases, the substitution test, headedness and selection
