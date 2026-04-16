---
title: "Stable Marriage Minimum Regret"
acronym: "SMMR"
book_id: "B.8.6"
categories: ["Matching"]
status: "open"
tags: ["CC"]
references: [255, 346]
---

## Given

A set of $n$ men and a set of $n$ women, for each person a ranking of the opposite sex according to their preference for a marriage partner, and an integer $k$, $1 \leq k \leq n$.

## Problem

Is there a stable marriage in which every person has regret at most $k$?

## Definitions

The *regret* of a person in a stable marriage is the position of her mate on her preference list.

## Status

Open (Mayr and Subramanian [[1]](#1), Subramanian [[2]](#2)).

## Remarks

This problem is in $\CC$, that is, it is equivalent to [CCVP]({{< relref "./ccvp.md" >}}).
The goal in this problem is to minimize the maximum regret of any person.
