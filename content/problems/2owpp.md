---
title: "2-Oriented Weighted Planar Partitioning"
acronym: "2OWPP"
book_id: "B.6.3"
categories: ["Logic"]
status: "open"
tags: []
references: [18]
related_problems:
  - id: 3owpp
    relation: variant
---

## Input

A set of nonintersecting segments $s_1, \ldots, s_n$ in the Euclidean plane, a set of associated integer weights $w_1, \ldots, w_n$, and two designated segments $r$ and $t$. The segments are *2-oriented* meaning that there are only two different possible slopes for the segments.

## Problem

Do segments $r$ and $t$ "touch" in the partitioning of the plane constructed by extending segments in the order of their weights? Segments are extended until they reach another segment or a previous segment extension.

## Status

Open (Atallah, Callahan, and Goodrich [[1]](#1)).

## Remarks

The 3-oriented version, [3OWPP]({{< relref "./3owpp.md" >}}), in which three different slopes are allowed, is $\P$-complete [[1]](#1).