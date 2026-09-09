# Concept: Causal Claim

**Status:** Accepted — Phase 002 Group 05

## Purpose

Represent an explicit proposition that one or more conditions caused, contributed to, enabled, or materially influenced a defined outcome, while preserving epistemic status, supporting and contradicting evidence, uncertainty, review provenance, and historical revision.

## Operational principle

Table C loses rows. One Causal Claim proposes that reduced B population contributed to the loss; another proposes that changed join-key quality contributed; a third proposes that a nearby Deployment caused the issue. Evidence supports the first two and contradicts the deployment claim because B changed before activation. If an agreed evidence/authority standard is later satisfied, the supported contributing claims may be confirmed. Rejected or weakened alternatives remain historically visible.

## Actors

- Data Engineer / Pipeline Maintainer
- Incident responder / on-call engineer
- Data Steward / Governance Steward
- Data Owner / accountable business party
- Authorized reviewer
- Monitoring framework

## State

- causal-claim identity;
- proposed cause condition(s), event(s), entity state, or change context;
- defined effect/outcome being explained;
- relevant effective/event-time interval;
- causal role, such as primary, contributing, enabling, preventing, or unresolved role where later useful;
- epistemic status, with candidate vocabulary such as `proposed`, `supported`, `weakened`, `rejected`, `confirmed`, `unresolved`;
- supporting evidence references and rationale;
- contradicting evidence references and rationale;
- relevant alternative/competing claim references where useful;
- uncertainty/confidence rationale without requiring a numerical score;
- proposer, reviewer, confirmation/rejection provenance;
- evidence/authority standard used for any high-consequence status when defined;
- recorded/knowledge-time status history and supersession/correction links.

## Actions

### `propose`
- **Intent:** record a causal explanation as a claim under evaluation rather than as a fact.

### `support`
- **Intent:** associate evidence/rationale that increases support for the causal proposition.
- **Important:** the underlying evidence remains owned by its source concept.

### `contradict`
- **Intent:** associate evidence/rationale that weakens or conflicts with the causal proposition.

### `reviseStatus`
- **Intent:** revise the claim's epistemic state as the evidence picture changes.
- **State effect:** preserves prior status and knowledge-time context.

### `confirm`
- **Intent:** record that the claim satisfies an explicit accepted confirmation standard and authority requirement.
- **Failure / unknown behavior:** if no such standard/authority is defined or evidence is insufficient, the claim cannot be promoted merely for completeness.

### `reject`
- **Intent:** record that the claim is sufficiently contradicted or otherwise rejected under the applicable review standard while preserving history.

## Invariants / behavioral expectations

- A Causal Claim is a proposition with epistemic status; it is not an Observation, Assessment, Change, or independent fact.
- Temporal proximity alone does not establish causation.
- Lineage reachability alone does not establish causation.
- Deployment activation alone does not establish causation.
- A realized Change matching registered Change Intent is evidence of intent consistency, not proof that the intended modification caused every coincident result.
- A planned change may explain one dimension while an unrelated or unintended condition causes another violation.
- Multiple contributing causes can coexist; the model does not require a single root cause.
- A claim can simultaneously have supporting and contradicting evidence.
- Lack of contradicting evidence is not proof.
- `confirmed` requires an explicit evidence/authority standard; neither automated ranking nor human title alone is magic confirmation authority.
- Confirmation provenance states who/what confirmed the claim and under which standard/basis.
- A previously confirmed claim can later be challenged or superseded by materially new evidence; historical confirmation remains reconstructable rather than silently erased.
- Rejected/weakened claims remain historically discoverable when material to understanding the Investigation.
- Qualitative contribution roles are supported without requiring quantitative causal allocation.

## Ambiguity and missing evidence

Evidence may be insufficient, contradictory, inaccessible, temporally ambiguous, or non-comparable. A claim may remain `proposed`, `supported`, or `unresolved` indefinitely.

A restricted evidence source may allow the product to expose only a safe claim status or an indication that undisclosed evidence materially affects confidence.

## Synchronizations

