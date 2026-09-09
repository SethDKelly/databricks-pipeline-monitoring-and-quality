# REF-002 — Coverage Profile and Opportunity to Observe

**Status:** Accepted — Phase 004 Group 01

## Outcome

Describe what portion of the relevant observation universe an evidence set actually covers, including whether the evidence-collection mechanism had a genuine opportunity to observe the event/state in question.

## Coverage is bounded

Coverage is always stated relative to a declared universe, such as:

- one execution window;
- all qualifying runs for a target between 06:00 and 07:00;
- all expected partitions for a business date;
- all refresh events for a report during an incident interval;
- all current qualifying outputs for a declared upstream dependency;
- all monitored upstream candidates in an Investigation scope.

The framework does not use `complete coverage` without naming the bounded universe to which completeness applies.

## Coverage dimensions

A Coverage Profile may describe:

- **temporal coverage** — which event intervals/opportunities were observable;
- **subject/population coverage** — which entities, partitions, records, tasks, outputs, consumers, or candidate set members were included;
- **source/query coverage** — whether the evidence mechanism successfully queried/enumerated the relevant source scope;
- **identity/version coverage** — whether events can be bound to the correct run/output/version/consumer;
- **measurement coverage** — whether the observed property was actually measured, rather than inferred from a neighboring metric;
- **sampling/estimation coverage** — whether evidence is complete enumeration, bounded sample, estimate, or other partial measurement;
- **monitoring/instrumentation coverage** — whether collection was active and functioning for the relevant opportunity;
- **known gaps** — outages, unavailable partitions, restricted sub-scopes, unresolved identities, late telemetry, or excluded intervals;
- **derivation coverage** — for aggregated evidence, which underlying evidence contributes and where derivation gaps exist.

## Opportunity to observe

A negative conclusion requires more than a query returning no matching rows. The mechanism must have been capable of observing the relevant event/state if it occurred within the bounded universe.

Examples of opportunity-to-observe include:

- an execution source that enumerates all qualifying runs for the target/window;
- a consumer-refresh source capable of recording all refreshes relevant to the exposure question;
- a partition inventory covering all required partitions for the business date;
- an output-version source capable of identifying the current qualifying upstream output.

If instrumentation was down, the query scope was incomplete, or the source does not capture the event class, opportunity-to-observe is inadequate even if the retrieved result is empty.

## Coverage outcomes

Coverage may be expressed as explicit dimensions/limitations rather than a mandatory scalar. Useful qualitative outcomes include:

- bounded-complete for the declared universe;
- materially complete for the target conclusion under a later explicit standard;
- partial with identified gaps;
- sampled/estimated;
- temporally incomplete;
- identity/version incomplete;
- unavailable;
- unknown.

`Materially complete` is conclusion-relative and should not be interpreted as globally complete monitoring.

## Invariants

- Missing telemetry is a coverage gap, not evidence of non-occurrence.
- A successful query can still have incomplete coverage if the query/source does not span the relevant universe.
- Monitoring Scope does not prove actual collection coverage.
- A source's existence does not prove it captured every relevant event.
- Coverage is not the same as source authority; authority/precedence is refined later.
- Restricted detail may be hidden from a requester while a safe coverage limitation/status is disclosed where authorized.
- More rows/events do not automatically mean better coverage if they duplicate the same observation opportunities.

## Examples

### Run absence
Querying one workflow's run list cannot prove no logical pipeline execution occurred if the pipeline can run through another job not included in the query universe.

### Consumer exposure
Knowing a report's last refresh timestamp may establish that it refreshed after C changed, but version-binding may still be inadequate to prove it consumed the affected C output.

### Gate readiness
An upstream task success event provides execution coverage but not necessarily output/version coverage required by the gate criterion.

## Non-goals

- selecting monitoring products;
- asserting universal completeness;
- defining source authority;
- converting coverage into a universal confidence percentage;
- deciding the final sufficiency standard for every evidence class.
