---
type: ComputerLanguage
paradigm: functional, procedural, reflective, meta
lineage: Lisp
first_appeared: 1958
status: reference
influenced_by:
implemented_in:
subfield:
  - Paradigms
  - Genealogy and lineages
  - Formal foundations
belongs_to: "[[Computer Languages]]"
related_to:
  - "[[The Chomsky hierarchy]]"
cites:
hopl_id:
wikidata:
---

# Lisp

Designed by John McCarthy at MIT from 1958, first appearing in 1960. The second-oldest high-level language still in use, and the root of a lineage running through Common Lisp, Scheme, Racket and Clojure.

## Why it belongs in a linguistics vault

Lisp is the cleanest case of a programming language built as a **notation** rather than as an instruction set. McCarthy conceived it as a practical mathematical notation for computer programs, influenced by Church's lambda calculus without being derived from it directly, and the consequence is a language whose [syntax](../General-Linguistics/syntax.md) is its own data structure.

That homoiconicity makes Lisp the strongest test case for the comparison this area is supposed to interrogate. In a natural language the distinction between an utterance and a description of an utterance is carried by quotation and metalanguage, and it is famously slippery. Lisp collapses the distinction deliberately: code and data are the same s-expressions, so a program can construct and evaluate programs. Whether that has any analogue in human language, or whether it marks precisely where the analogy fails, is a question worth an argued note.

It also sits close to [the Chomsky hierarchy](../General-Linguistics/chomsky-hierarchy.md). Lisp's parenthesised syntax is trivially context-free and needs almost no parser, which is one reason macros are tractable in Lisp and painful in languages with richer surface grammar. Syntactic simplicity buys semantic extensibility, which is a trade-off with no clear counterpart in natural language.

## Contributions

Tree data structures, automatic storage management, dynamic typing, conditionals, higher-order functions, recursion as a primary control structure, and the read-eval-print loop. Its influence reaches Python, Ruby, JavaScript, Haskell and Scala.

## Sources

- [Lisp, Wikipedia](https://en.wikipedia.org/wiki/Lisp_(programming_language))
