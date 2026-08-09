#!/usr/bin/env python3
"""Consistency checker for the Linguistics vault.

Validates frontmatter, resolves relative links, and checks house style.
No dependencies. Run from anywhere:

    python3 scripts/check-vault.py
    python3 scripts/check-vault.py --quiet     # only failures
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Published titles and proper nouns keep their own spelling. Never normalize these.
PROTECTED = [
    "On automatic decipherment of lost ancient scripts relying on combinatorial "
    "optimisation and coupled simulated annealing",
    "Archaeological Decipherment",
    "Research Organization Registry",
    "Association for Computational Linguistics",
]

# House style is International English (US). Flag British forms in prose.
# Note the explicit endings: "formalism" and "mechanism" are correct in both
# varieties, so a bare "formalis\w*" would produce false positives.
BRITISH = re.compile(
    r"\b(?:"
    r"(?:organis|recognis|standardis|formalis|generalis|visualis|industrialis|"
    r"mechanis|minimis|characteris|normalis|specialis|emphasis(?!\b)|hypothesis(?!\b))"
    r"(?:e|es|ed|ing|ation|ations)"
    r"|catalogu(?:e|es|ed|ing)|programme|programmes|licence|licences|centre|centres"
    r"|colour|colours|coloured|behaviour|behaviours|behavioural"
    r"|palaeo\w+|artefact|artefacts|defence|modelling|labelled|travelled|mediaeval"
    r")\b",
    re.I,
)

VALID_TYPES = {
    "MOC", "Language", "Script", "ComputerLanguage", "Cipher", "Method",
    "Concept", "Person", "Place", "Reference", "Note", "Media", "Doc", "Type",
}

INLINE_CODE = re.compile(r"`[^`]*`")
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def markdown_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for name in sorted(filenames):
            if name.endswith(".md"):
                yield os.path.join(dirpath, name)


def mask_protected(text):
    for i, phrase in enumerate(PROTECTED):
        text = text.replace(phrase, f"\x00P{i}\x00")
    return text


def check(path):
    problems = []
    rel = os.path.relpath(path, ROOT)
    raw = open(path, encoding="utf-8").read()

    # Frontmatter must be present, closed, and declare a known type.
    if not raw.startswith("---\n"):
        problems.append((rel, 1, "missing frontmatter"))
    else:
        end = raw.find("\n---\n", 3)
        if end == -1:
            problems.append((rel, 1, "unclosed frontmatter"))
        else:
            fm = raw[4:end]
            m = re.search(r"^type:\s*(\S+)", fm, re.M)
            if not m:
                problems.append((rel, 1, "no type declared"))
            elif m.group(1) not in VALID_TYPES:
                problems.append((rel, 1, f"unknown type '{m.group(1)}'"))

    if "—" in raw:
        for i, line in enumerate(raw.splitlines(), 1):
            if "—" in line:
                problems.append((rel, i, "em-dash"))

    base = os.path.dirname(path)
    for i, line in enumerate(raw.splitlines(), 1):
        prose = INLINE_CODE.sub("", mask_protected(line))

        hit = BRITISH.search(prose)
        if hit:
            problems.append((rel, i, f"British spelling '{hit.group(0)}'"))

        for m in LINK.finditer(prose):
            target = m.group(1).split("#")[0]
            if not target or target.startswith(("http", "mailto:")):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(base, target))):
                problems.append((rel, i, f"broken link -> {target}"))

    return problems


def main():
    quiet = "--quiet" in sys.argv
    files = list(markdown_files())
    problems = []
    for path in files:
        problems.extend(check(path))

    for rel, line, msg in problems:
        print(f"{rel}:{line}: {msg}")

    if problems:
        print(f"\n{len(problems)} problem(s) across {len(files)} files.")
        return 1
    if not quiet:
        print(f"OK: {len(files)} files. Frontmatter valid, links resolve, style clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
