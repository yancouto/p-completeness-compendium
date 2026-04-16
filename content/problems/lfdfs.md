---
title: "Lexicographically First Depth-first Search Ordering"
acronym: "LFDFS"
book_id: "A.3.3"
categories: ["Searching Graphs"]
status: "p-complete"
tags: []
references: [300, 12, 133, 186, 145, 152, 334, 85, 86, 135, 379, 325, 366, 55]
related_problems:
  - id: lfmp
    relation: reduces-from
  - id: dfs
    relation: variant
---

## Given

An undirected graph $G = (V, E)$ with fixed ordered adjacency lists, and two designated vertices $u$ and $v$.

## Problem

Is vertex $u$ visited before vertex $v$ in the depth-first search of $G$ induced by the order of the adjacency lists?

## Status

$\P$-complete (Reif [[1]](#1)).

## Remarks

The reduction to show hardness is from [LFMP]({{< relref "./lfmp.md" >}}).

The directed case can be reduced to the undirected case easily. The reduction is dependent on the adjacency lists fixing the order in which the adjacent vertices are examined. The problem remains open if this constraint is relaxed. For example, the problem remains open for graphs presented with all adjacency lists sorted in order of increasing vertex number. The problem remains $\P$-complete if the input graph is given with a fixed vertex numbering and the search order is based on this numbering rather than the fixed ordered adjacency lists ([[2]](#2), Greenlaw [[3]](#3)). Anderson showed that computing just the first branch of the lexicographically first [DFS]({{< relref "./dfs.md" >}}) tree, called the lexicographically first maximal path, is $\P$-complete [[2]](#2), see [LFMP]({{< relref "./lfmp.md" >}}).

Computing the LFDFS tree in planar graphs is $\P$-complete as well [[2]](#2). However, *Planar Directed Depth-first Search* is in $\NC$ (Kao [[4]](#4)). The depth-first search tree constructed in [[4]](#4) is not the lexicographically first. Hagerup shows that a depth-first search tree can be constructed in a planar graph on a PRIORITY CRCW-PRAM using $O(\log n)$ time and $n^3$ processors [[5]](#5). In $\mathsf{RNC}$, it is possible to find some depth-first vertex numbering and the depth-first spanning tree corresponding to it; see [DFS]({{< relref "./dfs.md" >}}). Computing a depth-first vertex numbering for planar graphs is in $\NC$ (He and Yesha [[6]](#6), Smith [[7]](#7)). Computing the lexicographically first depth-first numbering for directed acyclic graphs is in $\NC$ (de la Torre and Kruskal [[8]](#8)[[9]](#9), Greenlaw [[10]](#10), Zhang [[11]](#11)). Determining whether a directed spanning tree of a general graph has a valid [DFS]({{< relref "./dfs.md" >}}) numbering is in $\NC$ (Schevon and Vitter [[12]](#12)). Vitter and Simons give a $\sqrt{n}$ time parallel algorithm for the non-sparse version of the problem [[13]](#13). Computing a LFDFS in a tree structured or outerplanar graph is in $\NC$ (Chlebus et al. [[14]](#14)).
