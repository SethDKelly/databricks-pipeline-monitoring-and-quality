# INTG-010 — Granularity, Cardinality & Context Binding

A capability states the grain at which evidence is produced: entity, field, metric, run, task, attempt, input/output version, query, consumer, path, cohort, control opportunity or other bounded unit.

Cardinality and aggregation behavior are explicit. Asset-level state cannot silently answer field-, consumer-, path- or run-specific questions.

The contract also records material environment/workspace/region/edition/profile/version/context bounds.

Aggregation can reduce detail but cannot create coverage, causality, exposure, health or authority not established at the underlying proposition grain.