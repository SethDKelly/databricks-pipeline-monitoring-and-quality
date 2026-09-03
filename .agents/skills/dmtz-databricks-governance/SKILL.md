---
name: dmtz-databricks-governance
description: Apply reviewed Unity Catalog governance/access guidance without conflating authentication, workspace privileges, Capability Authorization, Assertion Authority, evidence sufficiency, or DMTZ disclosure policy.
---

# DMTZ Databricks governance

## Human-directed boundary

Unity Catalog GRANT/REVOKE, ownership changes, external locations, storage credentials, connections, masks/filters or other governance mutations are A3 and require explicit task-specific authorization. A vendor skill cannot grant that permission.

## Workflow

1. Resolve applicable AUTH/REF/ARCH authority and authorization contracts first.
2. Read the reviewed `databricks-unity-catalog`, `databricks-core` and `databricks-dbsql` vendor skills when materialized.
3. Keep authentication distinct from Capability Authorization and Assertion Authority.
4. Treat Unity Catalog privileges/ownership as source/platform access-control evidence; map them into DMTZ only through an accepted authority/policy contract.
5. Keep requester visibility/disclosure separate from service processing permission and from historical truth.
6. Verify target-specific privilege behavior rather than assuming vendor-documented capability is enabled/configured in every workspace.
7. For changes, identify exact securable, principal, privilege, profile/workspace and rollback before execution.
8. Never place storage credentials, tokens or secret values into repository artifacts or prompts.

## Output expectations

State the platform privilege fact, DMTZ mapping basis, current authorization/disclosure implication if any, and explicit non-implications.

## Stop conditions

Stop before any unapproved governance mutation, secret handling, implicit profile selection, or mapping from platform privilege directly to DMTZ Assertion Authority without accepted policy evidence.
