---
title: "Finitely Presented Algebras Triviality"
acronym: "FPAT"
book_id: "A.8.19"
categories: ["Algebra"]
status: "p-complete"
tags: []
references: [221]
related_problems:
  - id: mcvp
    relation: reduces-from
  - id: uwpfpa
    relation: see-also
---

## Input

A finitely presented algebra $A = (M, \mathcal{A}, \Gamma)$.

## Problem

Is $A$ trivial?

## Definitions

See [UWPFPA]({{< relref "./uwpfpa.md" >}}). An algebra $A$ is *trivial* if it contains only one element.

## Status

$\P$-complete (Kozen [[1]](#1)).

## Remarks

A polynomial time algorithm for the problem is given in [[1]](#1). The reduction to show hardness is from [MCVP]({{< relref "./mcvp.md" >}}).