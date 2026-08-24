# Phase 005 Group 04 — Capability Authorization & Restricted Analytical Visibility

**Status:** Planned — not yet started

## Goal

Refine permission truth independently from governance authority, evidence sufficiency, and action success while preserving useful restricted-data analysis.

## Primary review questions

- canonical capability vocabulary for raw data, metadata/governance, metrics/Assessments, Lineage/RCA, job operations, safeguards, gates/override, causal confirmation, Annotation, and Explanation;
- `allow`, `deny`, `conditional`, `unknown`, and `conflicting` semantics;
- purpose/environment/tenant/subject/consumer/time conditions;
- user/group/role/service-principal combination without hidden precedence;
- historical authorization versus current disclosure;
- Authorized Analytical Projection, opacity, and inference-leakage constraints.

## Boundaries

Do not select RBAC/ABAC/IAM technology or treat metadata/derived metrics as automatically unrestricted. Capability Authorization does not prove an action succeeded.

## Exit direction

Group 04 exits when the framework can represent least-privilege analytical and operational capabilities without conflating authorization with governance responsibility or evidence truth.