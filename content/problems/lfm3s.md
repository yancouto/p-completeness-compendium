---
title: "Lexicographically First Maximal 3 Sums"
acronym: "LFM3S"
categories: ["Combinatorial Optimization"]
status: "p-hard"
tags: []
references:
  - author: "A. Fujiwara, M. Inoue, and T. Masuzawa"
    title: "Parallelizability of some P-complete problems"
    year: 2000
    doi: "10.1007/3-540-45591-4_14"
related_problems:
  - id: lfmis
    relation: reduces-from
---

## Input

A set $I$ of distinct integers.

## Problem

Compute $\\{(a_1, b_1, c_1), \ldots, (a_k, b_k, c_k)\\}$, the lexicographical first maximal 3 sums of $I$.

## Definitions

The *lexicographical first maximal 3 sums of $I$* are a set satisfying the following conditions:
1. The set $S = \\{a_1, b_1, c_1, \ldots, a_k, b_k, c_k\\}$ is a subset of $I$.
2. For $1 \leq i \leq k$, $(a_i, b_i, c_i)$ is the lexicographically first set of three integers which satisfies $a_i + b_i + c_i = 0$ for $I - \\{a_1, b_1, c_1, \ldots, a_{i-1}, b_{i-1}, c_{i-1}\\}$.
3. There are no three distinct integers $a', b', c'$ in $I - S$ which satisfy $a' + b' + c' = 0$.


## Status

$\P$-complete (Fujiwara, Inoue, and Masuzawa [[1]](#1)).

## Remarks

The reduction to show hardness is from [LFMIS]({{< relref "./lfmis.md" >}}) with maximum degree three. The authors show an algorithm for LFM3S which is *cost-optimal* for up to $\frac{n}{\log n}$ processors, that is, over the best sequential algorithm it presents linear speedup with the number of processors.
