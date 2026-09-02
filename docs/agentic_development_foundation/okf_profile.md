# DMTZ OKF v0.2 Producer Profile

**Status:** ACCEPTED — ADF-B

## Purpose

DMTZ uses Open Knowledge Format v0.2 as a portable knowledge-routing format over canonical repository authority. This profile is intentionally stricter than base OKF for DMTZ-maintained concept documents while remaining consumable by generic OKF readers.

## External format authority

The upstream `GoogleCloudPlatform/knowledge-catalog/okf/SPEC.md` v0.2 specification is the format authority. Base OKF requires only `type` for concept documents and permits producer-defined types. DMTZ adds required routing metadata for maintainability.

## Required DMTZ concept fields

Every non-reserved DMTZ concept document under `knowledge/` must contain YAML frontmatter with:

```yaml
---
type: "<producer-defined knowledge type>"
title: "<human-readable title>"
description: "<concise routing purpose>"
resource: "<canonical repository-relative path or stable URI>"
tags: ["dmtz", "..."]
status: "draft|stable|deprecated"
---
```

`index.md` and `log.md` are reserved routing/history files. The root `knowledge/index.md` declares `okf_version: "0.2"`.

## Initial DMTZ knowledge types

- `Project Authority`
- `Architecture Reference`
- `Implementation Package`
- `Domain Routing Reference`
- `Development Workflow`
- `Tool Compatibility Reference`

These are OKF producer classifications only. They are not additions to DMTZ's accepted product Concept catalog.

Consumers must tolerate unknown valid OKF types.

## Lifecycle meaning

- `draft` — routing concept exists but its referenced workflow/capability or review state is not yet final;
- `stable` — the routing concept is currently maintained and appropriate for normal discovery;
- `deprecated` — the concept remains readable for transition/history but should not be selected as current routing when a replacement exists.

Lifecycle describes the **knowledge artifact**, not DMTZ domain state.

## Optional v0.2 fields

Use `sources`, `generated`, `verified` and `stale_after` only when they add real maintenance value. They are not required merely because v0.2 defines them.

When used:

- `sources` describes provenance of the knowledge artifact;
- `generated` records who/what produced the knowledge artifact and when;
- `verified` records checks of the knowledge artifact against its sources;
- `stale_after` indicates when time-sensitive knowledge routing should be rechecked.

## Trust-semantics firewall

Never interpret OKF metadata as DMTZ proposition semantics:

- OKF `verified` ≠ Assertion Authority;
- OKF review/trust ≠ evidence sufficiency;
- OKF review/trust ≠ causal confirmation authority;
- OKF `stable` ≠ health/quality state;
- OKF `stale_after` ≠ monitored-data freshness;
- OKF provenance ≠ proposition-level DMTZ evidence unless the canonical DMTZ contract explicitly says so.

## Resource rule

`resource` should point to the smallest canonical repository artifact that owns the routed meaning. Bodies may link additional canonical references and stable-ID families.

If an OKF summary conflicts with its resource, the canonical resource wins and the OKF entry must be corrected.

## Content rule

Knowledge concepts should be short routing aids. They may state critical boundary reminders but must not reproduce complete contract semantics, status histories, or implementation plans.

Do not create one OKF concept per SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH ID unless future evidence shows a concrete retrieval need.

## Deferred OKF features

ADF-B does not adopt:

- OKF Attested Computation runtime protocols;
- an OKF MCP server;
- remote knowledge service dependencies;
- OKF as a replacement for code/tests/contracts/ADRs.
