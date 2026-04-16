---
title: "k-Truss"
acronym: "k-Truss"
categories: ["Graph Theory"]
status: "p-complete"
tags: []
references:
  - author: "Y. S. Couto and C. G. Fernandes"
    title: "Hardness of Dynamic Core and Truss Decompositions"
    year: 2025
    doi: "10.1007/978-3-032-06706-7_5"
  - author: "K. Saito and T. Yamada"
    title: "Extracting Communities from Complex Networks by the k-dense Method"
    year: 2006
    doi: "10.1109/ICDMW.2006.76"
related_problems:
  - id: am2cvp
    relation: reduces-from
  - id: kcore
    relation: variant
---

## Given

An undirected graph $G = (V, E)$, an edge $e$, and an integer $k$.

## Problem

Is $e$ contained in the $k$-truss of $G$?

## Definitions

The *$k$-truss* of a graph is its maximum subgraph with no isolated vertices such that each edge is contained in at least $k-2$ triangles. It is unique.

## Status

$\P$-complete (Couto and Fernandes [[1]](#1)).

## Remarks

The reduction to show hardness is from [AM2CVP]({{< relref "./am2cvp.md" >}}), and it is given in [[1]](#1) for dynamic algorithms, though it easily translates to $\P$-completeness. It follows for when $k \geq 4$. When $k \leq 3$ it can be solved using triangle detections, which is in $\NC$.

This is a generalization of the [k-Core]({{< relref "./kcore.md" >}}), and each $k$-truss is also a $(k-1)$-core.
The "$k-2$ triangles" in the definition of $k$-truss is awkward, and used so it matches more neatly with $k$-core.
Saito and Yamada generalize all these concepts using the $k$-dense model, where $k$-core is 1-level $(k+1)$-dense, $k$-truss is 2-level $k$-dense and $k$-clique union is $(k-1)$-level $k$-dense, see [[2]](#2) for full definitions. They provide a $\P$ algorithm for $k$-dense extraction.