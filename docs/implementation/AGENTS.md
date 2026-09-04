# Implementation Agent / Developer Instructions

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-C; IN EXECUTION CKR-D; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

CKR-D is in execution; product implementation remains blocked until CKR-K.

Use `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` to select current semantic ownership, then root `AGENTS.md`, live CKR/implementation status, accepted ADF mechanics, and only then implementation/vendor guidance.

CKR-D candidates do not become current by path presence. `candidate_ready` means Phase 004/005 remain current authority for REF/AUTH/authority vocabulary until atomic cutover.

Do not create product source, schemas, product tests or deployment configuration as CKR work. Completing CKR-D does not authorize CKR-E.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
