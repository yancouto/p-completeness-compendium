---
title: "Circuit Value Problem"
acronym: "CVP"
book_id: "A.1.1"
categories: ["Circuit Complexity"]
status: "p-complete"
tags: ["circuits", "boolean", "fundamental"]
draft: false
references:
  - author: "Ladner, R. E."
    title: "The Circuit Value Problem is Log Space Complete for P"
    year: 1975
    doi: "10.1145/990518.990519"

related_problems:
  - id: "a-1-2-topcvp"
    relation: "variant"
  - id: "a-1-3-mcvp"
    relation: "variant"
  - id: "a-1-7-pcvp"
    relation: "variant"
---

## Given

A **Boolean circuit** $C$ with $n$ input gates, some number of internal gates (each computing AND, OR, or NOT of its inputs), and a designated output gate $g$. The circuit is given as a list of gates in topological order, where each gate specifies its type and input gates. Also given are Boolean input values $x_1, \ldots, x_n \in \{0, 1\}$.

## Problem

Does the output gate $g$ evaluate to 1 (true) when the circuit is given inputs $x_1, \ldots, x_n$?


## Status

P-complete via NC reduction [1].

## Remarks

The Circuit Value Problem plays the same role in P-completeness theory that the **Satisfiability Problem** does in NP-completeness theory. It is the canonical P-complete problem from which most other P-completeness proofs derive.

For the two-input basis of Boolean functions, it is known that CVP is P-complete except when the basis consists solely of:
- **or** gates only
- **and** gates only
- Any combination of **xor**, **equivalence**, and **not** gates

These restricted cases can be solved in NC (Goldschlager and Parberry [127], Parberry [281]).

The problem remains P-complete even when the circuit is topologically ordered (TopCVP, Problem A.1.2).

