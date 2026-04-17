---
title: "Fluid Invasion"
acronym: "FLUID"
book_id: "A.12.4"
categories: ["Miscellaneous"]
status: "p-complete"
tags: []
references: [249, 142, 141]
related_problems:
  - id: nandcvp
    relation: reduces-from-variant-of
  - id: nandcvp
    relation: see-also
---

## Input

A graph $G = (V, E)$, a source $s$ and a sink $s'$, a distinguished vertex $u$, a time $t$, nonnegative real conductances $k_{ij}$ for each edge $ij$, and nonnegative real capacities $\phi_l$ for each vertex $l \in V$ .

## Problem

Is vertex $u$ filled by the invading fluid at time $t$ according to the fluid invasion algorithm?

## Definitions

Informally, the *fluid invasion algorithm* proceeds by adding vertices to the cluster one at a time depending on when they fill up with the fluid being inserted at the source $s$. The *cluster* consists of those vertices that have been filled by the invading fluid. The evolution of the fluid configuration is governed by Darcy's law. Refer to Machta [[1]](#1) for additional details of the fluid model.

## Status

$\P$-complete (Machta [[1]](#1)).

## Remarks

The reduction to show hardness is from [NORCVP]({{< relref "./nandcvp.md" >}}).

Fluid Invasion remains $\P$-complete when $G$ is restricted to being a $l \times l$ two dimensional lattice in which $s$ ($s'$) is connected to all sites on one face (respectively, the opposite face) of the lattice and with all of the conductances equal to one [[1]](#1). The proof that this restricted version is $\P$-complete is complicated and does not seem to follow easily from the result for FLUID. Additional schemes designed to model pattern formation processes are studied from a computational complexity point of view in Greenlaw and Machta [[2]](#2)[[3]](#3). There they provide $\NC$ algorithms to compute *percolation clusters* for three different models — *invasion percolation*, *invasion percolation with trapping*, and *ordinary percolation*.