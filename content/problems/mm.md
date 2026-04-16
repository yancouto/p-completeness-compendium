---
title: "Maximum Matching"
acronym: "MM"
book_id: "B.9.7"
categories: ["Network Flows"]
status: "open"
tags: ["RNC"]
references: [103, 196, 271, 188]
related_problems:
  - id: pme
    relation: see-also
---

## Given

An undirected graph $G = (V, E)$.

## Problem

Find a maximum matching of $G$.

## Definitions

A *matching* is a subset of edges that share no endpoints. A matching is *maximum* if no matching of larger cardinality exists.

## Status

Open (Feather [[1]](#1), Karp, Upfal, and Wigderson [[2]](#2), Mulmuley, Vazirani, and Vazirani [[3]](#3)).

## Remarks

Feather shows that the problem of finding the *size* of a maximum matching is in $\mathsf{RNC}$ [[1]](#1). Karp, Upfal, and Wigderson gave the first $\mathsf{RNC}$ algorithm for *finding* the maximum matching [[2]](#2). A more efficient algorithm was given by Mulmuley, Vazirani, and Vazirani [[3]](#3).

Karloff shows how any $\mathsf{RNC}$ algorithm for matching can be made errorless [[4]](#4). *Maximum Edge-weighted Matching* for unary edge weights and *Maximum Vertex-weighted Matching* for binary vertex weights are also known to be in $\mathsf{RNC}$ [[2]](#2)[[3]](#3). See also [PME]({{< relref "./pme.md" >}}).