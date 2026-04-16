---
title: "Two-way DPDA Acceptance"
acronym: "2DPDA"
book_id: "A.7.8"
categories: ["Formal Languages"]
status: "p-complete"
tags: []
references: [61, 111, 112, 225, 162, 348]
related_problems:
  - id: cvp
    relation: reduces-from
  - id: lgap
    relation: reduces-to
---

## Given

A two-way deterministic pushdown automaton $M = (Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$ and a string $x$.

## Problem

Is $x$ accepted by $M$?

## Status

$\P$-complete (Cook [[1]](#1), Galil [[2]](#2)[[3]](#3), Ladner [[4]](#4)).

## Remarks

See, for example, Hopcroft and Ullman [[5]](#5) for a definition of 2DPDAs. Cook gives a direct simulation of a polynomial time Turing machine by a logarithmic space *auxiliary* pushdown automaton [[1]](#1). Galil shows the existence of a $\P$-complete language accepted by a 2DPDA, in effect showing that the logarithmic space work tape is not crucial to Cook's simulation [[2]](#2)[[3]](#3). (See also Sudborough [[6]](#6) for a general reduction of auxiliary PDAs to ordinary PDAs.) Ladner gives a much more direct proof by observing that a suitably encoded version of [CVP]({{< relref "./cvp.md" >}}) is solvable by a 2DPDA, basically by doing a depth-first search of the circuit, using the stack for backtracking [[4]](#4).

Remains in $\P$ when generalized to nondeterministic and/or logarithmic space auxiliary PDAs [[1]](#1). When restricted to one-way PDAs, or other polynomial time PDAs, even with a logarithmic space work tape, the problem is in $\NC$; specifically, it is complete for $\mathsf{LOGDCFL}$ in the deterministic case, and for $\mathsf{LOGCFL} = \mathsf{SAC}^1$ in the nondeterministic case.
