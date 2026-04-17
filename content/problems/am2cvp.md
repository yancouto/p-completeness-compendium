---
title: "Alternating Monotone Fanin 2, Fanout 2 CVP"
acronym: "AM2CVP"
book_id: "A.1.4"
categories: ["Circuit Complexity"]
status: "p-complete"
tags: []
references: [128]
related_problems:
  - id: mcvp
    relation: reduces-from
  - id: game
    relation: reduces-to
  - id: nandcvp
    relation: reduces-to
  - id: sam2cvp
    relation: reduces-to
  - id: cvp
    relation: see-also
  - id: agap
    relation: reduces-to
  - id: kcore
    relation: reduces-to
  - id: hcs
    relation: reduces-to
  - id: maxflow
    relation: reduces-to
  - id: lfbf
    relation: reduces-to
  - id: ffdbp
    relation: reduces-to
  - id: ktruss
    relation: reduces-to
  - id: abbcore
    relation: reduces-to
  - id: kldcore
    relation: reduces-to
  - id: ne-k-core
    relation: reduces-to
---

## Input

An encoding $\overline{\alpha}$ of a Boolean circuit $\alpha$, inputs $x_1, \ldots, x_n$ and designated output $y$. On any path from an input to an output the gates are required to alternate between OR and AND gates. Inputs are required to be connected only to OR gates, and outputs must come directly from OR gates. The circuit is restricted to have fanout exactly two for inputs and internal gates, and to have a distinguished OR gate as output.

## Problem

Is output $y$ of $\alpha$ true on inputs $x_1, \ldots, x_n$?

## Definitions

See [CVP]({{< relref "./cvp.md" >}}).

## Status

$\P$-complete under $\NC^1$ reductions (Greenlaw, Hoover and Ruzzo [[2, Theorem 6.2.3]](#2)).

## Remarks

The reduction to show hardness is from [MCVP]({{< relref "./mcvp.md" >}}).
Goldschlager, Shaw, and Staples gave a $\P$-completeness proof for Monotone, Fanout 2 [CVP]({{< relref "./cvp.md" >}}) [[1]](#1).
