# AUTH-006 — Authority Revision, Correction, Supersession, and Time

**Status:** Accepted — Phase 005 Group 01

## Purpose

Preserve historical authority correctly when authority rules or authoritative assertions change.

## Distinctions

- **revision** — prospective change to an authority rule or authoritative assertion;
- **supersession** — prior state stops governing after an effective boundary and replacement/current state takes over;
- **correction** — later knowledge establishes that prior state/rule was wrong for some earlier effective interval;
- **retirement/end** — authority or assertion ceases without necessarily identifying a replacement;
- **late discovery** — evidence/rule existed earlier but becomes known to the framework later; this is not itself correction.

## Contract

Every material change preserves:

- prior assertion/rule identity;
- effective interval;
- recorded/knowledge time;
- relationship to revised/corrected/superseding state;
- provenance/basis.

Historical resolution uses the authority rules/assertions applicable to the effective-time question and known by the requested knowledge cutoff.

## Invariants

- Current authority does not overwrite historical authority.
- A prospective authority transfer does not make the successor authoritative before the transfer effective time.
- A correction may change today's retrospective resolution for an earlier interval while leaving an `as-known-then` resolution unchanged.
- Correction of an authority rule does not erase decisions/explanations that actually used the earlier rule.
- Later resolution of an authority conflict does not imply the conflict was resolved at the earlier knowledge cutoff.
- Source correction, authority-rule correction, assertion revision, and later precedence resolution remain distinguishable.
