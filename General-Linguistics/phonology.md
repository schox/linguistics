---
type: Concept
subfield:
  - Levels of analysis
belongs_to: "[[Levels of analysis]]"
related_to:
  - "[[Phonetics]]"
  - "[[Morphology]]"
cites:
  - "[[Anderson et al. 2022]]"
status: open
---

# Phonology

The study of the patterns that determine which combinations of a language's physical units are valid, and what changes occur when those units are combined. [Anderson et al. 2022](../references/anderson-et-al-2022.md) define it in those terms.

Where [phonetics](phonetics.md) describes the signal, phonology describes the system: which differences a language treats as differences, and which it ignores.

## Phonemes and allophones

The central abstraction.

In most North American English the consonant in the middle of *atom* is an alveolar flap, `[ɾ]`. In *atomic* the corresponding consonant is an aspirated voiceless alveolar plosive, `[tʰ]`. The two are physically different phones, but the words are transparently related, and it is useful to treat the two as one object at an abstract level.

That object is a **phoneme**. Its physical realizations are its **allophones**. The conditions that select one allophone over another are its **environments**, most commonly stated in terms of what stands immediately to the left, immediately to the right, or both.

A phoneme can be thought of as a set of allophones, here `{[ɾ], [tʰ]}`, each tied to particular positions. By convention it is written with a single symbol between **slashes**, in this case `/t/`, because listing every allophone would be unwieldy.

Anderson et al. note that real environments "can be more complex than what is presented in the simpler cases discussed in this textbook".

## Notation

| Brackets | Contains |
| --- | --- |
| `[ ]` | phones, a phonetic transcription |
| `/ /` | phonemes, a phonemic transcription |
| `< >` | symbols of a writing system |

## Contrastive distribution and minimal pairs

Two phones **contrast** when their distributions overlap, that is, when there are environments in which both can occur. They are then in **contrastive distribution** and belong to different phonemes.

A **minimal pair** is two words identical in every position but one. In English `[pɪl]` *pill* and `[kɪl]` *kill* differ only in the first phone, as do `[lɪp]` *lip* and `[lɪk]` *lick*, and `[spɪl]` *spill* and `[skɪl]` *skill*. **A single minimal pair is sufficient** to establish that two phones contrast.

Minimal pairs are not always available. Anderson et al. give `[ʒ]` as the rarest English consonant, occurring in *rouge*, *garage*, *vision* and *measure*, and almost never word-initially except in borrowings and names. Two fallbacks exist:

- A **near-minimal pair** differs elsewhere in the word as well as in the position of interest. *pleasure* `[plɛʒr̩]` and *pressure* `[prɛʃr̩]` differ in `[ʒ]` against `[ʃ]` but also in `[l]` against `[r]`. A single near-minimal pair proves nothing, because the incidental difference may not be incidental; several are needed.
- A **nonce word** is invented for the purpose. Taking *beige* `[beʒ]` and constructing `[beʃ]`, a speaker asked whether that could be a different word of English will generally say yes, which supports the contrast.

The concept transfers to signed languages, where a minimal pair is two signs alike except in one parameter.

## Complementary distribution

The converse case: two phones that never occur in the same environment are in **complementary distribution** and are candidates to be allophones of one phoneme.

## Phonotactics

The constraints a language places on which sequences are possible at all.

Of the six orderings of the phones `[m]`, `[i]` and `[k]`, English has *meek* `[mik]`. Four of the remaining five, `[imk]`, `[ikm]`, `[mki]` and `[kmi]`, are normally unpronounceable for English speakers. The fifth, `[kim]`, could be an English word and simply is not: an accidental gap rather than a systematic one.

**The distinction between an impossible form and a possible but unattested one is the subject matter of phonotactics.**

## Phonology is not specific to sound

Anderson et al. open the topic with a signed example. In American Sign Language the signs FOOD and BED compound to form HOME, and not as a strict sequence: the two merge into a single sign carrying properties of both. It keeps the flat-O handshape from FOOD and the location from BED, reduces the repetition, and drops the nonmanual head tilt from BED.

Phonology is therefore about the combinatorics of a signal in general, not about acoustics.

## Child topics

To be written as notes of their own: phoneme, allophone, minimal pair, contrastive distribution, complementary distribution, phonotactics, natural class, phonological rule, phonological derivation, aspiration, signed language phonology.

## Open questions

- **Phonological rules and derivations are not covered here**, though the source has four sections on them: rule notation, rule types, derivations and ordering. Natural classes likewise.
- **The relationship between phonemic analysis and script classification is unwritten.** The `class` value carried by every `Script` note in this vault (alphabet, abjad, abugida, syllabary, logographic, mixed) is a claim about which phonological unit a sign corresponds to, and nothing in the vault defines that vocabulary. It belongs under **Writing systems**.
- **Nothing here covers phonemic analysis as a procedure**, which is the practical skill the source devotes two worked sections to.

## Sources

- [Anderson et al. 2022](../references/anderson-et-al-2022.md), section 4.1 for the definition of phonology, the ASL compound, the *meek* orderings and the *atom* and *atomic* phoneme example; section 4.3 for contrastive distribution, minimal pairs, the `[ʒ]` examples, near-minimal pairs and nonce words
