---
title: "Average Cost Markov Decision Process"
acronym: "ACMDP"
book_id: "A.8.3"
categories: ["Algebra"]
status: "p-complete"
tags: []
references: [279]
related_problems:
  - id: mcvp
    relation: reduces-from-variant-of
  - id: mcvp
    relation: see-also
  - id: fhmdp
    relation: see-also
---

## Input

A stationary Markov decision process $M = (S, c, p)$.

## Problem

Is the minimum expected cost of $$\lim_{T \to \infty} \left( \sum_{i=0}^{T} c(s_t, \delta(s_t, t)) / T \right)$$ over all policies $\delta$ equal to $0$?

## Definitions

See [FHMDP]({{< relref "./fhmdp.md" >}}). This problem is *infinite horizon*, that is, there is no time bound.

## Status

$\P$-complete (Papadimitriou and Tsitsiklis [[1]](#1)).

## Remarks

The problem can be phrased as a linear programming problem and solved in polynomial time. The reduction to show hardness is from a synchronous variant of [MCVP]({{< relref "./mcvp.md" >}}).

The *Infinite Horizon, Average Cost, Deterministic Problem* is in $\NC$ [[1]](#1). The *deterministic* problem requires that $p$ only has values $0$ or $1$.
