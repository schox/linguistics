---
type: MOC
aliases:
  - "Genealogy and lineages"
area: Computer-Languages
subfield:
  - Genealogy and lineages
belongs_to: "[[Computer Languages]]"
updated: 2026-08-12
---
# Genealogy and lineages

Descent among programming languages, recorded in the `lineage` field.

Stubbed out on 2026-08-12, one level. Nothing here is written beyond what is listed below.

## Notes in this subfield

- [The ALGOL descent](algol-descent.md)
- [The Lisp descent](lisp-descent.md)
- [The ML and typed functional line](ml-and-typed-functional.md)
- [C and its successors](c-and-its-successors.md)
- [Smalltalk and message passing](smalltalk-and-message-passing.md)
- [The scripting languages](the-scripting-languages.md)

## The languages

Selected 2026-08-12 on Andrew's criterion: the most popular languages, plus enough coverage that every paradigm has a member. Two instruments, because neither alone is sufficient.

**Taken by popularity**, from [TIOBE index, August 2026](../references/tiobe-2026-08.md), which measures popularity and says so:

- [Python](python.md) 1, [C](c.md) 2, [C++](cpp.md) 3, [Java](java.md) 4, [C#](csharp.md) 5, [JavaScript](javascript.md) 6, [Visual Basic](visual-basic.md) 7, [Rust](rust.md) 10, [Pascal and Delphi](pascal.md) 11, [Scratch](scratch.md) 12, [PHP](php.md) 13, [Go](go.md) 14, [Fortran](fortran.md) 15, [Ruby](ruby.md) 16, [Swift](swift.md) 17, [Perl](perl.md) 18, [COBOL](cobol.md) 19, [Ada](ada.md) 21, [Objective-C](objective-c.md) 23

Three more from that list are filed under [Domain and non-general-purpose languages](domain-and-non-general-purpose-languages.md), being query or numerical rather than general-purpose: [SQL](sql.md) 8, [R](r.md) 9, [MATLAB](matlab.md) 25.

**Added for coverage**, because popularity alone leaves gaps that are facts about the index rather than about the field:

- [ALGOL](algol.md), [Simula](simula.md), [Smalltalk](smalltalk.md), [ML](ml.md), for the lineages. Four of this area's six named lineages have their origin outside any current ranking.
- [Haskell](haskell.md) and [Erlang](erlang.md), because **no pure functional language appears in the TIOBE top twenty-five**.
- [Prolog](prolog.md), because **no logic language appears in either instrument's list**.
- [APL](apl.md), for the array paradigm and as the boundary case with mathematical notation.
- [Forth](forth.md), the **only concatenative language either instrument names**, and it appears in [GEN 2024](../references/gen-2024.md) rather than in TIOBE.
- [BASIC](basic.md), named in the forty-year set of GEN 2024 as a language that mattered and stopped, which a current snapshot cannot see.

[Lisp](lisp.md) was already written and is named by both instruments.

**Two paradigms still have no language.** Dataflow has none, and declarative has only SQL. Neither instrument names a candidate for dataflow, and the gap is recorded rather than filled by guessing.

**What the selection rests on, stated plainly.** TIOBE is a popularity proxy built from search and vendor data, not a measure of importance or of code in service. GEN 2024 is a self-published blog whose figures are its author's stated best guesses, held only for the set of languages it names and never for its numbers. The additions above are this corpus's own judgement, made to satisfy Andrew's paradigm-coverage criterion, and are marked as additions in each note rather than presented as findings.
