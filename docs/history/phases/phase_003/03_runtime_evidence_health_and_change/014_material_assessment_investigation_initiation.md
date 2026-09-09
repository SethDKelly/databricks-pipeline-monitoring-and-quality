# SYN-014 — Material Assessment → Investigation Initiation

**Status:** Accepted — Phase 003 Group 03 handoff to Group 04

## Outcome

Ensure analysts can intervene quickly when runtime/data evidence warrants research while avoiding an ecosystem that automatically opens incidents for every ordinary or merely atypical change.

## Participating concepts and actions

- **Assessment** — source evaluation/basis.
- **Investigation** — `open`.
- **Responsibility Assignment** — optional routing context.
- **Impact** — optional significance/blast-radius context.

## Trigger / initiating condition

Either an authorized analyst explicitly requests investigation of an Assessment, or a later-accepted response rule determines that the Assessment/context warrants automatic initiation.

## Preconditions

The initiating Assessment and subject/time context are traceable. Automatic initiation requires an explicit policy/authority criterion; this synchronization does not invent one.

## Coordination semantics

1. Preserve the Assessment as the initiating evidence; do not translate it into a cause.
2. Manual analyst initiation is always possible where authorization permits, including atypical, violated, unresolved, or suspicious-but-not-yet-normative cases.
3. Automatic initiation may consider normative violation, persistence/magnitude, business criticality, prospective/actual Impact, timing deadlines, or unresolved evidence only where an accepted response rule explicitly defines that behavior.
4. Baseline atypicality alone does not mandate Investigation.
5. Opening Investigation registers the inquiry promptly and allows human evidence gathering/annotation without requiring the ecosystem to have a definite root cause first.
6. Responsibility Assignment may help route participation but does not establish response authority by itself.

## State and evidence effects

Assessment remains source evaluation; Investigation owns inquiry lifecycle. No separate alert/incident truth is introduced in Phase 003.

## Ambiguity / failure propagation

Insufficient evidence can itself justify analyst review when context is high-risk, but it does not become a violation. Duplicate/low-value investigation suppression rules remain deferred.

## Temporal semantics

Investigation opening time is knowledge/response time distinct from the Assessment's evaluated event time.

## Provenance / traceability

The Investigation retains the triggering Assessment and any rule/actor that initiated it.

## Security / authorization

Analyst access to the Investigation does not broaden access to underlying restricted evidence.

## Invariants

- Assessment ≠ Investigation;
- atypicality ≠ mandatory intervention;
- violation ≠ confirmed cause;
- insufficient evidence may warrant review without becoming failure;
- automation requires explicit accepted criteria;
- human research remains first-class.

## Scenarios

Minor volume variation remains within Baseline and no Investigation opens. A materially atypical client-critical table is manually investigated despite no volume Expectation. A severe freshness violation automatically opens Investigation only under an explicitly accepted later response rule.

## Non-goals

Notification channels, ticketing implementation, pager/on-call product choice, automatic root cause, or response-policy definition.
