# Active-Control Evidence Model

## Canonical journals

Group 07 extends the Group 02 evidence plane with append/supersede journals for:

- `control_profile_revision`;
- `control_opportunity`;
- `gate_criterion_revision`;
- `evidence_suitability_evaluation`;
- `readiness_evaluation`;
- `gate_decision`;
- `control_delivery_attempt`;
- `control_enforcement_observation`;
- `override_request_authorization_decision`;
- `fallback_trigger_decision`;
- `protected_state`;
- `safeguard_decision`;
- `safeguard_enforcement_observation`;
- `alternate_path_manifest`;
- `exposure_opportunity`;
- `prevention_evaluation`;
- `control_release_event`;
- `recovery_evaluation`.

## Required provenance

Material control records preserve tenant, subject/opportunity, control/profile/criterion revision, actor/workload principal, authorization decision, knowledge cut, basis proposition IDs, adapter capability instance, source request/response identity where available, event/effective time, source-availability time and persistence time.

## Non-rewriting history

Decision corrections/supersessions do not rewrite what was actually issued/enforced. A later retrospective assessment can label an earlier decision stale, mistaken or based on incomplete evidence without replacing the historical record.

## Common derivation

Repeated delivery attempts, duplicate audit events and source/API mirrors of the same enforcement occurrence are linked as common-derived rather than treated as independent proof.

## Retention

Control records that support regulated/audit/product promises can pin their exact basis under Group 02 lifecycle rules. Routine low-value transport traces may age more aggressively once decision/enforcement identity and required diagnostic evidence remain durable.

Retention is not universal forever storage.
