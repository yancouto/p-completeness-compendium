---
title: "Maximum Flow"
acronym: "MaxFlow"
problem_id: "A.4.4"
category: "Combinatorial Optimization"
status: "p-complete"
tags: ["flow", "networks", "optimization", "graphs"]
draft: false
references:
  - author: "Goldschlager, L. M., Shaw, R. A., and Staples, J."
    title: "The Maximum Flow Problem Is Log Space Complete for P"
    year: 1982
    citation: "[128]"
related_problems:
  - id: "a-4-5-hf"
    relation: "see-also"
  - id: "a-4-6-lfbf"
    relation: "see-also"
  - id: "b-9-6-01maxflow"
    relation: "see-also"
---

## Given

A directed graph $G = (V, E)$ with positive integer capacities $c(e)$ for each edge $e \in E$, designated source $s$ and sink $t$ vertices, and a positive integer $k$.

## Problem

Is the maximum flow from $s$ to $t$ at least $k$?

## Remarks

The Maximum Flow Problem is one of the most fundamental problems in combinatorial optimization, with applications ranging from transportation and logistics to network routing and matching.

The P-completeness of MaxFlow has significant implications:
- Despite the existence of efficient sequential algorithms (Ford-Fulkerson, Edmonds-Karp, Push-Relabel), no efficient parallel algorithm is known
- The large numbers involved in capacity representations appear essential for P-completeness

**Note:** The restriction to **0-1 capacities** (Problem B.9.6) is an open problem — it is not known to be P-complete or in NC. This suggests the hardness may come from handling large capacity values rather than the flow structure itself.

The related **Lexicographically First Blocking Flow** problem (A.4.6) is also P-complete, showing that specific flow algorithms like Dinic's algorithm are inherently sequential.

Many sequential maximum flow algorithms can be parallelized to run in $O(n^2)$ parallel time, but achieving polylogarithmic time remains open.
