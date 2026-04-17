---
title: "ϵ-Circuit Depth Ones"
acronym: "ϵCDO"
book_id: "A.1.10"
categories: ["Circuit Complexity"]
status: "p-hard"
tags: []
references: [215, 327]
related_problems:
  - id: mcvp
    relation: reduces-from
  - id: cvp
    relation: see-also
---

## Input

An encoding $\overline{\alpha}$ of a Boolean circuit $\alpha$, plus inputs $x_1, \ldots, x_n$, and a number $\epsilon \in (0, 1]$. Let $d$ denote the maximum depth that a true value propagates to in $\alpha$ on the given input.

## Problem

Find an integer $d'$ such that $d \geq d' \geq \epsilon d$.

## Definitions

See [CVP]({{< relref "./cvp.md" >}}).

## Status

$\P$-hard (Kirousis and Spirakis [[1]](#1)).

## Remarks

This problem is stated as a computation problem. Thus, it is technically not in $\P$. The reduction to show hardness is from [MCVP]({{< relref "./mcvp.md" >}}). Given $\alpha$ it is easy to construct a deeper circuit such that if we could approximate the depth of ones in the new circuit, we could determine the output of $\alpha$.

The extension to $\alpha$ can be constructed to preserve properties such as monotonicity, fan-out, alternation, and planarity (Kirousis and Spirakis [[1]](#1), Serna [[2]](#2)).
