---
title: "Propositional Horn Clause Satisfiability"
acronym: "PHCS"
book_id: "A.6.3"
categories: ["Logic"]
status: "p-complete"
tags: []
references: [202, 290, 203]
related_problems:
  - id: agap
    relation: reduces-from
  - id: rcl
    relation: reduces-to
---

## Input

A set $S$ of Horn clauses in the propositional calculus.

## Problem

Is $S$ satisfiable?

## Status

$\P$-complete (Kasif [[1]](#1), Plaisted [[2]](#2)).

## Remarks

The reduction to show hardness is from [AGAP]({{< relref "./agap.md" >}}).
The problem remains $\P$-complete when there are at most three literals per clause [[2]](#2). Plaisted has shown that two problems involving proofs of restricted depth are also $\P$-complete. They are the *Two Literal Horn Clause Unique Matching Problem* and the *Three Literal Horn Clause Problem* [[2]](#2). Kasif observes that PHCS remains $\P$-complete when the set of clauses is restricted so that implications have at most two atoms on their right-hand side [[3]](#3).
