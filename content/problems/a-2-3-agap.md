---
title: "Alternating Graph Accessibility Problem"
acronym: "AGAP"
problem_id: "A.2.3"
category: "Graph Theory"
status: "p-complete"
tags: ["graphs", "accessibility", "and-or-graphs", "alternating"]
draft: false
references:
  - author: "Immerman, N."
    title: "Languages that Capture Complexity Classes"
    year: 1987
    citation: "[168, 169]"
  - author: "Chandra, A. K., Kozen, D., and Stockmeyer, L. J."
    title: "Alternation"
    year: 1981
    citation: "[49]"
related_problems:
  - id: "a-1-4-am2cvp"
    relation: "reduces-from"
  - id: "a-2-4-hgap"
    relation: "variant"
---

## Given

A directed graph $G = (V, E)$, a partition $V = A \cup B$ of the vertices, and designated vertices $s$ and $t$.

## Problem

Is $\text{apath}(s, t)$ true?, where **apath** is defined recursively as follows. Vertices in $A$ are "universal" (AND vertices), those in $B$ are "existential" (OR vertices). The predicate $\text{apath}(x, y)$ holds if and only if:

1. $x = y$, or
2. $x$ is existential and there exists a $z \in V$ with $(x, z) \in E$ and $\text{apath}(z, y)$, or
3. $x$ is universal and for all $z \in V$ with $(x, z) \in E$, $\text{apath}(z, y)$ holds.

## Remarks

Such a graph is called an **alternating graph** or an **and/or graph**. The problem captures the essence of P-completeness: deciding whether a configuration is reachable in an alternating computation.

**Hint for reduction:** Reduce from AM2CVP (Problem A.1.4). Create two existential vertices labeled 0 and 1. Put edge $(x_i, 0)$ into $E$ if input $x_i$ is 0, and edge $(x_i, 1)$ if input $x_i$ is 1. AND gates become universal vertices and OR gates become existential vertices. Inputs to a gate correspond to children in the alternating graph. For output gate $z$ of the circuit, $\text{apath}(z, 1)$ holds if and only if the output is 1.

The original proof simulated an alternating Turing machine (ATM) directly to show AGAP was complete for ATM logarithmic space [168]. Since ALOG = P [49], this shows AGAP is P-complete.

When this problem is generalized to hierarchical graphs, it remains in P provided the graph is "breadth-first ordered" (see Lengauer and Wagner [231]).

The problem remains P-complete when the partition $(A, B)$ induces a bipartite graph. When restricted to only existential vertices, the problem is equivalent to the **Directed Graph Accessibility Problem** (GAP/STCON), shown by Savitch to be complete for NLOG [322].

Peterson shows that the undirected version of AGAP is also P-complete.
