---
type: Script
class: mixed
period: c. 3300-2900 BCE
decipherment_status: partial
status: open
writes:
found_at:
  - "[[Susa]]"
corpus_size: c. 1,700 clay tablets from eight or nine sites; several hundred non-numerical signs
subfield:
  - Unsolved, partial and contested
  - The problem space
belongs_to: "[[Decipherment]]"
related_to:
  - "[[Indus script]]"
  - "[[Script versus language]]"
  - "[[The evidentiary threshold and unicity distance]]"
cites:
  - "[[Kelley 2026]]"
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

About 1,700 clay tablets, from eight or nine excavation sites across Iran. At least 620 are held in Iran's National Museum and more than a thousand in the Louvre and other collections.

That is a large corpus by this area's standards, comfortably above [Linear A](linear-a.md) in document count and in the same range as the [Indus script](indus-script.md) in objects. It is also administrative, which usually helps. What it lacks is a bilingual, a securely identified underlying language, and a descendant script that can be read.

Kelley notes that Proto-Elamite scholarship has been marginal relative to the script's importance, and that recent progress has come from digitizing the corpus and applying computational methods. That is a rare case in this vault of the constraint being attention rather than evidence.

## Not Linear Elamite

**Proto-Elamite and Linear Elamite are different scripts and the vault must not merge them.** Proto-Elamite is the earlier system described here. Linear Elamite is a later and much smaller corpus, and it appears in this vault first through [Farmer, Sproat and Witzel](../references/farmer-sproat-witzel-2004.md), who use it as a comparison case for the [Indus script](indus-script.md): only 21 or 22 Linear Elamite inscriptions are known, and most are longer than the longest of the 4,000 to 5,000 Indus texts.

That comparison is the reason Linear Elamite deserves a note of its own. It is the cleanest demonstration in the vault that corpus volume and text length are independent variables, and that a very small corpus of long texts can be more tractable than a large corpus of short ones.

Neither script has an ISO 15924 code beyond Proto-Elamite's own: Linear Elamite is absent from the registry, checked on 2026-08-10.

## Encoding

`iso15924` is `Pelm`, numeric 016, assigned 2021-01-25. Note that 016 is outside the 600-699 range reserved for undeciphered scripts, which is consistent with `decipherment_status: partial` but was not verified as a deliberate registry decision.

**There is no Unicode block**, verified against `Blocks.txt`, and none for Linear Elamite either.

## Open questions

- **The volume has not been read.** Everything above comes from the publisher's abstract and landing page for [Kelley 2026](../references/kelley-2026.md). For a note whose whole point is a careful distinction about what "partly deciphered" means, that is thin, and the Element is short enough to read properly.
- **`class: mixed` is an inference.** A system with understood numerical notation plus several hundred ideographic signs is not an alphabet, abjad, abugida or syllabary, and `mixed` is the closest value in the vault's enum. No source read here classifies it in those terms.
- **The eight or nine sites are unnamed here.** Only Susa is recorded under `found_at`. Kelley gives a count and not, on the landing page, a list. Tepe Yahya and Tal-i Malyan are commonly associated with Proto-Elamite in general literature but were not confirmed from a source read.
- **The Cuneiform Digital Library Initiative holds a digitized subset** and is the obvious next source, both for a per-site breakdown and for the corpus itself. It has not been consulted.

## Sources

- [Kelley 2026](../references/kelley-2026.md), *Proto-Elamite: Writing and Society in Early Iran*, for the corpus size, dating, sign inventory and decipherment status
- [Farmer, Sproat and Witzel 2004](../references/farmer-sproat-witzel-2004.md), for the Linear Elamite comparison
- [ISO 15924](../references/iso15924.md), for `Pelm` 016 and the absence of Linear Elamite, verified against the Unicode Consortium code list
- [Unicode block data](https://www.unicode.org/Public/UNIDATA/Blocks.txt), checked and containing no Proto-Elamite or Elamite block
- [Wikidata Q25474080](https://www.wikidata.org/wiki/Q25474080)
