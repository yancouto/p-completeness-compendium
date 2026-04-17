---
title: "Nonempty k-Core"
acronym: "NE-k-Core"
book_id: "A.2.7"
categories: ["Graph Theory"]
status: "p-complete"
tags: []
references:
  - 14
  - author: "Y. S. Couto and C. G. Fernandes"
    title: "Hardness of Dynamic Core and Truss Decompositions"
    year: 2025
    doi: "10.1007/978-3-032-06706-7_5"
related_problems:
  - id: am2cvp
    relation: reduces-from
  - id: kcore
    relation: variant
---

## Input

An undirected graph $G = (V, E)$ and an integer $k$.

## Problem

Is the $k$-core of $G$ nonempty?

## Definitions

The *$k$-core* of a graph is its maximum subgraph with minimum degree at least $k$. It is unique.

## Status

$\P$-complete (Anderson and Mayr [[1]](#1)).

## Remarks

The reduction to show hardness is from [AM2CVP]({{< relref "./am2cvp.md" >}}), and it follows even when $k \leq 3$ (NE-3-Core) on graphs of maximum degree 4.

Let the core value $C(G)$ of $G$ be the largest $k$ such that its $k$-core is nonempty. We can consider the optimization problem of finding $C(G)$ for the graph. Note that this is exactly the *degeneracy* of $G$.

For any $\epsilon > 0$, there is a $(2+\epsilon)$-approximation algorithm for finding $C(G)$ [[1]](#1), that is, computing $x$ such that $C(G) \leq x \leq (2+\epsilon)C(G)$. Furthermore, computing any $(2-\epsilon)$-approximation is $\P$-hard.

This is a direct variant of [k-Core]({{< relref "./kcore.md" >}}), though it might be easier than [k-Core]({{< relref "./kcore.md" >}}) in some contexts. For example, NE-[k-Core]({{< relref "./kcore.md" >}}) in chordal graphs is in $\NC$ (as it follows directly from finding maximal cliques in chordal graphs, which is in $\NC$), while [k-Core]({{< relref "./kcore.md" >}}) on chordal graphs is open.