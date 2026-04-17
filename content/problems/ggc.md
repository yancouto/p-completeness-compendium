---
title: "General Graph Closure"
acronym: "GGC"
book_id: "A.2.19"
categories: ["Graph Theory"]
status: "p-complete"
tags: []
references: [208]
related_problems:
  - id: mcvp
    relation: reduces-from
  - id: gc
    relation: variant
---

## Input

An undirected graph $G = (V, E)$, a subset $E' \subseteq V \times V$ with $E' \cap E = \varnothing$, and a designated edge $e = (u, v) \in E'$.

## Problem

Is $e$ in the general closure $G(G, E')$ of $G$? 

## Definitions

The *general closure* of $G$ is the graph obtained from $G$ by repeatedly joining nonadjacent pairs of vertices $u$ and $v$ whose degree sum is at least $|V|$ and such that $(u, v) \in E'$. The edges in $E'$ are called *admissible edges*.

## Status

$\P$-complete (Khuller [[1]](#1)).

## Remarks

An $O(n^3)$ algorithm solving the problem is given in [[1]](#1).
The reduction to show hardness is from [MCVP]({{< relref "./mcvp.md" >}}).

This was initially modified from the *Graph Closure Problem* ([GC]({{< relref "./gc.md" >}})), in which $E' = V \times V - E$, since it was an open problem. However, it has now been proved $\P$-complete.
