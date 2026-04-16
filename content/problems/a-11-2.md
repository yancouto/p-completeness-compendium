---
title: "Cat and Mouse"
acronym: "CM"
book_id: "A.11.2"
categories: ["Games"]
status: "p-complete"
tags: []
references: [50]
---

## Given

A directed graph $G = (V, E)$ with three distinguished vertices c, m, and g.

## Problem

Does the mouse have a *winning strategy* in the game?

## Definitions

The game is played as follows. The cat starts on vertex $c$, the mouse on vertex $m$, and $g$ represents the goal vertex. The cat and mouse alternate moves with the mouse moving first. Each move consists of following a directed edge in the graph. Either player has the option to pass by remaining on the same vertex. The cat is not allowed to occupy the goal vertex. The mouse wins if it reaches the goal vertex without being caught. The cat wins if the mouse and cat occupy the same vertex.

## Status

$\P$-complete (Chandra and Stockmeyer [[1]](#1)).

## Remarks

The reduction to show hardness is from a logarithmic space alternating Turing machine.
