---
title: "Visibility Layers"
acronym: "VL"
book_id: "A.9.3"
categories: ["Geometry"]
status: "p-complete"
tags: []
references: [18, 156]
related_problems:
  - id: mcvp
    relation: reduces-from-variant-of
  - id: mcvp
    relation: see-also
---

## Input

A set of $n$ nonintersecting line segments in the Euclidean plane and a designated segment $s$.

## Problem

Is the label assigned to segment $s$ by the visibility layering process congruent to one mod three?

## Definitions

The *visibility layering process* is repeatedly to compute and delete the upper envelope of the remaining set of segments and label those segments with the current depth. The *upper envelope* consists of those segments visible from the point $(0, +\infty)$. A segment is *visible* from a point $p$ if a ray cast from $p$ can hit the segment before hitting any other segment.

## Status

$\P$-complete (Atallah, Callahan, and Goodrich [[1]](#1), Hershberger [[2]](#2)).

## Remarks

The visibility layering process can be performed in polynomial time [[2]](#2). The reduction to show hardness is from a topologically ordered variant of [MCVP]({{< relref "./mcvp.md" >}}).
The reduction given in [[1]](#1) is similar and is also from a variant of [MCVP]({{< relref "./mcvp.md" >}}). The main difference is in the way fanout is treated. The version of [MCVP]({{< relref "./mcvp.md" >}}) used in [[1]](#1) consists of *crossing fanout gates*, single output AND gates, and single output OR gates. An instance consists of alternate routing and logic layers. Gadgets are constructed for the three types of gates and a similar decision problem to the one in [[2]](#2) is posed to determine the output of the circuit.

If the length of all segments is required to be the same, the complexity of the problem is not known [[1]](#1). In [[1]](#1) they conjecture that this version of the problem is in $\NC$.
