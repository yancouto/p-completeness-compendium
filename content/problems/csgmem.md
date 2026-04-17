---
title: "Forward Deterministic Growing Context-sensitive Grammar Membership"
acronym: "CSGmem"
book_id: "A.7.5"
categories: ["Formal Languages"]
status: "p-complete"
tags: []
references: [312]
related_problems:
  - id: gmsp
    relation: reduces-from
---

## Input

A forward deterministic growing context-sensitive grammar $G = (N, T, P, S)$ and a string $x \in T^\ast$. 

## Problem

Is $x \in L(G)$?

## Definitions

A context-sensitive grammar is *growing* if for each production $\alpha \to \beta \in P$, where $\alpha, \beta \in (N \cup T)^\ast$, $|\alpha|$ is less than $|\beta|$. A context-sensitive grammar is *forward deterministic* if whenever there are derivations of a sentential form $u$, $u \Rightarrow v$ and $u \Rightarrow v'$, then $v$ equals $v'$.

## Status

$\P$-complete (Sang Cho and Huynh [[1]](#1)).

## Remarks

The reduction to show hardness is from a version of [GMSP]({{< relref "./gmsp.md" >}}).
The proof yields as a straightforward corollary that *Nondeterministic Growing Context-sensitive Grammar Membership* is $\NP$-complete [[1]](#1).
