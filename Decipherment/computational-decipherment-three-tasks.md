---
type: Concept
subfield:
  - Computational method
belongs_to: "[[Decipherment]]"
related_to:
  - "[[General Linguistics]]"
  - "[[Computer Languages]]"
cites:
  - "[[Assael et al. 2022 (Ithaca)]]"
  - "[[Luo, Cao and Barzilay 2019]]"
  - "[[Luo et al. 2021]]"
  - "[[Tamburini 2025]]"
status: open
---

# Computational decipherment: three distinct tasks

Popular coverage runs three different problems together under "AI deciphers ancient language". They differ in what is known at the outset, and conflating them produces persistently overstated claims.

## 1. Restoration and attribution

Script and language are both fully known; the text is physically damaged. The model fills lacunae and estimates date and provenance.

DeepMind's Ithaca does this for Greek inscriptions (Nature, 2022), following Pythia, and Aeneas extends it to Latin. These are useful tools with real epigraphic uptake. **They decipher nothing**, and are routinely misreported as though they do.

## 2. Decipherment proper

The script is unknown; the aim is to map it onto a known language.

Luo, Cao and Barzilay (2019) frame this as minimum-cost flow, learning character-level correspondences without parallel text, evaluated on Ugaritic to Hebrew and Linear B to Greek. Luo et al. (2021) extend it to undersegmented scripts using phonetic priors, which matters because undersegmentation is the normal condition of an undeciphered corpus. Tamburini (2025) reaches higher accuracy with combinatorial optimisation and coupled simulated annealing.

The structural limitation is shared by all of them: **the method needs a correct guess about which known language to align against.** It exploits a relative, it does not find one. Evaluation is possible only on already-solved cases, which means reported accuracy measures performance on problems where the answer was available to check.

## 3. Cognate and related-language search

Neither script nor language is known, and the task is to identify a plausible relative so that task 2 becomes possible at all.

This is where Linear A actually sits. The University of Melbourne project (Brent Davis and Emily Tour, with Robert Turnbull's MDAP team) pre-trains models on candidate related languages and fine-tunes on Linear A to test degrees of relatedness. It is a search for the right hypothesis, not a reading, and it is honest about that.

## The recurring error

Reports of "AI cracking Linear A" typically describe work in category 1 or 3 while implying category 2. Linear A remains undeciphered. Its constraint is the corpus, not the algorithm, and no method in any of these categories addresses corpus size. See [The evidentiary threshold and unicity distance](evidentiary-threshold-and-unicity-distance.md).

Tamburini is explicit on the same point: these systems require segmented and clean corpora, extensive cognate lists, and human paleographic expertise, and assist paleographers rather than replacing them.

## Sources

- [Assael et al. 2022](../references/assael-2022.md), *Restoring and attributing ancient texts using deep neural networks*, Nature 603, 280-283. [DOI](https://www.nature.com/articles/s41586-022-04448-z)
- [Luo, Cao and Barzilay 2019](../references/luo-cao-barzilay-2019.md), [ACL Anthology](https://aclanthology.org/P19-1303/)
- [Luo et al. 2021](../references/luo-2021.md), [TACL](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00354/97780/Deciphering-Undersegmented-Ancient-Scripts-Using)
- [Tamburini 2025](../references/tamburini-2025.md), [Frontiers in AI](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1581129/full)
- [Melbourne MDAP Linear A project](https://www.unimelb.edu.au/mdap/research/2024-collaborations/using-deep-neural-network-models-in-the-decipherment-of-linear-a)
- [Aeneas, Google DeepMind](https://deepmind.google/blog/aeneas-transforms-how-historians-connect-the-past/)
