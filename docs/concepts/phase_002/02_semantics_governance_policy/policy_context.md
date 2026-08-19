# Concept: Policy Context

**Status:** Accepted — Phase 002 Group 02

## Purpose

Let users understand which declared policies, handling expectations, restrictions, or governance obligations are asserted to apply to an identified subject in a relevant context and time without claiming enforcement, legal interpretation, or compliance.

## Operational principle

An affected table is classified as PHI. A governance/policy source asserts that, for the production healthcare use of that table, a named handling policy applies and identifies relevant restrictions for monitoring/reporting. Policy Context preserves the policy reference, applicability basis, effective time, and provenance. The product can communicate that context without asserting that the classification alone created the obligation, that access has been enforced, or that compliance has been proven.

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
- relevant applicability context, such as environment, organizational use, jurisdiction, purpose, or other declared condition when supplied;
- handling/restriction/obligation summary appropriate for monitoring use;
- applicability basis, including linked classification or other evidence when provided;
- effective interval;
- assertion provenance, actor/source, and authority context;
- supersession/correction history;
- unknown, stale, or conflicting policy-context assertions.

## Actions

### `associate`
- **Intent:** record or synchronize that a declared policy/handling context applies to a subject under stated conditions.
- **State effect:** preserves the policy reference, applicability basis, context, provenance, and effective time.

### `supersede`
- **Intent:** prospectively replace or end an applicability assertion while preserving historical policy context.

### `resolveAt`
- **Intent:** return policy-context assertions applicable to a subject, declared use/context, and time.
- **Observable result:** applicable assertion(s), unknown, conflicting, stale, unauthorized, or unavailable, with provenance where disclosure is allowed.
- **Conflict behavior:** the concept does not silently choose between incompatible policy authorities when precedence is undefined.

## Invariants / behavioral expectations

- Policy Context does not grant or deny access.
- Policy Context does not prove enforcement or compliance.
- Policy Context does not perform legal interpretation.
- Classification may inform applicability but is not itself a policy and does not by itself prove applicability.
- Multiple policies can legitimately apply at the same time and are not automatically conflicts.
- Applicability is context- and time-aware; a policy applying in one environment/use/jurisdiction does not silently become global.
- Missing policy context is `unknown`, not `unrestricted`.
- A policy summary does not replace the authoritative policy reference/source.
- Current policy context does not overwrite historical applicability.
- Monitoring does not broaden sensitive-data access merely to explain policy context.

## Ambiguity and missing evidence

If applicability cannot be established, the product reports unknown/incomplete policy context rather than treating the subject as unrestricted. Stale policy metadata remains marked stale. Conflicting applicability assertions remain provenance-bearing until an accepted authority rule resolves them. A viewer may be told that special handling applies without being shown restricted policy details.

## Synchronizations

- **Entity Identity** supplies the subject.
- **Classification** may supply evidence relevant to policy applicability but does not determine it alone.
- **Responsibility Assignment** may identify policy/stewardship contacts without making those parties automatically authoritative for policy interpretation.
- **Explanation** can include authorized policy context and disclose limitations without claiming compliance.
- Later authorization/enforcement mechanisms may consume policy context, but authorization decisions and enforcement remain separate concepts/mechanisms.
- Future control-evidence concepts may show whether a specific policy-related control operated; that evidence remains distinct from Policy Context and compliance determination.

## Security / privacy / governance considerations

Policy metadata can reveal sensitive organizational practices, legal/regulatory exposure, or the existence of restricted data domains. Disclosure should be minimized to what the viewer is permitted to know.

## Evidence / provenance considerations

Every policy-context assertion should retain its policy/source reference, applicability basis, source/actor, assertion time, effective time, and context dimensions when known. Derived summaries must remain traceable to those assertions. Source precedence must not be inferred from synchronization order.

## Representative scenarios

### Happy path
A PHI-classified production asset has an explicit policy-context assertion linking it to a named handling policy; an authorized explanation communicates relevant monitoring/reporting restrictions.

### Classification without policy applicability
An asset is classified as PHI, but no applicable policy-context assertion can be resolved. The product reports incomplete policy context rather than inventing a policy conclusion from the label.

### Multiple applicable policies
An internal handling policy and a jurisdiction-specific retention policy both apply. Both are returned as applicable rather than treated as conflicting merely because they are separate policies.

### Stale context
A synchronized policy assertion has exceeded its accepted freshness window. The product marks policy context stale instead of presenting it as current certainty.

### Conflicting applicability
Two policy authorities disagree about whether a restriction applies in the same context/time. The conflict remains explicit.

### Historical replay
A policy applicability assertion changes prospectively. Incident analysis for an earlier date resolves the earlier context.

### Unauthorized evidence
A business analyst is told that special handling limits the detail of an explanation without receiving restricted policy text or sensitive classification details.

## Non-goals

- access-control enforcement;
- legal interpretation;
- compliance certification/determination;
- classification assignment;
- proving that a required control operated;
- silently deriving policy applicability from classification alone;
- choosing policy authority by synchronization order.

## Deferred questions

- Which policy-context facts are required for MVP versus later enrichment?
- Which context dimensions must be represented for useful applicability decisions?
- Which policy summaries can be safely exposed to business users versus only governance/security users?
- What source-precedence rules apply when policy authorities conflict?
