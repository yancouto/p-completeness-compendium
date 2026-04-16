---
title: "Path Systems"
acronym: "PATH"
book_id: "A.6.8"
categories: ["Logic"]
status: "p-complete"
tags: []
references: [64, 60, 181, 328, 366]
related_problems:
  - id: gen
    relation: reduces-from
  - id: lqp
    relation: reduces-to
  - id: ctq
    relation: reduces-to
---

## Given

A path system $P = (X, R, S, T)$, where $S \subseteq X$, $T \subseteq X$, and $R \subseteq X \times X \times X$.

## Problem

Is there an admissible vertex in $S$?

## Definitions

A vertex $x$ is *admissible* if and only if $x \in T$, or there exists admissible $y, z \in X$ such that $(x, y, z) \in R$.

## Status

$\P$-complete under $\LOGSPACE$ reductions (Cook [[1]](#1)).

## Remarks

Cook defined path systems in [[2]](#2). This is the first problem shown to be logarithmic space complete for  $\P$. The original proof by Cook does a direct simulation of a Turing machine [[1]](#1), while Jones and Laaser reduce from [GEN]({{< relref "./gen.md" >}}) [[3]](#3). Under the appropriate definitions, it is known that approximating this problem is also  $\P$-complete (Serna and Spirakis [[4]](#4)). Vitter and Simons give a $\sqrt{n}$ time parallel algorithm for the non-sparse version of the problem [[5]](#5).
