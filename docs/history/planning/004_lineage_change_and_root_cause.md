# 004 — Lineage, Change Attribution, and Root-Cause Reasoning

**Status:** Discovery input — refined/superseded where necessary by accepted Phase 002 concepts: Change Intent, Execution History, Deployment, Lineage, Change, Investigation, Causal Claim, and Impact.

## Goal

Turn Lineage and historical evidence into a structure for asking where a change may have originated and what may be exposed downstream without manufacturing causal certainty.

## Accepted conceptual refinements

- planned modification is **Change Intent**, not realized Change;
- Deployment attempt/activation is historical evidence, not cause;
- Lineage is typed/temporal and identifies relationship paths, not blame;
- realized Change describes what actually differed;
- Investigation organizes the inquiry;
- causal propositions are explicit **Causal Claims** with support/contradiction and epistemic status;
- multiple contributors/unresolved outcomes are valid;
- downstream Impact separates reachability, exposure, observed effect, and business consequence;
- quantitative attribution such as `4.2M rows from B` is a target reasoning pattern only when evidence can justify it, not a default product conclusion.

## Canonical example: A+B→C

If C falls materially, investigate whether A/B volume, freshness, schema, key quality/distribution, join match behavior, transformation logic, Change Intent, Deployment activation, upstream execution, or another condition changed.

The accepted model can represent:

- Observation of A/B/C and join behavior;
- Assessment against Expectations/Baselines;
- Change Intent versus realized Change;
- temporal Lineage and execution/Deployment context;
- competing Causal Claims;
- supporting and contradicting evidence;
- multiple contributors;
- downstream Impact candidates/exposure/effects;
- unresolved uncertainty.

## Causal discipline

The product may say a claim is proposed, supported, weakened, rejected, confirmed under an accepted standard, or unresolved. Correlation, topology, Deployment timing, and intent consistency are evidence/context but not automatic confirmation.

## Historical reasoning

Questions should distinguish effective/event time from recorded/knowledge time so a retrospective explanation can differ from what the team reasonably knew during the incident.

## Downstream reasoning

Lineage traversal creates candidates. Actual exposure requires consumption/version/timing evidence. Observed downstream degradation and business consequence remain stronger/different statements. If the origin is asserted to have caused a downstream effect, use Causal Claim semantics.

## Evidence chain

Potential evidence includes Change Intent, Deployment/Execution History, Observations/Assessments, Baselines/Expectations, Lineage, realized Change, semantic/governance context, and attributed Annotation.

This planning note is not the authoritative definition of those concepts; the Phase 002 specifications are.
