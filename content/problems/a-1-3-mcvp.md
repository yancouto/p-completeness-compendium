---
title: "Monotone Circuit Value Problem"
acronym: "MCVP"
book_id: "A.1.3"
categories: ["Circuit Complexity"]
status: "p-complete"
tags: ["circuits", "boolean", "monotone"]
draft: false
references:
  - author: "Goldschlager, L. M."
    title: "The Monotone and Planar Circuit Value Problems Are Log Space Complete for P"
    year: 1977

related_problems:
  - id: "a-1-1-cvp"
    relation: "reduces-from"
  - id: "a-1-4-am2cvp"
    relation: "variant"
---

## Given

A **monotone Boolean circuit** $C$ — a circuit containing only AND and OR gates (no NOT gates) — with $n$ input gates and a designated output gate $g$. Also given are Boolean input values $x_1, \ldots, x_n \in \{0, 1\}$.

## Problem

Does the output gate $g$ evaluate to 1 (true) when the circuit is given inputs $x_1, \ldots, x_n$?


## Status

P-complete via NC reduction [1].

## Remarks

The restriction to monotone circuits is natural in many contexts and the problem remains P-complete despite the absence of negation gates.

Vitter and Simons give a $\sqrt{n}$ time parallel algorithm for the non-sparse version of the problem [366].

MCVP serves as a common source problem for P-completeness reductions, particularly for problems involving monotone structures. Many graph accessibility and flow problems reduce from MCVP.

