# Active-Control Degradation & Failure Model

## Principle

The runtime must know the difference between **domain not-ready**, **evidence unsuitable**, **decision unavailable**, **delivery failed**, **enforcement unknown**, and **execution happened despite control**.

## Gate failure classes

- evidence/source unavailable or stale;
- criterion/rule resolution failure;
- authorization unresolved/denied;
- decision service unavailable;
- stale/mismatched decision;
- adapter authentication/permission failure;
- delivery timeout/throttle;
- enforcement rejection;
- enforcement accepted but later contradicted by actual execution;
- bypass/alternate trigger observed;
- multi-Gate conflict.

Each Gate profile explicitly maps eligible failure classes to governed behavior. `Unavailable` is not silently translated into ADMIT/HOLD.

## Safeguard failure classes

- target state/path identity unresolved;
- enforcement mechanism unavailable;
- partial cohort/path coverage;
- alternate path discovered after protection;
- enforcement response ambiguous;
- consumer encounter occurs despite protection;
- expiry/release uncertainty;
- recovery evidence insufficient.

## Model/search/reasoning degradation

Group 06 model/vector/search facilities cannot be a mandatory control-decision dependency. If optional model-assisted candidate work is unavailable, deterministic exact propositions and rules remain the control basis. If required deterministic evidence itself is unavailable, the Gate profile's explicit degraded-evidence policy applies.

## Historical truth

Recovery of the service today does not erase yesterday's unknown enforcement interval. Later logs may improve current retrospective interpretation only if they are valid evidence and availability-by-K is preserved.
