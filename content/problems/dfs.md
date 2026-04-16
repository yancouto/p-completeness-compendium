---
title: "Directed or Undirected Depth-first Search"
acronym: "DFS"
book_id: "B.9.2"
categories: ["Network Flows"]
status: "open"
tags: ["RNC"]
references: [5, 6, 334, 85, 86, 135]
related_problems:
  - id: lfdfs
    relation: variant
---

## Given

A graph $G = (V, E)$ and a vertex $s$.

## Problem

Construct the depth-first search numbering of $G$ starting from vertex $s$.

## Status

Open (Aggarwal and Anderson [[1]](#1), Aggarwal, Anderson, and Kao [[2]](#2)).

## Remarks

$\mathsf{RNC}$ algorithms are now known for both the undirected [[1]](#1) and directed [[2]](#2) cases, subsuming earlier $\mathsf{RNC}$ results for planar graphs (Smith [[3]](#3)). For directed acyclic graphs, DFS is in $\NC$ (de la Torre and Kruskal [[4]](#4)[[5]](#5), Greenlaw [[6]](#6)).
