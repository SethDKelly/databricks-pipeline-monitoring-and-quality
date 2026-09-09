# AUTH-008 — Authority Separation from Evidence, Permission, Responsibility, Policy, and Enforcement

**Status:** Accepted — Phase 005 Group 01

## Purpose

Keep assertion authority from stealing truth or permission owned by other concepts/refinements.

## Required separations

### Assertion Authority ≠ evidence sufficiency
A source may be authoritative for a governance assertion while the evidence supporting an operational/causal conclusion remains insufficient. Phase 004 applicability/coverage/sufficiency rules still apply.

### Assertion Authority ≠ Capability Authorization
Capability Authorization answers whether a principal may perform a named action. Assertion Authority answers what standing an assertion has once contributed. A principal may be permitted to submit only advisory assertions; an authoritative source does not receive unrelated permissions.

### Assertion Authority ≠ Responsibility Assignment
Being the steward, technical owner, or accountable party does not automatically make that party authoritative for every assertion category.

### Assertion Authority ≠ Policy Context / Classification
Policy applicability or sensitivity labels do not confer general authority to define semantics, expectations, access, or controls.

### Assertion Authority ≠ enforcement/success
An authoritative rule can state what should govern, but does not prove an external access control, gate, safeguard, job action, or other mechanism actually enforced it.

### Assertion Authority ≠ factual infallibility
Authoritative assertions can later be corrected, contradicted, or challenged. Authority determines governed standing, not physical truth by fiat.

## Invariants

- No authority rule may waive REF-001–REF-030 evidence requirements.
- No authority rule may convert Capability Authorization `unknown/denied` into permission.
- No authority rule may turn responsibility into access/control rights unless a separate capability rule explicitly does so.
- No authority rule may turn policy applicability into compliance proof.
- No authority rule may turn configured control policy into enforcement evidence.
- Source-specific operational/evidence reliability belongs to Phase 009 integration/source contracts and Phase 004 evidence semantics, not generic assertion authority.
