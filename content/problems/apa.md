---
title: "Andersen's Pointer Analysis"
acronym: "APA"
categories: ["Formal Languages"]
status: "p-complete"
tags: []
references:
  - author: "A. A. Mathiasen and A. Pavlogiannis"
    title: "The fine-grained and parallel complexity of andersen's pointer analysis"
    year: 2000
    doi: "10.1007/3-540-45591-4_14"
related_problems:
  - id: mcvp
    relation: reduces-from
---

## Input

A set $A$ of $n$ *pointers* and a set $S$ of $m$ *statements*. Two pointers $a, b \in A$.

## Problem

Could $b$ point to $a$ after a sequence of statements? That is, is $b \in [[a]]$?

## Definitions

Each statement may be of the type `a = b`, `a = &b`, `a = *b` or `*a = b` (note $m = O(n^2)$). Each pointer starts pointing to `null`, and after that, any number of statements (including repetitions) may be used in any order.

More formally, each $[[p]] \subseteq A$ is the smallest set which satifies all the constraints of the statements, and each stament may be the constraint $[[b]] \subseteq [[a]]$, $b \in [[a]]$, $\forall c \in [[b]] \colon [[c]] \subseteq [[a]]$ or $\forall c \in [[a]] \colon [[b]] \subseteq [[c]]$, corresponding to the types defined previously.

## Status

$\P$-complete (Mathiasen and Pavlogiannis [[1]](#1)).

## Remarks

The reduction to show hardness is from [MCVP]({{< relref "./mcvp.md" >}}).
The problem is $\NC^{i+2}$ if one is restricted to use only $\log^i n$ type-4 statements in the solution [[1]](#1).