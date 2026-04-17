---
title: "Stable Marriage"
acronym: "SM"
book_id: "B.8.3"
categories: ["Matching"]
status: "open"
tags: ["CC"]
references: [255, 291, 116]
related_problems:
  - id: ccvp
    relation: equivalent
  - id: smfp
    relation: see-also
  - id: smsp
    relation: see-also
  - id: smmr
    relation: see-also
---

## Input

A set of $n$ men and a set of $n$ women. For each person a ranking of the opposite sex according to their preference for a marriage partner. Note that a preference list does not need to include a ranking for every member of the opposite sex. This problem is sometimes called the *Stable Roommates Problem*.

## Problem

Does the given instance of the problem have a set of marriages that is stable? The set is stable (or a set of stable marriages) if there is no unmatched pair $\\{m, w\\}$ such that both $m$ and $w$ prefer each other to their current partners.

## Status

Open (Mayr and Subramanian [[1]](#1), Pólya, Tarjan, and Woods [[2]](#2)).

## Remarks

This problem is in $\CC$, that is, it is equivalent to [CCVP]({{< relref "./ccvp.md" >}}).

See, for example, Gibbons [[3]](#3) or [[2]](#2) for background on SM. If the preference lists are complete, the problem always has a solution [[2]](#2). Several variations of SM are also known to be in $\CC$. For example, the *male-optimal* Stable Marriage Problem in which there is a designated couple $\\{m, w\\}$ and the question asked is whether man $m$ is married to woman $w$ in the male-optimal stable marriage? [[1]](#1). The male-optimal stable marriage is the one formed by the algorithm given in [[2]](#2). It finds a matching in which no man could do any better in a stable marriage. Several other versions of SM are discussed in [SMFP]({{< relref "./smfp.md" >}}), [SMSP]({{< relref "./smsp.md" >}}) and [SMMR]({{< relref "./smmr.md" >}}).
