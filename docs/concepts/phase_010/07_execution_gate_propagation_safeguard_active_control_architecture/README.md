# Phase 010 Group 07 — Execution Gate, Propagation Safeguard & Active-Control Architecture

**Status:** COMPLETE / ACCEPTED

## Accepted result

- **ARCH-351–ARCH-420 accepted.**
- Cumulative Phase 010 architecture range: **ARCH-001–ARCH-420**.
- **ACS07-01–ACS07-120 pass.**
- **D-1545–D-1602 accepted.**
- No new product concept is required.

## Goal

Realize Execution Gate and Propagation Safeguard as independent active-control architectures without weakening the accepted separation between readiness, decision, delivery, enforcement, execution, exposure, prevention, release, recovery and causality.

## Selected logical chains

Execution Gate:

**exact execution opportunity → criterion identity/revision → evidence suitability → readiness → normal/override/fallback decision → issuance → delivery/acceptance → enforcement → independently observed execution/non-execution**.

Propagation Safeguard:

**exact affected/protected state + surface/path/cohort → proposal → authorization → enforcement request/attempt → effective enforcement → encounter opportunity + alternate-path coverage → REF-028 prevention evaluation → extension/expiry/release → independent recovery evaluation**.

Neither chain automatically establishes the next stage.

## Active-control boundary

Passive monitoring, Investigation, reasoning and Explanation remain useful when no active-control capability is enabled. Gate/Safeguard support is explicit opt-in and deployment-capability dependent.

A control mechanism may be unavailable in one enterprise environment even if vendor documentation describes it. Group 01 capability-instance verification therefore applies before a control adapter can be selected.

## Execution Gate architecture

A Gate is bound to one control opportunity and one immutable Gate/profile revision. Criteria reference exact proposition/Assessment identities rather than free-form prose or model recommendations. The Gate evaluation records evidence suitability before readiness, and readiness before the decision.

Normal decisions are HOLD or ADMIT. Override and fallback are explicit alternative paths with their own authorization and basis; neither rewrites the underlying readiness state.

Decision issuance, transport, acceptance and enforcement are separately persisted. Actual execution/non-execution is then joined from Group 05 runtime evidence.

A HOLD is therefore not a failed run; an ADMIT is not a run; and absence of a run is not proof that HOLD enforcement worked unless execution-opportunity coverage is adequate.

## GitHub pre-start realization

A GitHub Actions environment can provide a strong pre-run enforcement point for the exact job that references the environment when the deployment/plan supports the required protection rules. GitHub documents that environment protection rules must pass before such a job is sent to a runner, and environment secrets are not available until the protected job proceeds.

Where target capability is verified, DMTZ may integrate through a custom GitHub App deployment protection rule or through governed reviewer/manual protection. Custom protection availability remains plan/deployment/preview dependent.

This evidence is scoped to the GitHub job/deployment opportunity. It becomes evidence about a downstream Databricks execution only when Group 05 provides durable cross-system correlation.

## Databricks Gate realizations

Two bounded patterns are accepted:

1. **Externally triggered pre-start broker.** A DMTZ-authorized broker evaluates the Gate before invoking Databricks `run-now`/submit. Stable idempotency and correlation tokens bind the decision to the resulting run. The architecture must govern alternate triggers/bypass paths; otherwise global pre-start enforcement cannot be claimed.
2. **In-job conditional Gate.** A Databricks `If/else` or `Run if` path may realize a Gate for a specific downstream task branch when exact criterion/opportunity mapping and actual conditional/execution evidence are retained.

Databricks cancel APIs are asynchronous interruption. They do not constitute pre-start HOLD for a run that already began. They may support containment/Safeguard behavior when their effect is separately evidenced.

## Control degradation

Every Gate profile explicitly defines behavior when required evidence, source integration, authorization, reasoning, or enforcement services are degraded. Allowed policy outcomes can include HOLD, manual review/escalation, bounded fallback, explicit unavailable state or other governed behavior.

There is no hidden universal fail-open or fail-closed default. A model/vector/search outage cannot silently change the control policy; deterministic accepted proposition/rule evaluation remains the authoritative decision path.

## Decision freshness and concurrency

