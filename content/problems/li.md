---
title: "Linear Inequalities"
acronym: "LI"
book_id: "A.4.1"
categories: ["Combinatorial Optimization"]
status: "p-complete"
tags: []
references: [207, 357]
related_problems:
  - id: cvp
    relation: reduces-from
  - id: lp
    relation: see-also
  - id: le
    relation: reduces-to
---

## Input

An integer $n \times d$ matrix $A$ and an integer $n \times 1$ vector $b$.

## Problem

Is there a rational $d \times 1$ vector $x > 0$ such that $Ax \leq b$? (It is not required to find such an $x$.)

## Definitions

We have that $x > 0$ when all components of $x$ are nonnegative and at least one is nonzero.

## Status

$\P$-complete (Khachian [[1]](#1), Valiant [[2]](#2)).

## Remarks

The reduction to show hardness is from [CVP]({{< relref "./cvp.md" >}}), and LI is in $\P$ by [[1]](#1).
Remains $\P$-complete if entries in $A$ and $b$ are restricted to $\\{0, 1\\}$. See also remarks for [LE]({{< relref "./le.md" >}}) and [LP]({{< relref "./lp.md" >}}).
