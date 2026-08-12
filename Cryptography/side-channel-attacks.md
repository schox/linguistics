---
type: Method
aliases:
  - "Side-channel attacks"
category: contextual
subfield:
  - Cryptanalysis
belongs_to: "[[Cryptanalysis]]"
cites:
  - "[[Kocher 1996]]"
status: open
---

# Side-channel attacks

**Stub.** Expected to cover attacks that measure an implementation rather than analyze an algorithm: timing, power, electromagnetic emission and cache behavior, and the constant-time discipline that answers them. The category is `contextual` because the evidence comes from the setting in which the algorithm runs rather than from its output.

## Child topics

- [Timing attacks](timing-attacks.md)
- [Power analysis](power-analysis.md)
- [Electromagnetic analysis](electromagnetic-analysis.md)
- [Cache-timing attacks](cache-timing-attacks.md)
- [Fault injection attacks](fault-injection-attacks.md)


## Sources

- [Kocher 1996](../references/kocher-1996.md), which introduced the timing attack against Diffie-Hellman, RSA and DSS implementations
