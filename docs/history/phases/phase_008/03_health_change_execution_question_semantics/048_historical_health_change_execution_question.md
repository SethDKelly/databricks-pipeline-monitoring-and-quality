# EXPL-048 — Historical Health, Change & Execution Question

**Status:** Accepted — Phase 008 Group 03

## Requirement

Historical domain answers bind both event/effective time and, where requested, the knowledge cut.

Preserve:

**actual retained historical state ≠ as-known-at-cut reconstruction ≠ current retrospective interpretation**.

## Rules

- current health profile/Baseline/Expectation/Deployment/topology is not projected backward;
- later lifecycle/version/activation evidence may improve current retrospective reconstruction without becoming evidence known then;
- historical `unknown` remains historically accurate when the earlier cut lacked sufficient evidence;
- corrections/supersessions do not rewrite prior retained statements/actions;
- current requester disclosure remains separately constrained by current authorization.

A past-event question without an earlier knowledge cut remains current retrospective under EXPL-006.