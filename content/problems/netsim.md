---
title: "Network Simulation"
acronym: "NetSim"
book_id: "A.12.8"
categories: ["Miscellaneous"]
status: "p-complete"
tags: []
references: [132]
related_problems:
  - id: mcvp
    relation: reduces-from
  - id: tc
    relation: see-also
---

## Input

A fully connected undirected network with $N$ vertices, a capacity $C(i, j)$ for each link $ij$ (counted in "trunks"), a list of tuples specifying call arrival and holding times, and a designated call $c$.

## Problem

During the simulation of the network (see Greenberg, Lubachevsky, and Wang [[1]](#1) for details) is call $c$ blocked?

## Status

$\P$-complete (Greenberg, Lubachevsky, and Wang [[1]](#1)).

## Remarks

The reduction to show hardness is from [MCVP]({{< relref "./mcvp.md" >}}).
They also prove that *multirate* simulation, in which a call may require more than one trunk on each link on its route, is $\P$-complete even for $N$ equal to two. See [TC]({{< relref "./tc.md" >}}) for a related question.