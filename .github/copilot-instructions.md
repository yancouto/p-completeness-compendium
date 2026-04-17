# Copilot Instructions for P-completeness Compendium

## Build Commands

```bash
hugo server -D          # Development server with drafts
hugo --minify           # Production build (output: public/)
```

No linters are configured.

## Architecture

This is a Hugo static site cataloging P-complete problems from computational complexity theory.

### Content Structure

- **Problems** (`content/problems/*.md`): 186 problem files with YAML frontmatter
- **Bibliography** (`data/bibliography.json`): 379 references indexed by number (e.g., `"127"`)
- **Templates** (`layouts/problems/`): Hugo templates that render problem pages

### Reference System

Problems can reference bibliography entries in two ways:

1. **ID-based** (preferred): `references: [127, 281]` (or strings) - looks up in `data/bibliography.json`
2. **Inline objects** (legacy): `references: [{citation: "...", year: "1986"}]`

The template (`layouts/problems/single.html`) handles both formats. When using IDs, citations display as `[127] Author. Title...`

Each problem page automatically appends the Greenlaw book as the last entry in the rendered references list (using `book_id`). This means the in-text book citation index is always `len(references) + 1`.

Preferred status format is: `$\P$-complete (Author [i], Other Author [j]).`

### Problem File Structure

```yaml
---
title: "Problem Name"
acronym: "ABC"
book_id: "A.1.1"           # Greenlaw et al. reference (auto-added to references)
categories: ["Circuit Complexity"]
status: "p-complete"       # or "open"
confidence: "high"         # data quality indicator
references: ["127", "281"] # bibliography IDs
---

## Input
[Input description with LaTeX: $G = (V, E)$]

## Problem
[Decision question]

## Remarks
[Notes, variants, related results with [127] citations]
```

## Conventions

### LaTeX

- All math must be wrapped in `$...$` delimiters
- Use `\text{NC}`, `\text{P}`, `\text{RNC}` for complexity classes
- Graph notation: `$G = (V, E)$`
- Variables: `$n$`, `$k$`, `$x_1, \ldots, x_n$`

### Categories

P-complete (Appendix A): Circuit Complexity, Graph Theory, Searching Graphs, Combinatorial Optimization, Local Optimality, Logic, Formal Languages, Algebra, Geometry, Real Analysis, Games, Miscellaneous

Open problems (Appendix B): Same categories plus CC, RNC

### File Naming

Problems use `{appendix}-{section}-{number}.md` format:
- `a-1-1.md` for Problem A.1.1
- `b-9-7.md` for Problem B.9.7
