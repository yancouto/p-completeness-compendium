---
title: "Lexicographically First Maximal Matching"
acronym: "LFMM"
problem_id: "B.8.2"
category: "CC"
status: "open"
tags: ["graphs", "matching", "lexicographic", "open-problem"]
draft: false
references:
  - author: "Cook, S. A."
    title: "An Overview of Computational Complexity"
    year: 1983
    citation: "[67]"
related_problems:
  - id: "b-9-7-mm"
    relation: "see-also"
  - id: "b-8-3-sm"
    relation: "see-also"
---

## Given

A graph $G = (V, E)$ with a fixed ordering on the edges, and an edge $e$.

## Problem

Is edge $e$ in the lexicographically first maximal matching of $G$?

## Remarks

A **maximal matching** is a matching (set of vertex-disjoint edges) that cannot be extended by adding another edge. The **lexicographically first** maximal matching is found by the greedy algorithm that examines edges in order and adds each edge if it doesn't share a vertex with any previously selected edge.

This problem is known to be in **CC** (the comparator circuit class) but its exact complexity is open:
- It is not known to be P-complete
- It is not known to be in NC

This is one of several natural problems related to stable marriage and matching that fall into the comparator circuit complexity class.

**Related open problems:**
- **Stable Marriage (SM)** — Problem B.8.3
- **Maximum Matching (MM)** — Problem B.9.7

The greedy nature of the lexicographic ordering makes this problem resistant to parallelization, similar to other lexicographically-first problems in this compendium.
