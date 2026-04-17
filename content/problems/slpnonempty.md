---
title: "Straight-line Program Nonempty"
acronym: "SLPnonempty"
book_id: "A.7.7"
categories: ["Formal Languages"]
status: "p-complete"
tags: []
references: [129]
related_problems:
  - id: gen
    relation: reduces-from
  - id: mcvp
    relation: reduces-from
  - id: slpmem
    relation: see-also
---

## Input

A straight-line program over a non-empty alphabet $\Sigma$ with operations taken from $\Phi = \Sigma \cup \\{\\{\epsilon\\}, \varnothing, \cup, \cdot\\}$, and a string $x$.

## Problem

Is the set constructed by the program nonempty? See [SLPmem]({{< relref "./slpmem.md" >}}) for definition.

## Status

$\P$-complete (Goodrich [[1]](#1)).

## Remarks

Same as [SLPmem]({{< relref "./slpmem.md" >}}), reduces from [GEN]({{< relref "./gen.md" >}}) and [MCVP]({{< relref "./mcvp.md" >}}).
With $\cap$ added, SLPnonempty becomes complete for nondeterministic exponential time [[1]](#1).
