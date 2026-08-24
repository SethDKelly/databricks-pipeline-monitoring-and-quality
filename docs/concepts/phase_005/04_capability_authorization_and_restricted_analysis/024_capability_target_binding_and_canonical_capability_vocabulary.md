# AUTH-024 — Capability Target Binding and Canonical Capability Vocabulary

**Status:** Accepted — Phase 005 Group 04

## Purpose

Bind authorization to the exact principal, capability, subject, context, and time being requested so broad labels such as `analyst`, `owner`, `admin`, or `can access table` do not silently grant unrelated visibility or operational powers.

## Contract

A material capability target should identify:

- principal identity or bounded principal set;
- named capability/action;
- subject/resource or bounded subject set;
- environment/tenant/domain where relevant;
- purpose/use/consumer context where relevant;
- effective interval and evaluation/knowledge time;
- requested detail level when a capability has materially distinct projections.

Canonical capability families must remain independently resolvable. Candidate families include:

- raw/direct data read and sensitive field/value access;
- schema/technical metadata visibility;
- semantic/governance/Classification/Policy Context/Responsibility/Assertion Authority visibility;
- metric/Observation value visibility;
- Assessment/health-summary visibility;
- Expectation/threshold/margin/severity visibility;
- Baseline/reference-detail visibility;
- Lineage node identity, edge/path detail, and topology-summary visibility;
- Investigation participation and evidence inspection;
- Causal Claim status and causal-evidence visibility;
- Impact/exposure/consequence visibility;
- gate/safeguard/control-state visibility;
- Annotation create/view capabilities;
- Explanation/report visibility;
- normative-rule propose/edit/approve/waive/suspend/retire actions;
- job/run, safeguard, gate, override, and causal-confirmation actions whose high-consequence semantics are refined in Group 05.

## Invariants

- Permission for one capability never implies another merely because they concern the same asset.
- `View Assessment` does not imply `view metric value`, `view threshold`, `view Baseline`, or `view raw evidence`.
- `View schema` does not imply raw-data read.
- `View Lineage summary` does not imply every node identity or edge detail is visible.
- `Investigation participation` does not imply complete evidence visibility.
- `Job operation` does not imply raw-data access, gate authority, safeguard authority, or causal-confirmation authority.
- Capability vocabulary is functional and implementation-neutral; it is not an RBAC role matrix or provider ACL taxonomy.
