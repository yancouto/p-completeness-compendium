---
title: "Generability"
acronym: "GEN"
book_id: "A.6.7"
categories: ["Logic"]
status: "p-complete"
tags: []
references: [181, 25, 328, 125]
related_problems:
  - id: cvp
    relation: reduces-from
  - id: unit
    relation: reduces-from
  - id: path
    relation: reduces-to
  - id: cfgmem
    relation: reduces-to
  - id: cfgempty
    relation: reduces-to
  - id: slpmem
    relation: reduces-to
  - id: slpnonempty
    relation: reduces-to
  - id: fgs
    relation: reduces-to
  - id: game
    relation: reduces-to
---

## Input

A finite set $W$, a binary operation $\bullet$ on $W$ (presented as a table), a subset $V \subseteq W$, and $w \in W$.

## Problem

Is $w$ contained in the smallest subset of $W$ that contains $V$ and is closed under the operation $\bullet$?

## Status

$\P$-complete under $\NC^1$ reductions (Jones and Laaser [[1]](#1), Barrington and McKenzie [[2]](#2)).

## Remarks

The reduction to show hardness is from [UNIT]({{< relref "./unit.md" >}}) or [CVP]({{< relref "./cvp.md" >}}).
The problem remains $\P$-complete if $V$ is a singleton set and $\bullet$ is commutative (Barrington and McKenzie [[2]](#2), [[1]](#1)). If $\bullet$ is associative, GEN is complete for $\mathsf{NLOG}$. The problem remains in $\P$ even with more than one operation.

The complexities of several other versions of GEN are addressed in [[2]](#2). Under the appropriate definitions, it is known that approximating this problem is also $\P$-complete (Serna and Spirakis [[3]](#3)). Simons developed an $O(n)$ time parallel algorithm for the problem in 1987, where $n = |W|$ [[5]](#5).
