---
type: Concept
subfield:
  - Levels of analysis
belongs_to: "[[General Linguistics]]"
related_to:
  - "[[Syntax]]"
  - "[[Pragmatics]]"
  - "[[Redundancy]]"
cites:
  - "[[Anderson et al. 2022]]"
status: open
---

# Semantics

The study of linguistic meaning: what a language user has to know in order to produce and understand meaning, as distinct from the several other things the word "meaning" is used for.

[Anderson et al.](../references/anderson-et-al-2022.md) fence the subject off by elimination, and the fence is useful. A tea stalk floating upright in a cup of green tea "means" good luck, but the stalk is not a linguistic expression. Saying there is no *meaning* in buying a sewing machine you cannot use is about the purpose of an action. Saying you did not *mean* something you said is about sincerity, and belongs to [pragmatics](pragmatics.md).

What is left is the sense in which the Ojibwe word *ode'imin* and the English word *strawberry* mean the same thing: each carries content that lets a user of that language decide, for any given object, whether the word applies to it.

## Entailment, and a test that needs no meanings supplied

The technical core, and the part with the clearest procedure.

*p* **entails** *q* when *p* being true makes *q* necessarily true. *The customer sighed* entails *The customer emitted a breath*.

The test is to negate the candidate and conjoin it: *The customer sighed, but it is not the case that the customer emitted a breath* is a **contradiction**, a sentence that is never true, and that is what shows the entailment holds. Contradiction is what negating an entailment produces.

An **implicature** fails the test. *The customer sighed* suggests *The customer is angry*, but *The customer sighed, but it is not the case that the customer is angry* is not a contradiction: the customer may have sighed with relief. Implicatures are **cancellable**, and cancellability is the diagnostic.

Anderson et al. put the methodological point first: a word's meaning cannot be studied in isolation, only through how it does and does not work in sentences. Meaning is recovered from distribution over contexts.

**That sentence is why this note matters to the rest of the vault**, and it is worth stating what it does and does not license.

## What decipherment can and cannot get here

**This is the vault's own reasoning and is not drawn from the source.**

The entailment test requires an informant who can judge whether a sentence is contradictory. For every language in the Decipherment area there is none, so the constraint already recorded in [phonology](phonology.md) and [syntax](syntax.md) applies a third time: the field's primary diagnostic presupposes a speaker.

But the methodological principle underneath it survives the loss of the informant, and that is the more important observation. If a word's meaning is approached through the contexts it occurs in, then a corpus is the right kind of evidence even without a speaker, because a corpus is a record of contexts. This is the assumption that distributional semantics makes explicit and that every computational decipherment method relies on. The vault's `ROADMAP.md` names an unwritten junction note on embeddings and distributional semantics; **this is where it attaches**, and the claim it will have to evaluate is that distribution approximates meaning well enough to be worth acting on.

The limit is equally plain. Distribution gives you which signs behave alike. It does not give you what any of them denotes, and the step from a coherent set of distributional classes to a reading is the step no method in this vault performs without external evidence: a bilingual, a proper name, a known related language, or an object depicted beside the text.

## A conflation the vault should avoid

[Redundancy](redundancy.md) is a statistical property: constraint on a text arising from its structure, in Shannon's sense. It is not semantic content, and a corpus can be highly redundant while carrying almost no information about what its signs mean.

Popular accounts of computational decipherment slide between the two, treating a demonstration that a corpus has language-like statistics as a demonstration that its meaning is within reach. The vault's standing caution about the three tasks in `Decipherment/computational-decipherment-three-tasks.md` is the same caution in a different vocabulary. Recovering statistical structure is not recovering meaning, and semantics is the level at which the difference is visible.

## Open questions

- **Formal semantics is not covered.** Denotation, set theory, truth conditions and compositionality are all in the source and none is used here, and **Formal foundations** in this area's index names formal semantics as a topic in its own right. The Montague tradition is entirely absent from the vault.
- **Lexical semantics is missing**: sense relations, the mental lexicon, polysemy, and how a dictionary definition differs from a denotation. The source has a section explicitly on why a dictionary is not a semantic theory.
- **The claim that distributional evidence survives the loss of an informant is the vault's own** and is not attributed. It is the foundational assumption of an entire subfield and someone will have stated it properly.
- **Nothing here addresses semantic change**, which is the historical half of the subject and the reason a cognate can be formally regular and semantically implausible. That belongs under **Historical and comparative** and bears directly on how decipherment proposals are judged.
- **The vault has no note on how a proposed reading is evaluated for meaning**, as opposed to for sound values. This is arguably the largest unwritten thing in the Decipherment area, and semantics is the level it belongs to.

## Sources

- [Anderson et al. 2022](../references/anderson-et-al-2022.md), section 7.1 for the delimitation of linguistic meaning and the *ode'imin* example; section 7.3 for entailment, the contradiction test, implicature and cancellability
