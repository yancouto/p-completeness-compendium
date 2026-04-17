---
title: "Finite Horizon Markov Decision Process"
acronym: "FHMDP"
book_id: "A.8.1"
categories: ["Algebra"]
status: "p-complete"
tags: []
references: [279, 164, 361]
related_problems:
  - id: mcvp
    relation: reduces-from
---

## Input

A nonstationary Markov decision process $M = (S, c, p)$ and an integer $T$. 

## Problem

Is the minimum expected cost of $$\sum_{t=0}^{T} c(s_t, \delta(s_t, t), t)$$ over all policies $\delta$ equal to $0$?

## Definitions

Before defining the problem, we present some background on Markov decision processes. The term *finite horizon* refers to the time bound $T$. The set of states $S$ is a finite and contains a designated initial state $s_0$. Let $s_t$ denote the current state of the system for each time $t = 1, 2, \ldots$ Associated with each state $s \in S$ is a finite set of decisions $D_s$. A cost of $c(s, i, t)$ is incurred at time $t$ by making decision $i \in D_{s_t}$. The next state $s'$ has probability distribution given by $p(s, s', i, t)$. If $c$ and $p$ are independent of $t$, then the process is said to be *stationary*. A *policy* $\delta$ is a mapping that assigns to each time step $t$ and each state $s$ a decision $\delta(s, t)$. A policy is *stationary* if $\delta$ is independent of time, and can then be supplied as an input.

## Status

$\P$-complete (Papadimitriou and Tsitsiklis [[1]](#1)).

## Remarks

There is a polynomial time algorithm for the problem that uses dynamic programming (Howard [[2]](#2)). The reduction to show hardness is from [MCVP]({{< relref "./mcvp.md" >}}).

The reduction shows that the finite horizon stationary version of the problem is $\P$-hard. This problem is not known to be in $\P$. The *deterministic* version of the FHMDP, which requires that $p$ only has values $0$ or $1$, is in $\NC$ [[1]](#1). Note, this last result holds for both the stationary and nonstationary versions of the problem.
