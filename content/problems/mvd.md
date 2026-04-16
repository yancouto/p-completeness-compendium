---
title: "Multivalued Dependency"
acronym: "MVD"
book_id: "A.6.5"
categories: ["Logic"]
status: "p-complete"
tags: []
references: [88]
related_problems:
  - id: horn
    relation: reduces-from
---

## Given

A set $\Sigma$ of multivalued dependencies and a multivalued dependency $\sigma$.

## Problem

Does $\Sigma$ imply $\sigma$?

## Definitions

Let $U$ denote the set of all attributes in the database and let $X$, $Y$, and $Z$ denote sets of attributes. An *embedded multivalued dependency* (EMVD) is an expression of the form $X \to\to Y \mid Z$, where $X$, $Y$, and $Z$ are disjoint sets of attributes in which $Y$ and $Z$ nonempty. A *multivalued dependency* (MVD) is an EMVD in which $Z$ is equal to $U - XY$. A set $\Sigma$ of MVDs implies a MVD $\sigma$ if $\sigma$ holds in every database in which every member of $\Sigma$ holds.

## Status

$\P$-complete (Denenberg [[1]](#1)).

## Remarks

The reduction to show hardness is from [HORN]({{< relref "./horn.md" >}}).