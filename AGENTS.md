---
type: Doc
status: living
---

# AGENTS.md

If you are an AI assistant working in this vault: read this file first, then `CONVENTIONS.md`.

## What this vault is

A Tolaria vault for linguistics, human languages, computer languages, and cryptography. A folder of Markdown files with YAML frontmatter plus attachments. It is a git repository with a GitHub remote. Tolaria is the desktop app Andrew uses to browse, edit and commit; any AI assistant can read and write the same files directly.

## What to read, in order

1. This file, for the operating model.
2. `CONVENTIONS.md`, for the folder layout, types, frontmatter and intake rules. This is the contract.
3. The relevant area's `_index.md` for whatever you are working on.

## The model in one paragraph

Content is organised into four areas: `General-Linguistics/`, `Human-Languages/`, `Computer-Languages/` and `Cryptography/`. Markdown notes carry a `type` (`MOC`, `Reference`, `Concept`, `Language`, `ComputerLanguage`, `Cipher`, `Note`, `Media`, `Doc`). Per-area `_index.md` MOC notes list and link the material in that area so the vault stays navigable in Tolaria. This is a reference archive: substantive content is a typed note (`Language`, `ComputerLanguage`, `Cipher`, `Concept`, `Reference`), usually wrapping or linking an attachment, not a raw file dump.

## Rules

1. Australian English. No em-dashes (use commas, parentheses, semicolons).
2. Follow the intake rules and hard exclusions in `CONVENTIONS.md`. This vault is about linguistics and languages, not a place to store real secrets, keys or credentials, even in a Cryptography note about them.
3. Keep original filenames for document attachments (PDF, docx). Images move to the root `attachments/` folder per convention.
4. Set `type` on every new content note, and `belongs_to` the relevant area's `_index.md` where it makes sense.
5. When you add or move files, update the relevant `_index.md` MOC.
6. This vault has a GitHub remote. Commit with descriptive messages. Ask Andrew before pushing unless he has said otherwise.

## Maintenance

There is no automated Downloads-triage routine for this vault yet (unlike the Andrew and Novansa vaults). Material is added deliberately. If Andrew wants a daily maintenance routine added later, mirror the one described in the Andrew/Novansa vaults and add a `_vault-admin/` folder for its logs.

## Cowork / Claude Code notes

- Vault path for Read/Write/Edit: `/Users/andrew/Documents/Tolaria/Linguistics/`.
- In the bash sandbox the files appear under `/sessions/<session>/mnt/...`; translate paths.
- `git` is available. Always check `git status` before assuming the working tree state.
