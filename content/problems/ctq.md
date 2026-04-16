---
title: "Corporate Takeover Query"
acronym: "CTQ"
book_id: "A.6.13"
categories: ["Logic"]
status: "p-complete"
tags: []
references: [59]
related_problems:
  - id: path
    relation: reduces-from
---

## Given

A group of $n$ companies $C_1, \ldots, C_n$ and a *partial* relation $\text{owns}(C_i, C_j, S)$, where $1 \leq i, j \leq n$, and two distinct integers $k$ and $l$. The relation $\text{owns}(C_i, C_j, S)$ indicates company $C_i$ owns $S\\%$ of company $C_j$'s stock.

## Problem

Has company $C_k$ bought company $C_l$? A company $B$ has *bought* company $D$ whenever $B$ controls more than $50\\%$ of $D$'s stock. A company $B$ *controls* itself, and also controls stock controlled by any other company $B$ has bought.

## Status

$\P$-complete (Consens and Mendelzon [[1]](#1)).

## Remarks

The reduction to show hardness is from [PATH]({{< relref "./path.md" >}}).
Other query languages are considered in [[1]](#1). For numerous of them, Consens and Mendelzon show any question that can be posed in the language can be resolved in $\NC$.
