---
title: '$d$-Dimensional Majority Cellular Automata Prediction'
acronym: "MAJPRED"
categories: ["Discrete Dynamical Systems"]
status: "p-complete"
tags: ["majority", "voting"]
references: [380, 381, 382]
related_problems:
  - id: mcvp
    relation: "reduces-from"  # also: reduces-from, reduces-from-variant-of, reduces-to, equivalent, variant
---

## Input

An integer $d \geq 2$, an integer $n \geq 3$, an initial configuration
$x \in \\{-1,+1\\}^{(\mathbb{Z}/n\mathbb{Z})^d}$, a time horizon $T \geq 0$
(encoded in binary), and a designated cell $v \in (\mathbb{Z}/n\mathbb{Z})^d$.

## Problem

Is the state of cell $v$ equal to $+1$ after $T$ synchronous updates
of the $d$-dimensional majority cellular automaton?

## Definitions

The automaton evolves on a $d$-dimensional torus. Each cell has state
$-1$ or $+1$ and updates synchronously according to the majority of
its $2d$ nearest neighbors, retaining its current state in case of a tie.

Writing $x^{(t)}$ for the configuration at time $t$, the update rule is

$$ x_v^{(t+1)}=
\operatorname{sgn}\left(
x_v^{(t)}+\sum_{u\sim v}x_u^{(t)}
\right),
$$

where $u\sim v$ denotes the $2d$ nearest neighbors of $v$ (von Neumann neigborhood).

## Status

$\P$-complete under logspace many-one reductions for every fixed
dimension $d \geq 2$.

## Remarks

Moore [[1]](#1) proved $\P$-completeness for every dimension $d \geq 3$.
Montealegre and Ríos-Wilson [[2]](#2) subsequently established
$\P$-completeness in dimension $d=2$, resolving the remaining case
for dimensions $d \geq 2$.

The time horizon $T$ is encoded in binary. Membership in $\P$
follows from the polynomial bound on the transient of the majority
dynamics, based on the energy-function approach of Goles,
Fogelman-Soulié, and Pellegrin [[3]](#3).
