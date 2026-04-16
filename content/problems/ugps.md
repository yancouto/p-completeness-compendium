---
title: "Unweighted Graph Partitioning SWAP"
acronym: "UGPS"
book_id: "A.5.6"
categories: ["Local Optimality"]
status: "p-hard"
tags: []
references: [278, 319, 320, 324, 178]
related_problems:
  - id: mcvp
    relation: reduces-from-variant-of
---

## Given

An undirected graph $G = (V, E)$ with $2n$ vertices.

## Problem

Find a locally optimal partition of $V$ into two equal size sets.

## Definitions

The partition $V_1$ and $V_2$ is *locally optimal* if the number of edges going between $V_1$ and $V_2$ is minimum among all neighbors of the partition. A *neighbor* is a partition that can be obtained from $V_1$ and $V_2$ by swapping one element of $V_1$ with one element of $V_2$.

## Status

$\P$-complete (Papadimitriou, Schäffer, and Yannakakis [[1]](#1), Savage and Wloka [[2]](#2)[[3]](#3), Schäffer and Yannakakis [[4]](#4)).

## Remarks

The reduction to show hardness is from a variant of [MCVP]({{< relref "./mcvp.md" >}}).
The weighted version of the problem in which the weights are encoded in binary is $\mathsf{PLS}$-complete [[1]](#1)[[4]](#4). If the weights are encoded in unary, the problem is $\mathsf{FP}$-complete (Johnson, Papadimitriou, and Yannakakis [[5]](#5)). Another problem the *Fiduccia-Mattheyses Heuristic Graph Partitioning SWAP* (FM-Graph Partitioning in [[4]](#4)) is defined similarly to UGPS except for the neighbors of a solution. The neighborhood of a solution may be obtained by a sequence of up to $|V|$ swaps following the Fiduccia-Mattheyses heuristic (see [[4]](#4)).

FM-Graph Partitioning is also $\mathsf{FP}$-complete [[3]](#3)[[4]](#4). In fact, a simpler local search problem in which each partition has just one neighbor, the one obtained after the first step of the Fiduccia-Mattheyses heuristic, is also $\mathsf{FP}$-complete [[3]](#3)[[4]](#4). This problem is called FM in [[3]](#3) and FM-SWAP in [[4]](#4). In [[3]](#3) they also show that a simulated annealing based on a SWAP neighborhood and a "cooling schedule" is $\P$-complete. Several additional results are presented proving other graph partitioning strategies are $\P$-hard. See [[2]](#2)[[3]](#3) for further details.
