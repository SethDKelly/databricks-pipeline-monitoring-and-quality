# SYN-003 — Classification as Policy-Context Evidence

**Status:** Accepted — Phase 003 Group 01

## Outcome

Allow Classification assertions to participate in determining/explaining declared policy applicability **without turning category membership into policy, authorization, legal interpretation, enforcement, or compliance**.

## Participating concepts and actions

- **Classification** — `resolveAt`.
- **Policy Context** — applicable assertion resolution / association behavior defined by the accepted concept.

## Trigger / initiating condition

A Policy Context assertion or downstream question depends on a classification facet/category as part of its declared applicability basis.

## Preconditions

The subject identity, relevant time, Classification scheme/category context, and Policy Context assertion/reference are sufficiently identified for the intended reasoning.

## Coordination semantics

1. Resolve the relevant Classification assertion(s) with provenance/time.
2. Resolve the applicable Policy Context assertion(s) independently.
3. Where a Policy Context assertion explicitly depends on a classification condition, use the Classification result as supporting/contradicting/uncertain applicability evidence.
4. Classification **alone never creates** a Policy Context assertion.
5. An independent authoritative Policy Context assertion may remain applicable even when Classification evidence is missing, if its own applicability semantics do not require that classification.
6. Preserve conflict/uncertainty rather than deriving a convenient policy result.

## State and evidence effects

Classification remains category state. Policy Context remains declared applicability/handling context. The synchronization records/returns the evidence relationship only where later design requires retention; it does not mutate source labels into policies.

## Ambiguity / failure propagation

- PHI/PII classification missing → cannot infer non-applicability;
- conflicting classification on a required predicate → dependent policy applicability may remain unresolved/conflicting;
- Policy Context missing → Classification remains valid but policy applicability is unknown;
- restricted policy/classification detail → safe abstraction may state that special handling context exists if authorized.

## Temporal semantics

Classification and Policy Context must be evaluated for the same relevant effective-time context. A later reclassification must not retroactively alter policy-context reasoning for an earlier incident without an explicit correction.

## Provenance / traceability

Any downstream statement such as `HIPAA-related policy context applies` must trace to the Policy Context assertion and, when used, the Classification evidence supporting its applicability. It cannot cite Classification alone as the policy claim.

## Security / authorization

Classification and policy metadata can themselves be sensitive. Synchronization may support an opaque `restricted handling applies` result without revealing the underlying label/policy text where disclosure is not allowed.

## Invariants

- Classification ≠ Policy Context;
- Classification ≠ authorization;
- Policy Context ≠ enforcement/control operation;
- Policy Context ≠ compliance;
- missing classification ≠ non-sensitive;
- missing policy ≠ unrestricted;
- synchronization order ≠ authority.

## Scenarios

**PHI-supported applicability:** C is classified PHI under the relevant scheme and an explicit policy assertion says that category activates a handling rule. The explanation can trace the policy context through both facts.

**Conflicting classification:** two classification sources disagree. If the policy depends on that classification, applicability remains unresolved rather than pretending the less restrictive label wins.

**Independent policy:** a retention policy explicitly applies to C regardless of sensitivity classification. Missing PII/PHI labels do not erase that Policy Context.

## Non-goals

Legal interpretation, compliance certification, access-control evaluation, automatic policy creation, control enforcement.

## Deferred questions

Detailed policy-expression/applicability language and source-authority contracts belong to later refinement/integration phases.
