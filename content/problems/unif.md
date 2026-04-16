---
title: "Unification"
acronym: "UNIF"
book_id: "A.6.9"
categories: ["Logic"]
status: "p-complete"
tags: []
references: [96, 97, 375, 305, 52, 366, 224, 74]
related_problems:
  - id: mcvp
    relation: reduces-from
  - id: nandcvp
    relation: reduces-from
  - id: cvp
    relation: reduces-from
---

## Given

Two symbolic terms $s$ and $t$.

## Problem

Is there a series of substitutions $\sigma$ that unify $s$ and $t$? 

## Definitions

Each term is composed of variables and function symbols. A *substitution* for $x$ in a term $u$ is the replacement of all occurrences of a variable $x$ in $u$ by another term $v$. A series of substitutions $\sigma$ unify $s$ and $t$ if $\sigma(s) = \sigma(t)$. The two terms are called unifiable if such a $\sigma$ exists.

## Status

$\P$-complete (Dwork, Kanellakis, and Mitchell [[1]](#1), Dwork, Kanellakis, and Stockmeyer [[2]](#2), Yasuura [[3]](#3)).

## Remarks

The reduction to show hardness is from [MCVP]({{< relref "./mcvp.md" >}}) [[1]](#1), [NANDCVP]({{< relref "./nandcvp.md" >}}) [[2]](#2) or another variant of [CVP]({{< relref "./cvp.md" >}}) [[3]](#3).

Robinson defined unification in [[4]](#4). The reader is also referred to Chang and Lee [[5]](#5) for some basic discussion about mechanical theorem proving. The *Unrestricted Unification Problem* is also  $\P$-complete [[1]](#1). *Unrestricted unification* is where substitutions are allowed to map variables to infinite terms. It is convenient to represent terms as labeled directed acyclic graphs. A term is *linear* if no variable appears more than once in it. The following two restricted versions of unification are also both  $\P$-complete: (a) both terms are linear, are represented by trees, and have all function symbols with arity less than or equal to two; (b) both terms are represented by trees, no variable appears in both terms, each variable appears at most twice in some term, and all function symbols have arity less than or equal to two [[2]](#2).

A restricted problem called *Term Matching* can be solved in $\NC$ [[1]](#1). A term $s$ *matches* a term $t$ if there exists a substitution $\sigma$ with $\sigma(s) = t$. Dwork, Kanellakis, and Mitchell used randomization to reduce the processor bound given in [[1]](#1). On a CREW-PRAM their algorithm runs in randomized time $O((\log n)^2)$ using $M(n)$ processors, where $M(n)$ denotes the complexity of an $n \times n$ matrix multiplication [[2]](#2). Vitter and Simons give a $\sqrt{n}$ time parallel algorithm for Unification when the instances of the problem are "dense" [[6]](#6).

Kuper et al. give an $\NC$ algorithm for the problem of constructing the most specific anti-unifier [[7]](#7). This is the dual problem of unification. The *most specific anti-unifier* of $m$ terms $t_1, \ldots, t_m$ is a term $t_g$ such that
1. Each $t_i$ is an instance of $t_g$ and
2. $t_g$ is an instance of any term with property one above.

Their algorithm produces a most specific anti-unifier for $m$ terms of size $O(n)$ on a CREW-PRAM in time $O((\log mn)^2)$ using $mn$ processors [[7]](#7).
