---
title: "Context-free Grammar ϵ-Membership"
acronym: "CFGϵmem"
book_id: "A.7.4"
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

Is $\epsilon \in L(G)$?

## Status

$\P$-complete (Goldschlager [[1]](#1), Jones and Laaser [[2]](#2)).

## Remarks

The reduction to show hardness is from [MCVP]({{< relref "./mcvp.md" >}}), a variant of [CFGempty]({{< relref "./cfgempty.md" >}}).