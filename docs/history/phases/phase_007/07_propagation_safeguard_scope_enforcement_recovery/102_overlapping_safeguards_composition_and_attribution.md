# OPS-102 — Overlapping Safeguards, Composition & Attribution

**Status:** Accepted — Phase 007 Group 07

## Purpose

Handle cases where more than one safeguard can protect the same state, consumer or path without inventing a single-control winner.

## Contract

For overlapping safeguards preserve:

- each safeguard identity/scope/interval;
- which paths/opportunities each actually constrained;
- ordered or concurrent enforcement where evidenced;
- whether one control alone was sufficient, several were jointly necessary, or materiality is unresolved;
- independent release/expiry history.

A consumer's non-exposure can coexist with multiple enforced controls. Attribution that one specific safeguard prevented exposure requires the REF-028/OPS-093 materiality basis for that control.

## Invariants

- multiple active safeguards ≠ independent corroboration of prevention.
- first activated ≠ primary protector.
- one safeguard release does not imply all protection ended.
- control contribution/causality remains proposition-specific.
