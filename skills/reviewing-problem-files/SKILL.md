---
name: reviewing-problem-files
description: Use when reviewing or authoring content/problems/*.md entries in this compendium, especially to enforce frontmatter shape, section order, status citation format, and problem-link/reference conventions.
---

# Reviewing Problem Files

## Overview

Use this skill to review new or edited `content/problems/*.md` files for structural consistency.

Core principle: review against corpus conventions, not personal style.

## Canonical file shape

Most files follow this frontmatter order:

`title > acronym > book_id > categories > status > tags > references > related_problems`

Canonical body order:

1. `## Input`
2. `## Problem`
3. `## Definitions` (optional if unnecessary)
4. `## Status`
5. `## Remarks`

In practice, `Input`, `Problem`, `Status`, and `Remarks` should be present.

## Frontmatter & filename checks

- The filename stem in `content/problems/<id>.md` must match the lowercased `acronym` (e.g., `acronym: "MAJPRED"` -> `majpred.md`).
- `title` should be plain text without `$...$` LaTeX delimiters (e.g., `"d-Dimensional ..."` or `"k-Core"` rather than `'$d$-Dimensional ...'`), because `title` is rendered as raw text in the HTML `<title>` element and search autocomplete.
- `status` must be one of: `p-complete`, `p-hard`, `open`.
- `categories`, `tags`, and `related_problems[*].relation` must use values from `data/problem_constraints.yaml`.
  - `tags` is reserved for complexity classes defined in `data/problem_constraints.yaml` (`CC`, `RNC`) and should be `tags: []` for standard problems (not free-form topic keywords).
- `book_id` is optional for non-book entries.
- `references` can mix bibliography IDs and inline objects.

## Content & section checks

- For problems parameterized by a fixed constant (e.g., dimension $d$), `## Input` should state *"For a fixed integer $d \geq \dots$"* rather than listing the fixed parameter as part of the instance input.

## Status and citation checks

Prefer status sentence forms:

- `$\P$-complete (...)`
- `$\P$-complete under $\LOGSPACE$ reductions (...)`
- `$\P$-hard (...)`
- `Open (...)`

Body citations should use linked format `[[i]](#i)`.

## Linking & automated validation checks

- Cross-problem links should use Hugo relref:
  - `[CVP]({{< relref "./cvp.md" >}})`
- Avoid raw relative links like `(./cvp.md)`.
- Always run `uv run python scripts/auto_link_problems.py` (`make autolink`) and `uv run python scripts/auto_link_problems.py --check` to:
  - Validate frontmatter fields against `data/problem_constraints.yaml` and `data/bibliography.json`.
  - Auto-link problem acronyms in prose.
  - Synchronize reciprocal `related_problems` entries (e.g., adding `reduces-to` on the source problem when `reduces-from` is added on a new problem).

## References policy

- Prefer bibliography IDs when entries already exist in `data/bibliography.json`.
- Use inline reference objects as first-class entries when a bibliography item is missing.
- Ensure each in-text citation index refers to an existing rendered reference item.

## Quick review checklist

1. Filename matches lowercased `acronym`, and `title` contains no raw `$...$` LaTeX.
2. Frontmatter keys present, ordered consistently, and using allowed vocabularies (`tags: []` unless `CC`/`RNC`).
3. Required sections present and in canonical order, with fixed parameters stated as fixed in `## Input`.
4. Status line uses canonical math notation and linked citations.
5. In-text citations use `[[i]](#i)`.
6. Problem cross-links use `relref`.
7. References are complete (ID-backed or inline object backed).
8. Remarks include reduction source / variants where relevant.
9. `uv run python scripts/auto_link_problems.py --check` passes with no changes or validation errors.
