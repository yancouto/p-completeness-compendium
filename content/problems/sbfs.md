---
title: "Stack Breadth-first Search"
acronym: "SBFS"
book_id: "A.3.5"
categories: ["Searching Graphs"]
status: "p-complete"
tags: []
references: [133, 135, 85, 86]
related_problems:
  - id: sam2cvp
    relation: reduces-from
---

## Given

An undirected graph $G = (V, E)$ with a numbering on the vertices, and two designated vertices $u$ and $v$.

## Problem

Is vertex $u$ visited before vertex $v$ in the stack breadth-first search of $G$ induced by the vertex numbering?

## Definitions

A *stack breadth-first search* is a breadth-first search that is implemented using a stack. The vertices most recently visited on a new level are searched from first at the next level.

## Status

$\P$-complete (Greenlaw [[1]](#1)[[2]](#2)).

## Remarks

The reduction to show hardness is from [SAM2CVP]({{< relref "./sam2cvp.md" >}}). The *Lexicographic Breadth-first Search Problem*, which has a natural implementation on a queue, is defined as follows: given a graph $G$ with fixed ordered adjacency lists, is vertex $u$ visited before vertex $v$ in the breadth-first search of $G$ induced by the order of the adjacency lists? This problem is in $\NC$ (de la Torre and Kruskal [[3]](#3)[[4]](#4), Greenlaw [[1]](#1)).
