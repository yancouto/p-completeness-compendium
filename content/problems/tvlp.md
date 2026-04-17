---
title: "Two Variable Linear Programming"
acronym: "TVLP"
book_id: "B.2.2"
categories: ["Graph Theory"]
status: "open"
tags: []
references: [248]
related_problems:
  - id: li
    relation: see-also
  - id: le
    relation: see-also
  - id: lp
    relation: see-also
  - id: opt2ilp
    relation: see-also
---

## Input

A linear system of inequalities $Ax \leq b$ over $\Q$, where each row of $A$ has at most two nonzero elements. $A$ is an $n \times d$ matrix and $b$ is an $n \times 1$ vector.

## Problem

Find a feasible solution if one exists.

## Status

Open (Lueker, Megiddo, and Ramachandran [[1]](#1)).

## Remarks

There is a polylogarithmic algorithm that uses $n(\log n)^{O(1)}$ processors on a CREW-PRAM [[1]](#1). See also Problems [LI]({{< relref "./li.md" >}}), [LE]({{< relref "./le.md" >}}), [LP]({{< relref "./lp.md" >}}) and [Opt2ILP]({{< relref "./opt2ilp.md" >}}).
