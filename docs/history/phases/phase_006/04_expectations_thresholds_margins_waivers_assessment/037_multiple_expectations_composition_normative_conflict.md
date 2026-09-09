# HLTH-037 — Multiple Expectations, Composition & Normative Conflict

## Purpose

Distinguish legitimately coexisting normative rules from unresolved conflict.

## Rule

Multiple Expectations can simultaneously apply when they bind different dimensions, contexts, consumers, windows or explicitly composable predicates. For the same bound normative proposition, conflicting co-authoritative criteria remain conflict unless an accepted authority/precedence/composition rule resolves them.

Examples:

- freshness <=30 minutes and completeness >=99.5% can both apply as separate dimensions;
- warning at 20 minutes and failure after 30 minutes can compose when explicitly defined as one rule structure;
- consumer A requiring column X and consumer B not requiring X are not conflicts when consumer context differs;
- `row_count >=15M` and `row_count >=18M` for the same subject/context/time are unresolved normative conflict absent a governed resolver.

## Invariants

- Do not silently apply strictest, loosest, newest, highest-severity, business, technical or numerically closest precedence.
- Distinct-context coexistence must not be mislabeled conflict.
- Conflict in one criterion does not erase resolved results in unrelated dimensions.
- Composite AND/OR/conditional rule semantics must be explicit rather than inferred from multiple records.
- Authority resolution can select standing; it does not change current evidence.

## Non-goals

- authority/precedence governance itself;
- overall-health aggregation;
- workflow for resolving conflicts.