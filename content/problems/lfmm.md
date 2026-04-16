---
title: "Lexicographically First Maximal Matching"
acronym: "LFMM"
book_id: "B.8.2"
categories: ["Matching"]
status: "open"
tags: ["CC"]
references: [255]
related_problems:
  - id: ccvp
    relation: equivalent
  - id: lfmis
    relation: see-also
  - id: ewm
    relation: see-also
---

## Given

An undirected graph $G = (V, E)$ with an ordering on its edges and a distinguished edge $e \in E$.

## Problem

Is $e$ in the lexicographically first maximal matching of $G$?

## Definitions

A matching is *maximal* if it cannot be extended.

## Status

Open (Mayr and Subramanian [[1]](#1)).

## Remarks

This problem is in $\CC$, that is, it is equivalent to [CCVP]({{< relref "./ccvp.md" >}}).
It resembles [LFMIS]({{< relref "./lfmis.md" >}}) that is $\P$-complete. A $\P$-completeness proof for LFMM would imply that [EWM]({{< relref "./ewm.md" >}}), is also $\P$-complete.
