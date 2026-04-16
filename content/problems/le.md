---
title: "Linear Equalities"
acronym: "LE"
book_id: "A.4.2"
categories: ["Combinatorial Optimization"]
status: "p-complete"
tags: []
references: [207, 357, 171, 73]
related_problems:
  - id: li
    relation: reduces-from
  - id: hf
    relation: see-also
---

## Given

An integer $n \times d$ matrix $A$ and an integer $n \times 1$ vector $b$.

## Problem

Is there a rational $d \times 1$ vector $x \geq 0$ such that $Ax = b$?

## Definitions

We have that $x > 0$ when all components of $x$ are nonnegative and at least one is nonzero.

## Status

$\P$-complete (Khachian [[1]](#1), Valiant [[2]](#2)).

## Remarks

The reduction to show hardness is from [LI]({{< relref "./li.md" >}}).
If LE is restricted so the coefficients of $A$ and $b$ are either $-1$, $0$, or $1$, LE is still $\P$-complete. This follows from the reduction given by Itai [[3]](#3). The restricted version of LE is denoted $[-1,1]$-LE and is used in proving that [HF]({{< relref "./hf.md" >}}) is $\P$-complete. Cucker and Torrecillas proved that the problem of deciding whether a system of equations of *degree* $d$, for $d \geq 2$, is solvable by substitution is $\P$-complete [[4]](#4).
