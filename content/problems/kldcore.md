---
title: "KL-Dcore"
acronym: "KL-Dcore"
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

## Given

A directed graph $G = (V, E)$, a vertex $v$, and integers $k$ and $l$.

## Problem

Is $v$ contained in the $(k,\ell)$-dcore of $G$?

## Definitions

The *$(k,\ell)$-dcore* of a directed graph is its maximum subgraph such that each vertex has in-degree at least $k$ and out-degree at least $\ell$. It is unique.

## Status

$\P$-complete (Couto and Fernandes [[1]](#1)).

## Remarks

The reduction to show hardness is from [AM2CVP]({{< relref "./am2cvp.md" >}}), and it is given in [[1]](#1) for dynamic algorithms, though it easily translates to $\P$-completeness. It follows when $\max(k, \ell) \leq 2$. When $\max(k, \ell) \leq 1$ it can be solved using strongly connected components and reachability, which are in $\NC$.


This is a generalization of the [k-Core]({{< relref "./kcore.md" >}}) for directed graphs.