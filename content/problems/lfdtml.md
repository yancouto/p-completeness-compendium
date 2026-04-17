---
title: "Lexicographically First Different Than Majority Labeling"
acronym: "LFDTML"
book_id: "A.5.8"
categories: ["Local Optimality"]
status: "p-complete"
tags: []
references: [316, 119, 246, 324]
related_problems:
  - id: mcvp
    relation: reduces-from
  - id: umcs
    relation: see-also
  - id: sccm
    relation: see-also
---

## Input

An undirected graph $G = (V, E)$ with a numbering on the vertices and a designated vertex $v$.

## Problem

Is vertex $v$ labeled $1$ in the lexicographically first different than majority labeling?

## Definitions

A *different than majority labeling* is a labeling of the vertices with either $0$ or $1$ such that each vertex is labeled differently than at least half of its neighbors. A greedy sequential algorithm for solving this problem begins by initially assigning the value $0$ to each vertex. The algorithm iterates through the vertices in order flipping a vertex's label if it is not correctly labeled. The flipping process is repeated until the overall labeling is a different than majority labeling. The labeling produced by this algorithm is called the *lexicographically first different than majority labeling*.

## Status

$\P$-complete (Sarnath and He [[1]](#1)).

## Remarks

The reduction to show hardness is from [MCVP]({{< relref "./mcvp.md" >}}). Additional reductions are given in [[2]](#2)[[3]](#3) for other versions of the problem.

The parallel complexity of *Different Than Majority Labeling* (DTML) was posed as an open question by Luby [[3]](#3). DTML was also discussed by Godbeer [[2]](#2) and the problem was reduced to a version of a connectionist model problem, see [SCCM]({{< relref "./sccm.md" >}}). Schäffer and Yannakakis proved the problem to be equivalent to [UMCS]({{< relref "./umcs.md" >}}) [[4]](#4). Therefore, the problem is $\P$-complete. Sarnath and He show that LFDTML remains $\P$-complete when restricted to planar graphs [[1]](#1). They also give another sequential algorithm for the problem and state that a decision problem based on this algorithm is also $\P$-complete [[1]](#1).