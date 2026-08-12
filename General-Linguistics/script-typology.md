---
type: Concept
aliases:
  - "Script typology"
subfield:
  - Writing systems
belongs_to: "[[Writing systems]]"
related_to:
  - "[[Script versus language]]"
  - "[[What counts as one sign]]"
cites:
  - "[[Baroni 2011]]"
  - "[[Unicode Standard 17.0, chapter 6]]"
  - "[[Daniels and Bright 1996]]"
  - "[[ISO 15924]]"
status: open
---

# Script typology

The classification of writing systems by the linguistic unit their signs stand for: a word or morpheme, a syllable, a consonant, or a phoneme. The categories in general use are logographic or logosyllabic, syllabary, abjad, abugida, alphabet, and featural.

The scheme is a description of tendencies rather than a partition. No major classification treats its own categories as exact, and the three consulted here disagree with one another about particular scripts.

## Writing system, script, and orthography

Three levels are routinely conflated and are worth separating first, because the typology applies to only one of them.

A **writing system** is the principle by which signs relate to language: alphabetic, syllabic, and so on. A **script** is a particular set of graphic shapes realizing that principle. An **orthography** is the set of conventions by which one language uses one script, including the correspondences, punctuation, spacing and capitalization.

[Baroni 2011](../references/baroni-2011.md) puts the first distinction as follows: Latin and Greek "had the same writing system (an alphabet) but employed different scripts" (p. 128). Italian and French share both a writing system and a script, and differ in orthography.

The term "writing system" is itself used in two senses. [The Unicode Standard](../references/unicode-standard-17.md) uses it both for a category of script and for the way a particular language is written, noting that "the modern Japanese writing system uses four scripts". Both senses are current, and which is meant is usually recoverable from context.

## What the signs stand for

The first cut is not between the familiar categories but above them. Following Coulmas 1989, Baroni divides systems into **cenemic**, whose elements stand for units of phonic expression, and **pleremic**, whose elements stand for units of content (p. 128).

The division is a matter of degree rather than of kind. Baroni is explicit that "there is no pure writing system: in every tradition cenemic and pleremic components coexist, to different extents". This is the fact the familiar six-way scheme has most trouble with, and it is why so many scripts are recorded with composite classifications.

Within the pleremic group, Baroni distinguishes **pictograms**, whose shape recalls the object represented, from **ideograms**, which represent abstract concepts iconically, from **logographic** systems proper, in which graphic elements stand for a word or a morpheme.

## The categories

### Logographic and logosyllabic

Signs stand for words or morphemes. Pure logography is not attested at scale: the systems so labeled all carry substantial phonetic machinery as well, which is why Unicode prefers **logosyllabary**, defined as a system in which "the units of the writing system are used primarily to write words and/or morphemes of words, with some subsidiary usage to represent syllabic sounds per se". Its example is the Han script.

Baroni notes one consequence of the type that a phonetic system does not share: Chinese writing is interdialectal, legible across varieties that are not mutually intelligible in speech, which he takes from Coulmas 1983: 246 as one reason for its persistence.

### Syllabary

Each graphic unit stands for one syllable, "normally a CV-type of syllable" (Baroni, p. 128). His examples are Japanese kana, [Linear B](../Decipherment/linear-b.md) and Cherokee.

The type suits languages with simple syllable structure and scales badly otherwise. Baroni observes that for a language with complex syllables, of the sort found in German or Russian, "the list of syllabograms would be endless".

### Abjad

Consonants are written and vowels are not, "even if there is the possibility to add diacritic vocalic signs to disambiguate" (Baroni, p. 128). Unicode's formulation is that "consonant sounds are written but short vowel sounds are typically omitted", with the main letters being consonants or long vowels.

Unicode gives the Phoenician script as the prototypical case and Arabic as the better-known one. Baroni connects the fit to Semitic [morphology](morphology.md), where the triconsonantal root carries the lexical content and the vowels carry inflection.

The term derives from the first letters of the Arabic script and was brought into the typology by [Daniels and Bright 1996](../references/daniels-bright-1996.md).

### Abugida

A consonant sign carries an inherent vowel, which other signs override. Unicode: "each consonant letter carries an inherent vowel, usually /a/", with dependent vowel signs, or *matras*, subordinate to the consonant letters. Devanagari is the standard example and Ethiopic is named in the same passage.

Baroni treats it as a subtype of syllabary in which the consonant and vowel parts remain separately identifiable, which is a different framing of the same facts. Unicode calls it "a kind of blend of syllabic and alphabetic characteristics".

### Alphabet

Signs stand for individual phonemes, consonants and vowels alike. Baroni's definition is a system "where ideally all the phonemes of a language are noted by separate elements" (p. 128); Unicode's is a system "that consists of letters for the writing of both consonants and vowels", adding that the two have equal status as letters.

The word "ideally" is doing real work. No alphabet achieves one sign per phoneme in practice, and the distance between the principle and any actual orthography is the subject of orthographic depth.

### Featural

An alphabet whose sign shapes are not arbitrary but correlate with the articulatory features of the sounds. Korean Hangul is the case both sources name. Unicode records that the jamo shapes "were devised with intentionally iconic shapes relating them to articulatory features of the sounds they represent in Korean", and classifies Hangul as a **featural syllabary**, since the jamo are grouped into syllable blocks. Baroni calls it featural writing and treats it as a kind of alphabet.

