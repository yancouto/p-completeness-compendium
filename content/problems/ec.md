---
title: "Edge Coloring"
acronym: "EC"
book_id: "B.9.3"
categories: ["Network Flows"]
status: "open"
tags: ["RNC"]
references:
  - 191
  - author: "A. Bernshteyn and A. Dhawan"
    title: "Fast algorithms for Vizing’s theorem on bounded degree graphs"
    year: 2025
    doi: "10.1016/j.jctb.2025.07.002"
  - author: "A. Bernshteyn and A. Dhawan"
    title: "Efficient Parallel (Δ + 1)-Edge-Coloring (preprint)"
    year: 2026
    doi: "10.48550/arXiv.2601.13822"
related_problems:
  - id: lfdvc
    relation: see-also
  - id: er
    relation: see-also
---

## Given

An undirected graph $G = (V, E)$ with maximum degree $\Delta$.

## Problem

Find an edge coloring of $G$ that uses less than or equal to $\Delta + 1$ colors.

## Definitions

An *edge coloring* is an assignment of colors to the edges such that no incident edges receive the same color.

## Status

Open (Karloff and Shmoys [[1]](#1)).

## Remarks

An $\NC$ algorithm is known for polylogarithmic $\Delta$ [[1]](#1). Karloff and Shmoys give an $\mathsf{RNC}$ algorithm on the COMMON CRCW-PRAM that uses $\Delta + 20 \cdot \Delta^{1/2 + \epsilon}$ colors with running time $(\log |V|)^{O(1)}$ and processors $|V|^{O(1)}$, where the running time is for a fixed $\epsilon > 0$ and the processor bound is independent of $\epsilon$. Also see Problems [LFDVC]({{< relref "./lfdvc.md" >}}) and [ER]({{< relref "./er.md" >}}).

Recently, the distributed version of this problem has been widely studied [[2]](#2). However, the parallel hardness of this problem remains open [[3]](#3).
