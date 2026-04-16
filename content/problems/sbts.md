---
title: "Strong Bisimilarity in Transition Systems"
acronym: "SBTS"
book_id: "A.7.10"
categories: ["Formal Languages"]
status: "p-complete"
tags: []
references: [11, 23, 378, 332]
related_problems:
  - id: sam2cvp
    relation: reduces-from
  - id: sbdts
    relation: see-also
---

## Given

An encoding of a finite labeled transition system $N$, and two designated states $p$ and $q$. 

## Problem

Are $p$ and $q$ strongly bisimilar?

## Definitions

A *finite labeled transition system* is a triple $M = \langle Q, \Sigma, T \rangle$, where $Q$ is a finite set of states, $\Sigma$ is a finite alphabet, and $T \subseteq Q \times \Sigma \times Q$ is the set of transitions. A relation $S \subseteq Q \times Q$ is a *strong bisimulation* of $M$ if $(s_1, s_2) \in S$ implies for all $x \in \Sigma$ that
1. whenever $(s_1, x, t_1) \in T$, then for some state $t_2$, $(s_2, x, t_2) \in T$ and $(t_1, t_2) \in S$; and
2. whenever $(s_2, x, t_2) \in T$, then for some state $t_1$, $(s_1, x, t_1) \in T$ and $(t_1, t_2) \in S$.

The *strong bisimulation relation* is defined as the union of all strong bisimulations of $M$. States $p$ and $q$ are *strongly bisimilar* if $(p, q)$ is in the strong bisimulation relation of $N$.

## Status

$\P$-complete (Àlvarez et al [[1]](#1), Balcázar, Gabarró, and Sántha [[2]](#2)).

## Remarks

The reduction to show hardness is from [SAM2CVP]({{< relref "./sam2cvp.md" >}}), and in it the transition system is nondeterministic. It is an open question whether the problem remains $\P$-complete in the deterministic case [[2]](#2), see [SBDTS]({{< relref "./sbdts.md" >}}). *Observation Equivalence* and *Observation Congruence* are two related problems that are both shown $\P$-complete in [[2]](#2). Zhang and Smolka implement parallel algorithms for equivalence checking [[3]](#3).
