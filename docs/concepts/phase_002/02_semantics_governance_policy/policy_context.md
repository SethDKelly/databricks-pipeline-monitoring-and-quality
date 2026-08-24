# Concept: Policy Context

**Status:** Accepted — Phase 002 Group 02; authority refined by Phase 005 Group 02

## Purpose

Let users understand which declared policies, handling expectations, restrictions, or governance obligations are asserted to apply to an identified subject in a relevant context and time without claiming enforcement, legal interpretation, or compliance.

## Operational principle

An affected table is classified as PHI. A governance/policy source asserts that, for the production healthcare use of that table, a named handling policy applies and identifies relevant restrictions for monitoring/reporting. Policy Context preserves the policy reference, applicability basis, effective time, provenance, and Assertion Authority context. The product can communicate that context without asserting that the classification alone created the obligation, that access has been enforced, or that compliance has been proven.

Authority over the policy text/reference and authority to assert that the policy applies to a particular subject/use/context may be separate targets.

## Actors

- Security / Privacy / Compliance Stakeholder
- Data Steward / Governance Steward
- Data Owner
- Business Analyst / Data Consumer
- Data Engineer / Pipeline Maintainer
- Monitoring framework

## State

- identified subject and optional facet;
- policy-context/applicability assertions;
- policy or control-framework reference;
- relevant applicability context, such as environment, organizational use, jurisdiction, purpose, or consumer when supplied;
- handling/restriction/obligation summary appropriate for monitoring use;
- applicability basis, including linked classification or other evidence when provided;
- effective interval;
- assertion provenance, actor/source, and Assertion Authority context;
- supersession/correction history;
- unknown, stale, unavailable, or conflicting policy-context assertions.

## Actions

### `associate`
- **Intent:** record or synchronize that a declared policy/handling context applies to a subject under stated conditions.
- **State effect:** preserves the policy reference, applicability basis, context, provenance, and effective time.

### `supersede`
- **Intent:** prospectively replace or end an applicability assertion while preserving historical policy context.

### `resolveAt`
- **Intent:** return policy-context assertions applicable to a subject, declared use/context, and time.
- **Observable result:** applicable assertion(s), unknown, conflicting, stale, unauthorized, or unavailable, with provenance where disclosure is allowed.
- **Conflict behavior:** Assertion Authority resolves standing for the bounded policy/applicability target; synchronization order does not choose a winner.

## Invariants / behavioral expectations

- Policy Context does not grant or deny access.
- Policy Context does not prove enforcement or compliance.
- Policy Context does not perform legal interpretation.
- Authority over policy text/reference does not automatically confer authority over every subject/context applicability assertion.
- Classification may inform applicability but is not itself a policy and does not by itself prove applicability.
- Multiple policies can legitimately apply at the same time and are not automatically conflicts.
- Conflict requires incompatible authoritative assertions for the same policy/applicability target/context/time, not merely several policies.
- Applicability is context- and time-aware; a policy applying in one environment/use/jurisdiction does not silently become global.
- Missing policy context is `unknown`, not `unrestricted`.
- A policy summary does not replace the authoritative policy reference/source.
- Current policy context does not overwrite historical applicability.
- Monitoring does not broaden sensitive-data access merely to explain policy context.
- Responsibility for privacy/security/compliance does not automatically confer Assertion Authority over policy applicability.
- Derived applicability from Classification, schema tags, parent-domain policy, or Lineage is not automatic; an explicit provenance-bearing governed assertion/rule is required.

## Ambiguity and missing evidence

If applicability cannot be established, the product reports unknown/incomplete policy context rather than treating the subject as unrestricted. Stale policy metadata remains marked stale. Conflicting authoritative applicability assertions remain provenance-bearing until accepted Assertion Authority rules resolve them. A viewer may be told that special handling applies without being shown restricted policy details.

## Synchronizations

- **Entity Identity** supplies the subject.
- **Assertion Authority** determines standing for policy-reference/applicability assertions by target/context/time.
- **Classification** may supply evidence relevant to policy applicability but does not determine it alone.
- **Responsibility Assignment** may identify policy/stewardship contacts without making those parties automatically authoritative for policy interpretation/applicability.
- **Capability Authorization** remains the separate permission truth; policy context can inform later authorization policy but is not itself a decision.
- **Explanation** can include authorized policy context and disclose limitations without claiming compliance.
- Later enforcement/control evidence may show whether a specific policy-related mechanism operated; that evidence remains distinct from Policy Context.

## Security / privacy / governance considerations

Policy metadata can reveal sensitive organizational practices, legal/regulatory exposure, restricted data domains, or control expectations. Disclosure should be minimized to what the viewer is permitted to know.

## Evidence / provenance considerations

Every policy-context assertion should retain its policy/source reference, applicability basis, source/actor, assertion time, effective time, context dimensions, and authority standing/basis when known. Derived summaries must remain traceable to those assertions.

## Representative scenarios

### Happy path
A PHI-classified production asset has an explicit authoritative policy-context assertion linking it to a named handling policy; an authorized explanation communicates relevant monitoring/reporting restrictions.

### Classification without policy applicability
An asset is classified as PHI, but no authoritative applicable policy-context assertion can be resolved. The product reports incomplete policy context rather than inventing a policy conclusion from the label.

### Policy text authority versus applicability authority
One governed source owns the policy text while another governed process is authoritative for whether the policy applies to a specific asset/use. Both authority targets coexist.

### Multiple applicable policies
An internal handling policy and a jurisdiction-specific retention policy both apply. Both are returned as applicable rather than treated as conflicting merely because they are separate policies.

### Stale context
A synchronized policy assertion has exceeded its accepted freshness window. The product marks policy context stale instead of presenting it as current certainty.

### Conflicting applicability
Two co-authoritative policy authorities disagree about whether the same restriction applies in the same context/time. The authoritative conflict remains explicit.

### Historical replay
A policy applicability assertion changes prospectively. Incident analysis for an earlier date resolves the earlier context and authority state.

### Unauthorized evidence
A business analyst is told that special handling limits the detail of an explanation without receiving restricted policy text or sensitive classification details.

## Non-goals

- access-control enforcement;
- legal interpretation;
- compliance certification/determination;
- classification assignment;
- proving that a required control operated;
- silently deriving policy applicability from Classification, schema, parent-domain state, or Lineage;
- choosing policy authority by synchronization order.

## Deferred questions

- Which policy-context facts are required for MVP versus later enrichment?
- Which context dimensions must be represented for useful applicability decisions?
- Which policy summaries can be safely exposed to business users versus only governance/security users?
- Which concrete sources/actors hold authority for policy reference and applicability targets in the deployment environment?
