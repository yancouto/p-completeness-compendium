---
title: "Lexicographically First Maximal Subgraph for π"
acronym: "LFMS(π)"
book_id: "A.2.16"
categories: ["Graph Theory"]
status: "p-complete"
tags: []
references: [263, 265]
related_problems:
  - id: lfmis
    relation: see-also
  - id: lfmc
    relation: see-also
---

## Given

An undirected graph $G = (V, E)$ with an ordering on $V$, a designated vertex $v$, and a *polynomial time testable*, nontrivial, hereditary property $\pi$.

## Problem

Is $v$ in the lexicographically first maximal subgraph $H$ of $G$ that satisfies $\pi$?

## Definitions

A property is *nontrivial* if there are infinitely many graphs that satisfy the property and at least one graph that does not. A property $\pi$ is *hereditary* on induced subgraphs if whenever $G$ satisfies $\pi$, so do all vertex induced subgraphs.

## Status

$\P$-complete (Miyano [[1]](#1)[[2]](#2)).

## Remarks

The following are examples of properties that meet the criteria stated in the problem: bipartite, chordal, clique ([LFMC]({{< relref "./lfmc.md" >}})), comparability graph, edge graph, forest, independent set ([LFMIS]({{< relref "./lfmis.md" >}})), outerplanar, and planar. Not all problems involving a lexicographically first solution are $\P$-complete. For example, the Lexicographically First Topological Order Problem is complete for $\mathsf{NLOG}$ and the Lexicographic Low Degree Subgraph Membership Problem is $\NP$-complete. For additional remarks relating to this problem see [[3, Chapter 7]](#3).
