# ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile

**Status:** COMPLETE / ACCEPTED

## Objective

Introduce a portable, tool-neutral knowledge-discovery plane over canonical DMTZ documentation using Open Knowledge Format (OKF) v0.2 without converting OKF into a new source of product truth.

## Standards decision

Use the upstream GoogleCloudPlatform `knowledge-catalog/okf/SPEC.md` **v0.2** specification as the external format authority. The independent `okf.md` site may be used as explanatory material but must not override the upstream version/specification.

OKF is appropriate because it is intentionally Markdown/YAML, git-friendly, consumer-neutral and supports progressive disclosure through `index.md` files. Version 0.2 also adds provenance, verification and lifecycle metadata useful for maintaining an agent-facing knowledge map.

## Core DMTZ rule

**OKF knowledge describes and routes to DMTZ authority; it does not become DMTZ authority.**

A knowledge document may summarize where a contract lives, what implementation area it supports and how current the routing entry is. Exact semantics remain in the referenced canonical document/code/test.

## Implemented bundle

```text
knowledge/
├── index.md
├── log.md
├── project/
│   ├── index.md
│   ├── authority.md
│   ├── architecture.md
│   ├── implementation-program.md
│   └── agentic-foundation.md
├── domains/
│   ├── index.md
│   ├── evidence-temporal.md
│   ├── identity-governance.md
│   ├── acquisition.md
│   ├── health-lineage-impact.md
│   ├── reasoning-explanation.md
│   ├── serving-security.md
│   └── active-control.md
├── implementation/
│   ├── index.md
│   ├── imp-001.md
│   └── ... imp-011.md
└── workflows/
    ├── index.md
    ├── resolve-context.md
    ├── implement-group.md
    ├── review-change.md
    └── exit-review.md
```

The bundle deliberately remains small enough to scan. DMTZ does not create one OKF document for every SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contract.

## DMTZ OKF profile

The accepted producer profile is documented in [`okf_profile.md`](okf_profile.md).

Every non-reserved DMTZ concept document under `knowledge/` requires:

```yaml
---
type: "<DMTZ knowledge type>"
title: "<human-readable title>"
description: "<one-sentence routing summary>"
resource: "<canonical repository-relative resource or stable URI>"
tags: ["dmtz", "..."]
status: "draft|stable|deprecated"
---
```

The root `knowledge/index.md` declares `okf_version: "0.2"`.

Initial producer-defined knowledge types are:

- `Project Authority`;
- `Architecture Reference`;
- `Implementation Package`;
- `Domain Routing Reference`;
- `Development Workflow`;
- `Tool Compatibility Reference`.

Future types may be added without changing the canonical DMTZ concept catalog; OKF `type` is a knowledge-routing classification, not a DMTZ product Concept. Unknown valid types must be tolerated.

## Trust-semantics firewall

OKF trust/lifecycle signals remain semantically separate from DMTZ domain authority:

- OKF `verified` ≠ Assertion Authority;
- OKF trust/review ≠ evidence sufficiency;
- OKF human review ≠ causal confirmation authority;
- OKF lifecycle `stable` ≠ DMTZ health/quality status;
- OKF `stale_after` describes a knowledge entry, not monitored-data freshness;
- OKF provenance describes the routing artifact's origin, not necessarily proposition-level DMTZ evidence.

This firewall is documented in the profile and represented in ADF-B fixture scenarios.

## Progressive disclosure

The accepted traversal is:

```text
knowledge/index.md
  → one category index
  → one routing concept
  → canonical document(s)
  → exact stable contract IDs when needed
```

The bundle is optimized to reduce context rather than encourage preloading.

## Validation and maintenance

- [`okf_maintenance_policy.md`](okf_maintenance_policy.md) defines ownership, lifecycle, provenance and update rules.
- `scripts/agentic/validate_okf.py` provides a dependency-free structural/profile/resource/local-link validator appropriate before Implementation 001 establishes the Python dependency baseline.
- [`fixtures/adf_b_knowledge_scenarios.yaml`](fixtures/adf_b_knowledge_scenarios.yaml) provides deterministic scenario inputs for later ADF-F automation.

ADF-F owns CI integration, richer parser/test harnesses and context-budget enforcement. ADF-B does not claim those later controls are already implemented.

## Acceptance findings

ADF-B passes because:

- a new developer/agent can route from `knowledge/index.md` to current project, domain and implementation sources through progressive disclosure;
- exact stable contracts remain retrieved from canonical docs rather than OKF summaries;
- the DMTZ validator does not reject a concept solely because its producer-defined `type` is unknown;
- `deprecated` and `stale_after` states are surfaced as knowledge-layer warnings rather than mapped to DMTZ domain state;
- broken repository-relative resources/local links are validation errors;
- generated/maintained knowledge is prohibited from writing product truth back into canonical docs;
- OKF trust metadata is explicitly firewalled from DMTZ authority/evidence/health/causality semantics.

See [`adf_b_execution_review.md`](adf_b_execution_review.md) for the execution closure.

## Deferred OKF capabilities

ADF-B does not introduce OKF Attested Computation runtime protocols or an OKF MCP server. These remain deferred unless a concrete later workflow justifies them.
