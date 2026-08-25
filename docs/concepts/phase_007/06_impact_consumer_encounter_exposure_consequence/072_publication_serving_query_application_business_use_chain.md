# OPS-072 — Publication, Serving, Query, Application & Business-Use Chain

**Status:** Accepted — Phase 007 Group 06

## Purpose

Prevent an affected state being available or served at one boundary from being treated as actual use at every downstream boundary.

## Contract

A material use chain may contain independently evidenced stages such as:

**producer output → publication/serving state → query/read → application/report result → human/process use → decision/action**.

Impact may link these stages where relevant, but each stage keeps its own identity/time/provenance. An exposure proposition must state which boundary is being claimed.

A business-process exposure claim generally requires evidence beyond publication or report refresh when actual human/process use is material to the proposition.

## Invariants

- served ≠ queried/read.
- queried/read ≠ application result actually used.
- report rendered ≠ decision relied on report.
- earlier-stage exposure can be true while later-stage exposure is unknown or false.
- business consequence does not arise merely from state availability.
