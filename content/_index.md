---
title: "P-Complete Problems Compendium"
---

<div class="home-hero">

# P-Complete Problems Compendium

<p class="lead">
A searchable collection of problems from computational complexity theory that are P-complete — problems for which efficient parallel algorithms are unlikely to exist.
</p>

<div class="home-cta">
  <a href="/problems/" class="btn btn-primary">Browse Problems</a>
  <a href="/about/" class="btn btn-secondary">Learn More</a>
</div>

</div>

## What is P-Completeness?

**P-complete** problems are the hardest problems in P to parallelize. Just as NP-complete problems are believed to have no efficient sequential algorithms, P-complete problems are believed to have no efficient *parallel* algorithms.

More precisely, a problem is P-complete if:
1. It is in P (solvable in polynomial time)
2. Every other problem in P can be reduced to it using highly parallel reductions (typically NC reductions)

If *any* P-complete problem can be solved efficiently in parallel (in NC), then *all* problems in P can be solved efficiently in parallel — that is, **P = NC**.

## About This Compendium

This compendium is based on the comprehensive list of P-complete problems from:

> Greenlaw, R., Hoover, H. J., & Ruzzo, W. L. (1995). *Limits to Parallel Computation: P-Completeness Theory*. Oxford University Press.

The book catalogs over 100 P-complete problems across categories including circuit complexity, graph theory, logic, algebra, and more.

### Contributing

This is an open-source project! You can contribute by:
- Adding new P-complete problems discovered since 1995
- Improving problem descriptions and remarks
- Fixing errors or adding references

See our [Contributing Guide](/about/#contributing) for details.

## Featured Problems

- **[Circuit Value Problem (CVP)](/problems/a-1-1-cvp/)** — The foundational P-complete problem, analogous to SAT for NP-completeness
- **[Monotone CVP](/problems/a-1-3-mcvp/)** — A restricted variant using only AND and OR gates
- **[Alternating Graph Accessibility](/problems/a-2-3-agap/)** — Determining reachability in and/or graphs
