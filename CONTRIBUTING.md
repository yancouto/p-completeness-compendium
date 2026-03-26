# Contributing to the P-Complete Problems Compendium

Thank you for your interest in contributing! This is an open-source project and we welcome contributions of all kinds.

## Ways to Contribute

### Adding a New Problem

1. **Fork** the repository on GitHub
2. **Create a new problem file** in `content/problems/`
3. **Submit a Pull Request**

### Problem File Format

Create a file named `{appendix}-{section}-{number}-{acronym}.md`, for example:
- `a-1-1-cvp.md` for Problem A.1.1 (Circuit Value Problem)
- `b-5-3-integergcd.md` for Problem B.5.3 (Integer GCD)

Use this template:

```markdown
---
title: "Full Problem Name"
acronym: "ABBREV"
book_id: "A.X.Y"  # optional; auto-adds Greenlaw reference
category: "Category Name"
status: "p-complete"  # or "open" for Appendix B problems
tags: ["tag1", "tag2", "tag3"]
draft: false

[[references]]
  author = "Author, A. B."
  title = "Paper Title"
  year = 1995
  link = "https://example.org/paper"      # optional direct URL
  doi = "10.1145/321941.321942"           # optional DOI (auto-links to doi.org)

[[related_problems]]
  id = "a-1-1-cvp"
  relation = "reduces-to"  # or: variant, reduces-from, see-also
---

## Given

Describe the input. Use LaTeX: $x_1, \ldots, x_n$, $G = (V, E)$, etc.

## Problem

State the decision question.

## Remarks

Additional notes about:
- Variants and special cases
- Related complexity results
- Known algorithms and their parallel complexity
- Historical context
```

### Categories

Use the standard category names from the book:

**Appendix A (P-Complete):**
- Circuit Complexity
- Graph Theory
- Searching Graphs
- Combinatorial Optimization
- Local Optimality
- Logic
- Formal Languages
- Algebra
- Geometry
- Real Analysis
- Games
- Miscellaneous

**Appendix B (Open):**
- Graph Theory, Combinatorial Optimization, Logic, Formal Languages, Algebra, Geometry, Real Analysis, CC, RNC

### Writing Guidelines

1. **Math notation**: Use `$...$` for inline math, `$$...$$` for display math
2. **Be precise**: Follow the exact problem formulation from the reference
3. **Include references**: Always cite the original P-completeness proof
4. **Link related problems**: Use the `related_problems` field
5. **Explain reductions**: In remarks, briefly describe the reduction hint
6. **Reference mentions in remarks**: You can refer to numbered references as `[1]`, `[2]`, etc., matching the order shown in the References section

### Reporting Issues

Found an error? [Open an issue](../../issues) with:
- The problem ID (e.g., A.1.1)
- Description of the error
- Suggested correction with reference

### Improving Documentation

Documentation improvements are always welcome:
- Clarifying explanations
- Adding examples
- Fixing typos
- Improving the "About" page

## Development Setup

To run the site locally:

1. Install [Hugo](https://gohugo.io/installation/) (extended version)
2. Clone the repository
3. Run `hugo server -D` from the project root
4. Open http://localhost:1313 in your browser

## Code of Conduct

Please be respectful and constructive in all interactions. This is an academic resource and we value accuracy and clarity.

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.
