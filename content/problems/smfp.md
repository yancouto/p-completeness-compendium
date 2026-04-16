---
title: "Stable Marriage Fixed Pair"
acronym: "SMFP"
book_id: "B.8.4"
categories: ["Matching"]
status: "open"
tags: ["CC"]
references: [255, 346]
related_problems:
  - id: ccvp
    relation: equivalent
---

## Given

A set of $n$ men and a set of $n$ women, for each person a ranking of the opposite sex according to their preference for a marriage partner, and a designated couple Alice and Bob.

## Problem

Are Alice and Bob a fixed pair for the given instance of the problem?

## Definitions

Alice and Bob are a *fixed pair* if they are married to each other in *every* stable marriage.

## Status

Open (Mayr and Subramanian [[1]](#1), Subramanian [[2]](#2)).

## Remarks

This problem is in $\CC$, that is, it is equivalent to [CCVP]({{< relref "./ccvp.md" >}}).