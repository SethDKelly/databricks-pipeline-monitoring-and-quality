# Group 01 — Scope & Identity

**Status:** Review complete — concepts accepted

## Goal

Establish how the ecosystem says **what it is responsible for monitoring** and **how the same logical entity is recognized across systems and time**.

These concepts come first because later observations, expectations, ownership assertions, lineage relationships, and explanations must reference stable logical subjects without assuming that a repository path, Databricks identifier, environment-specific name, or human-readable label is globally stable.

## Accepted concepts

- [Monitoring Scope](monitoring_scope.md)
- [Entity Identity](entity_identity.md)

## Boundary decisions

### 1. Identity is broader than data assets

The seed name `Asset Identity` was too narrow. The same behavior is required for logical pipelines, Databricks jobs/tasks, repositories, data assets, deployment-related entities, consumers, and other subjects that later concepts may need to reference.

The concept is therefore renamed **Entity Identity**.

### 2. Scope describes monitoring responsibility, not ecosystem existence

The seed name `Monitored Scope` is refined to **Monitoring Scope**. An entity can be known to the ecosystem while explicitly excluded from monitoring or while its scope remains unknown.

This distinction is required for evidence-aware RCA: an upstream dependency can be known while monitoring coverage stops at that boundary.

### 3. Scope attaches to entities, not relationships or expectations

Lineage/dependency edges can cross a scope boundary and remain known subject to authorization. Expectations and policies have their own applicability/lifecycle semantics and are not independently "in scope" through this concept.

### 4. Scope never implicitly propagates

Including Table C, a logical pipeline, or a repository does not automatically include every upstream/downstream entity. Onboarding automation may propose or create explicit assertions later, but the accepted concept does not hide propagation inside scope semantics.

### 5. Identity continuity requires evidence

A rename can preserve identity when continuity is justified. Name equality alone is insufficient.

Production and non-production objects remain distinct by default. Delete-and-recreate is not continuity merely because a name is reused.

### 6. Split, merge, replacement, and succession are not identity

Those events connect distinct identities and belong to Change/Lineage behavior. Entity Identity owns sameness/separation, not lifecycle derivation relationships.

### 7. Identity and scope are not authorization

A caller may be authorized to know that an opaque entity or monitoring boundary exists without being authorized to see its identifying metadata, raw values, or policy details.

## Scenario review

### S-01 — Join-volume degradation

Pass. A, B, and C can have independent identities and scope states. C may be monitored while A is known but out of scope; RCA can disclose the evidence-coverage boundary without inventing upstream observations.

### S-02 — Stale upstream with successful downstream execution

Pass. Identity/scope do not conflate job success, freshness, or quality; they only supply referents and monitoring-responsibility context.

### S-03 — Deployment-correlated shift

Pass. Repository, deployment-related, job/task, and data-asset references can resolve through Entity Identity without forcing those entity kinds into one object model.

### S-04 — Cross-repository dependency

Pass. Repository boundaries do not define identity or scope inheritance. Cross-repository logical entities remain independently referenceable.

### S-05 — Conflicting governance metadata

Pass. Identity and scope preserve source/provenance conflicts rather than flattening them. Governance-specific conflict behavior remains with later concepts.

### S-06 — Policy-sensitive explanation

Pass. Opaque identity and authorization-aware scope disclosure allow useful explanations without revealing restricted entity details.

### S-07 — Historical replay

Pass. Reference validity, identity correction history, and effective scope assertions allow incident-time reconstruction without rewriting earlier state.

## Deferred questions

The following are implementation/MVP or later-concept questions and do not block Group 01:

- exact first-MVP list of independently scopeable entity kinds;
- automated identity-association authority thresholds;
- precedence among conflicting synchronized scope authorities;
- whether discovery/onboarding deserves a standalone concept rather than remaining external synchronization behavior.

## Group exit gate

**Satisfied.** Later concepts can safely reference identified entities, distinguish known/out-of-scope/unknown monitoring coverage, preserve cross-system continuity without vendor IDs, and avoid treating scope as authorization.

The next review group is **Group 02 — Semantics, Governance & Policy**.
