---
title: "Lexicographically First Maximal k-cycle Free Edge Induced Subgraph"
acronym: "LFEdge"
book_id: "A.2.21"
categories: ["Graph Theory"]
status: "p-complete"
tags: []
references: [264, 265]
related_problems:
  - id: cvp
    relation: reduces-from-variant-of
  - id: mfvs
    relation: see-also
  - id: emas
    relation: see-also
  - id: lf3edge
    relation: see-also
  - id: lfmm
    relation: see-also
  - id: lfms
    relation: see-also
---

## Given

An undirected graph $G = (V, E)$ with an ordering on the edges in $E$ and a designated edge $e \in E$.

## Problem

Is $e$ in the lexicographically first maximal $k$-cycle free edge induced subgraph of $G$?

## Definitions

The *lexicographically first maximal $k$-cycle free edge induced subgraph of $G$* is the graph formed by processing each edge in $E$ in order and adding it to the subgraph being built if it does not form a cycle of size $k$.

## Status

$\P$-complete (Miyano [1, 2]).

## Remarks

The reductions (for different values of $k$) are from several variants of [CVP]({{< relref "./cvp.md" >}}).
For $k = 3, 4, 5, 6$, or $k \geq 7$ with $G$ of maximum degree $6, 4, 4, 3$, or $3$ respectively, the problem is $\P$-complete. For $G$ a planar graph and $k = 4, 5, 6$, or $k \geq 7$ with $G$ of maximum degree $5, 4, 4$, or $3$ respectively, the problem is $\P$-complete. For $G$ a general graph and $k = 3$ or $4$ with $G$ of maximum degree $4$ or $3$ respectively, the problem is in $\NC^2$ [[1]](#1)[[2]](#2). See [MFVS]({{< relref "./mfvs.md" >}}) and [EMAS]({{< relref "./emas.md" >}}) for results with a similar flavor.

It is also interesting to contrast the results for the edge induced subgraph problem with those for the vertex induced subgraph problem; see [LFMS(π)]({{< relref "./lfms.md" >}}). Also see [LF3Edge]({{< relref "./lf3edge.md" >}}) for related open questions. Lastly, note that for $k = 1$ this problem becomes [LFMM]({{< relref "./lfmm.md" >}}); it is in $\CC$.
