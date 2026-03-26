---
title: "About"
---

## About This Compendium

The **P-Complete Problems Compendium** is a collaborative, open-source resource cataloging problems from computational complexity theory that are **P-complete** — problems believed to have no efficient parallel algorithms.

### Why P-Completeness Matters

In complexity theory, we study not just *whether* problems can be solved efficiently, but *how* they can be solved. While the famous **P vs NP** question asks about sequential computation, an equally important question concerns parallel computation:

> **Can all problems with efficient sequential algorithms also be solved efficiently in parallel?**

This is the **NC = P?** question. The complexity class **NC** (Nick's Class) contains problems solvable in polylogarithmic time using polynomially many parallel processors. Clearly NC ⊆ P, but whether P ⊆ NC is a major open problem.

**P-complete problems** are the hardest problems in P to parallelize. They act as a barrier: if *any* P-complete problem is in NC, then P = NC and all polynomial-time problems have efficient parallel algorithms.

### The Greenlaw-Hoover-Ruzzo Book

This compendium is based on the landmark textbook:

> Greenlaw, R., Hoover, H. J., & Ruzzo, W. L. (1995). *Limits to Parallel Computation: P-Completeness Theory*. Oxford University Press.

The book provides:
- A comprehensive introduction to parallel complexity theory
- The theory of P-completeness and NC reductions
- A catalog of over 100 P-complete problems across 12 categories
- A list of problems whose parallel complexity remains open

### Problem Categories

Problems are organized into categories following the book's structure:

**Appendix A: P-Complete Problems**
- A.1 Circuit Complexity
- A.2 Graph Theory
- A.3 Searching Graphs
- A.4 Combinatorial Optimization
- A.5 Local Optimality
- A.6 Logic
- A.7 Formal Languages
- A.8 Algebra
- A.9 Geometry
- A.10 Real Analysis
- A.11 Games
- A.12 Miscellaneous

**Appendix B: Open Problems**
- Problems whose P-completeness or membership in NC is not yet known

---

## Contributing {#contributing}

This compendium is open source and welcomes contributions! Here's how you can help:

### Adding a New Problem

1. **Fork** the repository on GitHub
2. **Create a new problem file** in `content/problems/` following the naming convention: `{section}-{number}-{acronym}.md` (e.g., `a-1-1-cvp.md`)
3. **Use the problem template** with all required fields:

```markdown
---
title: "Problem Name"
acronym: "ACRONYM"
problem_id: "A.X.Y"
category: "Category Name"
status: "p-complete"  # or "open"
tags: ["tag1", "tag2"]
draft: false

[[references]]
  author = "Author Name"
  title = "Paper Title"
  year = 1995
  citation = "[123]"

[[related_problems]]
  id = "a-1-1-cvp"
  relation = "reduces-to"  # or: variant, reduces-from, see-also
---

## Given

Describe the input to the problem. Use LaTeX syntax for math: $x_1, \ldots, x_n$.

## Problem

State the decision question clearly.

## Remarks

Add any additional notes about variants, complexity, algorithms, etc.
```

4. **Submit a Pull Request** with a clear description

### Guidelines

- **Math notation**: Use `$...$` for inline math and `$$...$$` for display math
- **References**: Include the original paper proving P-completeness
- **Related problems**: Link to problems used in reductions
- **Remarks**: Note interesting variants, special cases in NC, approximation algorithms, etc.

### Reporting Issues

Found an error? Have a suggestion? [Open an issue](https://github.com/yourusername/p-complete-compendium/issues) on GitHub.

---

## Contact

This project is maintained by the open-source community. For questions or suggestions, please use GitHub issues.
