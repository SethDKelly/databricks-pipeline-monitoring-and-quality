# Concept: Expectation

**Status:** Accepted — Phase 002 Group 03

## Purpose

Let an authorized actor or source state what behavior or condition should be considered acceptable for an identified subject in a defined context and time.

## Operational principle

A consumer-facing table is expected to be materially refreshed by 7:00 AM on business days and a key identifier is expected to remain below an agreed null-rate threshold. Those are normative criteria, not descriptions of historical behavior. When the freshness requirement changes next quarter, the new version applies prospectively; an incident replay for the prior quarter still resolves the expectation that was effective then.

## Actors

- Data Owner / accountable business party
- Data Steward / Governance Steward
- Data Engineer / Pipeline Maintainer
- Data Platform Administrator
- Monitoring framework
- Authoritative external source

## State

- identified subject;
- expectation dimension/property;
- normative criterion or acceptable condition;
- applicability context, such as environment, consumer/use, business calendar, operating window, or other relevant scope;
- effective interval and lifecycle state;
- assertion provenance, actor/source, and authority context;
- bounded exception/suspension context when explicitly adopted;
- supersession/correction history;
- unresolved or conflicting expectation assertions.

## Actions

### `establish`
- **Intent:** assert or synchronize a normative criterion for a subject/context.
- **State effect:** records the expectation, provenance, and effective-time context.
- **Failure / unknown behavior:** unresolved subject identity or insufficient assertion authority does not create a guessed expectation.

### `revise`
- **Intent:** change future normative behavior while retaining the earlier version for historical interpretation.
- **State effect:** supersedes prospectively rather than rewriting prior expectation history.

### `exceptFor`
- **Intent:** record a bounded context/time in which the expectation is suspended or excepted.
- **State effect:** changes applicability for the bounded exception without deleting the underlying expectation or altering observations.
- **Important:** an exception does not mean the observed condition was healthy; it only changes the normative applicability used by later assessment.

### `retire`
- **Intent:** end future applicability of an expectation while preserving its historical state.

### `resolveApplicable`
- **Intent:** determine the expectation assertion(s) applicable to a subject, dimension, context, and time.
- **Observable result:** applicable expectation(s), none known, conflicting, unauthorized, or unavailable with provenance where disclosure is allowed.

## Invariants / behavioral expectations

- Expectation is normative: it describes what **should** be true or acceptable.
- Historical or common behavior does not become an Expectation merely because it is frequent.
- A Baseline may inform a human decision to establish an Expectation, but the product must not silently promote a Baseline into a normative rule.
- Expectation does not measure data, execution, or system state.
- Expectation does not decide whether its criterion was met; that belongs to Assessment using Observation evidence.
- Multiple expectations can simultaneously apply when they address different dimensions or contexts.
- Incompatible expectations for the same relevant dimension/context remain conflicting until explicit authority/precedence semantics resolve them.
- A missing applicable expectation does not mean the subject is healthy or acceptable; it means the product lacks a normative criterion for that dimension/context.
- Current expectations do not rewrite historical assessments or the expectation version effective at an earlier incident time.
- Exceptions/suspensions are explicit and time/context bounded; they do not mutate underlying evidence.
- Expectation is implementation-neutral and is not defined by DQX, SQL, scheduler, or metric syntax.

## Ambiguity and missing evidence

If no applicable expectation can be resolved, later assessment must not fabricate a normative result. Conflicting expectations remain visible. If an expectation exists but its details are restricted, a viewer may receive an authorized abstract result such as "an applicable requirement exists" without receiving the sensitive threshold or business rule.

## Synchronizations

- **Entity Identity** supplies the subject.
- **Responsibility Assignment** may identify parties responsible for maintaining or approving an expectation without making those parties universally authoritative.
- **Semantic Definition** can provide interpretation needed to understand the criterion, such as metric grain or business calendar semantics.
- **Observation** provides evidence relevant to the criterion but does not own it.
- **Assessment** compares authorized Observation evidence with the applicable Expectation.
- **Baseline** may provide descriptive context but cannot silently replace or become an Expectation.
- **Change** can later represent expectation changes across time without treating them as data-health changes.

## Security / privacy / governance considerations

Expectations can reveal sensitive thresholds, operating schedules, business rules, or control intentions. Establishment/revision authority and viewer disclosure are separate concerns and both require later authorization semantics.

An actor authorized to maintain a technical expectation is not automatically authorized to establish business, privacy, or compliance-related expectations.

## Evidence / provenance considerations

Every expectation assertion should retain source/actor, assertion time, effective interval, relevant context, and revision/exception history. Historical assessment must be able to identify exactly which normative criterion was effective and used.

## Representative scenarios

### Freshness requirement
A production table must be materially refreshed by 7:00 AM on business days. An observation of last material update at 6:42 AM can later be assessed against that criterion.

### Successful run, failed expectation
A Databricks job succeeds, but the published table is not refreshed by its applicable deadline. Execution success does not satisfy the freshness expectation.

### Baseline without expectation
Table C usually contains about 20 million rows, but no approved row-count requirement exists. The Baseline cannot be treated as an Expectation merely because it is stable.

### Conflicting expectations
Two relevant sources assert different freshness deadlines for the same subject/context. The conflict remains unresolved rather than selecting the latest synchronization.

### Historical revision
A threshold changes on April 1. A March incident must continue to resolve the March criterion even when viewed later.

### Unauthorized expectation detail
A business analyst may learn that a quality criterion was violated while the exact sensitive threshold remains hidden.

## Non-goals

- measuring or recording actual conditions;
- deriving historical Baselines;
- producing health status;
- defining root cause;
- encoding vendor-specific quality-rule syntax;
- establishing universal source-precedence rules.

## Deferred questions

- Which expectation dimensions and lifecycle states are required for the first MVP?
- Which bounded exception semantics are needed beyond simple suspension/non-applicability?
- How should explicit authority/source precedence for expectation categories be modeled?
- Should consequence/severity policy remain outside Expectation and be introduced only when alerting/impact behavior is designed?
