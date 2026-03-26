---
title: "Lexicographically First Depth-First Search Ordering"
acronym: "LFDFS"
problem_id: "A.3.3"
category: "Searching Graphs"
status: "p-complete"
tags: ["graphs", "dfs", "depth-first-search", "lexicographic", "ordering"]
draft: false
references:
  - author: "Reif, J. H."
    title: "Depth-First Search is Inherently Sequential"
    year: 1985
    citation: "[300]"
related_problems:
  - id: "a-3-1-lfmp"
    relation: "see-also"
  - id: "b-9-2-dfs"
    relation: "see-also"
---

## Given

An undirected graph $G = (V, E)$ with fixed ordered adjacency lists, and two designated vertices $u$ and $v$.

## Problem

Is vertex $u$ visited before vertex $v$ in the depth-first search of $G$ induced by the order of the adjacency lists?

## Remarks

This result demonstrates that depth-first search is **inherently sequential** — there is no efficient parallel algorithm for computing the DFS ordering unless P = NC.

**Hint:** Follows easily from Problem A.3.1 (LFMP), since the leftmost path in the lexicographically first depth-first search tree is the lexicographically first maximal path (Anderson [12]).

Reif gives a direct reduction from NORCVP (Problem A.1.5) to LFDFS, taking advantage of the fixed order by which adjacency lists are examined [300]. The directed case is presented, from which the undirected case is easily derived.

Without loss of generality, assume gates are numbered in topological order. A gadget replaces each NOR gate $i$ having inputs $i_1$ and $i_2$, and outputs to gates $j_1$ and $j_2$. The gadget has eight vertices and uses careful edge orderings to simulate gate evaluation through the DFS traversal order.

**Open problems:** The general question of computing *any* DFS ordering in parallel (Problem B.9.2) remains open — it is not known to be P-complete or in NC.
