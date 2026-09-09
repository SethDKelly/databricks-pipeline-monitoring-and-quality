# Phase 010 Group 09 — Data / Store Ownership Map

**Status:** ACCEPTED

This map prevents physical convenience from becoming truth ownership.

| Store / state family | Canonical? | Owner / authority posture | Rebuildable? | Critical rules |
|---|---|---|---|---|
| Source systems / vendor APIs/tables | Source-owned | Authority depends on accepted source/facet/context mapping | No, external | Availability is not Assertion Authority; source limitations retained |
| DMTZ canonical evidence journals | Yes for framework-retained evidence identity/provenance/history | Framework persistence of source evidence; copied facts retain original source semantics | Protected, not treated as disposable | Non-rewriting correction/supersession; multi-coordinate time |
| Canonical Entity Identity / source bindings | Yes | DMTZ ecosystem identity proposition | Protected | Rename/incarnation/conflict history retained |
| Canonical Principal / acting/delegation bindings | Yes | DMTZ canonical identity mapping, with upstream identity provenance | Protected | Human/group/service/workload identities distinct |
| Monitoring Scope policy/materializations | Yes | Organization-owned DMTZ policy | Protected | Discoverability != scope; unknown membership retained |
| Assertion Authority policy | Yes | Organization-owned DMTZ policy | Protected | Proposition/facet/context/time specific |
| Capability Authorization/disclosure policy and material decisions | Yes | Organization-owned DMTZ policy/decision | Protected | Authorization != enforcement; current != historical |
| Change Intent / Deployment associations | Yes for DMTZ association/workflow state plus retained source evidence | DMTZ records association evidence without replacing source truth | Protected | Names/timestamps not exact joins |
| Runtime implementation/input/output manifests | Yes as DMTZ evidence/attestation records | Source/attestation bounded | Protected | Missing facets remain partial |
| Measurement/Observation records | Yes | Source/measurement-engine evidence under exact definition/provenance | Protected per policy | Observation != Assessment |
| Expectation/Baseline/Assessment definitions/results | Yes for DMTZ-governed state | Authority/definition-specific | Protected | Baseline descriptive; Expectation normative |
| Typed Lineage evidence | Yes where source evidence/accepted attestation is retained canonically | Source/attestation bounded | Protected | Coverage limitations retained |
| Consumer encounter/exposure/effect/consequence records | Yes where evidence is captured | Source-specific proposition ownership | Protected | Each layer remains independent |
| Investigation/lead/annotation/Causal Claim workflow | Yes | DMTZ workflow/proposition state | Protected | Lead/annotation origin does not create truth |
| Retained Explanation snapshot/communication | Yes for actual communication evidence when promised | DMTZ communication record; not source-domain truth | Protected for promised horizon | Reconstruction != retained communication |
| Gate/Safeguard decision/enforcement/control journals | Yes when active control deployed | DMTZ control state + source enforcement evidence | Protected per policy | Decision != enforcement != execution/prevention |
| Acquisition checkpoints/cursors | Operational state, not domain truth | Adapter/source-plan specific | Reconstructable where source permits | Advance only after durable evidence publication |
| Quarantine/raw source envelopes | Retained evidence payload support, not independent authority | Source representation with minimization policy | Policy-dependent | Copy is common-derived, not corroboration |
| Delta-backed operational/reasoning graph projection | No | Derived DMTZ projection | Yes | Exact edge provenance; current graph not replay truth |
| Search/full-text/vector index | No | Derived candidate-recall store | Yes | Authorization/residency filtering before sensitive exposure |
| Serving materialized views/read models | No | Derived projection | Yes | Projection revision + canonical/source watermark |
| Authorization-sensitive response cache | No | Derived request-context result | Yes | Tenant/principal/purpose/detail/policy context in key as needed |
| UI session state | No | Experience/session | Yes/ephemeral | Cannot write truth by convenience |
| API gateway state | No | Transport/security | Yes/ephemeral | Authentication/routing does not create authorization/domain truth |
| Model prompt/tool/trace store | No domain truth; invocation provenance may be retained | Operational/reasoning provenance | Policy-dependent | Model output not source evidence/authority |
| Observability metrics/logs/traces | Operational evidence | DMTZ runtime operations | Policy-dependent | Platform health != monitored-domain health; minimize sensitive data |
| Cost/usage attribution projection | Derived from source billing/usage + DMTZ dimensions | Operational/economic evidence | Yes where source history retained | Cost policy cannot change epistemic truth |
| Cold archive/backups | Protected copy of canonical/retained material | Same ownership/authority as source canonical objects | Restoreable by promise | Archive does not broaden disclosure or create new authority |

## Ownership invariants

1. **One physical platform may host several logical ownership classes.** Unity Catalog governance over a table does not make every table equivalent in truth ownership.
2. **A copied source record does not become an independent corroborating source.**
3. **A derived store can be operationally indispensable without becoming canonical.** If a graph/search/cache loss cannot be rebuilt from retained canonical state, the implementation has violated the architecture or has silently created a new canonical store.
4. **Historical replay reads canonical time-aware journals and retained source/basis state, not current read models.**
5. **Authorization/disclosure applies to archived and derived material as well as recent canonical records.**
6. **Physical backup/restore does not rewrite when evidence was available or what was communicated at a prior time.**
