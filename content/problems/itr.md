---
title: "Incomplete Table Recovery"
acronym: "ITR"
book_id: "A.6.14"
categories: ["Logic"]
status: "p-complete"
tags: []
references: [267, 268]
related_problems:
  - id: agap
    relation: reduces-from
---

## Input

A collection $F$ of functional dependencies on a finite attribute set $\\{A_1, \ldots, A_m\\}$, a matrix $T = (T_{ij})$ for $0 \leq i \leq n$ and $1 \leq j \leq m$ called an *incomplete table* where $T_{0j} = A_j$ for $1 \leq j \leq m$, and the value of each $T_{ij}$ is either a nonnegative integer or the null value $*$ for $1 \leq i \leq n$ and $1 \leq j \leq m$. Refer to [[1]](#1) for definitions regarding this problem.

## Problem

Is $T$ uniquely recoverable under $F$ when the domain of each attribute $A_j$ is the set of nonnegative integers?

## Status

$\P$-complete (Miyano and Haraguchi [[1]](#1), Miyano, Shiraishi, and Shoudai [[2]](#2)).

## Remarks

The reduction to show hardness is from [AGAP]({{< relref "./agap.md" >}}).
