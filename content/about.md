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

### Main Reference

This compendium uses the following as a core reference:

> Greenlaw, R., Hoover, H. J., & Ruzzo, W. L. (1995). *Limits to Parallel Computation: P-Completeness Theory*. Oxford University Press.

It is a great reference to learn about P-completeness. This compendium aims to catalog all problems listed there, but also all new developments in the area.

### Formal definition

A *decision problem* is a set of binary strings. An instance of a decision problem is a binary string, and solving it means determining whether it belongs to the set. Sometimes, problems are also called languages, and we say a language *accepts* an input.

It is common to just use *problem* instead of decision problem. Note decision problems always have a binary output. Sometimes, when talking loosely about problems, the output may not be a single bit, but another binary string (or a more complex object). Formally, there are other definitions for these classes of problems (e.g. FP vs P), though usually it is simple to transform the function problem into an equivalent decision problem.

[P](https://complexityzoo.net/Complexity_Zoo:P#p) is the class of problems that have polynomial time sequential algorithms (we usually assume algorithms in the [RAM model](https://en.wikipedia.org/wiki/Random-access_machine), though there are other models, and more formal circuit-based definitions). [NC](https://complexityzoo.net/Complexity_Zoo:N#nc) is the class of problemas that have polylogarithmic time parallel algorithms with polynomially many processors.

A problem is P-complete if:
1. It is in P.
2. Every other problem in P can be reduced to it using an NC reduction.

That means, if $\pi$ is P-complete and $\pi \in \NC$ then $\P \subseteq \NC$ (which is widely believed to be false).

More formally, we say $\pi$ is P-complete *under NC reductions*, just as NP-complete actually means NP-complete under P reductions. Very few authors actually use the wording "NC-complete for P", which is technically more correct, but less used.

Sometimes, more strict reductions are used, such as [$\NC^1$](https://complexityzoo.net/Complexity_Zoo:N#nc1), [$\NC^2$](https://complexityzoo.net/Complexity_Zoo:N#nc2) or [LOGSPACE](https://complexityzoo.net/Complexity_Zoo:L#l) (a.k.a. L), which also work since all these classes are contained in NC.



---

## Contributing {#contributing}

This compendium is open source and welcomes contributions! Here's how you can help:

### Adding a New Problem

1. **Fork** the repository on GitHub
2. **Create a new problem file** in `content/problems/` (e.g., `cvp.md`)
3. **Use the problem template** with all required fields:

```markdown
---
title: "Problem Name"
acronym: "ACRONYM"
book_id: "A.X.Y"  # optional; auto-adds Greenlaw reference
category: "Category Name"
status: "p-complete"  # or "open"
tags: ["tag1", "tag2"]
draft: false
references:
  - author: "Author Name"
    title: "Paper Title"
    year: 1995
    link: "https://example.org/paper"      # optional direct URL
    doi: "10.1145/321941.321942"           # optional DOI (auto-links to doi.org)
related_problems:
  - id = "a-1-1-cvp"
    relation = "reduces-to"  # or: variant, reduces-from, see-also
  - id = "a-1-3-mcvp"
    relation = "see-also"
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
