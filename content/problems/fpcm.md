---
title: "Fixed Points of Contraction Mappings"
acronym: "FPCM"
book_id: "A.10.2"
categories: ["Real Analysis"]
status: "p-hard"
tags: []
references: [159]
related_problems:
  - id: cvp
    relation: reduces-from
  - id: realcvp
    relation: see-also
---

## Given

An $\NC$ *real function* $C$ that behaves as a contractor on some interval $I$ contained in $(-\infty, +\infty)$. The endpoints of $I$ are specified as integers.

## Problem

Compute the fixed point of $C$ in $I$ with absolute error less than $2^{-n}$.

## Definitions

A real function $f$ is in $\NC$ if an approximation to $f(x)$ with absolute error less than $2^{-n}$, for $x \in [-2^n, +2^n]$, can be computed in $\NC$ (with the same input/output conventions as for [RealCVP]({{< relref "./realcvp.md" >}})).


## Status

$\P$-hard (Hoover [[1]](#1)).

## Remarks

The reduction to show hardness is from [CVP]({{< relref "./cvp.md" >}}).
This provides an argument that fast numerical methods based on fixed points probably have to use contraction maps with better than linear rates of convergence, such as Newton's method.
