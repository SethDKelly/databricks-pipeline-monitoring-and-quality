# EXPL-065 — `Affected` / `Unaffected` Aggregation & Coverage Question

**Status:** Accepted — Phase 008 Group 04

## Requirement

`Affected` is too broad to be a universal Impact state. Resolve whether the request means exposed, observed effect, consequence, or causally attributed consequence.

For multi-consumer answers, preserve consumer/path-specific states. One exposed consumer can establish `at least one exposed`; one safe consumer cannot establish `nobody affected`.

Strong `none`, `all`, `only`, or count/coverage claims require the exact bounded population and sufficient coverage.