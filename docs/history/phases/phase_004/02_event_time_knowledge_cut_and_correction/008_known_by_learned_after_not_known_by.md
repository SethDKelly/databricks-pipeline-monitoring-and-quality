# REF-008 — `Known By`, `Learned After`, and `Not Known By` Claims

**Status:** Accepted — Phase 004 Group 02

## Purpose

Prevent historical epistemic claims from becoming vague shorthand for missing records.

## Distinctions

### `Known by K`
Supported when retained provenance establishes that the relevant evidence/assertion entered the monitoring framework's usable reasoning boundary at or before cutoff `K`.

### `Learned after K`
Supported when the evidence/assertion has an event/effective-time relationship relevant to the historical question but its recorded/knowledge time is later than `K`.

### `Not recorded by K`
A narrow claim about the retained framework record. It requires adequate retention/query coverage of the relevant record class through `K`.

### `Not known by K`
A stronger epistemic negative. It requires sufficient evidence that the relevant framework knowledge paths/opportunities were adequately covered and that no qualifying evidence/assertion entered the reasoning boundary by `K`.

### `Not available by K`
A source-availability claim, separate from framework knowledge. It requires evidence about the source/integration's availability state; absence from the framework record alone is insufficient.

## Rules

- missing retained records do not automatically establish `not known`;
- monitoring outage or incomplete retention weakens `not recorded`/`not known` conclusions;
- source availability before `K` does not imply framework knowledge by `K`;
- framework knowledge by `K` does not prove a particular human actor saw or understood the evidence;
- an actual recorded Assessment/claim/Explanation is stronger evidence of historical interpretation/communication than merely showing that its inputs were known;
- restricted current disclosure may hide details without changing the underlying historical knowledge status.

## Example

A consumption log for Report R is created at 08:12 but is not ingested until 09:05. For an 08:30 knowledge cut, the framework may say `exposure evidence learned after 08:30`. It cannot say the framework knew exposure at 08:30. If retention coverage is incomplete, it also may be unable to claim that no other exposure evidence was known by 08:30.

## Non-goals

- proving what a human personally remembered;
- defining legal discovery/records standards;
- equating source existence with user awareness;
- widening current disclosure authorization.
