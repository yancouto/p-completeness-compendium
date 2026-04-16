---
title: "Mostowski Epimorphism"
acronym: "MostEpi"
book_id: "A.6.12"
categories: ["Logic"]
status: "p-complete"
tags: []
references: [74]
related_problems:
  - id: mcvp
    relation: reduces-from
---

## Given

A *well-founded relation* $(V, E)$ and $x_1, x_2 \in V$. Let $f$ be the *Mostowski epimorphism* of the relation. Refer to [[1]](#1) for definitions.

## Problem

Is $f(x_1) = f(x_2)$?

## Status

$\P$-complete (Dahlhaus [[1]](#1)).

## Remarks

The reduction to show hardness is from [MCVP]({{< relref "./mcvp.md" >}}).
The result indicates that the programming language SETL may not be well suited to parallelism [[1]](#1). See Problem B.3.1 for a related open problem.
