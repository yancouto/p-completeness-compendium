---
title: "Lexicographically First Maximal Matching"
acronym: "LFMM"
book_id: "B.8.2"
categories: ["CC"]
status: "open"
tags: ["graphs", "matching", "lexicographic", "open-problem"]
draft: false
references:
  - author: "Cook, S. A."
    title: "An Overview of Computational Complexity"
    year: 1983

related_problems:
  - id: "b-9-7-mm"
    relation: "see-also"
  - id: "b-8-3-sm"
    relation: "see-also"
---

## Given

An undirected graph $G = (V, E)$ with a fixed total ordering on the edges $e_1 < e_2 < \cdots < e_m$, and a specific edge $e$.

A **matching** is a set of edges with no shared vertices. A matching is **maximal** if no edge can be added without violating this property.

## Problem

Is edge $e$ contained in the **lexicographically first maximal matching**? This is the matching found by the greedy algorithm that considers edges in order $e_1, e_2, \ldots$ and includes each edge if and only if it shares no vertices with previously included edges.


## Status

Open (not known to be P-complete or in NC) [1].

## Remarks

This problem is known to be in **CC** (the comparator circuit class) but its exact complexity is open:
- It is not known to be P-complete
- It is not known to be in NC

This is one of several natural problems related to stable marriage and matching that fall into the comparator circuit complexity class.

**Related open problems:**
- **Stable Marriage (SM)** — Problem B.8.3
- **Maximum Matching (MM)** — Problem B.9.7

The greedy nature of the lexicographic ordering makes this problem resistant to parallelization, similar to other lexicographically-first problems in this compendium.

