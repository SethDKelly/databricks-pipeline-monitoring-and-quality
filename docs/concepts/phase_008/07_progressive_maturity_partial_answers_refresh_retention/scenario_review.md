# Group 07 Scenario Review — PMR07-01–PMR07-44

**Result:** PASS

| ID | Scenario | Required result |
|---|---|---|
| PMR07-01 | Health answer available while RCA pending | Emit bounded health answer; cause unresolved |
| PMR07-02 | One compound subquestion unavailable | Answer siblings independently |
| PMR07-03 | Later RCA evidence arrives | Refresh only affected causal statements |
| PMR07-04 | Ten minutes pass with no new evidence | No epistemic maturation |
| PMR07-05 | Same answer recomposed with different wording | Presentation-only/no-op delta |
| PMR07-06 | New independent corroboration, same status | Basis enriched; status unchanged |
| PMR07-07 | Duplicate telemetry arrives | No independent-confidence gain |
| PMR07-08 | New contradiction makes evidence conflicting | Source conflict visible after re-evaluation |
| PMR07-09 | Supported causal claim becomes confirmed | Only source-governed transition may say confirmed |
| PMR07-10 | Supported claim simply ages | Remains supported |
| PMR07-11 | Confirmed claim later challenged | Preserve prior snapshot; current source state may revise |
| PMR07-12 | Observation corrected | Re-evaluate dependent Assessment/derived statements |
| PMR07-13 | Correction irrelevant to answer | Statement remains unchanged |
| PMR07-14 | Derived statement has one changed dependency | Re-evaluate exact join; no automatic reversal |
| PMR07-15 | Sibling statement changes | Unrelated siblings need not change |
| PMR07-16 | Same proposition rendered more concisely | Statement identity stable |
| PMR07-17 | Event window changes | New proposition/comparison, not simple refresh |
| PMR07-18 | Knowledge cut changes | New temporal proposition |
| PMR07-19 | Population scope expands | New scoped proposition; prior result not silently broadened |
| PMR07-20 | Statement becomes immaterial to question | Remove from current composition without declaring false |
| PMR07-21 | Statement source result becomes false/rejected | Record source-status revision distinctly from omission |
| PMR07-22 | Authorization expands exact metric visibility | Newly visible detail; source truth unchanged |
| PMR07-23 | Authorization expands basis only | `inspectBasis` broadens; conclusion unchanged |
| PMR07-24 | Authorization revoked for one statement | Current projection narrows; internal truth unchanged |
| PMR07-25 | Revocation hides limitation required for safe headline | Narrow/withhold conclusion, do not overstate |
| PMR07-26 | Current user gains access to old restricted detail | Current replay may enrich; old retained snapshot unchanged |
| PMR07-27 | Current user loses access to prior visible detail | Present projection narrows; prior communication record remains |
| PMR07-28 | Retained snapshot exists | Can state what was actually communicated then |
| PMR07-29 | No retained snapshot, historical sources available | Reconstruct only; do not claim exact prior communication |
| PMR07-30 | Current source truth differs from retained statement | Preserve historical communication + current correction |
| PMR07-31 | Prior answer was valid under then-known evidence | Do not call it retrospectively certain/false by recency alone |
| PMR07-32 | High-consequence communication retracted | Preserve release/retraction history; truth governed separately |
| PMR07-33 | Partial answer gains one newly answered subquestion | Add bounded statement; no global completeness score |
| PMR07-34 | Three of four subquestions answered | Do not compute 75% answer confidence/completeness |
| PMR07-35 | Answer loses one subquestion to new conflict | Current coverage narrows explicitly |
| PMR07-36 | New limitation only | Refresh if limitation materially constrains visible answer |
| PMR07-37 | New evidence changes basis but not visible answer | Internal delta may be material without stronger headline |
| PMR07-38 | New evidence remains restricted | No hidden-evidence strengthening; projection may remain unchanged |
| PMR07-39 | Query repeated across audiences | Different projection deltas may occur over one truth |
| PMR07-40 | Notification says `confidence improved` only because time passed | Reject wording |
| PMR07-41 | Notification says supported→confirmed after governed transition | Valid bounded change summary |
| PMR07-42 | Refresh produces identical semantics | Do not claim incident/status changed |
| PMR07-43 | Retained snapshot predecessor chain has a gap | Preserve gap; do not invent missing version |
| PMR07-44 | Historical/comparative handoff | Retained vs reconstructed vs current retrospective remain distinct |

All scenarios pass without a new concept, scalar maturity score or persistence architecture.
