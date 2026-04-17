---
title: "Ordered High Degree Vertex Removal"
acronym: "OHDVR"
book_id: "A.2.10"
categories: ["Graph Theory"]
status: "p-complete"
tags: []
references: [134]
related_problems:
  - id: nandcvp
    relation: reduces-from
  - id: oldvr
    relation: reduces-to
  - id: ovr
    relation: reduces-to
  - id: nr
    relation: reduces-to
  - id: gds
    relation: reduces-to
---

## Input

An undirected graph $G = (V, E)$ with a numbering on the vertices in $V$, and two designated vertices $u$ and $v$.

## Problem

Is there an elimination order on $V$, $v_1, \ldots, v_n$, satisfying the properties that $u$ is eliminated before $v$ and for $1 \leq i \leq n$, $v_i$ is the lowest numbered vertex of maximum degree in the $(i-1)$-st remaining subgraph of $G$?

## Definitions

An *elimination order* is a sequence of vertices ordered as they and their corresponding edges are to be deleted from the graph.

## Status

$\P$-complete (Greenlaw [[1]](#1)).

## Remarks

The reduction to show hardness is from [NANDCVP]({{< relref "./nandcvp.md" >}}).