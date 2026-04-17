---
title: "Uniform Word Problem for Lattices"
acronym: "UWPL"
book_id: "A.8.22"
categories: ["Algebra"]
status: "p-complete"
tags: []
references: [71, 181]
related_problems:
  - id: unit
    relation: see-also
  - id: horn
    relation: see-also
---

## Input

A set of equations $E$ and $e_1 = e_2$ an equation.

## Problem

Does $E \models e_1 = e_2$?

## Definitions

A *lattice* is a set $L$ with two binary operations $\\{+, \cdot\\}$ that satisfy the lattice axioms. Let $x, y, z \in L$. The *lattice axioms* are as follows:

1. Associativity: $(x \cdot y) \cdot z = x \cdot (y \cdot z)$ and $(x + y) + z = x + (y + z)$
2. Commutativity: $x \cdot y = y \cdot x$ and $x + y = y + x$
3. Idempotence: $x \cdot x = x$ and $x + x = x$
4. Absorption: $x + (x \cdot y) = x$ and $x \cdot (x + y) = x$

Let $\mathcal{U}$ be a countably infinite set of symbols. The set of terms over $\mathcal{U}$, $W(\mathcal{U})$, is defined inductively as follows:

1. If $\alpha$ is in $\mathcal{U}$, then $\alpha$ is in $W(\mathcal{U})$.
2. If $p$ and $q$ are in $W(\mathcal{U})$, then $(p + q)$ and $(p \cdot q)$ are in $W(\mathcal{U})$.

Let $e_1$ and $e_2$ be terms over $\mathcal{U}$. An *equation* is a formula of the form $e_1 = e_2$. A *valuation* for a given lattice $L$ is a mapping $\mu : U \to L$. The valuation is extended to $W(\mathcal{U})$ by defining $\mu(p + q) = \mu(p) + \mu(q)$ and $\mu(p \cdot q) = \mu(p) \cdot \mu(q)$.

A lattice satisfies an equation $e_1 = e_2$ under a valuation $\mu$, denoted $L \models_\mu e_1 = e_2$, if and only if $\mu(e_1) = \mu(e_2)$. A lattice $L$ satisfies a set of equations $E$, denoted $L \models_\mu E$, if and only if $L$ satisfies every member of $E$ under $\mu$. $E$ *implies* $e_1 = e_2$, denoted $E \models e_1 = e_2$, if and only if for every lattice $L$ and valuation $\mu$ such that $L \models_\mu E$, it follows that $L \models_\mu e_1 = e_2$.

## Status

$\P$-complete (Cosmadakis [[1]](#1)).

## Remarks

A polynomial time algorithm for the problem is given in [[1]](#1). The reduction to show hardness is from the *Implication Problem for Propositional Horn Clauses* (Jones and Laaser [[2]](#2)). See Problems [UNIT]({{< relref "./unit.md" >}}) and [HORN]({{< relref "./horn.md" >}}).

The problem remains $\P$-complete if we use inequalities instead of equations. Furthermore, the problem remains $\P$-complete when $E = \varnothing$ and the terms are represented by directed acyclic graphs instead of trees. However, if $E = \varnothing$ and the terms are represented as trees, the problem is in $\mathsf{DLOG}$ [[1]](#1). This problem is called the *Identity Problem for Lattices*.
