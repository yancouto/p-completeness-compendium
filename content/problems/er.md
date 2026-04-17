---
title: "Edge Ranking"
acronym: "ER"
book_id: "B.1.2"
categories: ["Circuit Complexity"]
status: "open"
tags: []
references: [91, 84, 81, 82, 191]
related_problems:
  - id: lfdvc
    relation: see-also
  - id: fill
    relation: see-also
  - id: ec
    relation: see-also
---

## Input

A tree $T = (V, E)$.

## Problem

Find an optimal edge ranking of $T$.

## Definitions

An *edge ranking* of a tree is a labeling of the edges using positive integers such that the path between two edges with the same label contains an intermediate edge with a higher label. An edge ranking is *optimal* if the highest label used is as small as possible.

## Status

Open (Dessmark, Lingas, and Maheshwari [[1]](#1)).

## Remarks

This problem was proved to be in $\P$ in [[2]](#2). They give a $\NC$ approximation algorithm for the problem that finds an edge ranking within a factor of two of optimal. An $\NC$ algorithm for constant degree trees is also given in [[2]](#2). A similar problem called the *Node Ranking Problem* for trees in which the vertices are labeled, instead of the edges, was proved to be in $\NC$ (de la Torre and Greenlaw [[3]](#3), de la Torre, Greenlaw, and Przytycka [[4]](#4)). See [FILL]({{< relref "./fill.md" >}}) for a related $\P$-complete problem. Karloff and Shmoys give $\NC$ algorithms for several versions of edge ranking multigraphs [[5]](#5), a problem having a similar flavor. See [LFDVC]({{< relref "./lfdvc.md" >}}) and [EC]({{< relref "./ec.md" >}}) for a description of their results.
