# Phase 010 Group 02 — Retention, Relevance & Lifecycle Architecture

## Purpose

Prevent historical evidence from becoming an indefinitely growing, noisy, expensive corpus while preserving the history required for monitoring, trends, replay, Investigation, audit and Explanation.

The architecture separates:

1. **storage retention** — whether material is still retained;
2. **resolution/detail** — full detail, normalized detail, aggregate, archive or provenance-only;
3. **reporting/retrieval relevance** — whether retained history is normally surfaced for a question/use class.

Age alone decides none of these universally.

## Lifecycle states

| State | Meaning |
|---|---|
| `RECENT_FULL` | recent evidence/detail optimized for routine operational and health queries |
| `WARM_REPLAY` | detailed normalized history retained for meaningful comparison/replay |
| `SUMMARY_ELIGIBLE` | exact detail may be downsampled only for record classes whose future promises permit it |
| `COLD_PINNED` | infrequently queried but retained due to dependency, incident, report, audit or hold |
| `PROVENANCE_STUB` | payload/detail expired; minimal evidence/provenance/lifecycle metadata remains |
| `EXPIRED` | configured retention obligations are closed and retained material has been purged |

These are storage lifecycle states, not evidence strength or importance labels.

## Reference profile for an ordinary non-regulated deployment

These are **starting defaults**, not semantic requirements. Deployment policy may shorten/extend them subject to product promises and holds.

| Material | Reference default |
|---|---|
| routine recent full-detail normalized evidence | about **120 days** |
| detailed normalized replay/trend evidence | about **400 days** |
| aggregatable health/metric trend rollups | up to about **24 months** where exact underlying detail is no longer promised |
| large/opaque raw payloads | minimize aggressively; ordinarily no longer than the detailed need unless pinned |
| incident/claim/control/report/audit evidence | dependency/hold-bound rather than ordinary age-only TTL |
| history beyond roughly 24 months | opt-in by explicit product/audit/legal/recurrence value rather than default accumulation |

Rationale: the reference profile keeps a quarter-plus of rich operational context and roughly a year of detailed comparison/replay while preventing multi-year detailed telemetry accumulation by default. Longer trend history can often be represented by approved aggregates, while exceptional evidence stays exact when its dependency requires it.

## Retention drivers

A retention decision considers categorical drivers rather than one universal relevance score:

- record/evidence class;
- SC-01–SC-06 service class;
- product/reporting/replay promise;
- active Investigation/Causal Claim dependency;
- retained Explanation/basis dependency;
- Gate/Safeguard/control-history dependency;
- legal/regulatory/contract/audit hold;
- security/minimization requirement;
- recurrence/comparison need explicitly established by a later question/workflow;
- tenant/residency policy;
- archive/restore capability and cost.

## Dependency pinning

Ordinary TTL cannot delete material still required to fulfill a retained artifact or active workflow promise.

Examples:

- a Causal Claim basis remains pinned while exact reviewability is promised;
- an actual retained Explanation can pin its exact permitted basis for the promised audit horizon;
- Gate/Safeguard enforcement evidence can be retained for the control-audit horizon;
- an incident may pin an otherwise expiring payload;
- legal/audit holds supersede ordinary TTL.

Pinning does not strengthen truth or evidence sufficiency.

## Reporting relevance

Retained evidence is **not automatically eligible for routine reports**.

Later Explanation/reporting architecture should normally prefer the question's bounded recent/comparison window. Older retained evidence can enter when:

- the user explicitly asks for historical/comparative analysis;
- a trend definition requires it;
- a recurring incident/proposition links it materially;
- an Investigation follows the historical chain;
- a retained basis/report requires it;
- an audit/legal workflow explicitly requests it.

This prevents a three-year history from flooding every current report while preserving purposeful retrieval.

## Downsampling rules

Lossy rollup is allowed only when exact detail is no longer required by the product promise.

Good candidates include older high-frequency measurements whose future use is trend comparison. Examples might age minute-level observations into hourly/daily/weekly/monthly summaries.

Poor candidates include:

- exact execution/run/input version evidence;
- exact source records used by active Causal Claims;
- Gate/Safeguard decision/enforcement evidence;
- retained communication content;
- exact basis inspection material;
- evidence whose negative/coverage semantics depend on individual occurrences.

A rollup never retroactively becomes the evidence that supported a prior exact conclusion.

## Provenance stubs

When payload bytes/details expire, a minimal stub can retain:

- durable evidence ID;
- source/capability-instance identity and locator where safe;
- event/effective/availability/collection coordinates that remain permitted;
- digest/fingerprint where safe;
- prior capture class;
- expiry/purge policy and time;
- dependency/hold closure context;
- basis/reference linkage where allowed.

A stub supports honest statements such as `basis reference retained; exact payload expired`. It cannot reproduce the expired contents.

## Retention-policy revision

Retention policies are versioned and effective-dated. A policy change can trigger lifecycle reevaluation of existing eligible material, but the prior policy and prior lifecycle decisions remain historically recorded.

Unknown legal/product requirements block irreversible purge of affected material until resolved or a governed assumption explicitly permits it.

## Cost discipline

Group 08 will own final cost controls, but Group 02 requires storage cost to be observable by record class/tier/tenant and retention driver. Cost savings must come from policy, minimization, safe rollup and tiering—not from silently shortening promised evidence horizons.
