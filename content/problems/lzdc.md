---
title: "Lempel-Ziv Data Compression"
acronym: "LZDC"
book_id: "A.12.6"
categories: ["Miscellaneous"]
status: "p-complete"
tags: []
references: [79, 80]
related_problems:
  - id: cvp
    relation: reduces-from-variant-of
  - id: cvp
    relation: see-also
---

## Given

Two binary strings: $s$ and $t$.

## Problem

Is string $t$ added to the dictionary when string $s$ is encoded using the LZ2 coding algorithm?

## Definitions

The *LZ2* algorithm reads string $s$ from left to right. The dictionary is initially empty. When a prefix of the unparsed portion of $s$ is not in the dictionary, the prefix is added to the dictionary. All but the last character of the prefix are compressed by replacing them with a pointer to the dictionary.

## Status

$\P$-complete (De Agostino [[1]](#1)).

## Remarks

The reduction to show hardness is from a variant of [CVP]({{< relref "./cvp.md" >}}) that consists of OR and NOT gates.

De Agostino also shows that two standard variations of the algorithm yield $\P$-complete problems. They are the *next character heuristic* and the *first character heuristic*. Both are proved $\P$-complete by reductions from the same version of [CVP]({{< relref "./cvp.md" >}}) [[1]](#1). De Agostino and Storer show that if given in advance a dictionary containing $n$ strings under the appropriate assumptions, they can compute the optimal compression in $O(\log n)$ time using $n^2$ processors on a CREW-PRAM or alternatively in $O((\log n)^2)$ time using $n$ processors [[2]](#2). They show the techniques can be generalized to the *sliding window* method. For such an approach De Agostino and Storer obtain an $O(\log n)$ time algorithm using $n^3$ processors again on the CREW-PRAM.
