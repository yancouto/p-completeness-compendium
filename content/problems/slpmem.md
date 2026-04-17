---
title: "Straight-line Program Membership"
acronym: "SLPmem"
book_id: "A.7.6"
categories: ["Formal Languages"]
status: "p-complete"
tags: []
references: [129]
related_problems:
  - id: gen
    relation: reduces-from
  - id: mcvp
    relation: reduces-from
---

## Input

A straight-line program over non-empty alphabet $\Sigma$ with operations taken from $\Phi = \Sigma \cup \\{\\{\epsilon\\}, \varnothing, \cup, \cdot\\}$, and a string $x$.

## Problem

Is $x$ a member of the set constructed by the program?

## Definitions

The *set constructed by the program*, when the last instruction involves $\cup$ or $\cdot$, is the set computed by the final instruction.

## Status

$\P$-complete (Goodrich [[1]](#1), Greenlaw, Hoover, and Ruzzo [[2]](#2)).

## Remarks

The reduction to show hardness is from [GEN]({{< relref "./gen.md" >}}) [[1]](#1) or [MCVP]({{< relref "./mcvp.md" >}}) [[2]](#2). Remains in $\P$ if $\cap$ is allowed. The analogous membership question for regular languages presented as regular expressions or nondeterministic finite automata is complete for $\mathsf{NLOG}$.