The two labels describe the same script and disagree about which property is criterial: the sign shapes, or the syllabic grouping.

## Composite systems

A single language's writing frequently uses more than one system at once. Unicode's case is Japanese, which "mixes a logosyllabary (Han), two syllabaries (Hiragana and Katakana), and one alphabet (Latin, for romaji)".

Type can also depend on use rather than on descent. Unicode records that Mahajani and Multani derive from Brahmic writing but lack the virama, matras and conjunct formation characteristic of abugidas, and so "behave respectively as an alphabet and an abjad, and are encoded and classified accordingly".

## Three classifications that do not agree

Three schemes are consulted here, and they conflict in ways worth stating, because a script's recorded type depends on which one was used.

1. **Baroni's linguistic scheme**: pleremic against cenemic, then syllabary, abjad, abugida, alphabet, featural.
2. **The Unicode Standard's Table 6-1**, which sorts every encoded script into Alphabets, Abjads, Abugidas, Logosyllabaries, Simple Syllabaries and Featural Syllabaries.
3. **[ISO 15924](../references/iso15924.md)'s numeric ranges**, which encode an older and coarser typology in the code numbers themselves: 000-099 hieroglyphic and [cuneiform](../Decipherment/cuneiform.md), 100-199 right-to-left alphabetic, 200-299 left-to-right alphabetic, 300-399 alphasyllabic, 400-499 syllabic, 500-599 ideographic, 600-699 undeciphered, 700-799 shorthands and notations.

The third is the odd one, and instructively so. Its top-level cut is partly by writing direction and partly by legibility, and it is the only one of the three with a category for scripts nobody can read.

Disagreements are visible inside the schemes as well as between them. Unicode's chapter 6 states in prose that "the Ethiopic script is an abugida", while Table 6-1 in the same chapter lists Ethiopic under Simple Syllabaries. Table 6-1 also assigns [Linear A](../Decipherment/linear-a.md) to Logosyllabaries and [Cypro-Minoan](../Decipherment/cypro-minoan.md) to Simple Syllabaries, although neither script has been deciphered and the assignment therefore rests on sign counts and structural inference rather than on readings.

The standard anticipates the objection and concedes it twice. Table 6-1 is "an approximate guide, rather than a definitive classification, because of the mix of features seen in many scripts", and the chapter warns that "one must always be careful not to assume too much about the structure of a writing system from its nominal classification".

## Child topics

Each should become a note of its own; none is written.

- **The history of the alphabet.** Proto-Sinaitic to Phoenician to Greek, and the addition of vowel letters.
- **Orthographic depth.** Transparent and opaque orthographies, and what depth predicts about reading. Baroni pp. 129 and following is the starting point held here.
- **Transliteration and romanization standards.** The ISO series, ALA-LC, Hepburn, Pinyin.
- **Script reform.** Deliberate change to a writing system by policy.
- **Grapheme.** The minimal contrastive graphic unit, and the graphoneme.
- **Featural writing**, and whether the category is criterial or descriptive.
- **Alphabetocentrism.** Gelb's evolutionary account and its critics, all attributed in Baroni pp. 129 to 131.

## Open questions

- **Whether a script can be typed before it is read.** Table 6-1 assigns types to Linear A and Cypro-Minoan, both undeciphered. What evidence supports a type assignment in the absence of readings, and whether the standard intends the assignment as a claim or as an encoding convenience, is not addressed by the sources read.
- **The Ethiopic discrepancy** between chapter 6's prose and its own Table 6-1 is unexplained. It may be an artifact of the table's stated approximateness, or an error. Nothing read resolves it.
- **The coinage of *abjad* and *abugida* is not established.** Both are commonly credited to Peter T. Daniels, but the review consulted attributes them only to the 1996 volume, and no primary statement has been read. See [Daniels and Bright 1996](../references/daniels-bright-1996.md).
- **Neither source read uses "mixed" or "undetermined" as a category name.** Unicode handles the first case with "composite system" and the second by omission, since it classifies only what it encodes. Whether a general typology should carry either as a category, or treat them as the absence of one, is not discussed in what has been read.
- **Featural is absent from ISO 15924's ranges**, which have no slot for it, and the two other schemes disagree on whether it names a kind of alphabet or a kind of syllabary.
- **Sign-count thresholds are not covered.** The rough figures often quoted for distinguishing types by inventory size, on the order of tens of signs for an alphabet, dozens to hundreds for a syllabary, and hundreds upward for a logosyllabary, appear in none of the three sources read here in that form. A source that states them explicitly would be worth having, since inventory size is the evidence actually used when a script is undeciphered.

## Sources

- [Baroni 2011](../references/baroni-2011.md), *Alphabetic vs. non-alphabetic writing: Linguistic fit and natural tendencies*, pp. 127-132
- [Unicode Standard 17.0, chapter 6](../references/unicode-standard-17.md), *Writing Systems and Punctuation*, including Table 6-1
- [Daniels and Bright 1996](../references/daniels-bright-1996.md), *The World's Writing Systems*, not read; held for the origin of the terms *abjad* and *abugida*
- [ISO 15924](../references/iso15924.md), for the typology carried in its numeric ranges
