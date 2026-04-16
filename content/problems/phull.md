---
title: "Point Location on A Convex Hull"
acronym: "PHULL"
book_id: "A.9.4"
categories: ["Geometry"]
status: "p-complete"
tags: []
references: [245, 91, 159, 158]
related_problems:
  - id: mcvp
    relation: reduces-from
  - id: sch
    relation: see-also
---

## Given

An integer $d$, a set $S$ of $n$ points in $\Q^d$, and a designated point $p \in \Q^d$.

## Problem

Is $p$ on the convex hull of $S$?

## Status

$\P$-complete (Long and Warmuth [[1]](#1)).

## Remarks

The reduction to show hardness is from [MCVP]({{< relref "./mcvp.md" >}}).

The result shows that [SCH]({{< relref "./sch.md" >}}), for arbitrary dimension $d$ is $\P$-complete. The convex hull of $n$ points in the Euclidean plane can be computed optimally on an EREW-PRAM in $O(\log n)$ time using $n$ processors (see Dessmark, Lingas, and Maheshwari [[2]](#2)).
