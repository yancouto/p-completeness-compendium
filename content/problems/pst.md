---
title: "Plane Sweep Triangulation"
acronym: "PST"
book_id: "A.9.1"
categories: ["Geometry"]
status: "p-complete"
tags: []
references: [18, 130]
related_problems:
  - id: pcvp
    relation: reduces-from-variant-of
  - id: pcvp
    relation: see-also
---

## Input

An $n$-vertex polygon $Q$ that may contain holes, and a designated vertex $u$.

## Problem

Is there a vertical edge connecting to $u$ in the plane sweep triangulation of $Q$?

## Definitions

The *plane sweep triangulation* is the triangulation produced by sweeping a horizontal line $L$ from top to bottom. When $L$ encounters a vertex $v$ of $Q$, each diagonal from $v$ to another vertex in $Q$, which does not cross a previously drawn diagonal, is added to the triangulation.

## Status

$\P$-complete (Atallah, Callahan, and Goodrich [[1]](#1)).

## Remarks

It is easy to see that the plane sweep triangulation algorithm runs in polynomial time. The reduction to show hardness is from a variant of [PCVP]({{< relref "./pcvp.md" >}}).

The problem of finding some arbitrary triangulation is in $\NC$ (Goodrich [[2]](#2)). If the polygon $Q$ is not allowed to have holes, the complexity of the problem is open. In [[1]](#1) they conjecture that this restricted version is in $\NC$.
