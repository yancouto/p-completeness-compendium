---
title: "Low Degree Subgraph"
acronym: "LDS"
book_id: "B.1.5"
categories: ["Circuit Complexity"]
status: "open"
tags: []
references: [119, 134]
related_problems:
  - id: lfmis
    relation: see-also
  - id: sccm
    relation: see-also
---

## Input

An undirected graph $G = (V, E)$ and an integer $k$.

## Problem

Find a maximal induced subgraph with maximum degree at most $k$.

## Status

Open (Godbeer [[1]](#1), Greenlaw [[2]](#2)).

## Remarks

The *Maximal Independent Set Problem* is a LDS with $k$ equal to zero, see [LFMIS]({{< relref "./lfmis.md" >}}). Godbeer shows that LDS can be viewed as a *Connectionist Model* problem in which edge weights have value $-1$ [[1]](#1), see [SCCM]({{< relref "./sccm.md" >}}). Two decision problems based on low degree subgraph computations are proved $\NP$-complete in [[2]](#2).
