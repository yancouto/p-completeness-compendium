---
title: "Nearest Neighbor Traveling Salesman Heuristic"
acronym: "NNTSH"
book_id: "A.2.15"
categories: ["Graph Theory"]
status: "p-complete"
tags: []
references: [212]
related_problems:
  - id: nandcvp
    relation: reduces-from
  - id: ts2opt
    relation: see-also
---

## Given

A finite set $C = \\{C_1, \ldots, C_n\\}$ of cities, and a distance matrix $D$ with entries $(d_{ij})$ that are positive integers ($1 \leq i, j \leq n$), and two distinguished vertices $s$ and $l$.

## Problem

Does the nearest neighbor tour starting at s visit l as the last vertex before completing the tour at s?

## Definitions

The *nearest neighbor tour* is a greedy heuristic that always chooses the nearest unvisited vertex as the next vertex on the tour.

## Status

$\P$-complete (Kindervater, Lenstra, and Shmoys [[1]](#1)).

## Remarks

The reduction to show hardness is from [NANDCVP]({{< relref "./nandcvp.md" >}}).

The *nearest merger*, *nearest insertion*, *cheapest insertion*, and *farthest insertion* heuristics are all $\P$-complete [[1]](#1). The *double minimum spanning tree* and *nearest addition* heuristics are in $\NC$ [[1]](#1). See [TS2Opt]({{< relref "./ts2opt.md" >}}).