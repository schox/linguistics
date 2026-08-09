---
type: MOC
area: cross-cutting
updated: 2026-08-09
---

# External data sources

What already exists in each area as curated, structured data, and how this vault relates to it.

The governing decision: **adopt external identifiers, link out, do not mirror.** Where a mature catalogue exists, this vault stores its identifier and defers to it rather than duplicating it. A copied dataset silently goes stale, and there is no value in maintaining a worse version of Glottolog. See "Mirroring" below for the exception.

## The four areas are not equally served

### Linguistics and human languages: mature

Best served by a long way, and worth studying closely because it is a working proof of the model this vault uses. The **CLLD** (Cross-Linguistic Linked Data) ecosystem at the Max Planck Institute is built on exactly these principles: curated entities, stable identifiers, typed relationships, open licensing, and its own visualisations.

- [Glottolog](references/glottolog.md) catalogues the world's languages, dialects and families, renders the genealogy as navigable trees, and assigns every languoid a stable **Glottocode**. CC BY 4.0, versioned with a DOI.
- [WALS](references/wals-2013.md) holds typological features (word order, tone, alignment) as citable authored chapters over a queryable data layer, mappable geographically. CC BY 4.0. Complete and frozen.
- [CLDF](references/forkel-et-al-2018.md) is the interchange standard underneath it all, and the model this vault imitates: reference catalogues supply identifiers, datasets cite the identifiers rather than restating the entities.
- **Ethnologue** is the large commercial catalogue alongside these. Proprietary and paywalled, so link only, never copy.

Consequence for this vault: genealogy is a safe canonical spine for Human Languages because Glottolog already maintains the tree. `Language` notes carry `glottocode`, `iso639_3`, `wals_code` and `wikidata`, so a note can be joined to real data instead of paraphrasing it.

### Scripts: well standardised, thinly catalogued

[ISO 15924](references/iso15924.md) gives every script a four-letter and numeric code, maintained by the Unicode Consortium, with a numeric range (600-699) reserved for undeciphered scripts. Unicode encoding covers many ancient scripts including Linear A and Linear B.

But there is no Glottolog for scripts: no curated relational dataset of script descent, borrowing and adaptation. The Latin alphabet's descent from Phoenician through Greek and Etruscan is well established scholarship and not, as far as I can find, an open structured dataset. A gap.

### Computer languages: good graphs, thinner curation

The relationship data exists but is scattered across separate projects rather than consolidated.

- [HOPL](references/hopl.md) is the closest to a real database: 8,945 languages with roughly 7,800 influence links.
- [Language Lineage](references/languagelineage.md) is an interactive graph of 152 languages and 443 relationships, recording the unusual and more specific relation *implemented in*, which captures compiler bootstrapping.
- [stereobooster's genealogical tree](https://github.com/stereobooster/programming-languages-genealogical-tree) and [Éric Lévénez's timeline](https://www.levenez.com/lang/) cover the same ground in other forms.

Licensing is mostly unstated, so treat these as link-only.

### Constructed languages: hobbyist patchwork

[CALS](references/cals.md), the Conlang Database, FrathWiki, and structured lists in Wikidata. Less rigorous than the natural-language side, but the ambition to structure it the same way is unmistakable, which is itself evidence that the WALS model generalises.

### Cryptography: essentially unstructured

The thinnest of the four. There are good narrative timelines (Wikipedia, vendor histories from Entrust and IBM) and at least one well-made interactive walkthrough in the [Cipher Museum](https://ciphermuseum.com/). What does not appear to exist is any treatment of cryptographers, ciphers and breakthroughs as a curated relational dataset with an influence or cryptanalysis graph.

**This is the open field.** For the other four areas, structuring work here largely duplicates something better maintained elsewhere. For cryptography it does not, which means the `Cipher` and `Method` notes in this vault, and the `broken_by` relation in particular, are original structuring work rather than a local copy of someone else's. Worth knowing when deciding where to spend effort.

## Identifiers used in this vault

| Type | Fields |
|---|---|
| `Language` | `glottocode`, `iso639_3`, `wals_code`, `wikidata` |
| `Script` | `iso15924`, `iso15924_num`, `unicode_block`, `wikidata` |
| `ComputerLanguage` | `hopl_id`, `wikidata`, plus `influenced_by` as an internal graph edge |
| `Cipher` | `wikidata` only; no domain scheme exists |

Wikidata Q-numbers are the universal fallback and the join key of last resort across all four.

## Mirroring

The exception to link-only. If a subset genuinely needs to be held locally, for offline work or because a note depends on a specific historical state of the data, then:

1. Only mirror what the licence permits. Glottolog and WALS are CC BY 4.0 and may be reused with attribution. Ethnologue and most of the programming-language projects may not.
2. Record the exact version and DOI of what was taken.
3. Store it in CLDF rather than an invented schema, so it stays interoperable.
4. Mark it clearly as a snapshot with a date, so nobody mistakes it for live data.

WALS is safer to mirror than Glottolog, being complete and no longer updated.

## Sources

- [CLLD, Cross-Linguistic Linked Data](https://clld.org/)
- [Glottolog](https://glottolog.org/)
- [WALS Online](https://wals.info/)
- [CLDF specification](https://cldf.clld.org/) and [Forkel et al. 2018, Scientific Data](https://www.nature.com/articles/sdata2018205)
- [ISO 15924, Unicode Consortium](https://www.unicode.org/iso15924/iso15924-codes.html)
- [HOPL](https://hopl.info/home.prx)
- [Programming Language Lineage](https://www.languagelineage.org/)
- [stereobooster, programming languages genealogical tree](https://github.com/stereobooster/programming-languages-genealogical-tree)
- [Éric Lévénez, language timeline](https://www.levenez.com/lang/)
- [Conlang Atlas of Language Structures](https://www.frathwiki.com/Conlang_Atlas_of_Language_Structures)
- [The Conlang Database](https://database.conlang.org/)
- [The Cipher Museum](https://ciphermuseum.com/)
