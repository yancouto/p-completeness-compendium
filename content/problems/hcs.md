---
title: "High Connectivity Subgraph"
acronym: "HCS"
book_id: "A.2.8"
categories: ["Graph Theory"]
status: "p-complete"
tags: []
references: [214, 326, 328, 209]
related_problems:
  - id: am2cvp
    relation: reduces-from
---

## Given

An undirected graph $G = (V, E)$ and an integer $k$.

## Problem

Does $G$ contain a vertex induced subgraph of vertex (edge) connectivity at least $k$?

## Status

$\P$-complete (Kirousis, Serna, and Spirakis [[1]](#1), Serna [[2]](#2)).

## Remarks

The reduction to show hardness is from [AM2CVP]({{< relref "./am2cvp.md" >}}).

Approximation algorithms for this problem exhibit a threshold type behavior. Below a certain value on the absolute *performance ratio* the problem remains $\P$-complete for fixed $k$, and above that ratio there are $\NC$ approximation algorithms for the problem (Serna and Spirakis [[3]](#3)). Specifically, let $o$ be the maximum size of a $k$-vertex connected induced subgraph of $G$. Then for $0 \leq c \leq 1/4$ it is possible to find, in $\NC$, a vertex induced subgraph of size greater than or equal to $co$, but for $1/4 < c \leq 1$ this is not possible, unless $\NC = \P$. For edge connectivity, the threshold is $c = 1/2$.

Khuller and Schieber present an algorithm for an ARBITRARY CRCW-PRAM that given an undirected graph $G$ and an integer $k$ tests whether $G$ is $k$-vertex connected [[4]](#4). If $G$ is not $k$-vertex connected, they obtain a set of at most $k - 1$ vertices whose removal disconnects $G$. Their algorithm runs in $O(k^2 \log n)$ time and uses $k(n + k^2)C(n, m)$ processors, where $C(n, m)$ is the number of ARBITRARY CRCW-PRAM processors required to compute the connected components of an $n$-vertex, $m$-edge graph in logarithmic time. For polylogarithmic $k$, this is an $\NC$ algorithm.
