---
title: 'Two-Dimensional Abelian Sandpile Prediction'
acronym: "2DSANDPRED"
categories: ["Discrete Dynamical Systems"]
status: "open"
tags: ["sandpiles", "chip-firing"]
references: [383, 384]
related_problems:
  - id: sandpile
    relation: "variant"
  - id: tsp2d
    relation: "variant"
---

## Input

An integer $n \geq 1$, a stable configuration
$x \in \\{0,\ldots,3\\}^{[n]^2}$, and two sites $u,v \in [n]^2$.

## Problem

Does site $v$ topple during the stabilization of the configuration
obtained by adding one grain to site $u$ in the initial configuration
$x$?

## Definitions

The sandpile evolves on the finite grid $[n]^2$ with open boundary
conditions. Each site contains a non-negative integer number of
grains. A site is unstable if it contains at least four grains.
When an unstable site topples, it loses four grains and sends one
grain to each of its four nearest neighbors; grains sent outside
the grid are dissipated.

The initial configuration $x$ is stable, meaning that every site
contains fewer than four grains. One grain is added to site $u$,
and the resulting configuration is stabilized by repeatedly
toppling unstable sites.

## Status

Open: the problem is in $\P$, but its $\P$-completeness in dimension
two is unresolved.

## Remarks

Moore and Nilsson [[1]](#1) proved $\P$-completeness of the
Abelian sandpile prediction problem in dimensions $d \geq 3$.

Concha-Vega et al. [[2]](#2) studied sandpile prediction for all
256 sub-neighborhoods of the two-dimensional Moore neighborhood
and established $\P$-completeness for 12 of them.

The complexity of prediction for the standard two-dimensional
von Neumann neighborhood remains open. The results for specific
sub-neighborhoods of the Moore neighborhood do not settle the
complexity for the full Moore neighborhood.