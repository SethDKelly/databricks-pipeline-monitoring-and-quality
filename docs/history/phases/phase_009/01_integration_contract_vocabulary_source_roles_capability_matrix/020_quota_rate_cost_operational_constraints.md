# INTG-020 — Quota, Rate, Cost & Operational Constraints

Where material, a capability records rate limits, quotas, query/compute/API cost characteristics, pagination/volume limits, export constraints and other operational limits that can affect feasible coverage or latency.

Cost and quota do not change truth semantics. If an operating constraint forces sampling, delayed collection or reduced coverage, the capability/support result must reflect that loss explicitly.

Phase 009 records the constraint; Phase 010 decides architecture and mitigation.