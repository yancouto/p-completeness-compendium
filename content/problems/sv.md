---
title: "Short Vectors"
acronym: "SV"
book_id: "B.7.1"
categories: ["Formal Languages"]
status: "open"
tags: []
references: [368, 232, 22]
related_problems:
  - id: integergcd
    relation: reduces-from
  - id: upfq
    relation: reduces-from
---

## Given

Input vectors $a_1, \ldots, a_n \in \Z^n$ that are linearly independent over $\Q$.

## Problem

Find a nonzero vector $x$ in the $\Z$-module (or "lattice") $M = \sum a_i \Z \subseteq \Z^n$ such that $\|x\| \leq 2^{(n-1)/2} \|y\|$ for all $y \in M - \\{\vec{0}\\}$, where $\|y\| = \left(\sum y_i^2\right)^{1/2}$ is the $L_2$ norm.

## Status

Open (von zur Gathen [[1]](#1)).

## Remarks

Lenstra, Lenstra, and Lovász show that the problem is in $\P$ [[2]](#2). [IntegerGCD]({{< relref "./integergcd.md" >}}) is $\NC^1$ reducible to SV [[1]](#1). For additional remarks about related problems, see Bachem and Kannan [[3]](#3).