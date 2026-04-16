---
title: "Horn Unit Resolution"
acronym: "HORN"
book_id: "A.6.2"
categories: ["Logic"]
status: "p-complete"
tags: []
references: [93, 181]
related_problems:
  - id: cvp
    relation: reduces-from
  - id: gmsp
    relation: reduces-from
  - id: mvd
    relation: reduces-to
  - id: lp
    relation: reduces-to
---

## Given

A Horn formula $F$.

## Problem

Can the empty clause $\Box$ be deduced from $F$ by unit resolution?

## Definitions

A *Horn formula* is a conjunctive normal form (CNF) formula with each clause a disjunction of literals having at most one positive literal per clause.

## Status

$\P$-complete (Dobkin, Lipton, and Reiss [[1]](#1), Jones and Laaser [[2]](#2)).

## Remarks

The reduction to show hardness is from [CVP]({{< relref "./cvp.md" >}}) or [GMSP]({{< relref "./gmsp.md" >}}).