- **Investigation** groups and contextualizes Causal Claims without owning their status.
- **Observation**, **Assessment**, **Change**, **Lineage**, **Execution History**, **Deployment**, and **Change Intent** provide evidence/context.
- **Expectation** and **Baseline** help distinguish normative violation, historical atypicality, and structural context from cause.
- **Annotation** can be cited as attributed human context/evidence with its human-authored status preserved.
- **Impact** may motivate separate Causal Claims when asserting that an originating issue caused a particular downstream effect.
- **Explanation** must preserve the claim's epistemic status and evidence limitations.

## Security / privacy / governance considerations

Causal claims can expose sensitive operational, organizational, vendor, or business conclusions even when underlying raw evidence is hidden. Proposal, review, confirmation, visibility, and explanation must respect authorization and Policy Context.

A user who can see that a cause is `confirmed` is not automatically entitled to see all supporting restricted evidence.

## Evidence / provenance considerations

Every material support/contradiction link, status revision, proposer/reviewer action, and confirmation/rejection action retains provenance and recorded/knowledge time. The claim references evidence; it never replaces or mutates it.

## Representative scenarios

### Multiple contributors
B population falls and join-key nulls rise. Two claims are supported as contributing explanations for C's row loss.

### Planned effect versus unintended effect
A filter Change Intent anticipates a lower C volume and the realized volume matches. A separate completeness failure appears. Intent consistency supports the explanation for the volume shift but does not confirm the filter as the cause of completeness loss.

### Deployment correlation weakened
A deployment occurs near the degradation, but upstream evidence shows the problematic condition began earlier. The deployment claim is weakened/rejected without deleting the deployment evidence.

### Unresolved cause
Several claims remain plausible and evidence cannot discriminate them. The Investigation may close unresolved while each claim retains its status.

### Later correction
A claim was confirmed under the then-current evidence standard. Later source evidence demonstrates a different sequence. A new status/supersession records the correction while preserving the original confirmation history.

### Restricted cause
The audience can be told that a supported upstream cause exists but cannot see the restricted system identity or evidence details.

## Non-goals

- hypothesis-generation algorithm selection;
- numerical confidence-model selection;
- automatically equating correlation with causation;
- changing source Observations or Assessments;
- legal/audit-grade causality guarantees by default;
- quantitative percentage attribution as a required capability.

## Later refinement — Phases 004, 005 and 007 Group 05

Phase 004 REF-013–REF-020 finalizes the epistemic vocabulary as `proposed`, `supported`, `weakened`, `unresolved`, `rejected`, `confirmed` and defines multidimensional causal evidence, material alternatives, confirmation evidence gates, multiple contributors and challenge after confirmation.

Phase 005 AUTH-034 establishes that `confirmed` is independently authority/capability gated in addition to the REF-017 evidence standard. No title, model, service principal or incident role self-authorizes confirmation.

Phase 007 Group 05 [`OPS-060–OPS-066`](../../phase_007/05_investigation_localization_causal_handoff/README.md) further fixes the Investigation handoff boundary:

- Investigation leads/localization are not causal claim states;
- the moment cause/contribution/enabling/triggering/preventing/material-influence is asserted, the proposition belongs here;
- first observed deviation, earliest evidenced change, reconciliation boundary, first post-change run, shared consumed version, rollback/retry contrast, Lineage distance and prospective blast-radius membership are evidence/context rather than causal status;
- Investigation priority or closure never transfers into claim status;
- confirmation remains REF-017 + AUTH-034 gated;
- operational resolution can coexist with non-confirmed causal state;
- historical claim state remains challengeable/non-rewriting when Investigation later reopens.

The earlier generic `uncertainty/confidence rationale` wording is qualitative rationale only and must not be interpreted as a universal numeric confidence score.

## Deferred questions

- concrete confirmation profiles for particular operational claim classes;
- whether quantitative contribution/attribution should be modeled if future scenarios require it;
- whether causal chains among several claims require additional structured relationship semantics beyond claim references;
- concrete automated causal-analysis mechanisms, which remain later implementation work.
