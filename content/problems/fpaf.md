---
title: "Finitely Presented Algebras Finiteness"
acronym: "FPAF"
book_id: "A.8.21"
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

## Given

A finitely presented algebra $A = (M, \mathcal{A}, \Gamma)$.

## Problem

Is $A$ finite?

## Definitions

See [UWPFPA]({{< relref "./uwpfpa.md" >}}).

## Status

$\P$-complete (Kozen [[1]](#1)).

## Remarks

A polynomial time algorithm for the problem is given in [[1]](#1). The reduction to show hardness is from [MCVP]({{< relref "./mcvp.md" >}}).