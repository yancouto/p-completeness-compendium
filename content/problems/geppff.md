---
title: "Gaussian Elimination with Partial Pivoting over Finite Fields"
acronym: "GEPPFF"
book_id: "B.5.2"
categories: ["Local Optimality"]
status: "open"
tags: []
references: [361]
related_problems:
  - id: gepp
    relation: see-also
---

## Given

An $n \times n$ matrix $A$ with entries over a finite field and an integer $l$.

## Problem

What is the smallest row index in the $l^\text{th}$ column that is nonzero when Gaussian elimination with partial pivoting is performed on $A$?

## Status

Open (Greenlaw, Hoover and Ruzzo [[2]](#2)).

## Remarks

Vavasis shows the analogous problem for unrestricted fields is $\P$-complete [[1]](#1), see [GEPP]({{< relref "./gepp.md" >}}).
