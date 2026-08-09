---
type: Doc
status: living
---

# Status

Where the project is up to, as at 2026-08-09. Update this when the picture changes; it is the first thing an incoming agent should read after `AGENTS.md`.

## What exists

The structure is complete and enforced. Five areas, thirteen note types plus `Type` itself, a stated subfield vocabulary per area, an external-identifier scheme, a bibliography, and a checker that fails the build on schema violations. Every type has at least one worked example, named in its type file.

The vault currently holds 72 notes. That is a skeleton with a good spine, not a body of research.

## What is deliberately thin

Content. The areas hold their taxonomy and a handful of exemplars, nothing more:

- **General Linguistics**: 1 note (the Chomsky hierarchy). Ten subfields, nine empty.
- **Human Languages**: 2 notes (Etruscan, Mycenaean Greek). The genealogy is mapped to branch level and almost entirely unpopulated.
- **Computer Languages**: 1 note (Lisp).
- **Cryptography**: 3 notes (Vigenère, and two methods).
- **Decipherment**: the most developed area, 8 notes, because it carries the vault's argument.

## Highest-value next work

Roughly in order, though this is a suggestion and not a plan Andrew has signed off.

1. **Populate the undeciphered scripts as `Script` notes**: Linear A, Indus, Rongorongo, Cypro-Minoan, Proto-Elamite, Phaistos Disc, Voynich. Each with its ISO 15924 code, Unicode block, `corpus_size` and `found_at`. Corpus size is the variable the whole Decipherment argument turns on, so this makes the central claim checkable rather than asserted.
2. **The remaining solved decipherments**: Egyptian hieroglyphs, cuneiform, Maya glyphs, Ugaritic. Each worth a note on *what actually broke it*, which is usually a bilingual, a proper name, or a structural regularity.
3. **People**: Champollion, Ventris, Knorozov, Rawlinson, al-Kindi, the Friedmans, Turing, Kerckhoffs. See the gap list in `people/_index.md`.
4. **The three junction notes still unwritten**, listed at the foot of `_junctions.md`.
5. **Fill identifiers on existing notes.** Several are present but empty (`wikidata`, `wals_code`). They were left empty deliberately rather than guessed.

## Known limitations

- `wikidata` is empty nearly everywhere. It is the universal join key, so filling it is cheap and high value.
- No `Media` notes and nothing in `attachments/` yet.
- No automated intake routine, unlike the Andrew and Novansa vaults. Material is added deliberately.
- The vault has never been tested against Tolaria's actual rendering of the newer types (`Script`, `Method`, `Person`, `Place`). Icons and colors in `types/*.md` are guesses at Tolaria's icon set and may need correcting in the app.

## Open questions for Andrew

- Whether grammatology should move wholesale into Decipherment, or stay split between there and General Linguistics. Deferred once already; `Script` notes currently live in `Decipherment/` regardless of status.
- Whether Noam Chomsky and Donald Knuth should get `Person` notes. Chomsky was deliberately not written because his current status could not be verified and false death reports circulated in 2024; see the living-people rule in `types/person.md`.
