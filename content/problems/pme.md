---
title: "Perfect Matching Existence"
acronym: "PME"
book_id: "B.9.8"
categories: ["Network Flows"]
status: "open"
tags: ["RNC"]
references:
  - 196
  - 271
  - 76
  - 200
  - 143
  - 144
  - 199
  - 275
  - author: "N. Anari and V. V. Vazirani"
    title: "Planar Graph Perfect Matching Is in NC"
    year: 2020
    doi: "10.1145/3397504"
  - author: "N. Anari and V. V. Vazirani"
    title: "Matching Is as Easy as the Decision Problem, in the NC Model"
    year: 2020
    doi: "10.4230/LIPIcs.ITCS.2020.54"
related_problems:
  - id: mm
    relation: see-also
---

## Given

An undirected graph $G = (V, E)$.

## Problem

Does $G$ have a perfect matching?

## Definitions

A *matching* is a subset of edges that share no endpoints. A *perfect matching* is a matching where each vertex is incident to one edge in the matching.

## Status

Open (Karp, Upfal, and Wigderson [[1]](#1), Mulmuley, Vazirani, and Vazirani [[2]](#2)).

## Remarks

See remarks for [MM]({{< relref "./mm.md" >}}). PME seems to be the simplest of the matching problems not known to be in $\NC$. Dahlhaus, Hajnal, and Karpinski show that a perfect matching can be found in a "dense" graph in $\NC^2$ [[3]](#3). Karpinski and Wagner show that when $G$ is given by its *vertex multiplicity graph* representation the problem becomes $\P$-complete [[4]](#4). Using such succinct graph representations they are also able to show that the *Perfect Bipartite Matching Problem* is $\P$-complete [[4]](#4).

Grigoriev and Karpinski show that if the *permanent* of $G$ is polynomially bounded, one can decide whether $G$ has a perfect matching in $\NC^2$. They show how to construct such a matching in $\NC^3$ [[5]](#5). See Grigoriev, Karpinski, and Singer [[6]](#6) and Karpinski [[7]](#7) for additional related work. Osiakwan and Akl designed an EREW-PRAM algorithm for solving the *Maximum Weight Perfect Matching Problem* for complete weighted graphs. Their algorithm runs in $O(n^3/p + n^2 \log n)$ time for $p \leq n$, where $n$ is the number of vertices in the graph and $p$ is the number of processors [[8]](#8).

The problem is in $\mathsf{RNC}$, and there exists an $\NC$ algorithm for PME in planar graphs.
However, only in 2020, Anari and Vazirani discovered an $\NC$ algorithm for its *search* variant, that is, an $\NC$ algorithm to *find* a perfect matching in planar graphs [[9]](#9).

Further developments show that the search variant is as hard as the decision variant, that is, given an $\NC$ algorithm for PME, it is possible to create an $\NC$ algorithm for *finding* a perfect matching in a general graph [[10]](#10). PME, however, remains an open problem.