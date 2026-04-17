---
title: "Lexicographically First Maximal Independent Set"
acronym: "LFMIS"
book_id: "A.2.1"
categories: ["Graph Theory"]
status: "p-complete"
tags: []
references: [67, 265, 194, 198, 246, 10, 121, 263]
related_problems:
  - id: nandcvp
    relation: reduces-from
  - id: lfms
    relation: see-also
  - id: lfmc
    relation: equivalent
  - id: grm
    relation: reduces-to
  - id: sccm
    relation: reduces-to
  - id: lfm3s
    relation: reduces-to
---

## Input

An undirected graph $G = (V, E)$ with an ordering on the vertices and a designated vertex $v$.

## Problem

Is vertex $v$ in the lexicographically first maximal independent set of $G$?

## Status

$\P$-complete under $\NC^1$ reductions (Greenlaw, Hoover and Ruzzo [[9, Theorem 7.1.2]](#9), Cook [[1]](#1)).

## Remarks

The reduction to show hardness is from [NORCVP]({{< relref "./nandcvp.md" >}}).
This is an instance of the [LFMS(π)]({{< relref "./lfms.md" >}}). LFMIS is $\P$-complete for bipartite or planar graphs restricted to degree at most three [[2]](#2). Karp observed that the completeness of LFMIS implies that determining the $i^\text{th}$ vertex chosen by any deterministic sequential algorithm for either LFMIS or [LFMC]({{< relref "./lfmc.md" >}}) is also complete [[3]](#3). Computing or approximating the size of the lexicographically first maximal independent set is also $\P$-complete [[9, Section 10]](#9).

Luby gave the first $\NC$ algorithm for finding a maximal independent set [[4]](#4), subsequently improved by Luby [[5]](#5), by Alon, Babai, and Itai [[6]](#6), and by Goldberg and Spencer [[7]](#7). These algorithms do not compute the *lexicographically first* maximal independent set. Using a general result involving inference systems, when $G$ is a forest LFMIS can be solved on a CREW-PRAM in $O(\log |V|)$ time using a polynomial number of processors [[8]](#8).
