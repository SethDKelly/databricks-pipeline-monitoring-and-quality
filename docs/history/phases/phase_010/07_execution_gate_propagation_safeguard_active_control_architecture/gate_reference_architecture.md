# Execution Gate Reference Architecture

## Objective

Provide opportunity-specific admission control without equating readiness, decision or configuration with actual enforcement/execution.

## Logical components

1. **Opportunity registrar** — creates the exact execution opportunity and correlation identity.
2. **Criterion resolver** — loads immutable Gate/profile and criterion revisions.
3. **Evidence suitability evaluator** — verifies required evidence families, freshness, coverage, knowledge cut and authorization.
4. **Readiness evaluator** — applies deterministic accepted rules to exact propositions/Assessments.
5. **Decision engine** — produces normal HOLD/ADMIT or explicitly governed override/fallback decisions.
6. **Decision journal** — persists basis, authorization and knowledge cut before external enforcement.
7. **Control adapter** — delivers the exact decision to a verified enforcement point.
8. **Enforcement reconciler** — obtains evidence of acceptance/effective enforcement.
9. **Execution reconciler** — joins Group 05 actual start/non-start and later lifecycle evidence.

## Preferred ordering

**opportunity registration → suitability/readiness → authorized decision journal commit → adapter delivery → enforcement evidence → execution correlation**.

A decision is persisted before invoking a mutable external enforcement API so retries and historical reconstruction remain unambiguous.

## Pre-start GitHub path

A protected Actions environment is a strong adapter candidate for a repository/deployment job when capability verification confirms the needed environment/protection feature. DMTZ can consume the environment/deployment opportunity identity and, where supported, provide an approval/rejection through a custom deployment protection integration.

The adapter records GitHub deployment/job identifiers and protection outcome. Downstream Databricks correlation is separate.

## Pre-start Databricks broker path

When organizational execution enters through a governed trigger API, DMTZ can evaluate the Gate before calling Databricks run submission. The broker requires:

- exact job/workspace identity;
- exact opportunity and Gate decision ID;
- stable request idempotency token where supported;
- resulting Databricks run ID;
- monitoring of unauthorized/alternate trigger paths.

The broker cannot claim universal hold if users/schedulers/other systems can bypass it.

## In-DAG path

A condition task or dependency condition can gate a downstream task branch. This is scoped to that downstream opportunity and requires exact rule/branch mapping. Native `Excluded`/upstream state must be translated carefully and never generalized to whole-job failure or DMTZ HOLD without the explicit mapping.

## Cancellation boundary

Databricks cancel is asynchronous. Record request, acknowledgement, observed cancellation state and any work that continued before termination. A cancel request may be containment evidence but cannot backdate a pre-start HOLD.

## Failure handling

Each Gate profile specifies behavior for:

- missing/stale evidence;
- unresolved authority/authorization;
- source/integration outage;
- decision service outage;
- adapter/enforcement outage;
- stale decision;
- duplicate/replayed delivery;
- conflicting Gate decisions;
- bypass detection.

No implicit fail-open/fail-closed behavior exists.
