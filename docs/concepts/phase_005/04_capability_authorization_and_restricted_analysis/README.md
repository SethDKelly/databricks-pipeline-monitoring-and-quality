# Phase 005 Group 04 — Capability Authorization & Restricted Analytical Visibility

**Status:** Next review group — not yet started

## Goal

Refine permission truth independently from governance authority, evidence sufficiency, and action success while preserving useful restricted-data analysis.

## Accepted handoff from Groups 01–03

- Assertion Authority and AUTH-001–AUTH-023 are accepted;
- authoritative governance standing does not grant Capability Authorization;
- metric meaning, profile selection, threshold/severity, waiver, and high-consequence-use eligibility are independently governable;
- an authoritative or control-eligible metric/Expectation does not grant a principal permission to view its values, edit the rule, configure a gate, or perform an operational action;
- restricted metric/schema/threshold/authority details may themselves be sensitive;
- waiver/exception state does not declassify the underlying metric, rule, or evidence;
- Phase 004 evidence sufficiency and control-enforcement meanings remain unchanged.

## Primary review questions

- canonical capability vocabulary for raw data, metadata/governance, schema, metrics/Assessments, thresholds/Expectations, Lineage/RCA, job operations, safeguards, gates/override, causal confirmation, Annotation, and Explanation;
- `allow`, `deny`, `conditional`, `unknown`, and `conflicting` semantics;
- purpose/environment/tenant/subject/consumer/time conditions;
- user/group/role/service-principal combination without hidden precedence;
- permission to view versus propose/edit/approve/waive/retire normative rules;
- permission to view restricted metric/schema detail versus safe health abstraction;
- current versus historical authorization;
- Authorized Analytical Projection, opacity, and inference-leakage constraints.

## Boundaries

Do not select RBAC/ABAC/IAM technology or treat metadata/derived metrics/schema/thresholds as automatically unrestricted. Capability Authorization does not create Assertion Authority, change normative standing, prove an action succeeded, or prove a control enforced.

Do not begin Group 05 high-consequence control/causal-confirmation authority or Group 06 disclosure governance except where a boundary must be identified.

## Exit direction

Group 04 exits when the framework can represent least-privilege analytical and operational capabilities—including permissions around normative metric/schema state—without conflating authorization with governance authority, evidence truth, or enforcement.

**Group 04 has not started.**