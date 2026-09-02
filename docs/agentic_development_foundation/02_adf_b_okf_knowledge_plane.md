# ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile

**Status:** PLANNED / READY TO EXECUTE

## Objective

Introduce a portable, tool-neutral knowledge-discovery plane over canonical DMTZ documentation using Open Knowledge Format (OKF) v0.2 without converting OKF into a new source of product truth.

## Standards decision

Use the upstream GoogleCloudPlatform `knowledge-catalog/okf/SPEC.md` **v0.2** specification as the external format authority. The independent `okf.md` site may be used as explanatory material but must not override the upstream version/specification.

OKF is appropriate because it is intentionally Markdown/YAML, git-friendly, consumer-neutral and supports progressive disclosure through `index.md` files. Version 0.2 also adds provenance, verification and lifecycle metadata useful for maintaining an agent-facing knowledge map.

## Core DMTZ rule

**OKF knowledge describes and routes to DMTZ authority; it does not become DMTZ authority.**

A knowledge document may summarize where a contract lives, what implementation area it supports and how current the routing entry is. Exact semantics remain in the referenced canonical document/code/test.

## Proposed bundle

```text
knowledge/
├── index.md
├── log.md
├── project/
│   ├── index.md
│   ├── authority.md
│   ├── architecture.md
│   └── implementation-program.md
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

The initial bundle should remain small. Do not create one OKF document for every SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contract.

## DMTZ OKF profile

OKF v0.2 requires only `type`, but DMTZ should define a stricter producer profile for repository-maintained entries.

Recommended required fields for DMTZ concept documents:

```yaml
---
type: <DMTZ knowledge type>
title: <human-readable title>
description: <one-sentence routing summary>
resource: <canonical repository-relative resource or stable URI>
tags: [dmtz, ...]
status: draft|stable|deprecated
---
```

Use optional OKF v0.2 families where they provide real value:

- `sources` when an entry synthesizes more than one canonical source;
- `generated` when a tool/process created or materially regenerated the knowledge entry;
- `verified` when a human or process has explicitly checked the entry against its source;
- `stale_after` only for genuinely time-sensitive routing/compatibility knowledge.

Do not add metadata merely because the format permits it.

## DMTZ knowledge types

Initial producer-defined types:

- `Project Authority`;
- `Architecture Reference`;
- `Implementation Package`;
- `Domain Routing Reference`;
- `Development Workflow`;
- `Tool Compatibility Reference`.

Future types may be added without changing the canonical DMTZ concept catalog; OKF `type` is a knowledge-routing classification, not a DMTZ product Concept.

## Trust-semantics firewall

OKF trust/lifecycle signals must remain semantically separate from DMTZ domain authority:

- OKF `verified` ≠ Assertion Authority;
- OKF trust tier ≠ evidence sufficiency;
- OKF human-reviewed ≠ causal confirmation authority;
- OKF lifecycle `stable` ≠ DMTZ health/quality status;
- OKF `stale_after` describes a knowledge entry, not monitored-data freshness;
- OKF provenance describes the routing artifact's origin, not necessarily the proposition-level evidence represented by DMTZ.

This firewall must be documented and tested in any generated tooling.

## Progressive disclosure

Agents should normally traverse:

```text
knowledge/index.md
  → domain or implementation index
  → one routing concept
  → canonical document(s)
  → exact stable contract IDs when needed
```

The bundle should reduce context, not encourage preloading.

## Generation strategy

Prefer deterministic generation for indexes and mechanical metadata where possible. Human-authored descriptions should remain concise and reviewed.

Generated OKF content must never overwrite canonical documentation. A generation error should fail validation of the knowledge layer, not mutate product truth.

## Deliverables

- `knowledge/` v0.2 bundle root with `okf_version: "0.2"` declaration;
- initial project/domain/implementation/workflow routing entries;
- DMTZ OKF profile documentation;
- deterministic OKF validation/index-link checks;
- source/verification/lifecycle maintenance policy.

## Acceptance scenarios

ADF-B passes when:

- a new developer/agent can reach the active implementation package and relevant Phase 010 architecture through progressive disclosure;
- an exact stable contract can still be retrieved from canonical docs without an OKF summary becoming authoritative;
- unknown OKF types are tolerated;
- deprecated/stale routing entries are surfaced rather than silently used as current;
- a broken OKF entry cannot corrupt or supersede canonical DMTZ documentation;
- OKF trust metadata is never interpreted as DMTZ authority/evidence status.

## Deferred OKF capabilities

Do not introduce OKF Attested Computation runtime protocols or an OKF MCP server in this foundation. These may be reconsidered later if a concrete workflow requires them.
