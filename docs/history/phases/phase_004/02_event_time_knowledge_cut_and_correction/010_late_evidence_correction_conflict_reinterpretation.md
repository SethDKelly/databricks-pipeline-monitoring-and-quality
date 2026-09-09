# REF-010 — Late Evidence, Correction, Conflict, and Reinterpretation

**Status:** Accepted — Phase 004 Group 02

## Purpose

Distinguish kinds of later information so historical truth is not rewritten and conflicting evidence is not mislabeled as correction.

## Later-information classes

### Late-arriving evidence
A fact/assertion relevant to an earlier event/effective time is first learned by the monitoring framework at a later knowledge time. The historical event time remains unchanged; the contemporaneous cut does not gain the evidence retroactively.

### Source correction
The owning/accepted source explicitly corrects or supersedes one of its earlier facts/assertions under source-supported correction semantics. The prior source state remains historically addressable.

### Independent conflicting evidence
A separate evidence source disagrees with an earlier fact/assertion. This is not automatically a correction. Both remain provenance-bearing until an accepted authority/correction rule resolves them.

### Semantic reinterpretation / reassessment
The source fact remains unchanged but its meaning or derived conclusion changes because reference context, evaluation logic, comparison context, or other evidence changed. The new Assessment/claim/Impact/etc. is a new derived state, not a correction to the original Observation merely because interpretation changed.

### Later authority resolution
A later governance/source-authority decision resolves which conflicting assertion governs current use. That resolution has its own effective/knowledge time and must not be backdated. Detailed authority semantics remain Phase 005 work.

## Rules

- every later-information item retains event/effective and knowledge timing;
- correction/supersession preserves prior state rather than deleting it;
- conflict remains conflict until explicit accepted resolution exists;
- a newer record is not automatically a correction merely because it is newer;
- reinterpretation does not mutate source evidence;
- actual historical controls and communications are never rewritten by later corrections;
- prospective knowledge is not backfilled with later evidence.

## Example

An 08:00 row-count Observation is later explicitly corrected by its owning source at 10:00: source correction. A separate audit source reporting a different row count at 08:00 is conflicting evidence, not correction. A new Assessment created because the accepted Baseline context was corrected is reassessment, not a correction to either row-count fact.

## Non-goals

- selecting source precedence;
- defining every vendor's correction mechanics;
- counterfactual rewriting;
- deleting superseded history.
