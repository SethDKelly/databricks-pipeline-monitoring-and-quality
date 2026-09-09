# EXPL-005 — Temporal Perspective: Event Window & Knowledge Cut

**Status:** Accepted — Phase 008 Group 01

## Requirement

Every materially time-sensitive question must resolve the relevant temporal perspective using the accepted bitemporal model.

Keep separate:

- **event/effective time** — when the questioned state/event/relationship/action applied;
- **recorded/knowledge cut** — latest evidence/state allowed to contribute to an as-known view;
- **question/composition time** — when the answer is requested/composed.

## Historical questions

Examples:

- `What happened at 10:00?` identifies an event-time target but, absent a knowledge cut, normally asks for the current retrospective interpretation of that historical event.
- `What did we know at 10:15 about the 10:00 incident?` binds both event time and knowledge cut.
- `What was the topology during the incident?` must resolve then-effective Lineage, not current topology.

## Discipline

Later evidence can contribute to a current retrospective answer but cannot be described as known at an earlier cut.

A single question can legitimately have multiple valid answers under different knowledge cuts. Those answers are not contradictory when their perspectives are explicit.
