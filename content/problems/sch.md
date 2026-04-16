---
title: "Successive Convex Hulls"
acronym: "SCH"
book_id: "A.9.5"
categories: ["Geometry"]
status: "p-complete"
tags: []
references: [91, 53, 29]
related_problems:
  - id: mlr
    relation: see-also
  - id: phull
    relation: see-also
---

## Given

A set $S$ of $n$ points in the Euclidean plane, an integer $k$, and a designated point $p \in \R^2$.

## Problem

Is $p$ in the $k^\text{th}$ remaining convex hull that is formed by repeatedly finding and removing convex hulls from $S$?

## Status

$\P$-complete (Dessmark, Lingas, and Maheshwari [[1]](#1)).

## Remarks

Chazelle shows the problem is in $\P$ [[2]](#2). The reduction to show hardness is from [MLR]({{< relref "./mlr.md" >}}).
See [PHULL]({{< relref "./phull.md" >}}) for a closely related question.
