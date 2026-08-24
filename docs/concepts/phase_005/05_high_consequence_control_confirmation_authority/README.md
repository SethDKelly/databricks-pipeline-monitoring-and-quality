# Phase 005 Group 05 — High-Consequence Action, Control & Causal-Confirmation Authority

**Status:** Next review group — not yet started

## Goal

Refine who may perform or authorize high-consequence actions while preserving Phase 004 evidence standards for confirmation/control enforcement and Group 04 capability-resolution semantics.

## Accepted handoff from Groups 01–04

- Assertion Authority and AUTH-001–AUTH-032 are accepted;
- Capability Authorization is exact principal/capability/subject/context/time permission truth and remains separate from Assertion Authority, evidence sufficiency, and enforcement;
- `allowed`, `denied`, `conditional`, `unknown`, `conflicting`, and `unavailable` remain distinct; runtime fail-safe behavior must not rewrite unresolved authorization truth;
- user/group/role/service-principal combination requires explicit rules and historical membership evidence;
- no implicit capability inheritance exists through domain/repository/pipeline/Lineage containment;
- permission to perform a governance/operational action does not make the result authoritative or prove the action occurred/succeeded;
- Group 03 high-consequence-use eligibility for a metric/Expectation does not grant control capability;
- raw-data, analytical visibility, job operations, safeguards, gates, override, and causal confirmation are independently resolvable capabilities;
- current authorization does not rewrite historical authorization, and historical permission is not reusable current permission.

## Primary review questions

- causal-confirmation capability/authority by claim class, subject, context, environment, and confirmation profile;
- which claim classes require human confirmation and whether any narrowly scoped automated confirmation can be explicitly authorized;
- job/run operational capabilities such as retry/cancel/update/restart and their separation from data read;
- Execution Gate registration/configuration/enable/retire/hold/admit/override authority;
- Propagation Safeguard proposal/activation/release/cancel/expire authority;
- separation among proposing, approving, executing, and overriding high-consequence actions;
- delegation, multi-party approval, separation of duties, emergency/break-glass, expiry, revocation, and recovery;
- authorization conflict/unavailable behavior for production-critical control paths;
- authority/permission versus actual action, enforcement, and success evidence.

## Boundaries

- Authority/capability cannot weaken REF-013–REF-030 causal/control evidence standards.
- Do not treat Group 03 control-use eligibility as authorization to operate a control.
- Do not select scheduler/orchestrator, quarantine implementation, causal engine, IAM system, or automatic-confirmation mechanism.
- Do not broaden raw-data access merely because operational action permission is required.
- Group 06 retains disclosure/audience governance.

## Exit direction

Group 05 exits when high-consequence permissions and governance are explicit, scoped, historically reconstructable, auditable, and independently resolvable from evidence proving that a control, job operation, override, or confirmation action actually occurred and succeeded.

**Group 05 has not started.**
