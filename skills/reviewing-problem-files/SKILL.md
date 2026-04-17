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

## Frontmatter checks

- `status` must be one of: `p-complete`, `p-hard`, `open`.
- `categories`, `tags`, and `related_problems[*].relation` must use values from `data/problem_constraints.yaml`.
- `book_id` is optional for non-book entries.
- `references` can mix bibliography IDs and inline objects.

## Status and citation checks

Prefer status sentence forms:

- `$\P$-complete (...)`
- `$\P$-complete under $\LOGSPACE$ reductions (...)`
- `$\P$-hard (...)`
- `Open (...)`

Body citations should use linked format `[[i]](#i)`.

## Linking checks

- Cross-problem links should use Hugo relref:
  - `[CVP]({{< relref "./cvp.md" >}})`
- Avoid raw relative links like `(./cvp.md)`.

## References policy

- Prefer bibliography IDs when entries already exist in `data/bibliography.json`.
- Use inline reference objects as first-class entries when a bibliography item is missing.
- Ensure each in-text citation index refers to an existing rendered reference item.

## Quick review checklist

1. Frontmatter keys present, ordered consistently, and using allowed vocabularies.
2. Required sections present and in canonical order.
3. Status line uses canonical math notation and linked citations.
4. In-text citations use `[[i]](#i)`.
5. Problem cross-links use `relref`.
6. References are complete (ID-backed or inline object backed).
7. Remarks include reduction source / variants where relevant.
