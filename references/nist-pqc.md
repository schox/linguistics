---
type: Reference
aliases:
  - "NIST post-quantum standards"
authors: "National Institute of Standards and Technology"
year: 2024
title: "Post-Quantum Cryptography project, and the first standards"
container: "NIST Computer Security Resource Center"
ref_type: website
url: "https://csrc.nist.gov/projects/post-quantum-cryptography"
accessed: 2026-08-12
status: read
subfield:
  - Post-quantum cryptography
belongs_to: "[[Cryptography]]"
---

# NIST post-quantum standards

The standardization program that selected the first post-quantum algorithms, and the source used here for the distinction between post-quantum and quantum cryptography.

## What it establishes

- **Three standards released in August 2024**: FIPS 203, Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM); FIPS 204, Module-Lattice-Based Digital Signature (ML-DSA); FIPS 205, Stateless Hash-Based Digital Signature (SLH-DSA). Two further algorithms, Falcon and HQC, are recorded as still undergoing standardization.
- **The purpose**, in the project's terms: securing information "against the future threat of quantum computers, machines that may be years or decades away but could eventually break many of today's widely used cryptographic systems".
- **The distinction from quantum cryptography**, quoted from the Institute's plain-language page and used verbatim in this area's index:

> "Though their names sound the same, they are very different. Post-quantum cryptography is a defense against potential cyberattacks from quantum computers. PQC algorithms are based on mathematical techniques that can be very old, such as elliptic curves, which trace their history back to ancient Greek times. Quantum cryptography, on the other hand, is based fundamentally on quantum physics, which originated in the 20th century."

**What it does not say.** Neither page names Shor's algorithm or Grover's algorithm. The threat is described generally, as quantum computers able to "sift through all of the potential prime factors simultaneously". The attribution of the threat to those two results comes from [Shor 1997](shor-1997.md) and [Grover 1996](grover-1996.md), not from here.

## Access

Free. The project page and the plain-language explainer were both read; the FIPS documents themselves were not, so the algorithms above are recorded by name and number only.

**The year is the release of the first three standards**, not the start or end of the project, which is ongoing. Any citation of a specific algorithm should carry its FIPS number rather than this date.

## Sources

- [Post-Quantum Cryptography project](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [What Is Post-Quantum Cryptography?](https://www.nist.gov/cybersecurity/what-post-quantum-cryptography)
