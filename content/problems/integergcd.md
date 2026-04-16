---
title: "Integer Greatest Common Divisor"
acronym: "IntegerGCD"
book_id: "B.5.3"
categories: ["Local Optimality"]
status: "open"
tags: []
references: [368, 69, 42, 184, 56, 335, 336, 90, 237, 329]
related_problems:
  - id: sv2
    relation: reduces-to
  - id: sv
    relation: reduces-to
---

## Given

Two $n$-bit positive integers $a$ and $b$.

## Problem

Compute the greatest common divisor (gcd) of $a$ and $b$, denoted $\gcd(a, b)$.

## Status

Open (von zur Gathen [[1]](#1)).

## Remarks

For $n^\text{th}$ degree polynomials $p, q \in \Q[x]$, computing $\gcd(p, q)$ is in $\NC^2$ via an $\NC^1$ reduction to *Determinant* (Cook and Sethi [[2]](#2), Borodin, Cook, and Pippenger [[3]](#3)). IntegerGCD is $\NC^1$ reducible to [SV2]({{< relref "./sv2.md" >}}) [[1]](#1). Kannan, Miller, and Rudolph give a sublinear CRCW-PRAM algorithm for computing the gcd of two $n$-bit integers [[4]](#4). Their algorithm requires $O(n \log \log n / \log n)$ time and $n^2 (\log n)^2$ processors. Chor and Goldreich give a CRCW-PRAM algorithm for the same problem with time bound $O(n / \log n)$ and processor bound $n^{1+\epsilon}$, for any positive constant $\epsilon$ [[5]](#5).

Sorenson presents an algorithm called the $k$-ary gcd algorithm [[6]](#6)[[7]](#7) whose sequential version is practical and whose parallel version has bounds that match those given in [[5]](#5). Also see (Deng [[8]](#8), Lin-Kriz and Pan [[9]](#9), Shallcross, Pan, and Lin-Kriz [[10]](#10)) for additional research on IntegerGCD and related problems.
