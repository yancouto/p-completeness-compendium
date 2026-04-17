---
title: "Iterated Shuffle"
acronym: "SHUF"
book_id: "A.7.15"
categories: ["Formal Languages"]
status: "p-complete"
tags: []
references: [332, 274]
related_problems:
  - id: nandcvp
    relation: reduces-from
---

## Input

A language $L$ over a finite alphabet $\Sigma$ described in terms of the operators $\cdot$, $\*$, $\cup$, $\cap$, $\Delta$, and $\dagger$; which denote concatenation, Kleene star, union, intersection, shuffle, and iterated shuffle, respectively; plus a designated word $w \in \Sigma^\ast$.

## Problem

Is $w \in L$?

## Definitions

The *shuffle* of two languages $L_1$ and $L_2$, denoted $L_1 \Delta L_2$, is $$\\{x_1 y_1 x_2 y_2 \cdots x_m y_m \mid x_1 x_2 \cdots x_m \in L_1, y_1 y_2 \cdots y_m \in L_2 \text{ and } x_i, y_i \in \Sigma^\ast \text{ for } i = 1, \ldots, m\\}.$$ The *iterated shuffle* denoted $L^\dagger$ is $$\\{\epsilon\\} \cup L \cup (L \Delta L) \cup (L \Delta L \Delta L) \cup \cdots.$$

## Status

$\P$-complete (Shoudai [[1]](#1)).

## Remarks

Certain restrictions must be placed on $L$ in order for this problem to be in $\P$. The reduction to show hardness is from a variant of [NORCVP]({{< relref "./nandcvp.md" >}}).

It is known that there are two deterministic context-free languages whose shuffle is $\NP$-complete (Ogden, Riddle, and Rounds [[2]](#2)). Here the intersection operation is used to force the problem into $\P$ [[1]](#1).
