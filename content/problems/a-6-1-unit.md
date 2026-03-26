---
title: "Unit Resolution"
acronym: "UNIT"
book_id: "A.6.1"
categories: ["Logic"]
status: "p-complete"
tags: ["logic", "sat", "resolution", "unit-propagation"]
draft: false
references:
  - author: "Jones, N. D. and Laaser, W. T."
    title: "Complete Problems for Deterministic Polynomial Time"
    year: 1976

related_problems:
  - id: "a-6-2-horn"
    relation: "variant"
  - id: "a-6-3-phcs"
    relation: "see-also"
---

## Given

A set of **clauses** $S$ over Boolean variables $x_1, \ldots, x_n$. A clause is a disjunction (OR) of **literals**, where a literal is either a variable $x_i$ or its negation $\neg x_i$. The set $S$ contains at least one **unit clause** (a clause with exactly one literal). Also given is a target variable $x_j$.

## Problem

Can $x_j$ or $\neg x_j$ be derived from $S$ using only **unit resolution**?

**Unit resolution** proceeds as follows: while there exists a unit clause $\{l\}$ containing a single literal $l$:
1. Remove from $S$ all clauses containing $l$ (they are satisfied)
2. Remove $\neg l$ from all remaining clauses (since $\neg l$ must be false)
3. If any clause becomes empty, the original set is unsatisfiable
4. If $x_j$ or $\neg x_j$ appears as a unit clause, it has been derived


## Status

P-complete via NC reduction [1].

## Remarks

Unit resolution is a restricted form of resolution that is commonly used in SAT solvers for **unit propagation** — a key technique in modern DPLL-based algorithms.

Despite being a "simple" inference rule, determining what can be derived by unit resolution alone is P-complete. This has implications for the parallelization of SAT solving techniques.

The related problem of **Horn clause satisfiability** (PHCS, Problem A.6.3) is also P-complete, showing that even very restricted forms of propositional reasoning are inherently sequential.

