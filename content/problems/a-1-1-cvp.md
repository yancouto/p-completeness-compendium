---
title: "Circuit Value Problem"
acronym: "CVP"
problem_id: "A.1.1"
category: "Circuit Complexity"
status: "p-complete"
tags: ["circuits", "boolean", "fundamental"]
draft: false
references:
  - author: "Ladner, R. E."
    title: "The Circuit Value Problem is Log Space Complete for P"
    year: 1975
    citation: "[225]"
related_problems:
  - id: "a-1-2-topcvp"
    relation: "variant"
  - id: "a-1-3-mcvp"
    relation: "variant"
  - id: "a-1-7-pcvp"
    relation: "variant"
---

## Given

An encoding $\alpha$ of a Boolean circuit $\alpha$, inputs $x_1, \ldots, x_n$, and designated output $y$.

## Problem

Is output $y$ of $\alpha$ true on input $x_1, \ldots, x_n$?

## Remarks

The Circuit Value Problem plays the same role in P-completeness theory that the **Satisfiability Problem** does in NP-completeness theory. It is the canonical P-complete problem from which most other P-completeness proofs derive.

For the two-input basis of Boolean functions, it is known that CVP is P-complete except when the basis consists solely of:
- **or** gates only
- **and** gates only
- Any combination of **xor**, **equivalence**, and **not** gates

These restricted cases can be solved in NC (Goldschlager and Parberry [127], Parberry [281]).

The problem remains P-complete even when the circuit is topologically ordered (TopCVP, Problem A.1.2).
