# Structural, Schema & Interface Compatibility

**Canonical key:** `health.structural-compatibility`

**Kind:** CONTRACT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `stable_family.HLTH`

**Owns current question:** How is realized or proposed structure evaluated against exact consumer/interface contracts without conflating schema meaning, planned state, observed state and compatibility?

**Stable IDs:** HLTH-009–HLTH-018

## Current semantics

### HLTH-009 — Structural Observation, Schema Snapshot & Contract-Surface Binding
Structural evidence binds the exact producer/interface surface, schema/version, subject, context and observation time. Observed fields/types/nullability/nesting are evidence, not compatibility by themselves.

### HLTH-010 — Structural Change Taxonomy, Field Identity, Add/Drop/Rename & Reordering
Add, remove, rename, reorder, nested movement and other structural transitions remain distinct. Rename identity requires evidence; identical names do not prove preserved semantic identity.

### HLTH-011 — Required/Optional Fields, Additive/Removal Compatibility & Consumer Sensitivity
Required/optional/additive/removal behavior is evaluated against the bound consumer/interface contract. An additive field may be safe for one consumer and breaking for another.

### HLTH-012 — Type, Precision, Scale, Casting & Nested-Shape Compatibility
Type, precision/scale, timezone/encoding, cast behavior and nested shape are contract-relative. Engine ability to cast or parse does not establish compatibility.

### HLTH-013 — Nullability, Defaults, Generated Values & Population-Presence Compatibility
Nullability, default/generated values and population-presence guarantees remain explicit contract predicates. Physical non-nullness or a sentinel/default does not automatically satisfy business completeness/validity semantics.

### HLTH-014 — Key, Identifier, Grain & Cardinality-Shape Compatibility
Key/identifier role, grain and cardinality-shape changes can be structurally material even when field names/types remain stable and can invalidate affected measurement and reconciliation assumptions.

### HLTH-015 — Consumer-Specific Contract, Interface Version & Compatibility Scope
Compatibility is bounded to a consumer/use/interface/version rather than being one universal producer label. Physical tables, stable projections/views, streams, exports and other interfaces may expose different compatibility surfaces.

### HLTH-016 — Planned, Declared, Proposed & Realized Structural State
Governed/declared structure, Change Intent/proposed structure, prospective compatibility and realized Observation/Change remain separate truths. Pre-deployment validation does not prove deployment or realized compatibility.

### HLTH-017 — Structural Change Impact on Metric/Profile/Baseline Applicability
Realized structural change triggers scoped review of affected metric definitions/profile membership/Baseline eligibility rather than global invalidation. Unaffected dimensions may retain continuity.

### HLTH-018 — Structural Compatibility Proposition, Evidence & Result Semantics
A bounded compatibility Assessment may resolve `compatible`, `incompatible`, `unknown/unresolved`, `conflicting`, `unavailable` or `not applicable`. `Compatible` requires sufficient applicable evidence for all required predicates; no detected diff under incomplete coverage is not enough.

## Invariants / boundaries

Declared/governed schema meaning ≠ normative structural Expectation/contract ≠ proposed/planned structural state ≠ realized structural Observation/Change ≠ compatibility Assessment.

Structural incompatibility does not prove execution failure, exposure, Impact or cause. Physical DDL/property changes matter only when the relevant contract depends on them.

## Provenance

- `docs/concepts/phase_006/02_structural_schema_ddl_compatibility/README.md`
- Phase 006 Group 02 accepted HLTH-009–HLTH-018.
