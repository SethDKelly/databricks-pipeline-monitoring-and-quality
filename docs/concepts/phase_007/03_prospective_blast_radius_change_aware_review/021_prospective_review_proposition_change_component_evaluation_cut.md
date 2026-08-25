# OPS-021 — Prospective Review Proposition, Change Component & Evaluation Cut

**Status:** Accepted — Phase 007 Group 03

## Purpose

Bind every prospective blast-radius/change-aware review to the exact proposal and knowledge context being evaluated so a review cannot silently drift to the latest intent, current topology or a different rollout slice.

## Contract

A material prospective review binds, where applicable:

- exact Change Intent identity, revision and component under OPS-010;
- proposed changed subject/facet and before/proposed-state description;
- target environment/region/cohort/population/interface/consumer slice;
- planned activation/effective context when known;
- implementation-state references from OPS-011 when available;
- topology evaluation time and knowledge cut;
- authorized Lineage/proposed-topology view;
- review purpose/question and evaluation time.

The result is a **derived prospective review profile**, not a new truth-owning concept.

## Invariants

- latest intent revision is not substituted for the revision actually reviewed;
- one rollout slice is not silently generalized to another;
- planned activation time is not actual activation;
- review evaluation time is not proposed effective time;
- absent Change Intent/planned detail limits the prospective basis; it does not mean zero change risk;
- a code diff or deployment payload may supply evidence used to register/refine Change Intent, but must not become a shadow plan truth owner.

## Handoff

OPS-022 defines how effective Lineage and planned topology deltas form the scenario used for candidate discovery.