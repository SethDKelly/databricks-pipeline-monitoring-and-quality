# Phase 007 Group 01 — Lineage Relationship Taxonomy, Historical Topology & Operational Relevance

**Status:** Next — not started

## Goal

Define the operational Lineage relationship vocabulary and evidence needed to reason about historical topology without turning topology into metric propagation, exposure or causality.

## Primary questions

- Which relationship classes must be distinguished: logical data dependency, runtime/input-output dependency, transformation relation, field/key/population derivation, publication/consumer relation, control dependency, repository/deployment association, or other operational relation?
- What makes a relationship applicable to a particular field, population, version, consumer and effective interval?
- How should active, inactive, planned, historical, unknown, conflicting and partially observed topology be represented?
- What evidence is sufficient to assert an edge exists or did not exist for a bounded interval?
- How should multiple Lineage sources disagree without introducing a universal confidence score or hidden precedence?
- How should relationship relevance differ from mere asset-level reachability?

## Required boundaries

Preserve:

- Lineage ≠ cause;
- relationship existence ≠ relationship relevance to every field/population/version;
- planned topology ≠ active topology;
- current topology ≠ historical topology;
- missing edge evidence ≠ proof no edge existed;
- asset-level reachability ≠ actual consumer/version encounter;
- Lineage relation ≠ automatic metric/status/governance/authorization propagation;
- source availability/majority ≠ authoritative topology truth absent accepted authority rules.

## Expected output

When started, Group 01 should define the first `OPS-###` contracts, a representative topology scenario suite, durable decisions, and a handoff to Group 02.

## Deferred

Do not choose graph storage, Unity Catalog Lineage APIs, Spark plan extraction, GitHub dependency parsing, event stores, or graph algorithms in this group.
