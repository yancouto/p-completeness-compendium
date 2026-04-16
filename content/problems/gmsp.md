---
title: "Generic Machine Simulation Problem"
acronym: "GMSP"
book_id: "A.12.1"
categories: ["Miscellaneous"]
status: "p-complete"
tags: []
references: [48, 165]
related_problems:
  - id: csgmem
    relation: reduces-to
  - id: pss
    relation: reduces-to
  - id: mlr
    relation: reduces-to
  - id: cfgempty
    relation: see-also
  - id: ca
    relation: reduces-to
  - id: cvp
    relation: reduces-to
  - id: topcvp
    relation: reduces-to
  - id: mcvp
    relation: reduces-to
  - id: horn
    relation: reduces-to
---

## Given

A string $x$, a description $M$ of a Turing machine $M$, and an integer $t$ coded in unary. (To be precise, the input is the string $x\\#\overline{M}\\#^t$, where $\\#$ is a delimiter character not otherwise present in the string.)

## Problem

Does $M$ accept $x$ within $t$ steps?

## Status

$\P$-complete (Greenlaw, Hoover and Ruzzo [[3, Theorem 4.1.2]](#3)).

## Remarks

Buss and Goldsmith show a variant of this problem is complete with respect to *quasilinear time reductions* for $\mathsf{N^mP_l}$, a subclass of $\P$. See [[1]](#1) for the appropriate definitions. They also show variants of [TopCVP]({{< relref "./topcvp.md" >}}) and [CFGempty]({{< relref "./cfgempty.md" >}}) are complete in this setting.
