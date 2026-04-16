---
title: "Longcake"
acronym: "LONGCAKE"
book_id: "A.11.4"
categories: ["Games"]
status: "p-complete"
tags: []
references: [51]
related_problems:
  - id: agg
    relation: reduces-from
---

## Given

Two players $H$ and $V$, a token, and an $m \times n$ Boolean matrix $M$.

## Problem

Does $H$ have a winning strategy on $M$?

## Description

Initially, the token is placed on position $m_{11}$ of $M$, it is $H$'s turn to move, and the current submatrix is $M$. The term *current submatrix* denotes the portion of $M$ that the game is currently being played on. $H$'s turn consists of moving the token horizontally within the current submatrix to some entry $m_{ij} = 1$. At this point, either all columns to the left of $j$ or all columns to the right of $j$ are removed from the current submatrix, depending on which causes fewer columns to be removed. Note that the token occupies a corner of the current submatrix again. $V$'s turn is similar except $V$ moves vertically and rows are removed. The first player with no moves left loses.

## Status

$\P$-complete (Chandra and Tompa [[1]](#1)).

## Remarks

The reduction to show hardness is from [AGG]({{< relref "./agg.md" >}}).
The game *Shortcake* is the same as Longcake except the larger portion of the current submatrix is thrown away. Shortcake is complete for $\mathsf{AC}^1$ [[1]](#1). Another variant of these games called *Semicake* is complete for $\mathsf{LOGCFL} = \mathsf{SAC}^1$ [[1]](#1).
