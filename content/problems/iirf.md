---
title: "Inverting An Injective Real Function"
acronym: "IIRF"
book_id: "A.10.3"
categories: ["Real Analysis"]
status: "p-hard"
tags: []
references: [218]
---

## Input

An $\NC$ real function $f$ defined on $[0, 1]$. The function is increasing and has the property that $f(0) < 0 < f(1)$. Thus, there is a unique root $x_0$ such that $f(x_0) = 0$. A real function $f$ is in $\NC$ if an approximation to $f(x)$ with error less than $2^{-n}$, for $x \in [-2^n, +2^n]$, can be computed in $\NC$.

## Problem

Compute $x_0$ with error less than $2^{-n}$.

## Status

$\P$-complete (Ko [[1]](#1)).

## Remarks

This problem was expressed originally in terms of logarithmic space computability and reductions --- if $f$ is logarithmic space computable then $f^{-1}(0)$ is not logarithmic space computable, unless $\mathsf{DLOG} = \P$. The problem remains hard even if $f$ is required to be differentiable.
