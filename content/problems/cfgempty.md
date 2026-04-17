---
title: "Context-free Grammar Empty"
acronym: "CFGempty"
book_id: "A.7.2"
categories: ["Formal Languages"]
status: "p-complete"
tags: []
references: [181, 125]
related_problems:
  - id: gen
    relation: reduces-from
  - id: mcvp
    relation: reduces-from
  - id: cfgmem
    relation: see-also
  - id: cfginf
    relation: see-also
---

## Input

A context-free grammar $G = (N, T, P, S)$.

## Problem

Is $L(G)$ empty?

## Status

$\P$-complete (Jones and Laaser [[1]](#1), Goldschlager [[2]](#2)).

## Remarks

Same reduction as for [CFGmem]({{< relref "./cfgmem.md" >}}) suffices, but it may also be reduced from [MCVP]({{< relref "./mcvp.md" >}}) [[3]](#3).

Note, this reduction and the one for [CFGinf]({{< relref "./cfginf.md" >}}), have no $\epsilon$-productions yet remain complete. The original proof of Jones and Laaser reduced [GEN]({{< relref "./gen.md" >}}) to CFGempty. Their proof used the reduction for [CFGmem]({{< relref "./cfgmem.md" >}}), and instead checked if $L(G)$ is empty [[1]](#1).
