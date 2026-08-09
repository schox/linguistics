#!/usr/bin/env python3
"""Consistency checker for the Linguistics vault.

Checks, per markdown file:
  * frontmatter present, closed, and declaring a known type
  * required fields present for the note's type
  * field values drawn from the allowed set, where one is defined
  * subfield values valid against the owning area's _index.md
  * wikilink values quoted (unquoted [[X]] is a nested YAML list and fails silently)
  * every relative markdown link resolves
  * every [[wikilink]] resolves to an H1 title or filename
  * content notes end with a ## Sources section
  * no Reference note points at Wikipedia (fine as a source in a note,
    never as an entry in the authoritative bibliography)
  * house style: International English, no em-dashes

Standard library only. Run from anywhere:

    python3 scripts/check-vault.py
    python3 scripts/check-vault.py --quiet    # failures only
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- style ----

# Published titles and proper nouns keep their own spelling. Never normalize.
PROTECTED = [
    "combinatorial optimisation",          # Tamburini 2025, title and its method name
    "Archaeological Decipherment",         # Barber 1974
    "Research Organization Registry",
    "Association for Computational Linguistics",
]

# Stems are matched WITHOUT a leading \b so prefixed forms are caught too
# (reorganise, disorganised). Endings are explicit because "formalism" and
# "mechanism" are correct in both varieties.
BRITISH = re.compile(
    r"\w*(?:organis|recognis|standardis|formalis|generalis|visualis|industrialis|"
    r"mechanis|minimis|characteris|normalis|specialis|analys|romanis|optimis|"
    r"summaris|utilis|prioritis|categoris|emphasis|apologis)"
    r"(?:e|es|ed|ing|ation|ations)\b"
    r"|\b(?:catalogu(?:e|es|ed|ing)|programme|programmes|licence|licences|"
    r"centre|centres|colour|colours|coloured|behaviour|behaviours|behavioural|"
    r"palaeo\w+|artefact|artefacts|defence|modelling|labelled|travelled|mediaeval)\b",
    re.I,
)

# ---------------------------------------------------------------- schema ----

STRUCTURAL = {"MOC", "Doc", "Type"}
CONTENT = {
    "Language", "Script", "ComputerLanguage", "Cipher", "Method",
    "Concept", "Person", "Place", "Note", "Media",
}
VALID_TYPES = STRUCTURAL | CONTENT | {"Reference"}

# Fields every content note must carry.
REQUIRED_COMMON = ["subfield", "belongs_to", "status"]

REQUIRED = {
    "Language":        REQUIRED_COMMON + ["family", "era"],
    "Script":          REQUIRED_COMMON + ["class", "decipherment_status"],
    "ComputerLanguage": REQUIRED_COMMON + ["paradigm", "first_appeared"],
    "Cipher":          REQUIRED_COMMON + ["category", "era"],
    "Method":          REQUIRED_COMMON + ["category"],
    "Concept":         REQUIRED_COMMON,
    "Note":            REQUIRED_COMMON,
    "Person":          ["field", "belongs_to", "status"],
    "Place":           ["kind", "belongs_to", "status"],
    "Media":           ["belongs_to", "status"],
    "Reference":       ["authors", "year", "title", "ref_type", "status", "belongs_to"],
    "MOC":             ["area"],
}

ENUMS = {
    ("Language", "era"): {"living", "historical", "extinct", "reconstructed"},
    ("Language", "status"): {"interested", "learning", "reference", "reading", "fluent"},
    ("Script", "class"): {"alphabet", "abjad", "abugida", "syllabary",
                          "logographic", "mixed", "undetermined"},
    ("Script", "decipherment_status"): {"deciphered", "partial", "contested", "undeciphered"},
    ("Cipher", "category"): {"classical", "mechanical", "symmetric",
                             "asymmetric", "hash", "protocol"},
    ("Cipher", "era"): {"ancient", "medieval", "early modern", "industrial",
                        "mechanical", "computer", "post-quantum"},
    ("Cipher", "status"): {"reference", "historical", "current", "broken"},
    ("ComputerLanguage", "status"): {"using", "reference", "historical", "learning"},
    ("Method", "category"): {"statistical", "combinatorial", "structural",
                             "contextual", "computational"},
    ("Place", "kind"): {"institution", "site", "region", "facility"},
    ("Reference", "ref_type"): {"paper", "book", "chapter", "website",
                                "dataset", "course", "thesis", "corpus"},
    ("Reference", "status"): {"unread", "in-progress", "read"},
    ("Concept", "status"): {"open", "draft", "settled"},
    ("Method", "status"): {"open", "draft", "settled"},
    ("Note", "status"): {"open", "draft", "settled"},
    ("Doc", "status"): {"living", "frozen"},
}

# Which area hub owns each folder, for subfield validation.
AREA_INDEX = {
    "General-Linguistics": "General-Linguistics/_index.md",
    "Human-Languages": "Human-Languages/_index.md",
    "Computer-Languages": "Computer-Languages/_index.md",
    "Cryptography": "Cryptography/_index.md",
    "Decipherment": "Decipherment/_index.md",
}

INLINE_CODE = re.compile(r"`[^`]*`")
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
WIKILINK_UNQUOTED = re.compile(r"^\s*(?:-\s*)?(\w+)\s*:\s*\[\[", re.M)


def parse_frontmatter(raw):
    """Minimal YAML subset: scalars and '- ' lists. Enough for this schema."""
    if not raw.startswith("---\n"):
        return None, "missing frontmatter"
    end = raw.find("\n---\n", 3)
    if end == -1:
        return None, "unclosed frontmatter"
    block, data, key = raw[4:end], {}, None
    for line in block.split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(("  - ", "- ")):
            if key:
                # 'key:' with an empty value parses to None; a following '- item'
                # means it was really a list all along.
                if data.get(key) is None:
                    data[key] = []
                if isinstance(data[key], list):
                    data[key].append(line.split("- ", 1)[1].strip().strip('"'))
            continue
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            key, value = m.group(1), m.group(2).strip()
            data[key] = value.strip('"') if value else None
    return data, None


def subfield_vocab(path):
    """Read the explicit '## Subfield vocabulary' list from an area index.

    Deliberately not inferred from prose headings: the vocabulary is stated,
    so that adding a value is a visible edit rather than a side effect.
    """
    if not os.path.exists(path):
        return set()
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^## Subfield vocabulary\s*\n(.*?)(?=^## )", text, re.M | re.S)
    if not m:
        return set()
    return {
        line[2:].strip()
        for line in m.group(1).split("\n")
        if line.startswith("- ")
    }


def resolvable_targets(files):
    """Every wikilink target Tolaria can resolve: H1 titles and bare filenames."""
    targets = set()
    for path in files:
        targets.add(os.path.basename(path)[:-3])
        m = re.search(r"^#\s+(.+)$", open(path, encoding="utf-8").read(), re.M)
        if m:
            targets.add(m.group(1).strip())
    return targets


def strip_fenced(raw):
    """Blank out fenced code blocks, keeping line numbers stable."""
    out, fenced = [], False
    for line in raw.split("\n"):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            out.append("")
            continue
        out.append("" if fenced else line)
    return "\n".join(out)


def markdown_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for name in sorted(filenames):
            if name.endswith(".md"):
                yield os.path.join(dirpath, name)


def mask(text):
    for i, phrase in enumerate(PROTECTED):
        text = text.replace(phrase, f"\x00P{i}\x00")
    return text


def check(path, vocabs, targets):
    rel = os.path.relpath(path, ROOT)
    raw = open(path, encoding="utf-8").read()
    out = []

    data, err = parse_frontmatter(raw)
    if err:
        return [(rel, 1, err)]

    ntype = data.get("type")
    if not ntype:
        out.append((rel, 1, "no type declared"))
    elif ntype not in VALID_TYPES:
        out.append((rel, 1, f"unknown type '{ntype}'"))
    else:
        for field in REQUIRED.get(ntype, []):
            if field not in data or data[field] in (None, ""):
                out.append((rel, 1, f"{ntype} requires '{field}'"))
        for (t, field), allowed in ENUMS.items():
            if t == ntype and data.get(field) and data[field] not in allowed:
                out.append((rel, 1,
                            f"{field}='{data[field]}' not in {sorted(allowed)}"))
        # subfield must come from the owning area's vocabulary
        area = rel.split(os.sep)[0]
        if area in vocabs and isinstance(data.get("subfield"), list):
            for value in data["subfield"]:
                if value not in vocabs[area]:
                    out.append((rel, 1,
                                f"subfield '{value}' not in {area} vocabulary"))
        # content notes must cite something
        if ntype in CONTENT and "## Sources" not in raw:
            out.append((rel, 1, f"{ntype} note has no '## Sources' section"))

        # references/ is the authoritative bibliography. Wikipedia is a finding
        # aid: welcome under a note's ## Sources, never a Reference of its own.
        if ntype == "Reference":
            for field in ("url", "doi"):
                value = data.get(field)
                if isinstance(value, str) and "wikipedia.org" in value:
                    out.append((rel, 1,
                                f"Reference '{field}' points at Wikipedia; cite the "
                                "work of record instead"))

    # the silent YAML trap
    for m in WIKILINK_UNQUOTED.finditer(raw[:raw.find("\n---\n", 3) + 5]):
        out.append((rel, 1,
                    f"'{m.group(1)}' has an unquoted wikilink; YAML reads it as a list"))

    if "—" in raw:
        for i, line in enumerate(raw.splitlines(), 1):
            if "—" in line:
                out.append((rel, i, "em-dash"))

    # wikilink targets must resolve; examples inside fenced blocks are exempt
    for i, line in enumerate(strip_fenced(raw).split("\n"), 1):
        for m in re.finditer(r"\[\[([^\]]+)\]\]", line):
            if m.group(1).strip() not in targets:
                out.append((rel, i, f"dangling wikilink [[{m.group(1).strip()}]]"))

    base = os.path.dirname(path)
    for i, line in enumerate(raw.splitlines(), 1):
        prose = INLINE_CODE.sub("", mask(line))
        hit = BRITISH.search(prose)
        if hit:
            out.append((rel, i, f"British spelling '{hit.group(0)}'"))
        for m in LINK.finditer(prose):
            target = m.group(1).split("#")[0]
            if not target or target.startswith(("http", "mailto:")):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(base, target))):
                out.append((rel, i, f"broken link -> {target}"))
    return out


def main():
    quiet = "--quiet" in sys.argv
    vocabs = {a: subfield_vocab(os.path.join(ROOT, p)) for a, p in AREA_INDEX.items()}
    files = list(markdown_files())
    targets = resolvable_targets(files)
    problems = []
    for path in files:
        problems.extend(check(path, vocabs, targets))
    for rel, line, msg in problems:
        print(f"{rel}:{line}: {msg}")
    if problems:
        print(f"\n{len(problems)} problem(s) across {len(files)} files.")
        return 1
    if not quiet:
        print(f"OK: {len(files)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
