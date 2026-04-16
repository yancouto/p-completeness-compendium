---
title: "Graph Closure"
acronym: "GC"
book_id: "B.1.4"
categories: ["Circuit Complexity"]
status: "p-complete"
tags: []
references:
  - author: "A. Monti"
    title: "On the computational complexity of graph closures"
    year: 1996
    doi: "10.1016/0020-0190(96)00027-0"
  - 208
related_problems:
  - id: ggc
    relation: variant
  - id: mcvp
    relation: see-also
---

## Given

An undirected graph $G = (V, E)$ with $N = |V|$ and a designated edge $e = uv$.

## Problem

Is $e$ in the *$N$-closure* of $G$?

## Definitions

The *$c$-closure* of a graph is the graph obtained from $G$ by repeatedly joining nonadjacent pairs of vertices $u$ and $v$ whose degree sum is at least $c$.

## Status

$P$-complete under $\LOGSPACE$ reductions (Monti [[1]](#1)).

## Remarks

An $O(n^3)$ algorithm solving the problem is given in [[1]](#1).
Monti shows the $(N+k)$-closure problem is $\P$-complete for any (fixed) integer $k$. As for the $(2N-k)$-closure problem, it is trivial for $k \leq 4$, in $\LOGSPACE$ for $k=5$ and $\P$-complete for $k \geq 6$ [[1]](#1). All reductions are from [MCVP]({{< relref "./mcvp.md" >}}).

The problem was stated as "Open" in the classic Greenlaw, Hoover, and Ruzzo book [3], but the completeness was settled shortly after.