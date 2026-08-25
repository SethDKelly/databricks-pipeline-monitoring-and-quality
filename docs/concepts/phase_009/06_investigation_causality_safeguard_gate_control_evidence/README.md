# Phase 009 Group 06 — Investigation, Causality, Safeguard, Gate & Control Evidence

**Status:** Review complete — accepted

## Result

Group 06 accepts **INTG-154–INTG-200** and **ICE06-01–ICE06-72**. No new product concept is required.

The group maps Databricks audit/runtime/control-flow evidence, GitHub environment/deployment protection, Immuta policy/query audit and environment-specific review/control records onto the accepted Investigation, Causal Claim, Propagation Safeguard and Execution Gate models without collapsing inquiry, assertion, authorization, enforcement or effect.

The three source chains remain independent:

**bounded Investigation → evidence-backed lead/localization → discriminating evidence → explicit Causal Claim → REF/AUTH-governed status**;

**protected state/path/cohort → proposal/authorization/request → control acceptance → evidence-established Safeguard enforcement → Group 05 opportunity/path result → REF-028 prevented exposure where justified → release/reopening → independent recovery evidence**;

**exact Gate/opportunity + criterion/profile → evidence suitability/readiness → HOLD/ADMIT/override/fallback decision → delivery/acceptance → Gate enforcement → actual execution/non-execution → independently evidenced operational/Impact effects**.

No stage automatically creates the next.

## Accepted contracts

1. **INTG-154** — Cross-Source Investigation Evidence Assembly
2. **INTG-155** — Investigation Trigger & Bounded Inquiry Source
3. **INTG-156** — First-Observed Localization Evidence
4. **INTG-157** — Earliest-Evidenced Change Localization
5. **INTG-158** — Transformation / Reconciliation Boundary Localization
6. **INTG-159** — Consumer-Effect Localization
7. **INTG-160** — Lead Generation Provenance
8. **INTG-161** — Lead Exclusion Negative-Evidence Contract
9. **INTG-162** — Human Review & Annotation Record
10. **INTG-163** — Automation / Model Research Record
11. **INTG-164** — Causal Proposition Identity & Source Binding
12. **INTG-165** — Causal Support & Contradiction Evidence Roles
13. **INTG-166** — Causal Confirmation Authority Requirement
14. **INTG-167** — Intervention / Remediation Contrast Evidence
15. **INTG-168** — Temporal / Mechanism Discrimination & Counterevidence
16. **INTG-169** — Investigation / Causal Historical Replay
17. **INTG-170** — Databricks Audit Control-Fact Surface
18. **INTG-171** — Audit Request vs Response / Outcome Boundary
19. **INTG-172** — Unity Catalog Grant / Revoke as Control Action
20. **INTG-173** — Current Privilege State vs Historical Enforcement
21. **INTG-174** — Immuta Policy Definition / Change Surface
22. **INTG-175** — Immuta Query-Time Applied-Policy Evidence
23. **INTG-176** — Immuta Denial / Entitlement Enforcement Evidence
24. **INTG-177** — Immuta Coverage, Registration & Audit Limits
25. **INTG-178** — Safeguard Proposal / Authorization / Request Record
26. **INTG-179** — Safeguard Acceptance & Effective Enforcement Evidence
27. **INTG-180** — Safeguard Protected-State / Path / Cohort Binding
28. **INTG-181** — Safeguard Partial & Alternate-Path Coverage
29. **INTG-182** — Safeguard No-Opportunity / Prevention Boundary
30. **INTG-183** — REF-028 Prevented-Exposure Composition
31. **INTG-184** — Safeguard Release / Regrant / Effective Reopening
32. **INTG-185** — Safe-State / Non-Delivery Effect Boundary
33. **INTG-186** — Overlapping Safeguards & No Hidden Attribution
34. **INTG-187** — Databricks Jobs Cancel as Post-Start Interruption
35. **INTG-188** — Native Output-Hold / Quarantine Gap
36. **INTG-189** — GitHub Environment Protection as Gate Surface
37. **INTG-190** — GitHub Reviewer Approval, Reject, Bypass & Wait Semantics
38. **INTG-191** — GitHub Custom Deployment Protection Rule
39. **INTG-192** — Databricks `Run if` / `If/else` Gate Mapping
40. **INTG-193** — Gate Criterion / Readiness Source Binding
41. **INTG-194** — Gate Decision, Delivery & Acceptance Evidence
42. **INTG-195** — HOLD Enforcement & Contradictory Start
43. **INTG-196** — ADMIT Barrier Removal & Non-Execution
44. **INTG-197** — Override, Fallback, Timeout & Escalation Evidence
45. **INTG-198** — Multiple Gates & Safeguard Composition
46. **INTG-199** — Control Telemetry Failure & Historical Replay
47. **INTG-200** — Group 06 Source Matrix & Group 07 Handoff

