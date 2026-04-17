---
title: "Context-free Grammar Infinite"
acronym: "CFGinf"
book_id: "A.7.3"
categories: ["Formal Languages"]
status: "p-complete"
tags: []
references: [125, 181]
related_problems:
  - id: mcvp
    relation: reduces-from
  - id: cfgempty
    relation: see-also
---

## Input

A context-free grammar $G = (N, T, P, S)$.

## Problem

Is $L(G)$ infinite?

## Status

$\P$-complete (Goldschlager [[1]](#1), Jones and Laaser [[2]](#2)).

## Remarks

The reduction to show hardness is from [MCVP]({{< relref "./mcvp.md" >}}), a variant of [CFGempty]({{< relref "./cfgempty.md" >}}).