---
title: "Circuit Value Problem"
acronym: "CVP"
book_id: "A.1.1"
categories: ["Circuit Complexity"]
status: "p-complete"
tags: []
references: [225, 127]
related_problems:
  - id: gmsp
    relation: reduces-from
  - id: topcvp
    relation: variant
  - id: unit
    relation: reduces-to
  - id: horn
    relation: reduces-to
  - id: gen
    relation: reduces-to
  - id: unif
    relation: reduces-to
  - id: 2dpda
    relation: reduces-to
  - id: realcvp
    relation: reduces-to
  - id: fpcm
    relation: reduces-to
  - id: life
    relation: reduces-to
  - id: ccvp
    relation: variant
  - id: epsilonctg
    relation: reduces-to
  - id: invnc0perm
    relation: reduces-to
  - id: cem
    relation: reduces-to
  - id: mcvp
    relation: reduces-to
  - id: pcvp
    relation: reduces-to
  - id: li
    relation: reduces-to
---

## Given

An encoding $\overline{\alpha}$ of a Boolean circuit $\alpha$, inputs $x_1, \ldots, x_n$ and designated output $y$.

## Problem

Is output $y$ of $\alpha$ true on inputs $x_1, \ldots, x_n$?

## Definitions

A Boolean circuit $\alpha$ is a labeled directed acyclic graph. Each vertex (gate) is labeled INPUT, AND, OR, or NOT, and computes its corresponding function over its $n$ inputs, whose values are given as $x_1, \ldots, x_n \in \\{0,1\\}$. An encoding $\overline{\alpha}$ of $\alpha$ is a string from $\\{0,1\\}^\ast$ where the vertices of $\alpha$ are listed with their types and connections, not necessarily in topological order.

## Status

$\P$-complete under $\NC^1$ reductions (Greenlaw, Hoover and Ruzzo [[3, Theorem 4.2.2]](#3), Ladner [[1]](#1)).

## Remarks

The CVP is the most fundamental $\P$-complete problem, in fact, it's one of the few where $\P$-completeness is proved directly (from [GMSP]({{< relref "./gmsp.md" >}})) instead of through reductions from other $\P$-complete problems.

For the two input basis of Boolean functions, it is known that CVP is  $\P$-complete except when the basis consists solely of or, consists solely of and, or consists of any or all of the following: XOR, EQUIVALENCE, and NOT (Goldschlager and Parberry [[2]](#2)).
