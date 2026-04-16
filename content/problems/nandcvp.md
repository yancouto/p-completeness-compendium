---
title: "NAND Circuit Value Problem"
acronym: "NANDCVP"
book_id: "A.1.5"
categories: ["Circuit Complexity"]
status: "p-complete"
tags: []
references: [292]
related_problems:
  - id: am2cvp
    relation: reduces-from
  - id: rcl
    relation: reduces-to
  - id: unif
    relation: reduces-to
  - id: shuf
    relation: reduces-to
  - id: gepp
    relation: reduces-to
  - id: im
    relation: reduces-to
  - id: gar
    relation: reduces-to
  - id: arithcvp
    relation: reduces-to
  - id: minpluscvp
    relation: reduces-to
  - id: cvp
    relation: see-also
  - id: lfmis
    relation: reduces-to
  - id: ohdvr
    relation: reduces-to
  - id: lfdvc
    relation: reduces-to
  - id: nntsh
    relation: reduces-to
  - id: abfs
    relation: reduces-to
---

## Given

An encoding $\overline{\alpha}$ of a Boolean circuit $\alpha$, inputs $x_1, \ldots, x_n$ and an output gate $y$. Circuit $\alpha$ is constructed only of NAND gates and is restricted to have fanout two for inputs and NAND gates.

## Problem

Is output $y$ of $\alpha$ true on inputs $x_1, \ldots, x_n$?

## Definitions

See [CVP]({{< relref "./cvp.md" >}}).

## Status

$\P$-complete under $\NC^1$ reductions (Greenlaw, Hoover and Ruzzo [[2, Theorem 6.2.4]](#2)).

## Remarks

The reduction to show hardness is from [AM2CVP]({{< relref "./am2cvp.md" >}}).
Any complete basis of gates suffices, by the obvious simulation of NAND gates in the other basis. For example, NOR gates form a complete basis. NORCVP is defined analogously to NANDCVP. See Post for a characterization of complete bases [[1]](#1). See the remarks for [CVP]({{< relref "problems/cvp.md" >}}) for other bases, not necessarily complete, for which the associated [CVP]({{< relref "./cvp.md" >}}) is still complete.
