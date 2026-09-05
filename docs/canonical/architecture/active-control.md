# Execution Gate, Propagation Safeguard & Active-Control Architecture

**Canonical key:** `architecture.active_control`

**Kind:** TECHNICAL ARCHITECTURE CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration records:** `stable_family.ARCH`, `architecture.active_control`

**Stable IDs:** ARCH-351–ARCH-420

**Stable ID index:** `ARCH-351`, `ARCH-352`, `ARCH-353`, `ARCH-354`, `ARCH-355`, `ARCH-356`, `ARCH-357`, `ARCH-358`, `ARCH-359`, `ARCH-360`, `ARCH-361`, `ARCH-362`, `ARCH-363`, `ARCH-364`, `ARCH-365`, `ARCH-366`, `ARCH-367`, `ARCH-368`, `ARCH-369`, `ARCH-370`, `ARCH-371`, `ARCH-372`, `ARCH-373`, `ARCH-374`, `ARCH-375`, `ARCH-376`, `ARCH-377`, `ARCH-378`, `ARCH-379`, `ARCH-380`, `ARCH-381`, `ARCH-382`, `ARCH-383`, `ARCH-384`, `ARCH-385`, `ARCH-386`, `ARCH-387`, `ARCH-388`, `ARCH-389`, `ARCH-390`, `ARCH-391`, `ARCH-392`, `ARCH-393`, `ARCH-394`, `ARCH-395`, `ARCH-396`, `ARCH-397`, `ARCH-398`, `ARCH-399`, `ARCH-400`, `ARCH-401`, `ARCH-402`, `ARCH-403`, `ARCH-404`, `ARCH-405`, `ARCH-406`, `ARCH-407`, `ARCH-408`, `ARCH-409`, `ARCH-410`, `ARCH-411`, `ARCH-412`, `ARCH-413`, `ARCH-414`, `ARCH-415`, `ARCH-416`, `ARCH-417`, `ARCH-418`, `ARCH-419`, `ARCH-420`

**Owns current question after cutover:** How are Execution Gate and Propagation Safeguard realized as independently evidenced opt-in controls without collapsing readiness, decision, enforcement, execution, exposure, prevention or recovery?

## Canonical contract

Execution Gate:

**exact execution opportunity → criterion identity/revision → evidence suitability → readiness → normal/override/fallback decision → issuance → delivery/acceptance → enforcement → independently observed execution/non-execution**.

Propagation Safeguard:

**exact affected/protected state + surface/path/cohort → proposal → authorization → enforcement request/attempt → effective enforcement → encounter opportunity + alternate-path coverage → REF-028 prevention evaluation → extension/expiry/release → independent recovery evaluation**.

Neither chain automatically establishes the next stage.

## Active-control boundary

Passive monitoring, Investigation, reasoning and Explanation remain fully meaningful when active control is disabled. Gate/Safeguard support is opt-in and deployment-capability dependent.

Criteria reference exact proposition/Assessment identities, not free-form prose, rendered answers or model recommendations. Evidence suitability precedes readiness; readiness precedes decision. Normal Gate decisions are HOLD or ADMIT. Override and fallback are explicit alternative paths with separate authorization/basis and never rewrite underlying readiness.

Decision issuance, delivery/acceptance and enforcement are separately persisted. Actual execution/non-execution comes from runtime evidence. HOLD is not a failed run; ADMIT is not a run; no run is not proof that HOLD enforcement worked without adequate opportunity coverage.

## Enforcement realizations

A verified GitHub environment protection point can provide bounded pre-run enforcement for the exact protected job. It becomes evidence about downstream Databricks execution only through durable cross-system correlation.

Databricks realizations may include an externally triggered pre-start broker with idempotent correlation or an in-job conditional Gate for an exact task branch. Alternate trigger/bypass paths must be governed before claiming broad enforcement. Asynchronous cancellation is interruption/containment, not retroactive pre-start HOLD.

## Degradation, freshness and concurrency

Each Gate profile explicitly defines degraded behavior when evidence, source integration, authorization, reasoning or enforcement is unavailable. There is no hidden universal fail-open or fail-closed default.

Decisions bind opportunity identity, profile/criterion revision, knowledge cut and applicability horizon. Stale or mismatched decisions are rejected/re-evaluated. Concurrent opportunities use distinct identities/revisions; a later result cannot overwrite what governed an earlier opportunity.

Override requires exact Capability Authorization and preserves the normal readiness result. Fallback is policy-as-data: eligibility, trigger, authorized decision and effective enforcement are separate. Multiple Gates compose only through explicit versioned policy; no first/last/deny/allow/service-order precedence is inferred.

## Propagation Safeguard

A Safeguard binds exact protected/affected state, delivery surface/path/cohort and interval. `protected`, `suspect`, `stale safe` and `defective` remain distinct. Proposal, authorization, request, attempt and effective enforcement are separate. Partial path/cohort enforcement remains partial.

Safeguards may withhold, quarantine/deny a bounded path, retain a prior safe state, redirect to a governed alternative or use another deployment-verified mechanism. No universal product-specific mechanism is required.

REF-028 prevention requires an actual encounter opportunity, effective applicable enforcement, alternate-path inventory/coverage and evidence the affected state was not encountered because of the Safeguard. `not exposed` is not synonymous with `prevented`.

Release request, configured expiry and effective release remain separate. Release does not establish fresh/healthy/recovered. Recovery is independently evaluated from output/currentness/health/use evidence.

## Historical and causal boundary

Historical actual control state requires retained authentic decision/enforcement records. Reconstructed historical policy evaluation is not the action that actually occurred. Current policy, health or authorization cannot rewrite historical behavior.

Narrow prevention attribution uses REF-028. Broader claims that a Gate/Safeguard caused an operational or business outcome remain Causal Claim work under REF-017 + AUTH-034.

## Architecture boundary

This segment does not mandate a control microservice, workflow engine, queue/bus, external policy engine, secrets product, API gateway, observability vendor, deployment topology or universal Safeguard mechanism.

## Provenance

- `docs/concepts/phase_010/07_execution_gate_propagation_safeguard_active_control_architecture/README.md`
- atomic ARCH-351–ARCH-420 files under that Phase 010 group
- Phase 010 decisions D-1545–D-1602 and ACS07-01–ACS07-120 review evidence
