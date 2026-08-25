# Group 07 Scenario Review — EBR07-01–EBR07-64

All scenarios pass the Group 07 Explanation/replay/basis/disclosure source-contract boundaries.

| ID | Scenario | Required result |
|---|---|---|
| EBR07-01 | Statement renders a friendly source name only | Internal basis still binds exact source object/event identity |
| EBR07-02 | Source object renamed after incident | Current name does not replace historical identity; crosswalk required |
| EBR07-03 | Two basis rows derive from one vendor event | Preserve common derivation; no double corroboration |
| EBR07-04 | Same source supports one statement and limits another | Basis role remains statement-relative |
| EBR07-05 | Event timestamp precedes K but source published after K | Exclude from as-known-at-K; allow current retrospective use |
| EBR07-06 | Source exposes received timestamp after K | Late evidence remains late; no backfill |
| EBR07-07 | Old event retrieved today with no availability history | Earlier-K eligibility unresolved |
| EBR07-08 | Historical source record corrected today | Current retrospective may change; earlier as-known state preserved |
| EBR07-09 | Correction includes explicit supersession chain | Preserve predecessor/successor source state and timing |
| EBR07-10 | Current table shows only latest row | Do not reconstruct earlier state absent history |
| EBR07-11 | Databricks SCD2 config row available at incident time | Historical configuration conditionally reconstructible |
| EBR07-12 | SCD2 intermediate records aged out but latest survives | Do not infer missing intermediate configuration history |
| EBR07-13 | Query history row has statement ID but text blank due CMK | Execution basis inspectable; exact query text unavailable |
| EBR07-14 | Query statement text is truncated | Preserve truncation limitation; do not reconstruct omitted text |
| EBR07-15 | Query parameter payload marked truncated | Parameter-dependent proposition remains limited |
| EBR07-16 | Query text contains sensitive customer identifier | Internal basis may retain; visible basis separately authorized/minimized |
| EBR07-17 | Query actor email is visible to admin | Admin availability does not grant audience disclosure |
| EBR07-18 | System table record absent minutes after event | Treat source lag as possible limitation, not negative fact |
| EBR07-19 | Databricks alert evaluation says notification delivered | Delivery proposition supported; exact rendered message unresolved |
| EBR07-20 | Alert config revision at evaluation time is retained | Alert-definition-at-time can be reconstructed |
| EBR07-21 | Alert delivery succeeded but no message archive exists | Actual exact communication content remains unavailable |
| EBR07-22 | Email archive retains exact alert body and recipient | Actual communication can be established for that delivery context |
| EBR07-23 | Recipient deletes email after delivery | Delivery may remain evidenced; retained exact communication may be lost |
| EBR07-24 | Dashboard snapshot sent but content archive absent | Delivery only; no exact retained Explanation content |
| EBR07-25 | Reconstruction exactly matches remembered message | Similarity does not make reconstruction authentic communication |
| EBR07-26 | Historical communication snapshot exists | Treat as evidence of actual prior communication, not timeless source truth |
| EBR07-27 | Snapshot omits basis due audience restriction | Preserve actual prior projection; do not assume raw basis was shown |
| EBR07-28 | Current source correction contradicts old snapshot | Old communication remains authentic historical communication; current truth may differ |
| EBR07-29 | No snapshot exists | Report retained communication unavailable; reconstruction separately labeled |
| EBR07-30 | GitHub issue comment currently contains incident conclusion | Current comment content supported; prior versions require edit history |
| EBR07-31 | GitHub comment was edited once and history survives | Historical revision can support retained communication at that edit cut |
| EBR07-32 | Sensitive GitHub comment revision was deleted from history | Exact deleted revision content unavailable |
| EBR07-33 | GitHub comment exceeds 100 edits | Old intermediate revisions beyond retained cap cannot be assumed available |
| EBR07-34 | GitHub enterprise audit event is 150 days old | Ordinary audit replay can be available within documented window |
| EBR07-35 | Git event is 30 days old with no external stream | Native Git audit event unavailable; no reconstruction by convenience |
| EBR07-36 | Audit stream retained Git event externally | Long-horizon event can be supported by retained export |
| EBR07-37 | Audit stream delivers duplicate event | Deduplicate/common-derivation; no independent corroboration |
| EBR07-38 | Collibra asset description changed and history enabled | Historical semantic value can be supported where logged |
| EBR07-39 | Collibra edit represented as delete + create | Preserve source semantics; do not infer two independent changes |
| EBR07-40 | Collibra inherited responsibility changed | Resource history gap retained; do not claim full responsibility replay |
| EBR07-41 | Collibra attribute has History Enabled=false | Historical attribute value unsupported from that history surface |
| EBR07-42 | User lacks Collibra View permission | Hidden resource/history is restricted/observer-relative, not absent |
| EBR07-43 | Immuta query audit record exists within 90 days | Query/policy basis conditionally inspectable |
| EBR07-44 | Immuta query audit older than native retention, no export | Historical basis unavailable from native source |
| EBR07-45 | Immuta UAM export retained old query event | Long-horizon replay can use retained export with provenance |
| EBR07-46 | Immuta Spark user not registered under integration semantics | Missing audit is coverage limitation, not no access |
| EBR07-47 | Immuta UC integration filters transformation-query patterns | Missing transformed query event cannot support universal absence |
| EBR07-48 | Current requester may see conclusion but not query text | Show authorized conclusion; basis detail remains restricted |
| EBR07-49 | Current requester may inspect coarse provenance only | Provide coarse source class/status without exact hidden payload |
| EBR07-50 | Even source existence is restricted | Do not reveal hidden-source count/type; retain material limitation internally |
| EBR07-51 | Hidden limitation materially narrows conclusion | Narrow/withhold visible statement rather than hiding limitation |
| EBR07-52 | Redaction merges two distinct consumers into one label | Reject projection if it changes proposition/population scope |
| EBR07-53 | Historical operator could view basis but current requester cannot | Historical access does not grant current `inspectBasis` |
| EBR07-54 | Current requester gains access today | Current projection can broaden; earlier retained snapshot stays unchanged |
| EBR07-55 | Current requester loses access today | Current projection narrows; historical communication is not erased |
| EBR07-56 | Source expires but citation/reference survives | Reference can remain visible while exact basis retrieval is unavailable |
| EBR07-57 | One subquestion has expired history; another remains supported | Return trustworthy partial answer with unresolved sibling explicit |
| EBR07-58 | Source outage blocks one basis family | Preserve surviving statements; outage is a limitation, not negative truth |
| EBR07-59 | New independent basis arrives with same source status | Basis enrichment only; no automatic status/confidence strengthening |
| EBR07-60 | New contradictory basis changes source-owned status | Record status/basis delta through owning semantics, not Explanation-owned truth |
| EBR07-61 | Current projection hides a previously visible basis item | Authorization delta, not source-truth delta |
| EBR07-62 | Compare incident-time vs current view with richer current retention | Record source/basis availability difference separately from truth change |
| EBR07-63 | Compare two sides with different source coverage | Do not claim same-proposition status delta until each side is independently supportable |
| EBR07-64 | Full replay asks source truth, as-known answer, actual message and current retrospective answer | Produce four separately labeled views; missing retained communication remains missing |

**Result:** EBR07-01–EBR07-64 PASS.