## Investigation and localization

Group 06 does not introduce a new RCA truth source. It composes the accepted Group 03–05 evidence while preserving source ownership.

First observed deviation, earliest evidenced state change, first transformation/reconciliation boundary and first consumer effect remain different propositions. Databricks runtime/system evidence, quality/reconciliation results, Lineage/query encounters and control/audit events can make those localizations materially stronger, but **localization remains inquiry evidence rather than causality**.

Every lead retains provenance, searched scope and limitations. Human reviewers, GitHub issues/tickets, vendor root-cause fields, automated RCA or models can propose leads/claims, but actor seniority, approval, tool origin, graph distance or ranking does not create causal status.

Lead exclusion remains a strong negative. For example, proving a proposed version was not consumed can materially discriminate a claim only when version-consumption coverage is sufficient.

## Causal Claim source support

A causal proposition is explicit before evaluation: exact cause, effect, causal role, population/scope, effective interval, mechanism/transmission assumptions and knowledge cut.

Runtime/version contrasts, reconciliation, affected-versus-unaffected populations, exposure/effect timing, rollback/rerun and control interventions may support or contradict a claim. These are claim-relative evidence roles, not universal source rankings.

**No evaluated Databricks, GitHub or Immuta feature automatically owns `confirmed` Causal Claim status.** Vendor RCA fields, analyst agreement, policy rationales, deployment reviews and remediation success remain evidence/context. Confirmation remains governed by **REF-017 + AUTH-034**.

## Databricks control/audit evidence

`system.access.audit` is a useful action-fact source because it can retain actor, service/action, request parameters, response, event ID and time for qualifying events. It currently has a documented 365-day free retention window.

Preserve:

**request recorded → response returned → target state changed → effective enforcement during relevant opportunity**.

Some actions can collapse parts of that chain when their documented semantics justify it; asynchronous/distributed actions cannot.

Unity Catalog grant/revoke/permission-change evidence is strong for the exact privilege plane it controls, but cannot prove every material alternate path was protected. Current privilege state also cannot be projected backward as historical enforcement.

Databricks Jobs cancellation is explicitly post-start interruption evidence: cancellation is asynchronous and acts on an existing run/task. It is therefore not a pre-start Execution Gate HOLD.

## Immuta enforcement evidence

Immuta application/UAM audit can retain policy, metadata/tag, entitlement, access-request and permission changes. Query audit can be materially stronger for enforcement because qualifying records can capture user entitlements and policies applied at execution, including denial context.

The important separation is:

**policy configured → user/data source covered → policy applicable → policy applied to query → query allowed/denied/transformed → downstream exposure outcome**.

A query-time applied-policy or denial record can be strong evidence for that bounded path/user/query. It cannot establish global protection where alternate paths or unregistered/uninstrumented populations remain unresolved.

Immuta history is also retention/configuration bound. Current SaaS guidance describes 90-day default retention with export recommended for longer analysis; deployed-version/integration semantics must be verified because version-specific documentation differs.

## Propagation Safeguard

No universal native quarantine/hold capability is assumed across every Databricks table/version, dashboard cache, export, API and application path.

Safeguard realization is therefore path-specific. Unity Catalog privileges, Immuta enforcement, publication routing, current-state presentation or other controls may realize a Safeguard only when the exact protected state/path/cohort/interval and effective enforcement are evidenced.

REF-028 prevention retains the full burden:

**relevant Group 05 encounter opportunity + path through protected surface + effective Safeguard enforcement + negative suspect-state encounter for controlled path + sufficient material alternate-path coverage**.

