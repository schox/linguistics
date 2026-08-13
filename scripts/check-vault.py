#!/usr/bin/env python3
"""Consistency checker for the Linguistics vault.

Checks, per markdown file:
  * frontmatter present, closed, and declaring a known type
  * required fields present for the note's type
  * field values drawn from the allowed set, where one is defined
  * subfield values valid against the owning area's _index.md
  * wikilink values quoted (unquoted [[X]] is a nested YAML list and fails silently)
  * every relative markdown link resolves
  * every [[wikilink]] resolves to a filename, alias or H1 title
  * every note whose H1 title differs from its filename carries that title
    in `aliases` (Obsidian resolves wikilinks by filename or alias only,
    so without the alias every title-style wikilink at the note breaks)
  * content notes end with a ## Sources section
  * no Reference note points at Wikipedia (fine as a source in a note,
    never as an entry in the authoritative bibliography)
  * a Reference of ref_type news or preprint declares claim_status and
    peer_reviewed, so an announcement cannot be filed as if it were a
    finding of record
  * every file in attachments/ is referenced by a note, and that note
    records where the file came from
  * the note count stated in STATUS.md matches the actual number of notes
  * house style: International English, no em-dashes

Standard library only. Run from anywhere:

    python3 scripts/check-vault.py
    python3 scripts/check-vault.py --quiet    # failures only
    python3 scripts/check-vault.py --report   # advisory sweep worklist, never fails
    python3 scripts/check-vault.py --stubs    # taxonomy stubs, and which lack a source

The checks above are enforcement: they resolve every link that exists. They
are blind in one direction, because nothing detects a link that is *missing*,
and that is how the graph decays quietly. --report covers that direction. It
is advisory, exits 0 whatever it finds, and is deliberately tuned to
over-report: a false positive costs a glance, a miss costs a broken join.
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
    "UNESCO World Heritage Centre",          # the body is named this
    "Easter Island Artefacts",               # Berthin 2024, title
    "Third Programme",                       # the BBC service was named this
    "Centre for Applied Cryptographic Research",   # the Waterloo centre is named this
    "Palaeohispanic",                        # the scripts and languages are named this in the field
]

# Stems are matched WITHOUT a leading \b so prefixed forms are caught too
# (reorganise, disorganised). Endings are explicit because "formalism" and
# "mechanism" are correct in both varieties.
BRITISH = re.compile(
    r"\w*(?:organis|recognis|standardis|formalis|generalis|visualis|industrialis|"
    r"mechanis|minimis|characteris|normalis|specialis|romanis|optimis|"
    r"summaris|utilis|prioritis|categoris|emphasis|apologis|civilis|hypothesis"
    r"|criticis|systematis|theoris|synthesis)"
    r"(?:e|es|ed|ing|ation|ations)\b"
    # 'analys' is handled separately: 'analyses' is the correct plural of
    # 'analysis' in every variety, so the 'es' ending must not fire here.
    r"|\w*analys(?:e|ed|ing)\b"
    r"|\b(?:catalogu(?:e|es|ed|ing)|programme|programmes|licence|licences|"
    r"centre|centres|colour|colours|coloured|behaviour|behaviours|behavioural|"
    r"neighbour|neighbours|neighbouring|honour|honours|honoured|favour|favours|"
    r"favoured|favourite|favourites|labour|labours|endeavour|endeavours|"
    r"rumour|rumours|humour|humours|vapour|vapours|odour|odours|armour|"
    r"savour|savours|splendour|fervour|harbour|harbours|"
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
    # Artifacts are attributed like any other claim: an image with no
    # recorded origin cannot be checked by a reader and cannot be relied on.
    "Media":           ["belongs_to", "status", "credit", "license",
                        "source_url", "retrieved"],
    "Reference":       ["authors", "year", "title", "ref_type", "status", "belongs_to"],
    "MOC":             ["area"],
}

ENUMS = {
    ("Language", "era"): {"living", "historical", "extinct", "reconstructed"},
    ("Language", "status"): {"interested", "learning", "reference", "reading", "fluent"},
    # 'logosyllabary' rather than 'logographic', following the Unicode
    # Standard: pure logography is not attested at scale. 'mixed' and
    # 'undetermined' are local terms with no counterpart in the sources;
    # types/script.md says what they mean and when not to use them.
    # 'featural' is deliberately absent until a note needs it.
    ("Script", "class"): {"alphabet", "abjad", "abugida", "syllabary",
                          "logosyllabary", "mixed", "undetermined"},
    ("Script", "decipherment_status"): {"deciphered", "partial", "contested", "undeciphered"},
    ("Cipher", "category"): {"classical", "mechanical", "symmetric",
                             "asymmetric", "hash", "protocol"},
    # 'unknown' exists for taxonomy stubs: a Cipher note requires an era, and
    # a stub asserts nothing about its subject, so it declares the era unknown
    # rather than dating the cipher from recall. See DECISIONS.md 2026-08-12.
    ("Cipher", "era"): {"ancient", "medieval", "early modern", "industrial",
                        "mechanical", "computer", "post-quantum", "unknown"},
    ("Cipher", "status"): {"reference", "historical", "current", "broken"},
    ("ComputerLanguage", "status"): {"using", "reference", "historical", "learning"},
    ("Method", "category"): {"statistical", "combinatorial", "structural",
                             "contextual", "computational"},
    ("Place", "kind"): {"institution", "site", "region", "facility"},
    # 'news' and 'preprint' exist because decipherment claims are announced
    # long before, and often instead of, being published. Such an item is not
    # a source for facts about the script; it is primary evidence that a
    # claim was made, by whom, and when. Filing it as a paper would lend it
    # an authority it has not earned.
    ("Reference", "ref_type"): {"paper", "book", "chapter", "website",
                                "dataset", "course", "thesis", "corpus",
                                "news", "preprint"},
    ("Reference", "claim_status"): {"peer-reviewed", "preprint",
                                    "press-release", "press-coverage",
                                    "self-published", "unpublished"},
    ("Reference", "peer_reviewed"): {"true", "false", "unknown"},
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
    """Every wikilink target Obsidian can resolve: bare filenames and aliases.

    H1 titles are included too, but only because the alias rule makes every
    H1 an alias; the title itself is not resolvable in Obsidian, which is
    exactly what the alias check below exists to guarantee.
    """
    targets = set()
    for path in files:
        targets.add(os.path.basename(path)[:-3])
        raw = open(path, encoding="utf-8").read()
        m = re.search(r"^#\s+(.+)$", raw, re.M)
        if m:
            targets.add(m.group(1).strip())
        data, _ = parse_frontmatter(raw)
        aliases = (data or {}).get("aliases")
        if isinstance(aliases, str):
            aliases = [aliases]
        for alias in aliases or []:
            targets.add(alias)
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

        # An announcement must declare what kind of claim it is. Decipherment
        # claims are routinely reported as settled by outlets that did not
        # check, and the difference between a press release and a reviewed
        # result is the whole of the vault's defense against repeating them.
        if ntype == "Reference" and data.get("ref_type") in ("news", "preprint"):
            for field in ("claim_status", "peer_reviewed"):
                if not data.get(field):
                    out.append((rel, 1,
                                f"ref_type '{data['ref_type']}' requires "
                                f"'{field}'"))

        # references/ is the authoritative bibliography. Wikipedia is a finding
        # aid: welcome under a note's ## Sources, never a Reference of its own.
        if ntype == "Reference":
            for field in ("url", "doi"):
                value = data.get(field)
                if isinstance(value, str) and "wikipedia.org" in value:
                    out.append((rel, 1,
                                f"Reference '{field}' points at Wikipedia; cite the "
                                "work of record instead"))

    # Obsidian resolves wikilinks by filename or alias, never by H1 title,
    # so a note titled differently from its filename must alias the title.
    m = re.search(r"^#\s+(.+)$", raw, re.M)
    if m:
        title, base_name = m.group(1).strip(), os.path.basename(rel)[:-3]
        if title not in (base_name, base_name + ".md"):
            aliases = data.get("aliases")
            if isinstance(aliases, str):
                aliases = [aliases]
            if title not in (aliases or []):
                out.append((rel, 1,
                            f"H1 '{title}' missing from aliases; title-style "
                            "wikilinks at this note will not resolve in Obsidian"))

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


# ---------------------------------------------------------------- sweep ----

# Notes worth linking to from prose. References are reached through `cites`
# rather than by name, and structural notes are scaffolding.
LINKABLE = CONTENT

# Words that open a capitalized phrase without making it a proper noun.
ARTICLES = {"The", "A", "An", "This", "That", "These", "Those", "Its", "Their"}

# Vault furniture and section headings, which are capitalized but are not
# subjects anyone would want a note about.
SWEEP_STOP = {
    "Sources", "Open questions", "Subfields", "Notes", "Documents", "Images",
    "Scripts", "Fields", "Identifiers", "Subfield vocabulary", "Current entries",
    "Obvious gaps", "See", "Compare", "Where", "Worked", "Prefer", "Every",
    "Use", "Do", "Read", "Run", "Keep", "Give", "Never", "Write", "Mark",
    "Wikipedia", "Markdown", "YAML", "Unicode", "Tolaria", "Obsidian", "Bases",
    "BCE", "CE", "ISO", "DOI", "CC", "MOC", "CLDF",
}

# Accented letters are part of a name: Vigenère must not truncate to 'Vigen'.
NAME_CHAR = r"[a-zA-ZÀ-ÿ'’\-]"

PROPER = re.compile(
    rf"\b(?:al-|el-|ibn )?[A-ZÀ-Þ]{NAME_CHAR}+"   # al-Kindi keeps its prefix
    rf"(?:\s+(?:of|the|and|von|van|de|du|di)\s+[A-ZÀ-Þ]{NAME_CHAR}+"
    rf"|\s+[A-ZÀ-Þ]{NAME_CHAR}+){{0,3}}"
)

POSSESSIVE = re.compile(r"['’]s$")

SENTENCE_START = re.compile(r"(?:^|[.!?:;]\s+|[-*>|]\s+|\*\*|\"|\()\s*$")


def blank_frontmatter(raw):
    """Blank the frontmatter block, keeping line numbers stable."""
    if not raw.startswith("---\n"):
        return raw
    end = raw.find("\n---\n", 3)
    if end == -1:
        return raw
    head = raw[:end + 5]
    return "\n" * head.count("\n") + raw[end + 5:]


def blank_section(text, heading):
    """Blank one '## Heading' section. Citations are not prose."""
    out, dropping = [], False
    for line in text.split("\n"):
        if line.startswith("## "):
            dropping = line.strip() == heading
        out.append("" if dropping else line)
    return "\n".join(out)


def prose_of(raw):
    """Body prose, line numbers preserved.

    Markdown links keep their display text rather than being blanked, so a
    link pointing somewhere other than the note it names still reads as a
    mention. That is the case worth catching: linear-b.md links the words
    'Linear A' at the Decipherment index because no Linear A note existed yet.
    """
    text = blank_frontmatter(raw)
    text = strip_fenced(text)
    text = blank_section(text, "## Sources")
    text = INLINE_CODE.sub(" ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", r"\1", text)
    return text


def outbound(raw, base):
    """Everything this note already links, by resolved path and by wikilink.

    Frontmatter is deliberately included: `related_to: "[[X]]"` is a link.
    """
    paths, wikis = set(), set()
    text = strip_fenced(raw)
    for m in LINK.finditer(text):
        target = m.group(1).split("#")[0]
        if target and not target.startswith(("http", "mailto:")):
            paths.add(os.path.normpath(os.path.join(base, target)))
    for m in re.finditer(r"\[\[([^\]]+)\]\]", text):
        wikis.add(m.group(1).split("|")[0].strip())
    return paths, wikis


def note_index(files):
    """Title, path and type for every note."""
    notes = []
    for path in files:
        raw = open(path, encoding="utf-8").read()
        data, err = parse_frontmatter(raw)
        m = re.search(r"^#\s+(.+)$", raw, re.M)
        notes.append({
            "path": path,
            "rel": os.path.relpath(path, ROOT),
            "title": m.group(1).strip() if m else os.path.basename(path)[:-3],
            "type": (data or {}).get("type"),
            "raw": raw,
        })
    return notes


def unlinked_mentions(notes):
    """Notes naming an existing note in prose without linking to it anywhere.

    'Anywhere' is deliberate: the house style is to link on first mention, so
    a note that already links a target is satisfied however often it repeats
    the name afterwards.
    """
    targets = [n for n in notes
               if n["type"] in LINKABLE and len(n["title"]) >= 4]
    rows = []
    for note in notes:
        # Doc and Type notes name entities to illustrate a rule, not to make a
        # claim about them, so linking those mentions would be noise. DECISIONS
        # is append-only besides. References are reached through `cites`.
        if note["type"] in {"Type", "Reference", "Doc"}:
            continue
        paths, wikis = outbound(note["raw"], os.path.dirname(note["path"]))
        lines = prose_of(note["raw"]).split("\n")
        hits = []
        for target in targets:
            if target["path"] == note["path"] or target["path"] in paths:
                continue
            if target["title"] in wikis:
                continue
            if os.path.basename(target["path"])[:-3] in wikis:
                continue
            pattern = re.compile(r"\b" + re.escape(target["title"]) + r"\b", re.I)
            for i, line in enumerate(lines, 1):
                found = pattern.search(line)
                if found:
                    hits.append((i, found.start(), found.end(), target))
                    break
        # 'Etruscan' inside 'Etruscan alphabet' is one mention, not two
        for hit in hits:
            i, start, end, target = hit
            if any(o is not hit and o[0] == i and o[1] <= start and o[2] >= end
                   and len(o[3]["title"]) > len(target["title"]) for o in hits):
                continue
            rows.append((note["rel"], i, target["title"], target["rel"]))
    return sorted(rows)


def recurring_proper_nouns(notes):
    """Capitalized phrases in two or more notes that have no note of their own.

    Heuristic, and it says so. A single-word candidate is dropped if the same
    word appears lowercase somewhere in the vault, which is a cheap stand-in
    for a dictionary. A candidate that only ever appears at the start of a
    sentence is dropped too, since that capital carries no information.
    """
    known = set()
    for note in notes:
        known.add(note["title"].lower())
        known.add(os.path.basename(note["path"])[:-3].replace("-", " ").lower())

    lowercase_vocab = set()
    for note in notes:
        lowercase_vocab.update(re.findall(r"\b[a-zà-ÿ]{2,}\b", note["raw"]))

    seen, mid_sentence = {}, set()
    for note in notes:
        if note["type"] not in LINKABLE | {"MOC"}:
            continue
        for line in prose_of(note["raw"]).split("\n"):
            if line.startswith("#"):
                continue
            for m in PROPER.finditer(line):
                phrase = m.group(0).strip()
                words = phrase.split()
                while words and words[0] in ARTICLES:
                    words.pop(0)
                if not words:
                    continue
                # "Ventris's" and "Ventris" are the same name
                words[-1] = POSSESSIVE.sub("", words[-1])
                phrase = " ".join(w for w in words if w)
                if not phrase or phrase.lower() in known or phrase in SWEEP_STOP:
                    continue
                if len(words) == 1 and phrase.lower() in lowercase_vocab:
                    continue
                seen.setdefault(phrase, set()).add(note["rel"])
                if not SENTENCE_START.search(line[:m.start()]):
                    mid_sentence.add(phrase)

    rows = [(len(where), phrase, sorted(where))
            for phrase, where in seen.items()
            if len(where) >= 2 and phrase in mid_sentence]
    return sorted(rows, key=lambda r: (-r[0], r[1]))


def open_questions(files):
    """Harvest every '## Open questions' bullet in the vault.

    ROADMAP.md holds judgement: what is worth doing, in what order, and what
    is blocked on something only Andrew can supply. It deliberately does not
    list the individual questions, because a hand-copied list of eighty items
    goes stale the first time a note is edited. This regenerates it instead.
    """
    rows = []
    for path in files:
        raw = open(path, encoding="utf-8").read()
        body, collecting = [], False
        for line in strip_fenced(raw).split("\n"):
            if line.startswith("## "):
                collecting = line.strip() == "## Open questions"
                continue
            if collecting and line.startswith("- "):
                body.append(line[2:].strip())
        if body:
            rows.append((os.path.relpath(path, ROOT), body))

    total = sum(len(b) for _, b in rows)
    print(f"Open questions: {total} across {len(rows)} notes\n")
    print("  Harvested from '## Open questions' sections. This is the live")
    print("  list; ROADMAP.md holds the ordering and the blockers.\n")
    for rel, body in sorted(rows):
        print(f"{rel}")
        for item in body:
            # the bolded lead-in is the question; the rest is the detail
            m = re.match(r"\*\*(.+?)\*\*", item)
            print(f"  - {m.group(1) if m else item[:100]}")
        print()
    return 0


def report(files):
    notes = note_index(files)

    rows = unlinked_mentions(notes)
    print("Unlinked mentions")
    print("  A note names an existing note in prose but never links to it.")
    print("  House style is to link on first mention only.\n")
    if not rows:
        print("  (none)\n")
    for rel, line, title, target in rows:
        print(f"  {rel}:{line}: '{title}' -> {target}")

    rows = recurring_proper_nouns(notes)
    print("\nRecurring names with no note")
    print("  Capitalized phrases in two or more notes. Feeds the inclusion")
    print("  tests in types/person.md and types/place.md. Heuristic: expect")
    print("  false positives, and judge each against the test rather than")
    print("  writing a note for everything listed.\n")
    if not rows:
        print("  (none)")
    for count, phrase, where in rows:
        print(f"  {count:2d}  {phrase}")
        print(f"      {', '.join(where)}")
    return 0


def attachment_provenance(files):
    """Every artifact must be traceable to where it came from.

    The evidentiary standard applies to files as much as to sentences: a PDF
    or a plate scan with no recorded origin cannot be checked by a reader and
    should not be relied on. Prose cannot be enforced, but this can, so it is.

    An artifact passes if some note references it and that note records the
    origin, either by being a `Media` note (whose required fields carry
    credit, license, source and retrieval date) or by carrying a
    `## Provenance` section.
    """
    adir = os.path.join(ROOT, "attachments")
    if not os.path.isdir(adir):
        return []

    artifacts = {}
    for dirpath, dirnames, filenames in os.walk(adir):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for name in filenames:
            if name.startswith("."):          # .gitkeep, .DS_Store
                continue
            full = os.path.join(dirpath, name)
            artifacts[os.path.relpath(full, ROOT)] = []
    if not artifacts:
        return []

    for path in files:
        rel = os.path.relpath(path, ROOT)
        raw = open(path, encoding="utf-8").read()
        data, err = parse_frontmatter(raw)
        if err:
            continue
        for target in LINK.findall(raw):
            target = target.split("#")[0].strip()
            if not target or "://" in target:
                continue
            resolved = os.path.normpath(
                os.path.join(os.path.dirname(path), target))
            key = os.path.relpath(resolved, ROOT)
            if key in artifacts:
                artifacts[key].append((rel, data, raw))

    out = []
    for key in sorted(artifacts):
        refs = artifacts[key]
        if not refs:
            out.append((key, 1, "artifact referenced by no note, so nothing "
                                "records where it came from"))
        elif not any(d.get("type") == "Media" or "## Provenance" in r
                     for _, d, r in refs):
            named = ", ".join(sorted({n for n, _, _ in refs}))
            out.append((key, 1,
                        f"no recorded provenance; referenced by {named}. Needs "
                        "a Media note, or a '## Provenance' section in a "
                        "referencing note"))
    return out


def stubs(files):
    """List every taxonomy stub, flagging those with no source yet.

    Advisory, never fails. This exists because the source requirement was
    relaxed for stubs while the taxonomy is being built (see `DECISIONS.md`,
    2026-08-12). A stub may carry '**To be researched.**' under `## Sources`
    instead of a citation. That is a temporary state, and it is only safe if
    the set of notes in it can be listed exactly, which is what this does.

    Run it before declaring the taxonomy finished. Every note it lists as
    unsourced needs either a reference or deletion.
    """
    sourced, unsourced = [], []
    for path in files:
        rel = os.path.relpath(path, ROOT)
        raw = open(path, encoding="utf-8").read()
        if not re.search(r"^\*\*Stub\.\*\*", raw, re.M):
            continue
        body = raw.split("## Sources", 1)
        pending = len(body) < 2 or "To be researched" in body[1]
        (unsourced if pending else sourced).append(rel)

    print("Taxonomy stubs\n")
    print(f"  {len(sourced) + len(unsourced)} stubs: "
          f"{len(sourced)} with a source, {len(unsourced)} awaiting one.\n")
    if unsourced:
        print("  Awaiting a source. Each needs a reference or deletion before")
        print("  the taxonomy is called finished.\n")
        for rel in unsourced:
            print(f"    {rel}")
    if sourced:
        print("\n  Already sourced.\n")
        for rel in sourced:
            print(f"    {rel}")
    return 0


def status_count(files):
    """STATUS.md states a note count. Check it against reality.

    Added after that number silently drifted from 107 to 132 across eight
    batches, because the edits updating it were string replacements that
    matched nothing and failed quietly. STATUS.md is the first thing an
    incoming agent reads, so a wrong figure there is worse than none.
    """
    path = os.path.join(ROOT, "STATUS.md")
    if not os.path.exists(path):
        return []
    raw = open(path, encoding="utf-8").read()
    m = re.search(r"The vault currently holds (\d[\d,]*) notes", raw)
    if not m:
        return [("STATUS.md", 1,
                 "no 'The vault currently holds N notes' line to check against")]
    stated = int(m.group(1).replace(",", ""))
    if stated != len(files):
        line = raw[:m.start()].count("\n") + 1
        return [("STATUS.md", line,
                 f"states {stated} notes; the vault has {len(files)}")]
    return []


def main():
    quiet = "--quiet" in sys.argv
    vocabs = {a: subfield_vocab(os.path.join(ROOT, p)) for a, p in AREA_INDEX.items()}
    files = list(markdown_files())
    if "--report" in sys.argv:
        return report(files)
    if "--questions" in sys.argv:
        return open_questions(files)
    if "--stubs" in sys.argv:
        return stubs(files)
    targets = resolvable_targets(files)
    problems = []
    for path in files:
        problems.extend(check(path, vocabs, targets))
    problems.extend(attachment_provenance(files))
    problems.extend(status_count(files))
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
