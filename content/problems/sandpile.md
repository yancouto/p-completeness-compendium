---
title: '$d$-Dimensional Abelian Sandpile Prediction'
acronym: "SANDPRED"
categories: ["Discrete Dynamical Systems"]
status: "p-complete"
tags: ["sandpiles", "chip-firing"]
references: [383]
related_problems:
  - id: mcvp
    relation: "reduces-from"
  - id: sp2d
    relation: "variant"
  - id: tsp2d
    relation: "variant"
---

## Input

An integer $d \geq 3$, an integer $n \geq 1$, a stable configuration
$x \in \\{0,\ldots,2d-1\\}^{[n]^d}$, and two sites $u,v \in [n]^d$.

## Problem

Does site $v$ topple during the stabilization of the configuration
obtained by adding one grain to site $u$ in the initial configuration
$x$?

## Definitions

The sandpile evolves on the finite $d$-dimensional grid $[n]^d$,
with open boundary conditions: grains sent outside the grid are
dissipated.

Each site contains a non-negative integer number of grains. A site
is unstable if it contains at least $2d$ grains. When an unstable
site topples, it loses $2d$ grains and sends one grain to each of
its $2d$ nearest neighbors; grains sent to sites outside the grid
are lost.

The initial configuration $x$ is stable, meaning that every site
contains fewer than $2d$ grains. The perturbation consists of adding
one grain to site $u$. The resulting configuration is then
stabilized by repeatedly toppling unstable sites. The Abelian
property guarantees that the number of times each site topples
during stabilization is independent of the order of topplings.

## Status

$\P$-complete under logspace many-one reductions for every fixed
dimension $d \geq 3$.

## Remarks

Moore and Nilsson [[1]](#1) proved $\P$-completeness of the
Abelian sandpile prediction problem in dimensions $d \geq 3$.

The problem asks whether a local perturbation of a stable
configuration causes an avalanche to reach a designated site.

The corresponding complexity classification in dimension $d=2$
remains open.