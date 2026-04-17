---
title: "Circuit Evaluation over Monoids"
acronym: "CEM"
book_id: "A.1.13"
categories: ["Circuit Complexity"]
status: "p-complete"
tags: []
references: [28]
related_problems:
  - id: cvp
    relation: reduces-from
---

## Input

A finite monoid $(M, \oplus, 1)$ containing a nonsolvable group; an encoding $\overline{\alpha}$ of a circuit $\alpha$, whose gates are of type $\oplus$, inputs $x_1, \ldots, x_n \in M$, and designated output $y$.

## Problem

Does $\alpha$ evaluate to $y$ on input $x_1, \ldots, x_n$?

## Definitions

See [CVP]({{< relref "./cvp.md" >}}). Set $M$ is finite, $\oplus$ is an associative binary operation on the elements of $M$, and $1$ acts as an identity element.

## Status

$\P$-complete (Beaudry, McKenzie, and Péladeau [[1]](#1)).

## Remarks

The reduction to show hardness is from [CVP]({{< relref "./cvp.md" >}}). If $M$ is solvable the same problem is in $\mathsf{DET}$, the class of problems $\NC^1$ Turing reducible to computing integer determinants.
