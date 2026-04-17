---
title: "Bounded Degree Graph Isomorphism"
acronym: "BDGI"
book_id: "B.1.1"
categories: ["Circuit Complexity"]
status: "open"
tags: []
references: [110, 118, 241]
related_problems:
  - id: sti
    relation: see-also
---

## Input

Two undirected graphs $G = (V, E)$ and $H = (V', E')$. The vertices in $G$ and $H$ have maximum degree at most $k$, a constant independent of the sizes of $G$ and $H$.

## Problem

Are $G$ and $H$ isomorphic?

## Definitions

$G = (V, E)$ and $H = (V', E')$ are *isomorphic* if and only if there are two bijections $f : V \to V'$ and $g : E \to E'$ such that for every edge $e = \\{u, v\\} \in E$, $f(u)f(v) = g(e) \in E'$.

## Status

Open (Furst, Hopcroft, and Luks [[1]](#1)).

## Remarks

Luks showed the problem is in $\P$ [[1]](#1). Without the degree bound, the problem is in $\NP$ but not known to be in $\P$, nor is it known to be either $\P$-hard or $\NP$-complete. Lindell shows that the *Tree Isomorphism* Problem is in $\NC$. *Subtree Isomorphism* is in $\mathsf{RNC}$ (Gibbons et al. [[2]](#2), Lingas and Karpinski [[3]](#3)). See [STI]({{< relref "./sti.md" >}}) for additional details.
