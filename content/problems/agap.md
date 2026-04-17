---
title: "Alternating Graph Accessibility Problem"
acronym: "AGAP"
book_id: "A.2.3"
categories: ["Graph Theory"]
status: "p-complete"
tags: []
references: [49, 168, 169, 231, 322, 233, 374]
related_problems:
  - id: am2cvp
    relation: reduces-from
  - id: path
    relation: see-also
  - id: itr
    relation: reduces-to
  - id: phcs
    relation: reduces-to
  - id: hgap
    relation: reduces-to
  - id: rcagap
    relation: reduces-to
---

## Input

A directed graph $G = (V, E)$, a partition $V = A \cup B$ of the vertices, and designated vertices $s$ and $t$.

## Problem

Is $\text{apath}(s, t)$ true?

## Definitions

The predicate $\text{apath}$ is defined as follows. Vertices in $A$ are "universal," those in $B$ are "existential." Such a graph is called an *alternating* graph or an AND/OR graph. The predicate $\text{apath}(x, y)$ holds if and only if:

1. $x = y$, or
2. $x$ is existential and there exists $z \in V$ with $(x, z) \in E$ and $\text{apath}(z, y)$, or
3. $x$ is universal and for all $z \in V$ with $(x, z) \in E$, $\text{apath}(z, y)$ holds.

## Status

$\P$-complete (Chandra, Kozen, and Stockmeyer [[1]](#1), Immerman [[2]](#2)[[3]](#3)).

## Remarks

The reduction to show hardness is from [AM2CVP]({{< relref "./am2cvp.md" >}}). The original proof simulated an alternating Turing machine (ATM) directly to show that AGAP was complete for ATM logarithmic space [[2]](#2). Since $\mathsf{ALOG} = \P$ [[1]](#1), this showed AGAP was $\P$-complete too. When this problem is generalized to hierarchical graphs it remains in $\P$, provided the graph is "breadth-first ordered"; see Lengauer and Wagner [[4]](#4). The proof sketched above also shows that the problem remains $\P$-complete when the partition $(A, B)$ induces a bipartite graph.

When restricted to only existential vertices, the problem is equivalent to the *Directed Graph Accessibility Problem*, variously called "GAP" and "STCON," and shown by Savitch to be complete for $\mathsf{NLOG}$ [[5]](#5). Peterson shows that the undirected version of AGAP is also $\P$-complete. When restricted to undirected graphs with only existential vertices, this problem is equivalent to the *Undirected Graph Accessibility Problem*, called "UGAP" or "USTCON," which is known to be complete for the special case of nondeterministic logarithmic space known as symmetric logarithmic space or $\mathsf{SLOG}$ (Lewis and Papadimitriou [[6]](#6)).

Yasuura shows a generalization of AGAP is $\P$-complete via a reduction to Path Systems ([PATH]({{< relref "./path.md" >}})) [[7]](#7). He considers the graph reachability problem on directed *hypergraphs*, graphs whose edges consist of a subset of vertices and a single vertex.
