---
title: "Restricted Chromatic Alternating Graph Accessibility Problem"
acronym: "RCAGAP"
book_id: "A.2.5"
categories: ["Graph Theory"]
status: "p-complete"
tags: []
references: [231]
related_problems:
  - id: agap
    relation: reduces-from
---

## Input

An alternating graph $G = (V, E)$, two natural numbers $k$ and $m$ (where $k \leq m \leq \log |V|$), a coloring $c : E \to \\{1, \ldots, m\\}$, and two vertices $s$ and $t$.

## Problem

Are there $k$ different colors $i_1, \ldots, i_k \in \\{1, \ldots, m\\}$ such that $\text{apath}(s, t)$ holds in the subgraph of $G$ induced by the edges with colors $i_1, \ldots, i_k$?

## Definitions

See [AGAP]({{< relref "./agap.md" >}}). Note that the coloring is an unrestricted assignment of colors to the edges. It may assign the same color to several edges incident to a common vertex.

## Status

$\P$-complete (Lengauer and Wagner [[1]](#1)).

## Remarks

The reduction to show hardness is from [AGAP]({{< relref "./agap.md" >}}). The problem remains $\P$-complete if the vertices are restricted to being breadth-first ordered [[1]](#1). When generalized to hierarchical graphs, the problem becomes $\NP$-complete [[1]](#1).