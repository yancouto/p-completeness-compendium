---
title: "Optimal Two Variable Integer Linear Programming"
acronym: "Opt2ILP"
book_id: "B.2.1"
categories: ["Graph Theory"]
status: "open"
tags: []
references: [90, 329]
related_problems:
  - id: tvlp
    relation: see-also
  - id: extendedgcd
    relation: see-also
---

## Given

A linear system of inequalities $Ax \leq b$ over $\Z$, where $A$ is an $n \times 2$ matrix and $b$ is an $n \times 1$ vector, and an ordered pair $u \in \Z^2$.

## Problem

Find a $2 \times 1$ vector $x$, with $x^T \in \Z^2$ ($T$ denotes transpose), such that $Ax \leq b$ and $ux$ is a maximum.

## Status

Open (Deng [[1]](#1), Shallcross, Pan, and Lin-Kriz [[2]](#2)).

## Remarks

This problem is $\NC$-equivalent to the problem of computing the remainders produced by the Euclidean algorithm, see [ExtendedGCD]({{< relref "./extendedgcd.md" >}}) and [[1]](#1)[[2]](#2). Shallcross, Pan, and Lin-Kriz illustrate reductions among problems $\NC$-equivalent to this and related problems [[2]](#2). See [[1]](#1) and the remarks for [TVLP]({{< relref "./tvlp.md" >}}) and [ExtendedGCD]({{< relref "./extendedgcd.md" >}}) as well.
