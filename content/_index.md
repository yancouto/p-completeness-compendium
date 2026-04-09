---
title: "P-Complete Problems Compendium"
---

<div class="home-hero">

# P-Complete Problems Compendium

<p class="lead">
A collaborative resource for parallel complexity theory.
</p>

<div class="home-cta">
  <a href="{{< relref "/problems/_index.md" >}}" class="btn btn-primary">Browse Problems</a>
  <a href="{{< relref "/about.md" >}}" class="btn btn-secondary">Learn More</a>
</div>

</div>

## What is P-Completeness?

**P-complete** problems are the hardest problems in P to parallelize. Just as NP-complete problems are believed to have no efficient sequential algorithms, P-complete problems are believed to have no efficient *parallel* algorithms, and are said to be inherently sequential.

More precisely, a problem is P-complete if:
1. It is in P (solvable in polynomial time)
2. Every other problem in P can be reduced to it using an NC reduction. NC is the class of problems/algorithms which use polylogarithmic time and polynomially many processors.

If *any* P-complete problem can be solved efficiently in parallel (in NC), then *all* problems in P can be solved efficiently in parallel — that is, **P = NC**.

## About This Compendium

This compendium uses the following as a main reference:

> Greenlaw, R., Hoover, H. J., & Ruzzo, W. L. (1995). *Limits to Parallel Computation: P-Completeness Theory*. Oxford University Press.

These references cover foundational results and broad problem catalogs across circuit complexity, graph theory, logic, algebra, and more.

### Contributing

This is an open-source project! You can contribute by:
- Adding new P-complete problems
- Improving problem descriptions and remarks
- Fixing errors or adding references

See our [Contributing Guide]({{< relref "/about.md" >}}#contributing) for details.

## Featured Problems

- **[Circuit Value Problem (CVP)]({{< relref "/problems/a-1-1.md" >}})** — The foundational P-complete problem, analogous to SAT for NP-completeness
- **[Monotone CVP]({{< relref "/problems/a-1-3.md" >}})** — A restricted variant using only AND and OR gates
