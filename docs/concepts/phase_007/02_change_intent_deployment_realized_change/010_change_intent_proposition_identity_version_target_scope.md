# OPS-010 — Change Intent Proposition Identity, Version & Target Scope

**Status:** Accepted — Phase 007 Group 02

## Purpose

Keep planned modification truth precise enough that later realization comparison does not silently compare a Deployment or realized Change against the wrong intent revision, target, facet or activation context.

## Contract

Every material Change Intent version must bind, where applicable:

- stable Change Intent identity plus explicit intent revision/version;
- identified target Entity Identity or bounded target set;
- environment/tenant/region/cohort/population/consumer or other context when material;
- intended change facet/type and functional description;
- intended implementation/reference state when known, without claiming it is deployed;
- planned activation time/window/condition when known;
- anticipated effects separately from the intended implementation modification;
- declared topology/schema/semantic/metric/reference implications where applicable;
- source revision/configuration/change-management references when known;
- registration/knowledge time, actor/source and provenance;
- authority/authorization context where applicable;
- revision, supersession and withdrawal history.

A multi-part intent must preserve independently comparable components when different targets/facets can realize at different times.

## Intent component

An **intent component** is a bounded planned proposition such as:

- activate transformation definition T2 for production C;
- enable configuration K7 for region East;
- replace source B1 with B2 for population P;
- add field `status_code` to consumer interface I;
- reduce the eligible C population by applying filter F.

Componentization is functional semantics, not an implementation requirement to store a separate object for every bullet.

## Invariants

- registration ≠ deployment attempt ≠ activation ≠ realized state;
- current intent revision does not erase prior intent revisions;
- intended implementation state ≠ anticipated downstream effect;
- planned activation time ≠ actual activation time;
- intent target scope does not silently broaden from one environment/cohort/population to all targets;
- anticipated effect does not become an Expectation, Baseline or Assessment;
- withdrawal ends prospective intent applicability but does not revert already active state;
- a Change Intent does not own a later realization/conformance status.

## Handoff

OPS-011 defines implementation-state references used to link intent and Deployment without equating repository revision with runtime identity. OPS-015 defines the derived intent-to-realization comparison.