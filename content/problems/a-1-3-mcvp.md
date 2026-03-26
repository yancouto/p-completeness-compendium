---
title: "Monotone Circuit Value Problem"
acronym: "MCVP"
problem_id: "A.1.3"
category: "Circuit Complexity"
status: "p-complete"
tags: ["circuits", "boolean", "monotone"]
draft: false
references:
  - author: "Goldschlager, L. M."
    title: "The Monotone and Planar Circuit Value Problems Are Log Space Complete for P"
    year: 1977
    citation: "[122]"
related_problems:
  - id: "a-1-1-cvp"
    relation: "reduces-from"
  - id: "a-1-4-am2cvp"
    relation: "variant"
---

## Given

An encoding $\alpha$ of a Boolean circuit $\alpha$, inputs $x_1, \ldots, x_n$, and designated output $y$, with the additional assumption that $\alpha$ is **monotone** — that is, it is constructed solely of **and** and **or** gates (no negations).

## Problem

Is output $y$ of $\alpha$ true on input $x_1, \ldots, x_n$?

## Remarks

The restriction to monotone circuits is natural in many contexts and the problem remains P-complete despite the absence of negation gates.

Vitter and Simons give a $\sqrt{n}$ time parallel algorithm for the non-sparse version of the problem [366].

MCVP serves as a common source problem for P-completeness reductions, particularly for problems involving monotone structures. Many graph accessibility and flow problems reduce from MCVP.
