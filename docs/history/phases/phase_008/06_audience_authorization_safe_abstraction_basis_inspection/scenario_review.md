# Phase 008 Group 06 Scenario Review

**Status:** PASS — AUD06-01–AUD06-44

| ID | Scenario | Required result |
|---|---|---|
| AUD06-01 | Analyst can see failed Assessment but not threshold | show outcome; hide threshold |
| AUD06-02 | Analyst can see metric category but not exact value | authorized coarse value only |
| AUD06-03 | Sensitive field identity restricted | preserve Assessment without naming field if valid/authorized |
| AUD06-04 | Business user sees supported cause, engineer sees evidence | same causal status |
| AUD06-05 | Confirmer identity restricted | confirmed status may remain visible if separately authorized |
| AUD06-06 | Consumer name restricted, exposure visible | coarse consumer/exposure projection only |
| AUD06-07 | Reachable consumer identity hidden | do not upgrade to affected/exposed |
| AUD06-08 | Restricted alternate path limits non-exposure | retain limitation or narrow/withhold global negative |
| AUD06-09 | Exact Lineage path hidden | no invented direct edge/path completeness |
| AUD06-10 | Policy applicability visible, policy text restricted | show applicability only |
| AUD06-11 | Classification itself restricted | safe handling context only if authorized |
| AUD06-12 | Responsibility team visible, person hidden | team-level projection |
| AUD06-13 | Gate override visible, operator hidden | control fact preserved without actor identity |
| AUD06-14 | Safeguard enforced, mechanism hidden | enforcement only; no prevention inference |
| AUD06-15 | Basis restricted but conclusion authorized | visible conclusion + allowed basis limitation |
| AUD06-16 | Conclusion restricted but basis item individually visible | do not synthesize/reveal restricted conclusion |
| AUD06-17 | Derived conclusion exists internally; basis partly hidden | disclose only if conclusion separately authorized |
| AUD06-18 | Hidden facts could imply a new coarse conclusion | Explanation may not invent inference |
| AUD06-19 | Opaque existence authorized | may say restricted evidence exists |
| AUD06-20 | Opaque existence not authorized | do not acknowledge exact hidden item |
| AUD06-21 | Redaction marker itself sensitive | safe non-disclosure permitted |
| AUD06-22 | `inspectBasis` exact evidence allowed | exact trace returned |
| AUD06-23 | `inspectBasis` only source class allowed | source class/status only |
| AUD06-24 | `inspectBasis` no basis disclosure allowed | safe non-disclosure; internal trace retained |
| AUD06-25 | Citation visible but raw source denied | citation does not grant source access |
| AUD06-26 | Restricted contradictory basis exists | headline cannot imply no contradiction if limitation material |
| AUD06-27 | Unknown exposure with hidden telemetry | remains unknown, not not-exposed |
| AUD06-28 | Unsupported causal claim hidden among supported sibling | visible sibling does not become confirmed/winner |
| AUD06-29 | Private inspection allowed; export denied | answer may be private only |
| AUD06-30 | Engineer requests client-facing export | client disclosure independently authorized |
| AUD06-31 | Requester has access; target audience does not | no delegated disclosure by possession |
| AUD06-32 | Audience label says executive but no entitlement | no permission from label |
| AUD06-33 | Multiple individually safe metrics reveal restricted count | mosaic risk limits projection |
| AUD06-34 | Repeated range queries reveal exact value | repeated-query/differencing risk retained |
| AUD06-35 | Business and engineering views same proposition | same polarity/status; detail may differ |
| AUD06-36 | Views have different authorized scope | scope difference explicit; not contradictory truth |
| AUD06-37 | Current access broadened after incident | current view can be richer; retained old Explanation unchanged |
| AUD06-38 | Current access revoked | retained historical communication may exist; current disclosure narrows |
| AUD06-39 | Historical analyst had raw access | does not grant current requester raw access |
| AUD06-40 | Current requester asks what analyst could know then | historical capability may be described only as currently authorized |
| AUD06-41 | Client-facing causal statement requires review | compose/view permission does not equal release permission |
| AUD06-42 | Communication approved despite unresolved evidence | approval cannot strengthen truth |
| AUD06-43 | Restricted limitation cannot itself be acknowledged | narrow/withhold conclusion rather than overstate |
| AUD06-44 | Full mixed-authority incident answer | each statement independently projected; no hidden-evidence leakage/global score |

**Result:** all scenarios pass without new concept or architecture selection.