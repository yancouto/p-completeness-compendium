---
title: "Aperiodic Monoid Membership Variety $B_2$"
acronym: "AMonMEMB"
book_id: "A.8.27"
categories: ["Algebra"]
status: "p-complete"
tags: []
references: [29]
related_problems:
  - id: gen
    relation: reduces-from-variant-of
---

## Input

A set of total functions $a_1, \ldots, a_r$ and a designated function $f$, all from the set $\\{1, 2, \ldots, m\\}$ to itself, with the property that $\langle a_1, \ldots, a_r \rangle \in B_2$.

## Problem

Does $f$ belong to $\langle a_1, \ldots, a_r \rangle$?

## Definitions

Value $\langle a_1, \ldots, a_r \rangle$ denotes the set of all functions obtained by composing the functions $a_i$ with one another. $B_2$ is a restricted class of *aperiodic monoids*. Refer to [[1]](#1) for further definitions.

## Status

$\P$-complete (Beaudry, McKenzie, and Thérien [[1]](#1)).

## Remarks

The reduction to show hardness is from a variant of [GEN]({{< relref "./gen.md" >}}).

The lattice of *aperiodic monoid varieties* is partitioned in [[1]](#1) into the following five sublattices: $B_1$, $B_2$, $B_3$, $B_4$, and $B_5$. The membership problem for varieties in $B_2$ as described above is $\P$-complete. For varieties in $B_1$ the problem is in $\mathsf{AC}^0$; for $B_3$ it is $\NP$-complete; for $B_4$ it is $\NP$-hard; for $B_5$ it is $\mathsf{PSPACE}$-complete [[1]](#1).
