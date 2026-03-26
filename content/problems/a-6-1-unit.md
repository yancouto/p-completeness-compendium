---
title: "Unit Resolution"
acronym: "UNIT"
problem_id: "A.6.1"
category: "Logic"
status: "p-complete"
tags: ["logic", "sat", "resolution", "unit-propagation"]
draft: false
references:
  - author: "Jones, N. D. and Laaser, W. T."
    title: "Complete Problems for Deterministic Polynomial Time"
    year: 1976
    citation: "[196]"
related_problems:
  - id: "a-6-2-horn"
    relation: "variant"
  - id: "a-6-3-phcs"
    relation: "see-also"
---

## Given

A set of clauses $S$ over the Boolean variables $x_1, \ldots, x_n$ containing at least one **unit clause** (a clause with exactly one literal), and a variable $x_j$.

## Problem

Can $x_j$ (or $\neg x_j$) be derived from $S$ by **unit resolution**?

Unit resolution is defined as follows: If $S$ contains a unit clause $\{l\}$ (where $l$ is a literal), then:
1. Remove from $S$ all clauses containing $l$
2. Remove $\neg l$ from all remaining clauses
3. Repeat until no unit clauses remain or the empty clause is derived

## Remarks

Unit resolution is a restricted form of resolution that is commonly used in SAT solvers for **unit propagation** — a key technique in modern DPLL-based algorithms.

Despite being a "simple" inference rule, determining what can be derived by unit resolution alone is P-complete. This has implications for the parallelization of SAT solving techniques.

The related problem of **Horn clause satisfiability** (PHCS, Problem A.6.3) is also P-complete, showing that even very restricted forms of propositional reasoning are inherently sequential.
