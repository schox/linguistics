---
type: Concept
subfield:
  - Epistemics
  - The problem space
belongs_to: "[[Decipherment]]"
related_to:
  - "[[Cryptography]]"
  - "[[The evidentiary threshold and unicity distance]]"
status: open
---

# Adversarial versus accidental encipherment

The boundary between cryptography and decipherment, and the reason one is the backdrop to the other rather than its parent.

## The distinction

**Cryptography is adversarial.** Someone designed the system specifically to resist you. A key existed and somebody held it. The design is usually known (Kerckhoffs's principle), the difficulty is deliberate and engineered, and the analyst can often obtain more ciphertext, chosen plaintext, or an operator's mistake.

**Decipherment is accidental.** Nobody was hiding anything. A [Linear A](linear-a.md) scribe was recording a commodity transaction for colleagues who read it fluently. The obscurity is a side effect of cultural loss: the reading community died and took the key with it. There is no adversary, no key schedule, no protocol, and crucially no way to obtain more text except by excavation.

## What transfers and what does not

Transfers cleanly: frequency analysis, positional and distributional statistics, entropy and redundancy measures, sign inventory analysis, the underdetermination result (see [The evidentiary threshold and unicity distance](evidentiary-threshold-and-unicity-distance.md)).

Does not transfer: threat models, chosen-plaintext and chosen-ciphertext attacks, key schedules and rotation, side channels, protocol analysis, and the entire apparatus of provable security. There is no adversary to model.

Transfers with distortion: the notion of a "key". In cryptography the key is a discrete object that existed. In decipherment the nearest equivalent is a sign-to-sound mapping plus a language identification, and the second half may have no answer, because the language may have no surviving relatives.

## Consequences

The asymmetry runs the other way in one respect. The cryptanalyst faces an opponent who is actively trying to defeat them, but can usually get more material. The decipherer faces no opposition at all, but the corpus is fixed, was never designed to be self-explanatory, and is usually administrative rather than discursive: inventories and receipts, which are the least informative genre imaginable for recovering a language.

The biographical overlap between the fields is real, though it is easy to overstate. John Chadwick broke Italian naval codes at Alexandria in 1942 and worked on Japanese naval traffic at Bletchley Park in 1944, and he later became Ventris's collaborator on Linear B. But he came to it in 1952 as a Cambridge classicist, not straight from codebreaking, and what he supplied Ventris was Greek dialectology rather than cryptanalysis. See [John Chadwick](../people/john-chadwick.md). The transfer between these fields is genuine at the level of statistical habit, and thinner at the level of career than the story usually suggests.

## Sources

- Kerckhoffs, A. (1883), "La cryptographie militaire", *Journal des sciences militaires* IX, 5-38 and 161-191. [Text](https://www.petitcolas.net/kerckhoffs/crypto_militaire_1.pdf)
- [Shannon 1949](../references/shannon-1949.md) for the formal treatment of the adversarial case
- [Barber 1974](../references/barber-1974.md) for the non-adversarial case
