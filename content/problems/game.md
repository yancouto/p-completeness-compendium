---
title: "Two Player Game"
acronym: "GAME"
book_id: "A.11.1"
categories: ["Games"]
status: "p-complete"
tags: []
references: [181, 202]
related_problems:
  - id: am2cvp
    relation: reduces-from
  - id: gen
    relation: reduces-from
---

## Given

A two player game $G = (P_1, P_2, W_0, s, M)$.

## Problem

Is $s$ a winning position for the first player?

## Definitions

In the game, $P_1 \cap P_2 = \varnothing$, $W_0 \subseteq P_1 \cup P_2$, $s \in P_1$, and $M \subseteq P_1 \times P_2 \cup P_2 \times P_1$. $P_i$ is the set of positions in which it is player $i$'s turn to move. $W_0$ is the set of immediate winning positions (defined below) for player one, and $s$ is the starting position. $M$ is the set of allowable moves; if $(p, q) \in M$ and $p \in P_1$ (or $P_2$) then player one (respectively, or two) may move from position $p$ to position $q$ in a single step. A position $x$ is *winning* for player one if and only if $x \in W_0$, or $x \in P_1$ and $(x, y) \in M$ for some winning position $y$, or $x \in P_2$ and $y$ is winning for every move $(x, y)$ in $M$.

## Status

$\P$-complete (Jones and Laaser [[1]](#1), Greenlaw, Hoover, and Ruzzo [[3]](#3)).

## Remarks

The reduction to show hardness is from [GEN]({{< relref "./gen.md" >}}) [[1]](#1) or [AM2CVP]({{< relref "./am2cvp.md" >}}) [[3]](#3). Since GAME is an instance of AND/OR Graph Solvability, it follows that determining whether an AND/OR graph has a solution is also $\P$-complete (Kasif [[2]](#2)).