No opportunity means no prevention credit. One denied path does not prove global prevention. Safe stale serving/non-delivery are separately evaluated health/Impact outcomes.

Release/regrant/effective reopening likewise remains separate from recovery/currentness.

## GitHub environment protection as Execution Gate

GitHub Actions environments provide the strongest evaluated native pre-start Gate semantics. A job referencing a protected environment does not proceed to a runner until configured protection rules pass.

Required-review approval, rejection, bypass, wait timer and custom GitHub App protection rules remain distinct. Approval/removal of a GitHub environment barrier is strong ADMIT-like enforcement evidence for that exact Actions job; rejection is a GitHub workflow outcome; bypass is an exceptional action whose DMTZ override authority/scope must be mapped explicitly.

Custom protection-rule apps can consult external observability/change/security/quality systems. Their approval/rejection is the Gate decision for the configured GitHub rule; it does not inherit truth authority over the external source proposition.

Most importantly, **GitHub Gate evidence applies to the GitHub job/deployment opportunity it actually protects**. Saying that it gated a Databricks run requires the explicit deployment/run correlation established in Group 03.

## Databricks conditional execution as Execution Gate

Lakeflow Jobs `Run if` dependencies and `If/else` condition tasks expose concrete control-flow semantics and condition outcomes. They can be strong Gate implementation candidates when the organization explicitly maps:

**exact Gate/profile + opportunity → accepted criterion/profile revision → operands/source evidence → condition evaluation → branch/blocked-task result**.

A task named `quality_gate`, upstream success, or a boolean expression is not automatically DMTZ readiness. Criterion identity, Assertion Authority/Capability Authorization and evidence suitability remain external accepted semantics.

## Gate enforcement, exceptional paths and overlap

Group 06 preserves:

**decision issued → delivered → accepted/acknowledged → effective barrier/permissive state → actual execution/non-execution**.

Not every integration exposes each stage. Missing stages remain unknown rather than inferred.

Reliable start during an applicable unsuperseded HOLD contradicts full HOLD enforcement. Conversely, no run does not prove HOLD without adequate opportunity/control/Execution History coverage.

ADMIT proves barrier removal/permissiveness when evidenced, not execution occurrence. Override preserves readiness truth. Fallback configuration, trigger, selection and enforcement remain distinct. Timeout and escalation are not admission decisions.

Multiple Gates and Safeguards have no hidden universal precedence. Their composition must be explicit, and broader claims that a control caused delay, staleness, business harm or prevention remain Causal Claim work except the narrow REF-028 prevented-exposure determination.

## Historical replay and degraded telemetry

Databricks audit, GitHub deployment/action history, Immuta audit and any custom Investigation/control records have different retention/detail windows. Historical replay therefore composes source-specific history rather than assuming a single control ledger.

Missing/conflicting control telemetry never proves fail-open, fail-closed, successful HOLD, successful Safeguard, fallback application or control-effect causality. Integration health remains a separate limitation.

## Artifacts

- [`source_capability_matrix.md`](source_capability_matrix.md) — proposition-specific support and residual gaps.
- [`external_source_review.md`](external_source_review.md) — current public documentation verified on 2026-08-25.
- [`scenario_review.md`](scenario_review.md) — ICE06-01–ICE06-72 pass.
- [`../../../decisions/phase_009_group_06_investigation_causal_control_sources.md`](../../../decisions/phase_009_group_06_investigation_causal_control_sources.md) — D-1119–D-1172.

## Architecture boundary

Group 06 does not choose incident/case software, RCA algorithms, causal inference engine, approval workflow, quarantine implementation, ACL/routing strategy, GitHub App, Databricks task design, Gate service, event store, retry/fallback implementation, control-state store or UI. Phase 010 owns technical realization.

## Handoff

**Group 07 — Explanation, Historical Replay, Basis Inspection & Disclosure Source Contracts is next.**

Group 07 receives source-established Investigation/localization facts, exact Causal Claim status/basis, Safeguard/Gate lifecycle/enforcement facts and control limitations only with their proposition identity, authority, event/knowledge time, coverage, retention and authorization constraints. It may not turn an unavailable control stage or unresolved causal proposition into a complete narrative.
