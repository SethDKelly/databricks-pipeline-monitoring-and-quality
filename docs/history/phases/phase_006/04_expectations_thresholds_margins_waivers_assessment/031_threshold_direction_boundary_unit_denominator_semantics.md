# HLTH-031 — Threshold Direction, Boundary, Unit & Denominator Semantics

## Purpose

Prevent threshold evaluation from depending on ambiguous shorthand.

## Rule

Threshold-like criteria must preserve explicit comparison semantics, including as applicable:

- upper/lower/range/set membership direction;
- inclusive versus exclusive boundary;
- unit and scale;
- denominator/population basis;
- absolute versus ratio/rate/percentage interpretation;
- timezone/calendar/window semantics for temporal criteria;
- structural predicate identity for schema/contract criteria.

Examples such as `<= 2%`, `< 2%`, `>= 99.5%`, `13M–15M inclusive`, and `fresh by 07:00 local business time` are materially different criteria.

## Invariants

- Display formatting never substitutes for criterion semantics.
- Unit conversion may support evaluation only when conversion meaning is explicit and loss/precision is suitable.
- A percentage without its denominator/population meaning is insufficiently bound.
- Boundary equality is evaluated according to the declared inclusive/exclusive rule, not a platform default.
- Changing comparison direction, unit, denominator or boundary semantics creates a materially revised criterion/version.

## Non-goals

- vendor expression syntax;
- threshold-authority rules;
- severity or alert-routing behavior.