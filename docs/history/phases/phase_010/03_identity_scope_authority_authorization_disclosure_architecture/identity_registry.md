# Phase 010 Group 03 — Identity Registry Architecture

## Purpose

Provide durable cross-system identity without replacing source identities or relying on names/timestamp proximity.

## Canonical entity record

Logical minimum fields:

- `tenant_id`;
- `entity_id` — framework durable UUID/opaque identifier;
- `entity_class` — dataset/table/view/pipeline/job/repository/environment/consumer/principal/etc.;
- `created_at_knowledge_time`;
- optional lifecycle/status metadata that does not replace source truth.

The record is intentionally small. Canonical identity does not need to duplicate every vendor attribute.

## Source identity binding

Each binding retains:

- `binding_id`;
- `tenant_id`;
- `entity_id`;
- source/capability-instance identity;
- source entity type;
- stable source-local identifier where available;
- source incarnation/version discriminator where needed;
- descriptive path/name history where useful;
- mapping assertion status: `provisional`, `verified`, `conflicting`, `superseded`, `unresolved`;
- assertion source/actor/rule;
- basis evidence IDs;
- effective interval;
- knowledge/persistence coordinates;
- supersession linkage.

## Identity-resolution rules

Strong mappings include source-native stable IDs and governed registration/crosswalk evidence. Weak matching signals such as equal names, path fragments, owners or timestamps can generate a candidate mapping but cannot silently create `verified` identity.

A deterministic transformation is valid only when its inputs and rule establish identity. For example, a repository numeric ID can preserve GitHub repository identity across rename; a repository path string alone cannot.

## Source lifecycle

Rename and move preserve canonical mapping only with continuity evidence. Delete/recreate can produce a new incarnation even if the visible path is reused. Historical bindings remain non-rewriting.

## Principal identities

Principal classes include:

- human;
- group/team;
- service principal;
- application;
- workload identity;
- external/unknown principal.

Each vendor-local principal retains upstream IdP provenance where known. Email or display-name equality is not cross-system principal proof.

Membership is modeled separately with source, effective interval and knowledge time. Current membership does not establish membership at an earlier authorization cut.

## Acting relationships

Run-as, impersonation, delegated action, app-on-behalf-of-user and managed-by relationships are explicit. They do not merge identities or automatically transfer Assertion Authority/Capability Authorization.

## Conflict behavior

Identity conflict blocks exact propositions that require the disputed association. Other statements that rely only on undisputed source-local identity can still proceed.

No identity confidence percentage is introduced.