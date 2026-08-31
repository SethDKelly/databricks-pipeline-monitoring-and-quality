# Implementation 006 — Serving, Explanation, Basis Inspection & User Experience

**Status:** PLANNED

## Objective

Turn the deterministic evidence/reasoning core into a governed product experience for engineering and business users.

## Entry gate

- 005 Statement/Answer IR and basis resolution stable;
- 002 current requester authorization/disclosure runtime stable;
- pilot audience/use cases defined.

## Group plan

### 006-A — API / Application Boundary

Select and implement a thin/stateless service framework; version request/response contracts independently from physical Delta layouts.

### 006-B — Authentication & Principal Binding

Integrate the target IdP/authentication mechanism and bind authenticated identities to canonical Principal/request context.

Authentication remains separate from authorization.

### 006-C — Query / Investigation / Replay Endpoints

Implement bounded exact endpoints for operational questions, Investigation state, historical replay and relevant subject/Lineage/Impact navigation.

### 006-D — Explanation Rendering

Implement deterministic template rendering from authorized Statement/Answer IR, preserving status/limitations and optional authentic communication retention.

### 006-E — `inspectBasis` / Safe Abstraction

Apply itemwise current disclosure to exact/coarse/redacted/opaque/withheld basis projection. Basis existence/count/type/provenance may itself require withholding.

### 006-F — Initial Business & Engineering UI

Build the initial UI around shared underlying IR with audience-specific authorized detail. Preserve unknown/partial/conflicting/stale states rather than reducing everything to traffic-light health.

### 006-G — Serving Performance / Cache Discipline

Add authorization-context-aware caches/materialized projections only where measured need exists. Cache state retains canonical/source watermarks and never becomes truth.

### 006-H — Consolidation / Exit

Prove business/engineering explanation consistency, cross-user isolation, basis-disclosure boundaries, historical view distinction and service degradation behavior.

## Exit result

A representative analyst and engineer can inspect the same incident and receive appropriately detailed, evidence-consistent, authorization-aware Explanations with exact traceability and historical perspective.
