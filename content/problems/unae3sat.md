---
title: "Unweighted, Not-all-equal Clauses, 3SAT FLIP"
acronym: "UNAE3SAT"
book_id: "A.5.3"
categories: ["Local Optimality"]
status: "p-hard"
tags: []
references: [278, 324]
related_problems:
  - id: nandcvp
    relation: reduces-from-variant-of
  - id: umcs
    relation: reduces-to
---

## Given

A Boolean formula $F$ in CNF with three positive literals per clause.

## Problem

Find a locally optimal assignment for $F$.

## Definitions

An assignment is *locally optimal* if it has maximum cost among its neighbors. The *cost* of the assignment is the number of not-all-equals clauses that are satisfied by the assignment; each clause has a weight of one. A truth assignment satisfies a clause $C$ under the *not-all-equals* criterion if it is such that $C$ has at least one true and one false literal. The *neighbors* of an assignment $s$ are assignments that can be obtained from $s$ by flipping the value of one variable.

## Status

$\P$-hard (Papadimitriou, Schäffer, and Yannakakis [[1]](#1), Schäffer and Yannakakis [[2]](#2)).

## Remarks

The reduction to show hardness is from [NORCVP]({{< relref "./nandcvp.md" >}}).

The weighted version of the problem in which each clause is given an integer weight coded in binary is $\mathsf{PLS}$-complete [[1]](#1)[[2]](#2). If the weights are encoded in unary, the problem is $\mathsf{FP}$-complete.
