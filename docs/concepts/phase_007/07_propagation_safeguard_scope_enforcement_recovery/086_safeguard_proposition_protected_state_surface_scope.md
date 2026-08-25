# OPS-086 — Safeguard Proposition: Protected State, Surface & Scope

**Status:** Accepted — Phase 007 Group 07

## Purpose

Bind every Propagation Safeguard to the exact thing it is intended to protect so control state cannot drift into a generic pipeline-wide `quarantined` flag.

## Contract

A safeguard proposition identifies, where material:

- protected/suspect output, version, state, missing-output/current-cycle context, or bounded condition;
- protection surface such as output publication, current-state presentation, consumer interface/path, downstream advancement, refresh opportunity, population/cohort or other bounded propagation surface;
- environment/consumer/region/cohort scope;
- effective protection interval;
- applicable historical Lineage/publication/consumption paths;
- originating rationale/evidence references;
- knowledge time and provenance.

The protected proposition may be narrower than an asset. One version, consumer path or cohort may be protected while another remains available.

## Invariants

- safeguard identity ≠ generic asset quarantine.
- protected subject ≠ every version/state of that subject.
- intended protection scope ≠ actual enforcement scope.
- suspect/protected ≠ defective.
- missing output is context for a held advancement/presentation boundary, not a quarantined nonexistent object.
