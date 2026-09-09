# Phase 005 Group 06 Scenario Checks

All scenarios are synthetic.

## DISC-01 — Technical exact metric / business health summary
Engineer may see null rate `7.2%` and threshold `1%`; business user may see `completeness degraded` only. **PASS** — same Assessment, different authorized detail.

## DISC-02 — Threshold restricted while result visible
Requester may see `Expectation violated` but not the exact threshold. **PASS** — result visibility does not imply normative-basis visibility.

## DISC-03 — Opaque restricted upstream contributor
Requester may know a restricted upstream contributor materially supports the RCA but may not know its identity/path. **PASS** — opaque existence preserves reasoning continuity without declassification.

## DISC-04 — Existence itself restricted
Requester may not know that restricted consumer R exists. **PASS** — omit R without saying `no additional consumers exist`.

## DISC-05 — Supported causal claim in executive summary
Underlying claim is `supported`, not confirmed. **PASS** — executive summary may simplify rationale but must not say `root cause confirmed`.

## DISC-06 — Multiple contributors
Two compatible causal claims are supported. **PASS** — business summary cannot collapse them into one cause merely for readability.

## DISC-07 — Reachable versus exposed
Report R is reachable; consumption evidence is unavailable. **PASS** — disclose `potential downstream candidate; exposure unresolved`, not `affected report`.

## DISC-08 — Not exposed but stale
Report used V-1 while suspect V was blocked. **PASS** — `not exposed to V` can be disclosed while freshness remains separately stale.

## DISC-09 — Hold decision / enforcement unknown
Gate emitted HOLD but control-plane enforcement telemetry is missing. **PASS** — say `hold decision issued; enforcement unknown`, not `run blocked`.

## DISC-10 — Safeguard active without prevention proof
Safeguard was enforced but no relevant refresh opportunity existed. **PASS** — communicate `safeguard active; consumer not exposed`, not `exposure prevented`.

## DISC-11 — Waived violation
Observed metric violates ordinary threshold during an authorized waiver. **PASS** — disclosure preserves underlying violation plus waiver; no false clean pass.

## DISC-12 — Break-glass state visible / actor hidden
Audience may know emergency override occurred but not operator identity or bypass details. **PASS** — disclose authorized abstraction while retaining provenance internally.

## DISC-13 — Confirmed cause visible / confirmer hidden
Claim is validly confirmed; requester lacks access to confirmer identity/profile details. **PASS** — confirmed status may be shown without disclosing restricted confirmer metadata.

## DISC-14 — Human Annotation with restricted author
Authorized audience may see sanitized human context but not author identity. **PASS** — preserve that the source is human-provided context rather than machine evidence.

## DISC-15 — Client-facing causal communication requires review
Internal users may see a confirmed causal claim, but policy requires approval before client communication. **PASS** — view permission does not imply publish permission.

## DISC-16 — Communication approval cannot upgrade truth
Reviewer approves an externally worded summary while claim remains supported. **PASS** — approval cannot change claim to confirmed.

## DISC-17 — Mosaic leakage from counts/path length
Individually allowed facts uniquely identify a restricted consumer when combined. **PASS** — reduce/omit composite detail rather than treating each permitted item independently.

## DISC-18 — Repeated narrowing / differencing
Repeated aggregate queries could derive a restricted small population. **PASS** — inference risk is considered across query history/context; no technology selected.

## DISC-19 — Historical retained Explanation
Incident-time retained report said `cause unresolved`; later evidence confirms one contributor. **PASS** — retain the old communication and produce a later retrospective Explanation rather than rewriting it.

## DISC-20 — Historical disclosure broader than current access
A prior responder saw a restricted identity; current requester cannot. **PASS** — historical disclosure proves what that responder saw, but current projection redacts the identity.

## DISC-21 — Current access broader than historical access
Requester can inspect raw detail today but lacked that permission during the incident. **PASS** — current access does not rewrite historical authorization/disclosure.

## DISC-22 — Disclosure rules conflict
Two applicable disclosure authorities conflict and no resolver applies. **PASS** — disclosure state remains conflicting; do not publish by convenience or claim an explicit deny that did not exist.

## DISC-23 — Review service unavailable
Client-facing communication requires review, but review authority is unavailable. **PASS** — no approval is manufactured; product may withhold according to policy while recording unavailable state.

## DISC-24 — Policy Context without compliance certification
Applicable handling policy is visible. **PASS** — Explanation can state policy applicability without claiming compliance.

## DISC-25 — Authority conflict visible without authority-holder detail
Audience may see that the normative threshold is under authoritative conflict but not the identities/rules of the conflicting sources. **PASS** — conflict status survives opacity.

## DISC-26 — Audit audience is not universal access
Actor is labeled auditor. **PASS** — audit purpose may shape projection but does not bypass Capability Authorization.

## Exit result

All scenarios pass AUTH-044–AUTH-053 without a new Concept or disclosure-specific truth store.
