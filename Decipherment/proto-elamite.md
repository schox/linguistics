---
type: Script
class: mixed
period: c. 3300-2900 BCE
decipherment_status: partial
status: open
writes:
found_at:
  - "[[Susa]]"
corpus_size: just over 1,600 pieces, c. 10,000 lines of text (Englund); c. 1,700 tablets (Kelley)
subfield:
  - Unsolved, partial and contested
  - The problem space
belongs_to: "[[Decipherment]]"
related_to:
  - "[[Indus script]]"
  - "[[Script versus language]]"
  - "[[The evidentiary threshold and unicity distance]]"
  - "[[Why a script stays unread]]"
  - "[[What counts as one sign]]"
cites:
  - "[[Kelley 2026]]"
  - "[[Englund 2004]]"
iso15924: Pelm
iso15924_num: 016
unicode_block:
wikidata: Q25474080
---

# Proto-Elamite

One of the world's earliest writing systems, used in Iran from roughly 3300 to 2900 BCE, principally at [Susa](../places/susa.md). It is the only script in this area whose `decipherment_status` is `partial` rather than `undeciphered`, and the reason is worth understanding precisely.

## Partly read, and not in the way that phrase usually means

Kelley describes the script as "only very partly deciphered". The partial success is asymmetric and does not point where the usual sense of the phrase suggests:

- **The numerical systems are substantially understood.** Proto-Elamite shares them with proto-[cuneiform](cuneiform.md), which is read, and quantity notations turn out to be the most recoverable part of an accounting corpus because they have internal structure that can be checked arithmetically.
- **The non-numerical signs are not.** Several hundred of them record commodities, personnel and institutions. Kelley's framing is that they encode ideographically rather than primarily linguistically.

That second point matters for the vault's taxonomy. Reading Proto-Elamite quantities is not partial decipherment in the [Linear B](linear-b.md) sense of recovering sound values for some signs. It is closer to understanding an accounting schema than to reading a language, and it can be done without settling what language, if any, lies underneath. Compare [computational decipherment's three tasks](computational-decipherment-three-tasks.md), which makes a related distinction: doing something useful with a corpus is not the same as reading it.

`writes` is empty for exactly that reason. The name attaches the script to Elamite by convention and by later association, not by demonstration.

## Corpus

[Englund](../references/englund-2004.md) gives "just over 1,600 pieces, with around 10,000 lines of text"; [Kelley](../references/kelley-2026.md) gives approximately 1,700 tablets. At least 620 are held in Iran's National Museum and more than a thousand in the Louvre and other collections.

**Englund makes the comparison this vault would otherwise have had to make for itself.** The proto-Elamite corpus is "about a quarter as many as from Babylonia (still, it represents a large amount of material compared to the relatively humble inscriptions of Linear A or of early Harappan)".

So the scholar most associated with the corpus, writing about his own material and with no stake in this vault's argument, places it well above [Linear A](linear-a.md) and the [Indus script](indus-script.md). That is as direct a confirmation as the diagnosis in [why a script stays unread](why-scripts-stay-unread.md) is going to get: proto-Elamite is not short of text.

It is also administrative, which usually helps. What it lacks is a bilingual, a securely identified underlying language, and a descendant script that can be read.

## Why it is stuck, in the words of the person best placed to say

The vault diagnosed proto-Elamite as blocked by **insufficient attention** rather than by evidence. Englund says as much, and more bluntly than a secondary source would.

The texts "have played an historically minor role relative to early cuneiform". The publication of tablets "appears to have proceeded with little understanding of the text corpus and the accounting system it represented, and with little attention paid to an accurate representation in hand copies of the texts themselves". Kelley, writing twenty years later, still describes proto-Elamite scholarship as marginal relative to the script's importance.

That last clause of Englund's is the sharpest of the three, and it is an infrastructure failure rather than a shortage of scholars: if the hand copies are unreliable, then the sign forms everyone works from are unreliable, and no amount of subsequent analysis repairs that. Compare the print-only corpus problem on [Linear A](linear-a.md). Both are cases where the evidence exists and the usable version of it does not.

## A sign list that ran from 5,500 to under 400

Englund records the history, and the spread is the widest in the vault.

- **Mecquenem (1949)**: a final list of "upwards of 5,500 signs", containing large numbers of sign variants.
- **Meriggi (1971-1974)**: grouped presumed variants under discrete headings "and so arrived at a total of less than 400".

