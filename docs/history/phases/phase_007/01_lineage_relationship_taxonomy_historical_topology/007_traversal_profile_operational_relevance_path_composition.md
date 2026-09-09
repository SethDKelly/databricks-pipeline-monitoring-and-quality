# OPS-007 — Traversal Profile, Operational Relevance & Path Composition

**Status:** Accepted — Phase 007 Group 01

## Purpose

Make Lineage traversal answer a bounded operational question rather than returning every graph-reachable entity and treating all paths as equally meaningful.

## Traversal profile

A material traversal binds, where applicable:

- starting Entity Identity/scope;
- upstream or downstream direction;
- permitted relationship families/roles;
- questioned event/effective time;
- historical knowledge cutoff when requested;
- field/key/population/consumer/use context;
- version/interface/transformation context;
- bounded traversal depth/path criteria appropriate to the question;
- authorization/disclosure context.

The traversal profile is a query/evaluation structure, not a new truth-owning concept or implementation query language.

## Operational relevance

For a defined traversal question, an effective relationship/path can be:

- `relevant` — its established family/role/scope can materially bear on the bounded question;
- `not relevant` — sufficient semantic scope establishes that it cannot bear on that question;
- `indeterminate` — relationship scope/semantics/evidence is insufficient to decide relevance safely.

Operational relevance is **question-bound**. It is not an intrinsic global edge score, causal probability or business priority.

## Path composition

Multi-hop relevance requires the intermediate relationship scopes to compose meaningfully.

Graph reachability alone is insufficient. For example, A may be asset-level upstream of B and B upstream of C, while the questioned C field/population is known to depend only on a B field/population unrelated to A. A can remain graph-reachable while the exact path is not relevant to that question.

If intermediate granularity is insufficient to prove or exclude relevance, return `indeterminate` rather than widening the path.

## Traversal behavior

- Direct path/shorter path does not imply stronger causal relevance.
- Repository boundaries do not terminate traversal by default.
- Monitoring Scope boundaries do not erase known Lineage.
- The model does not assume Lineage is a DAG. Traversal must be semantically cycle-safe/bounded without declaring every cycle invalid.
- A traversal may return several simultaneously relevant paths.
- Relevance does not establish actual execution/encounter or Impact.

## Invariants

- Reachable ≠ operationally relevant.
- Operationally relevant ≠ exposed/affected.
- Operationally relevant ≠ cause.
- Nearest upstream ≠ root cause.
- Field/population relevance is not inferred from asset reachability when scope is insufficient.
- Path composition never creates metric/status/governance propagation.

## Handoff

OPS-008 qualifies whether the returned traversal has enough coverage to support completeness or missing-path conclusions. Later Phase 007 Investigation/Impact groups consume relevance without promoting it to causality/exposure.