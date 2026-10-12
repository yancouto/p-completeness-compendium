---
title: 'Two-Dimensional Timed Sandpile Prediction'
acronym: "TIMEDSANDPRED"
categories: ["Discrete Dynamical Systems"]
status: "open"
tags: ["sandpiles", "chip-firing"]
references: [385]
related_problems:
  - id: sp2d
    relation: "variant"
  - id: sandpile
    relation: "variant"
---

## Input

A finite stable configuration $x \in \\{0,\ldots,7\\}^{\mathbb{Z}^2}$,
two sites $u,v \in \mathbb{Z}^2$, and a time $t \geq 1$.

## Problem

Does site $v$ topple at time $t$ under the synchronous
two-dimensional Moore-neighborhood sandpile dynamics, starting
from the configuration obtained by adding one grain to site $u$
in $x$?

## Definitions

The sandpile evolves on $\mathbb{Z}^2$. Each site contains a
non-negative integer number of grains and is unstable if it
contains at least eight grains.

The neighborhood is the two-dimensional Moore neighborhood:
the eight sites at offsets
$(i,j) \in \\{-1,0,1\\}^2 \setminus \\{(0,0)\\}$.

At each time step, every unstable site topples simultaneously,
losing eight grains and sending one grain to each of its eight
neighbors.

The initial configuration $x$ is stable, meaning that every site
contains fewer than eight grains, and has finite support. One grain
is added to site $u$ before the synchronous dynamics begins.
Time $t$ counts synchronous update rounds, with round $1$ being
the first update after the grain is added.

## Status

Open.

## Remarks

Concha-Vega and Perrot [[1]](#1) proposed and studied the timed prediction
problem for two-dimensional sandpile models with different
sub-neighborhoods of the Moore neighborhood. They established
$\P$-completeness for several specific neighborhoods using
timed logical gates and crossover gadgets.

These results do not settle the complexity of timed prediction
for the full Moore neighborhood.