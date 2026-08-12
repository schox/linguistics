---
type: Concept
aliases:
  - "The Chomsky hierarchy"
subfield:
  - Formal foundations
  - Computational linguistics
belongs_to: "[[General Linguistics]]"
related_to:
  - "[[Computer Languages]]"
status: open
---

# The Chomsky hierarchy

The same formalism claimed by two fields, and the cleanest junction between General Linguistics and Computer Languages.

## The hierarchy

Chomsky (1956) classifies formal grammars by the restrictions on their production rules, giving a strict containment: regular (type 3) inside context-free (type 2) inside context-sensitive (type 1) inside recursively enumerable (type 0). Each class corresponds to a machine that recognizes it: finite automaton, pushdown automaton, linear bounded automaton, Turing machine.

## Two careers

In **computer science** it became foundational infrastructure. Regular expressions are type 3, and the reason a regular expression cannot match balanced brackets is precisely that the language is not regular. Parser generators, BNF and the whole compiler front end sit on the context-free layer.

In **linguistics** it was a claim about human language, and a contested one. The long argument over whether natural language is context-free came to a head with Shieber's demonstration of cross-serial dependencies in Swiss German, generally taken to show that natural language exceeds context-free power. This produced the mildly context-sensitive formalisms (TAG, CCG, minimalist grammars) that aim to be just powerful enough.

## Why the junction matters here

It is the concrete case for treating computer languages as a linguistic subject rather than a metaphor. The same mathematics describes both, but the questions differ: for a programming language the grammar is *stipulated* and the interesting problem is efficient parsing; for a human language the grammar is *hypothesized* and the interesting problem is whether the hypothesis is true of speakers.

There is also a decipherment angle worth pursuing: measures of structural complexity on an undeciphered corpus are attempts to locate it on something like this scale, which connects to [Is it writing at all?](../Decipherment/is-it-writing-at-all.md)

## Sources

- Chomsky, N. (1956), "Three models for the description of language", *IRE Transactions on Information Theory* 2(3), 113-124. [DOI](https://doi.org/10.1109/TIT.1956.1056813)
- Chomsky, N. (1959), "On certain formal properties of grammars", *Information and Control* 2(2), 137-167. [DOI](https://doi.org/10.1016/S0019-9958(59)90362-6)
- Shieber, S. (1985), "Evidence against the context-freeness of natural language", *Linguistics and Philosophy* 8(3), 333-343. [DOI](https://doi.org/10.1007/BF00630917)
- Hopcroft, J. and Ullman, J. (1979), *Introduction to Automata Theory, Languages, and Computation*, Addison-Wesley
