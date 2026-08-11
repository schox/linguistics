---
type: Concept
subfield:
  - Levels of analysis
belongs_to: "[[General Linguistics]]"
related_to:
  - "[[Phonology]]"
  - "[[What counts as one sign]]"
  - "[[Morphology]]"
cites:
  - "[[Anderson et al. 2022]]"
status: open
---

# Phonetics

The physical study of the speech signal: how it is produced, how it travels, how it is received. The level at which language is a fact about bodies and air rather than about grammar.

Conventionally divided three ways, which is the division this area's index uses:

| Branch | Studies |
| --- | --- |
| articulatory | how the vocal tract produces the signal |
| acoustic | the physical properties of the signal itself |
| auditory | how a hearer perceives it |

**The vault's source covers the first of these and very little of the other two.** [Anderson et al.](../references/anderson-et-al-2022.md) is articulatory throughout chapter 3: articulators, place and phonation, manner, vowels, then syllables, stress and intonation. Acoustic phonetics appears only where waveforms are needed to make a point, and auditory phonetics is left to the psycholinguistics chapters. This note inherits that shape and should not be read as a balanced treatment.

## Signed language is not an afterthought here

Chapter 3 puts signed-language articulators, sign description and signed-language notation inside the phonetics chapter rather than in an appendix.

That is worth recording rather than passing over. It means "phonetics" in current usage is the study of the **physical realization of a linguistic signal**, whatever the modality, not the study of sound. The vault's habit of treating the spoken and the written as the only two things a language can be is a habit, not a fact about language.

## Segmentation, which is the vault's problem one level down

Anderson et al. introduce the term **segment** for dividing a word into its component phones, and then immediately warn that it often cannot be done. They contrast waveforms for the English words *nab* and *wool*: *nab* shows abrupt transitions between three regions corresponding to three phones, while *wool* has smooth transitions from beginning to end with no obvious divisions.

Their warning is directed at students: "when working with raw data from a spoken language, it may not be so clear where the boundaries are between phones".

The vault has already written this argument about writing. [What counts as one sign](../Decipherment/segmentation-and-transcription.md) holds that deciding where one sign stops and the next begins is prior to reading, contested, and quietly determines every count downstream.

**This is the vault's own observation and is not drawn from the source.** The two problems are the same problem at two levels. A continuous signal has to be cut into units before anything can be counted, the cuts are analytic decisions rather than observations, and in both cases the decision is usually made silently and inherited by everyone downstream. A decipherer inherits a sign list; a phonetician inherits a segmentation.

## Why the IPA exists, and why decipherment cannot skip it

Phonetic transcription is written in **square brackets**, and can be **broad**, giving only what is needed to tell one word from another, or **narrow**, giving fine detail. Symbols of a writing system are written in **angle brackets**, a convention that exists precisely to keep the two apart.

Anderson et al. give the reason a writing system cannot serve as a transcription system, and it is the reason this vault keeps `Script` and `Language` as separate types. An existing orthography is optimized for one language and has no way to write the phones of another. Worse, orthographies are internally inconsistent: they note that English uses one letter for the different vowels of *nab*, *father*, *halo* and *diva*, and writes one vowel five different ways in *diva*, *meet*, *meat*, *me* and *mummy*. Their conclusion is that the English writing system "does not have a one-to-one relationship between phones and letters".

Even a regular orthography would not be enough, because the same word varies across speakers. Their example is the vowel of *mop*, which is low and back in Los Angeles, low and back with some lip rounding in London, and articulated further forward in Chicago.

**The consequence for this vault is direct.** A script does not record a pronunciation, and it never did. Decipherment recovers a script's relation to a phonological system, not a recording of speech, and every sound value assigned to an ancient sign is a value in someone's reconstructed phonology rather than a phone anyone heard. That is why the vault's `Script` notes carry `writes` and the `Language` notes carry `written_in`, and why conflating them breaks the decipherment material.

## Open questions

- **Acoustic and auditory phonetics are effectively unwritten here**, because the source is articulatory. Formants, spectrograms, the acoustic correlates of the articulatory categories, and categorical perception are all missing, and two of the three branches named in this area's index have no content.
- **There is no note on the International Phonetic Alphabet itself**, and the vault has no record of the association that maintains it, the chart's revision history, or the current revision. That is an obvious gap for a vault about writing systems, and the chart is a candidate for the empty `attachments/` directory.
- **Nothing here is instrumental.** How phonetic claims are actually measured, and how much of the descriptive apparatus predates the ability to measure it, is not addressed.
- **The relation between phonetic segments and script signs is asserted rather than worked through.** The claim that both segmentation problems are one problem is the vault's own and has not been checked against anyone who has argued it.
- **Sign-language phonetics is mentioned and not covered**, despite being the part of the chapter that most directly challenges how this vault frames writing.

## Sources

- [Anderson et al. 2022](../references/anderson-et-al-2022.md), section 3.6, for segmentation, the *nab* and *wool* waveforms, broad and narrow transcription, the bracket conventions, the English orthography examples and the *mop* variation; and chapter 3 generally for the scope of the phonetics chapter
