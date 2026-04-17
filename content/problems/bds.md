---
title: "Breadth-depth Search"
acronym: "BDS"
book_id: "A.3.4"
categories: ["Searching Graphs"]
status: "p-complete"
tags: []
references: [163, 139, 133]
related_problems:
  - id: nandcvp
    relation: reduces-from-variant-of
  - id: lfdfs
    relation: see-also
---

## Input

An undirected graph $G = (V, E)$ with a numbering on the vertices, and two designated vertices $u$ and $v$.

## Problem

Is vertex $u$ visited before vertex $v$ in the breadth-depth first search of $G$ induced by the vertex numbering?

## Definitions

A *breadth-depth first search* (Horowitz and Sahni [[1]](#1)) starts at a vertex $s$ and visits all children of $s$ pushing them on a stack as the search proceeds. After all of $s$'s children have been visited, the search continues with the vertex on the top of the stack playing the role of $s$.

## Status

$\P$-complete (Greenlaw [[2]](#2)).

## Remarks

A reduction from [NORCVP]({{< relref "./nandcvp.md" >}}) is presented in [[3]](#3) for both undirected and directed graphs. Several other reductions for the problem are described in detail in [[1]](#1), the main one being from [LFDFS]({{< relref "./lfdfs.md" >}}).