Gate decisions carry opportunity identity, profile/criterion revisions, knowledge cut and applicability horizon. Stale or mismatched decisions are rejected or re-evaluated before enforcement.

Decision delivery uses idempotency where supported. Concurrent opportunities and changing readiness use explicit opportunity IDs/revisions so a later result cannot overwrite the decision that actually governed an earlier opportunity.

## Override and fallback

Override requires exact Capability Authorization and records requester, reason, scope, expiry and decision. Override admission explicitly preserves the fact that normal readiness may have been HOLD/not ready.

Fallback is policy-as-data: configured eligibility, evidenced trigger, authorized fallback decision and effective enforcement are all independent. Timeout and escalation do not imply fallback unless an exact policy states that relationship.

## Multiple Gates

Multiple Gates retain independent criteria, decisions and enforcement points. Composition/precedence is an explicit versioned policy for the exact opportunity. No first-wins, last-wins, deny-wins, allow-wins or service-order precedence is inferred.

## Propagation Safeguard architecture

A Safeguard protects exact state/version(s) and exact delivery surface/path/cohort/interval. `protected`, `suspect`, `stale safe` and `defective` remain distinct.

Proposal, authorization, request, attempt and effective enforcement are separately recorded. Partial path/cohort enforcement is represented as partial rather than a universal safeguard-success flag.

A Safeguard can withhold delivery, quarantine/deny a bounded path, retain a prior safe state, redirect to an explicitly governed alternative, or invoke another verified enforcement mechanism. The architecture does not require one universal product-specific safeguard mechanism.

## Prevention evidence

REF-028 prevention requires more than active enforcement. DMTZ assembles an exact prevention manifest containing:

- affected/protected state;
- actual consumer exposure opportunity;
- applicable delivery path(s);
- effective Safeguard enforcement for those paths;
- materially applicable alternate-path inventory/coverage;
- evidence that the opportunity did not encounter the affected state because of the Safeguard.

No opportunity means no prevention credit. `not exposed` is not synonymous with `prevented by Safeguard`.

## Release, expiry and recovery

Configured expiry, release request and effective release remain separate. Releasing a Safeguard does not assert that data is fresh, healthy or recovered.

Recovery is evaluated independently using Group 05 output/currentness/health/use evidence. A successful rerun may contribute evidence but cannot by itself establish recovery for all consumers/use contexts.

## Overlapping controls and causal attribution

Overlapping Gates/Safeguards are retained independently. Narrow REF-028 prevention can be attributed where exact opportunity/enforcement/path evidence permits. Broader claims that a control caused an operational or business outcome remain Causal Claim work governed by REF-017 + AUTH-034.

## Historical replay

Actual historical decision/enforcement records bind the knowledge cut and policy revisions that existed then. Group 06 may reconstruct what the evidence/rules would have yielded at a historical cut, but that reconstruction is not the actual control action unless authentic decision/enforcement records survive.

Current policy, current health, current authorization or a preferred counterfactual action cannot rewrite historical control behavior.

## Phase 009 gap treatment

- **GAP-009-21:** no universal native Propagation Safeguard is assumed; a canonical Safeguard state machine and pluggable deployment-verified enforcement adapters are architecturally resolved.
- **GAP-009-22:** REF-028 prevention is realized through opportunity + exact enforcement + alternate-path coverage manifests; wide negative/prevention claims remain evidence intensive.
- **GAP-009-23:** GitHub Gate → Databricks execution correlation consumes Group 05 correlation/attestation; absence of the join remains explicit.
- **GAP-009-24:** criterion, override, fallback, timeout and multi-Gate rules are organization-owned versioned policy-as-data rather than vendor defaults.

## Technology decisions intentionally not made

Group 07 does not select a final control microservice runtime, workflow engine, queue/bus, external policy engine, secrets product, API gateway, observability vendor, deployment topology or universal Safeguard enforcement product. Group 08 owns packaging/operations.

## Group 08 handoff

Group 08 may now design serving/security/deployment/observability/cost topology over **ARCH-001–ARCH-420**. It must preserve separate passive reasoning and active-control paths, deterministic control decision semantics, least-privilege enforcement identities, control auditability, explicit degradation behavior, and cost/latency observability without relaxing evidence or safety boundaries.
