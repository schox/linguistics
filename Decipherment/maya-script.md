---
type: Script
aliases:
  - "Mayan hieroglyphs"
class: mixed
period: c. 3rd century BCE to the 16th century CE
decipherment_status: deciphered
status: open
writes:
  - "[[Classic Maya]]"
found_at:
  - "[[Piedras Negras]]"
corpus_size: not established here; inscriptions on stelae, lintels, ceramics and four surviving codices
subfield:
  - Solved decipherments
  - Epistemics
belongs_to: "[[Decipherment]]"
related_to:
  - "[[Script versus language]]"
  - "[[Egyptian hieroglyphs]]"
  - "[[Cuneiform]]"
  - "[[What counts as one sign]]"
cites:
  - "[[Proskouriakoff 1960]]"
iso15924: Maya
iso15924_num: 090
unicode_block:
wikidata: Q211248
---

# Mayan hieroglyphs

The logosyllabic script of the Maya civilization, combining logograms for whole words with syllabograms for sounds, and the third solved decipherment this vault has covered. Its interest here is that it was blocked for a reason neither of the others was.

## Three ways to not read a script

The vault now has a set, and they are genuinely different failures.

- **[Egyptian hieroglyphs](egyptian-hieroglyphs.md)** were blocked by a *wrong theory*. Horapollo's symbolic tradition held for fourteen centuries over an abundant corpus.
- **[Cuneiform](cuneiform.md)** was blocked by an *argument from implausibility*: polyvalence looked unusable, so the decipherment had to be false. It was settled by an experiment.
- **Maya was blocked by authority and politics.** The University of North Carolina's exhibit states it plainly: "The opposition of leading Mayanist J. Eric S. Thompson, as well Cold War suspicion of Knorozov's Soviet citizenship, slowed the reception of his brilliant analysis for many years."

Only the third has nothing to do with the evidence. Thompson held that the script was ideographic and that [Knorozov](../people/knorozov.md), working in Moscow, was producing something closer to propaganda than scholarship. The argument was not answered for years because of who was making it and where he lived.

That is worth holding beside the [evidentiary threshold](evidentiary-threshold-and-unicity-distance.md), which explains why some scripts *cannot* be read. Maya is a reminder that a corpus can be sufficient and a script still go unread, and that the reasons are not always epistemic.

## What actually broke it

**Landa's alphabet, which was in print for four centuries.** In the sixteenth century Diego de Landa asked Maya informants to give him glyphs corresponding to Spanish letters. The Maya had no alphabet, so what he recorded was not what he thought he was recording, and the resulting table was treated as a curiosity or a confusion.

**Knorozov, 1952: it is a syllabary.** He argued that Landa's "alphabet" listed *syllables* rather than letters, and therefore that the glyphs carried phonetic values. He had published on the de Landa alphabet earlier, and set out the system in *Sistema pis'ma drevnikh maiia* (Moscow, 1955).

The key had been available since the sixteenth century. What was missing was the idea that it was a key. Compare [Egyptian](egyptian-hieroglyphs.md), where medieval Arab scholars had already compared hieroglyphs with Coptic and got no further, and the vault's recurring observation that the obstacle is often a concept rather than a document.

**Proskouriakoff, 1960: the texts are history.** Working at [Piedras Negras](../places/piedras-negras.md), [she showed](../references/proskouriakoff-1960.md) that dates on consecutive monuments fall into sets whose intervals span plausible human lifespans, and concluded that the monuments record the births, accessions and reigns of individual rulers rather than astronomy and ritual.

She did that **without reading the script**. The argument is entirely from the distribution of dates. It is the same discipline as [Alice Kober](../people/alice-kober.md) on [Linear B](linear-b.md), and the vault has now recorded three independent instances of the structural finding preceding the phonetic one.

The two results are complementary and that is why the field moved. Knorozov supplied a mechanism for reading signs; Proskouriakoff supplied a reason to believe the texts said something readable in the first place. Neither alone dislodged Thompson.

## Deciphered and unencoded

`unicode_block` is empty, and this is the interesting case.

- **ISO 15924 has a code**: `Maya`, numeric 090, dated 2004-05-01. Its Unicode alias column is **empty**.
- **Unicode has no block for the script.** The only related block is Mayan Numerals at U+1D2E0-U+1D2FF, verified against `Blocks.txt`.

**This breaks an inference the vault made.** [What counts as one sign](segmentation-and-transcription.md) suggested that encoding follows a settled sign list and a settled sign list follows decipherment, on the evidence that the Aegean scripts had blocks and the unread ones did not. Maya is deciphered and unencoded, so decipherment is necessary but not sufficient.

The likely reason is the thing that makes the script hard to count: signs combine into glyph blocks, with infixing, conflation and heavy calligraphic variation, so deciding what the encodable units are is a harder problem than agreeing what the signs mean. That is a segmentation problem of exactly the kind that note is about, surviving a successful decipherment.

## Open questions

- **No sign count is given here.** Figures around 800 signs circulate, but the source that offered one turned out to be a private magazine with no institutional affiliation, so nothing is asserted. A count from the epigraphic literature would settle it, and would also let the segmentation point above be made quantitatively.
- **`corpus_size` is not a number.** The corpus is large and spread across monuments, ceramics and four surviving codices, and no source read here totals it.
- **Knorozov's 1952 article is not identified by title.** The UNC exhibit refers to "an important article in 1952" without naming it. The 1955 book is identified.
- **Thompson's position is reported only through his opponents.** The vault should read something of his own before letting "communist propaganda" stand as the summary of a scholar who dominated the field for decades.
- **Neither Knorozov nor Proskouriakoff has been read in the original.** The 1960 paper is paywalled; the 1952 and 1955 works are in Russian.
- **`period` is loose** and covers the script's attested span rather than being tied to a source read here.
- **Landa's *Relación de las cosas de Yucatán*** is the primary document for the alphabet and has not been consulted.

## Sources

- [Proskouriakoff 1960](../references/proskouriakoff-1960.md), for the historical hypothesis and its method
- [Sistema pis'ma drevnikh maiia, UNC Library exhibit](https://exhibits.lib.unc.edu/exhibits/show/maya/decipherment/sistema-pisma-drevnikh-maiia), for Knorozov's argument, the 1955 book and the reception
- [ISO 15924](../references/iso15924.md), for `Maya` 090 and its empty Unicode alias, verified against the Unicode Consortium code list
- [Unicode block data](https://www.unicode.org/Public/UNIDATA/Blocks.txt), checked: Mayan Numerals only, no block for the script
- [Wikidata Q211248](https://www.wikidata.org/wiki/Q211248)
