---
title: "Linear Programming"
acronym: "LP"
book_id: "A.4.3"
categories: ["Combinatorial Optimization"]
status: "p-hard"
tags: []
references: [93, 94, 207, 357, 277, 304, 327, 257, 237, 75]
related_problems:
  - id: li
    relation: see-also
  - id: horn
    relation: reduces-from
  - id: dmdp
    relation: see-also
---

## Given

An integer $n \times d$ matrix $A$, an integer $n \times 1$ vector $b$, and an integer $1 \times d$ vector $c$.

## Problem

Find a rational $d \times 1$ vector $x$ such that $Ax \leq b$ and $cx$ is maximized.

## Status

$\P$-hard (Dobkin, Lipton, and Reiss [[1]](#1), Dobkin and Reiss [[2]](#2), Khachian [[3]](#3), Valiant [[4]](#4)).

## Remarks

The original reduction in [[1]](#1) is from [HORN]({{< relref "./horn.md" >}}) to LP. In [[2]](#2), LP and [LI]({{< relref "./li.md" >}}) are shown to be logarithmic space equivalent by reducing LP to [LI]({{< relref "./li.md" >}}) using *rational binary search* (Papadimitriou [[5]](#5), Reiss [[6]](#6)) to find the value of the maximum and an $x$ that yields it. However, it is not clear how to perform this reduction in $\NC^1$. Since LP and [LI]({{< relref "./li.md" >}}) are complete via $\NC^1$ reductions though, there must be an $\NC^1$ reduction between the two problems. Although we know that LP and [LI]({{< relref "./li.md" >}}) are $\NC^1$ equivalent, the $\NC^1$ reduction between them is not an obvious one.

Serna shows it is $\P$-complete to approximate a *solution approximation*, which requires finding an $x'$ close to the optimal solution, and to approximate a *value approximation*, which requires finding an $x'$ such that $cx'$ is close to $cx$ [[7]](#7). Megiddo gives a reduction of LP to Serna's approximate problem [[8]](#8). It is also $\P$-hard to approximate $cx$ to within any constant fraction, even given a feasible solution $x'$ [[11]](#11); reduction is from [DMDP]({{< relref "./dmdp.md" >}}). See Lin-Kriz and Pan [[9]](#9) for some results on two variable linear programming. Dahlhaus observes that for $d$ equal to 3 and values over the reals the problem is $\P$-complete, whereas for $d$ equal to 2, the problem is in $\NC$ [[10]](#10).

