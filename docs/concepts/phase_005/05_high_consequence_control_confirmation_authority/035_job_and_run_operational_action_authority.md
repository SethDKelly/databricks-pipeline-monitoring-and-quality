# AUTH-035 — Job and Run Operational Action Authority

**Status:** Accepted — Phase 005 Group 05

## Purpose

Separate permission to operate jobs/runs from raw-data access, analytical visibility, gate/safeguard authority, deployment authority, and other high-consequence actions.

## Contract

Job/run operational authorization should bind the exact action, such as:

- trigger/run-now;
- retry/restart/resume;
- cancel/terminate;
- pause/disable/resume scheduling where represented;
- modify a bounded operational setting where later supported;
- acknowledge/close an operational control request where separately governed.

The authorization should also bind target job/pipeline/run or bounded set, environment, reason/purpose where required, effective interval, approval conditions, and provenance.

## Invariants

- Permission to retry does not imply permission to cancel, modify, deploy, or change scheduling.
- Permission to operate a job does not imply raw-row or sensitive-column access.
- Raw-data access does not imply job-operation permission.
- Repository ownership, commit access, job creator identity, and platform administration do not silently imply every operational action.
- Job-operation authority does not imply Execution Gate or Propagation Safeguard authority.
- Permission to invoke a job action does not prove the action was accepted by the external runtime, executed, or succeeded.
- A retry/restart does not erase or mutate the original Execution History.
- Any code/configuration change that becomes a Deployment or Change remains governed by its own concept/state rather than being hidden inside `job operation`.

## Example

An incident responder may be allowed to retry failed Job C but denied access to C's rows and denied authority to override C's Execution Gate. The retry request and the resulting run remain separately evidenced.