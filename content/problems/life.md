---
title: "Game of Life"
acronym: "LIFE"
book_id: "A.11.5"
categories: ["Games"]
status: "p-complete"
tags: []
references: [33]
related_problems:
  - id: cvp
    relation: reduces-from
  - id: ca
    relation: see-also
---

## Input

An initial configuration of the Game of Life, a time bound $T$ expressed in unary, and a designated cell $c$ of the grid. 

## Problem

Is cell $c$ live at time $T$?

## Definitions

The *Game of Life* is played on an infinite grid. *Cells*, squares on the grid, are either *live* or *dead*. Each cell has eight *neighbors*. An *initial configuration* specifies that certain cells are live at the beginning of the game. The rules of the game are as follows:
1. A cell that is dead at time $t$ becomes live at time $t+1$ if it had exactly three live neighbors at time $t$.
2. A cell dies at time $t+1$ unless it had two or three live neighbors at time $t$.

## Status

$\P$-complete (Berlekamp, Conway, and Guy [[1, pages 817--850]](#1), Greenlaw, Hoover, and Ruzzo [[2]](#2)).

## Remarks

Berlekamp, Conway, and Guy sketch a reduction that the Game of Life is capable of universal computation and [[2]](#2) translates it into the statement of a $\P$-complete problem from [CVP]({{< relref "./cvp.md" >}}).

The Game of Life is an example of a two dimensional cellular automata, see [CA]({{< relref "./ca.md" >}}). It is not known whether a one dimensional version of the Game of Life can simulate a Turing machine. See [CA]({{< relref "./ca.md" >}}) for more details about one dimensional cellular automata.
