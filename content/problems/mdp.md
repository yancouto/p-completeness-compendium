---
title: "Maximum Disjoint Paths"
acronym: "MDP"
book_id: "B.9.5"
categories: ["Network Flows"]
status: "open"
tags: ["RNC"]
references: [12]
related_problems:
  - id: paths
    relation: variant
---

## Given

An undirected graph $G = (V, E)$ and a set of vertices $U \subseteq V$.

## Problem

Find a maximum cardinality set of nontrivial vertex disjoint paths that have their endpoints in $U$.

## Status

Open (Anderson [[1]](#1)).

## Remarks

MDP is first reduced to a bidirectional flow problem that is in turn reduced to a matching problem [[1]](#1). See [PATHS]({{< relref "./paths.md" >}}).