A factor of roughly fourteen, on one corpus, from a decision about what counts as a variant. The [Indus script](indus-script.md)'s well-known spread of 20 to 676 is narrower. See [what counts as one sign](segmentation-and-transcription.md).

This also explains why the vault could not state a sign count earlier and why Kelley says only "several hundred non-numerical signs".

## The first archaic Near Eastern script known to anyone

Englund records a fact that reframes the neglect. The late nineteenth and early twentieth century French excavations at [Susa](../places/susa.md) "made that script the first archaic Near Eastern writing system known to us", a quarter of a century before the British and American excavators of Jemdet Nasr and the Germans at Uruk found their proto-cuneiform tablets.

Proto-Elamite was not overlooked because it turned up late. It was there first and was overtaken.

He is also unsparing about how it was recovered: de Morgan's "archaeological earth-moving machine" sent examples to the Louvre. That single phrase accounts for both the Louvre holdings recorded on the [Susa](../places/susa.md) note and for a good deal of what is not known about the material's context.

**The name is a convention, not a finding.** The script is "based on a presumed genetic relationship to texts of the later-attested Elamite-speaking peoples of the Susiana plain" and "has been only conventionally named proto-Elamite". That is why `writes` is empty here.

## Not Linear Elamite

**Proto-Elamite and Linear Elamite are different scripts and the vault must not merge them.** Proto-Elamite is the earlier system described here. Linear Elamite is a later and much smaller corpus, and it appears in this vault first through [Farmer, Sproat and Witzel](../references/farmer-sproat-witzel-2004.md), who use it as a comparison case for the [Indus script](indus-script.md): only 21 or 22 Linear Elamite inscriptions are known, and most are longer than the longest of the 4,000 to 5,000 Indus texts.

That comparison is the reason Linear Elamite deserves a note of its own. It is the cleanest demonstration in the vault that corpus volume and text length are independent variables, and that a very small corpus of long texts can be more tractable than a large corpus of short ones.

Neither script has an ISO 15924 code beyond Proto-Elamite's own: Linear Elamite is absent from the registry, checked on 2026-08-10.

## Encoding

`iso15924` is `Pelm`, numeric 016, assigned 2021-01-25. Note that 016 is outside the 600-699 range reserved for undeciphered scripts, which is consistent with `decipherment_status: partial` but was not verified as a deliberate registry decision.

**There is no Unicode block**, verified against `Blocks.txt`, and none for Linear Elamite either.

## Open questions

- **Kelley 2026 has still not been read**, being paywalled. Englund now carries most of this note, so the dependence on an abstract is much reduced, but the two are twenty years apart and Kelley is the current statement of the field.
- **`class: mixed` is an inference.** A system with understood numerical notation plus several hundred ideographic signs is not an alphabet, abjad, abugida or syllabary, and `mixed` is the closest value in the vault's enum. No source read here classifies it in those terms.
- **The findspots are now partly known and still not counted.** Englund's map of sites with proto-Elamite tablets appears to mark Susa, Sialk, Malyan, Tepe Yahya, Shahr-i Sokhta and Ozbaki. That was read from a figure rather than from prose, and no per-site tablet counts are given, so `found_at` still lists Susa alone.
- ~~The Cuneiform Digital Library Initiative has not been consulted.~~ Its holdings supplied [Englund 2004](../references/englund-2004.md). The catalog itself has still not been queried for a per-site breakdown, which is what would close the question above.
- **Englund's chapter was read only to page 103 of 149.** The sign-list analysis, the accounting systems and the decipherment attempts are all in the part not read.

## Sources

- [Englund 2004](../references/englund-2004.md), for the corpus figures, the sign-list history, the findspots, the priority of Susa and the assessment of the field
- [Kelley 2026](../references/kelley-2026.md), *Proto-Elamite: Writing and Society in Early Iran*, for the dating and the current decipherment status
- [Farmer, Sproat and Witzel 2004](../references/farmer-sproat-witzel-2004.md), for the Linear Elamite comparison
- [ISO 15924](../references/iso15924.md), for `Pelm` 016 and the absence of Linear Elamite, verified against the Unicode Consortium code list
- [Unicode block data](https://www.unicode.org/Public/UNIDATA/Blocks.txt), checked and containing no Proto-Elamite or Elamite block
- [Wikidata Q25474080](https://www.wikidata.org/wiki/Q25474080)
