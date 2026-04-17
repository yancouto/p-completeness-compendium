---
title: "αβ-Bcore"
acronym: "αβ-Bcore"
categories: ["Graph Theory"]
status: "p-complete"
tags: []
references:
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

An undirected bipartite graph $G = (A \cup B, E)$, a vertex $v$, and integers $\alpha$ and $\beta$.

## Problem

Is $v$ contained in the $(\alpha,\beta)$-bcore of $G$?

## Definitions

The *$(\alpha,\beta)$-bcore* of a graph is its maximum subgraph such that each vertex in $A$ has degree at least $\alpha$ and each vertex in $B$ has degree at least $\beta$. It is unique.

## Status

$\P$-complete (Couto and Fernandes [[1]](#1)).

## Remarks

The reduction to show hardness is from [AM2CVP]({{< relref "./am2cvp.md" >}}), and it is given in [[1]](#1) for dynamic algorithms, though it easily translates to $\P$-completeness.

This is a generalization of the [k-Core]({{< relref "./kcore.md" >}}) for directed graphs.