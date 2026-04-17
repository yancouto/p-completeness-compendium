---
title: "Maximal Path"
acronym: "MP"
book_id: "B.9.4"
categories: ["Network Flows"]
status: "open"
tags: ["RNC"]
references: [16, 13]
related_problems:
  - id: lfmp
    relation: variant
---

## Input

An undirected graph $G = (V, E)$ with a numbering on the vertices in $V$ and a designated vertex $r$.

## Problem

Find a maximal path originating from $r$. 

## Definition

A path is *maximal* if it cannot be extended without encountering a vertex already on the path.

## Status

Open (Anderson and Mayr [[1]](#1), Anderson [[2]](#2)).

## Remarks

Anderson shows that the problem of computing a maximal path is in $\mathsf{RNC}$ [[2]](#2). Lexicographically First Maximal Path ([LFMP]({{< relref "./lfmp.md" >}})) is $\P$-complete even when restricted to planar graphs with maximum degree three. If the maximum degree of any vertex in $G$ is at most $\Delta$, there is an algorithm that can find a maximal path in $O(\Delta (\log n)^3)$ time using $n^2$ processors [[1]](#1). There is also an $\NC$ algorithm for finding a maximal path in planar graphs [[1]](#1).
