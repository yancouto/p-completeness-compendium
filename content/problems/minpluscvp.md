---
title: "Min-plus Circuit Value Problem"
acronym: "MinPlusCVP"
book_id: "A.1.9"
categories: ["Circuit Complexity"]
status: "p-complete"
tags: []
references: []
related_problems:
  - id: mcvp
    relation: reduces-from
  - id: nandcvp
    relation: reduces-from
  - id: arithcvp
    relation: see-also
---

## Input

An encoding $\overline{\alpha}$ of a $(\min, +)$ circuit $\alpha$ and rational inputs $x_1, \ldots, x_n$.

## Problem

Does $\alpha$ on input $x_1, \ldots, x_n$ output a nonzero value?

## Definitions

See [ArithCVP]({{< relref "./arithcvp.md" >}}).

## Status

$\P$-complete (Greenlaw, Hoover and Ruzzo [[1]](#1)).

## Remarks

The reduction to show hardness is from [MCVP]({{< relref "./mcvp.md" >}}) and works in any ordered semi-group with additive identity $0$ and an element $1$ such that $1 + 1 \geq 1 > 0$. If there is a nonzero element $1$ such that $1 + 1 = 0$ (e.g. in $\Z_2$), then a reduction from [NANDCVP]({{< relref "./nandcvp.md" >}}) exists. In a well-ordered semigroup where $0$ is the minimum element, one or the other of these cases holds. If the semigroup is infinite, the problem may not be in $\P$.
