---
title: "Maximum Flow"
acronym: "MaxFlow"
book_id: "A.4.4"
categories: ["Combinatorial Optimization"]
status: "p-complete"
tags: ["flow", "networks", "optimization", "graphs"]
draft: false
references:
  - author: "Goldschlager, L. M., Shaw, R. A., and Staples, J."
    title: "The Maximum Flow Problem Is Log Space Complete for P"
    year: 1982

related_problems:
  - id: "a-4-5-hf"
    relation: "see-also"
  - id: "a-4-6-lfbf"
    relation: "see-also"
  - id: "b-9-6-01maxflow"
    relation: "see-also"
---

## Given

A **flow network**: a directed graph $G = (V, E)$ with a **source** vertex $s$ (no incoming edges), a **sink** vertex $t$ (no outgoing edges), and a positive integer **capacity** $c(e)$ for each edge $e \in E$. Also given is a positive integer $k$.

A **flow** assigns a non-negative value $f(e)$ to each edge such that:
- $f(e) \le c(e)$ for all edges (capacity constraint)
- For every vertex except $s$ and $t$, the total flow in equals the total flow out (conservation)

The **value** of a flow is the total flow leaving $s$ (equivalently, entering $t$).

## Problem

Is the maximum possible flow value from $s$ to $t$ at least $k$?


## Status

P-complete via NC reduction [1].

## Remarks

The Maximum Flow Problem is one of the most fundamental problems in combinatorial optimization, with applications ranging from transportation and logistics to network routing and matching.

The P-completeness of MaxFlow has significant implications:
- Despite the existence of efficient sequential algorithms (Ford-Fulkerson, Edmonds-Karp, Push-Relabel), no efficient parallel algorithm is known
- The large numbers involved in capacity representations appear essential for P-completeness

**Note:** The restriction to **0-1 capacities** (Problem B.9.6) is an open problem — it is not known to be P-complete or in NC. This suggests the hardness may come from handling large capacity values rather than the flow structure itself.

The related **Lexicographically First Blocking Flow** problem (A.4.6) is also P-complete, showing that specific flow algorithms like Dinic's algorithm are inherently sequential.

Many sequential maximum flow algorithms can be parallelized to run in $O(n^2)$ parallel time, but achieving polylogarithmic time remains open.

