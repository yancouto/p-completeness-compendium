---
title: "Monadic Krom Satisfiability"
acronym: "MKS"
book_id: "A.6.4"
categories: ["Logic"]
status: "p-complete"
tags: []
references: [89, 88]
related_problems:
  - id: 2dpda
    relation: see-also
---

## Input

A monadic Krom formula $F$.

## Problem

Is $F$ satisfiable?

## Definitions

A *Krom formula* is a $2$-CNF formula. That is, a formula in CNF with at most two disjuncts per clause. Let $\varphi$ and $\psi$ be predicate letters that may be preceded by a negation. A conjunct of $F$ is *monadic* if it is of the form $(\varphi y_1 y_1 \vee \psi y_1 y_1)$.

## Status

$\P$-complete (Denenberg and Lewis [[1]](#1)).

## Remarks

An algorithm showing the problem is in P is given in [[1]](#1).
The reduction to show hardness is from a Nonacceptance Problem for Pushdown Automata (Denenberg [[2]](#2)[[1]](#1)), see [2DPDA]({{< relref "./2dpda.md" >}}).
