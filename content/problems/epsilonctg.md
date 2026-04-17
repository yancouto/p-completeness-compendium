---
title: "ϵ-Circuit true Gates"
acronym: "ϵCTG"
book_id: "A.1.11"
categories: ["Circuit Complexity"]
status: "p-hard"
tags: []
references: [326, 327]
related_problems:
  - id: cvp
    relation: reduces-from
---

## Input

An encoding $\overline{\alpha}$ of a Boolean circuit $\alpha$, plus inputs $x_1, \ldots, x_n$, and a number $\epsilon \in (0, 1]$. Let $t$ denote the number of gates in $\alpha$ that evaluate to true.

## Problem

Find an integer $d$ such that $\lfloor \epsilon t \rfloor \leq d < t$.

## Definitions

See [CVP]({{< relref "./cvp.md" >}}).

## Status

$\P$-hard (Serna [[1]](#1)[[2]](#2)).

## Remarks

This problem is stated as a computation problem. Thus, it is technically not in $\P$. The reduction to show hardness is from [CVP]({{< relref "./cvp.md" >}}). Given $\alpha$ it is easy to construct a deeper circuit such that if we could approximate the output of the new circuit, we could determine the output of $\alpha$.

The extension to $\alpha$ can be constructed to preserve properties such as monotonicity, fan-out, alternation, and planarity [[2]](#2).
