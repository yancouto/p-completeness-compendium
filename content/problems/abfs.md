---
title: "Alternating Breadth-first Search"
acronym: "ABFS"
book_id: "A.3.6"
categories: ["Searching Graphs"]
status: "p-complete"
tags: []
references: [12, 271, 196]
related_problems:
  - id: mm
    relation: see-also
  - id: pme
    relation: see-also
  - id: cvp
    relation: reduces-from-variant-of
  - id: nandcvp
    relation: reduces-from
---

## Given

An undirected graph $G = (V, E)$ with $E$ partitioned into two sets $M$ and $U$, a designated vertex $v$, and a designated start vertex $s$.

## Problem

Does vertex $v$ get visited along an edge from the set $M$ during an alternating breadth-first search of $G$?

## Definitions

An *alternating breadth-first search*, which has applications in some matching algorithms, is a breadth-first search in which only edges in the set $U$ ($M$) can be followed in going from even (respectively, odd) to odd (respectively, even) levels.

## Status

$\P$-complete (Anderson [[1]](#1), Greenlaw, Hoover and Ruzzo [[4]](#4)).

## Remarks


The reduction to show hardness is from a variant of [CVP]({{< relref "./cvp.md" >}}) with OR and NOT gates, or from [NANDCVP]({{< relref "./nandcvp.md" >}}).
The matching constructed by the search is not necessarily maximal. The problem of finding a *maximum matching* is in $\mathsf{RNC}$ (Mulmuley, Vazirani, and Vazirani [[2]](#2)). The problem of finding a *perfect matching* is also in $\mathsf{RNC}$ (Karp, Upfal, and Wigderson [[3]](#3)[[2]](#2)). See [MM]({{< relref "./mm.md" >}}) and [PME]({{< relref "./pme.md" >}}).
