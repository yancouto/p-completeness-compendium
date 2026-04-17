---
title: "Monotone Circuit Value Problem"
acronym: "MCVP"
book_id: "A.1.3"
categories: ["Circuit Complexity"]
status: "p-complete"
tags: []
references: [122, 366]
related_problems:
  - id: cvp
    relation: reduces-from
  - id: gmsp
    relation: reduces-from
  - id: llsu
    relation: reduces-to
  - id: mostepi
    relation: reduces-to
  - id: unif
    relation: reduces-to
  - id: cfgempty
    relation: reduces-to
  - id: cfginf
    relation: reduces-to
  - id: cfgepsilonmem
    relation: reduces-to
  - id: slpmem
    relation: reduces-to
  - id: slpnonempty
    relation: reduces-to
  - id: fhmdp
    relation: reduces-to
  - id: uwpfpa
    relation: reduces-to
  - id: fpat
    relation: reduces-to
  - id: fpaf
    relation: reduces-to
  - id: phull
    relation: reduces-to
  - id: agg
    relation: reduces-to
  - id: zsbg
    relation: reduces-to
  - id: gdd
    relation: reduces-to
  - id: netsim
    relation: reduces-to
  - id: epsiloncdo
    relation: reduces-to
  - id: am2cvp
    relation: reduces-to
  - id: minpluscvp
    relation: reduces-to
  - id: rcin
    relation: reduces-to
  - id: mfvs
    relation: reduces-to
  - id: ggc
    relation: reduces-to
  - id: maxflipv
    relation: reduces-to
  - id: lfdtml
    relation: reduces-to
  - id: apa
    relation: reduces-to
---

## Input

An encoding $\overline{\alpha}$ of a Boolean circuit $\alpha$, inputs $x_1, \ldots, x_n$ and designated output $y$, with the additional assumption that $\alpha$ is monotone. That is, it is constructed solely of INPUT, AND and OR gates.

## Problem

Is output $y$ of $\alpha$ true on inputs $x_1, \ldots, x_n$?

## Definitions

See [CVP]({{< relref "./cvp.md" >}}).

## Status

$\P$-complete under $\NC^1$ reductions (Greenlaw, Hoover and Ruzzo  [[3, Theorem 6.2.2]](#3), Goldschlager [[1]](#1)).

## Remarks

The reduction to show hardness is from [CVP]({{< relref "./cvp.md" >}}) or [GMSP]({{< relref "./gmsp.md" >}}). It remains complete when the fan-in and fan-out is 2, which is often implied in several reductions, while the more technically correct term would be M2CVP.
Vitter and Simmons give a $\sqrt{n}$ time parallel algorithm for the non-sparse version of the problem [[2]](#2).
