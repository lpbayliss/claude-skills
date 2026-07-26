# Specification Review Checklist

Use this as a risk-based review, not a form-filling exercise. Score `0 absent`, `1 weak/implicit`, `2 clear`, `3 strong and evidenced` where a score is useful.

## Problem and scope

- [ ] The problem is supported by evidence and is stated independently of the proposed solution.
- [ ] Primary users, stakeholders, operators, and maintainers are identified.
- [ ] Goals are observable outcomes.
- [ ] Non-goals exclude plausible adjacent scope.
- [ ] Success measures have a basis, owner, method, and timeframe.
- [ ] Constraints and key terms are explicit.

## Requirements

- [ ] Each consequential requirement has a stable ID.
- [ ] Each requirement is necessary and traces to a need, risk, or constraint.
- [ ] Each statement contains one obligation.
- [ ] Actors, conditions, behaviours, objects, and limits are unambiguous.
- [ ] Numeric thresholds include measurement method and reference environment.
- [ ] Mandatory requirements have objective verification and pass conditions.
- [ ] The set is consistent, prioritised, non-duplicative, and complete for the current decision.
- [ ] Normative MUST/SHOULD/MAY terms are used consistently if adopted.

## Behaviour and boundaries

- [ ] Primary, alternate, error, cancellation, and recovery flows are covered.
- [ ] Concurrency, ordering, retries, idempotency, timeouts, and backpressure are covered where relevant.
- [ ] Lifecycle, import/export, deletion, migration, upgrade, and compatibility behaviour is covered.
- [ ] System, trust, data, and ownership boundaries are explicit.
- [ ] Sources of truth and data owners are named.
- [ ] Invariants and forbidden outcomes are explicit.

## Design and decisions

- [ ] The simplest credible solution was considered.
- [ ] Components have clear responsibilities and interfaces.
- [ ] Runtime flows and failure/degraded behaviour are understandable.
- [ ] Credible alternatives, drawbacks, and status quo are assessed fairly.
- [ ] Selected trade-offs map to goals and quality scenarios.
- [ ] Consequential decisions are captured or linked as ADRs.
- [ ] Assumptions have confidence, validation method, owner, and deadline.

## Quality, security, and operations

- [ ] Performance/capacity targets use defined workloads.
- [ ] Availability, durability, recovery, and disaster scenarios are proportionate to risk.
- [ ] Security requirements and threat boundaries are explicit.
- [ ] Privacy, data classification, retention, deletion, residency, and audit needs are covered.
- [ ] Accessibility and usability obligations are covered where user-facing.
- [ ] SLOs/SLIs, telemetry, alerts, dashboards, runbooks, and operational ownership are defined.
- [ ] Dependencies, resource exhaustion, and graceful degradation are covered.

## Verification and delivery

- [ ] Every mandatory requirement maps to a planned verification method and observable pass condition.
- [ ] Evidence required before coding is distinguished from post-implementation results; planned checks are not reported as completed.
- [ ] Existing tests that must remain green are named.
- [ ] New unit, integration, contract, e2e, migration, performance, security, or resilience tests are specified as needed.
- [ ] Verification uses real repository commands and locations for the implementation scope being authorized.
- [ ] Enable/disable, rollout cohorts, and blast-radius controls are defined.
- [ ] Success, degradation, and rollback or recovery signals are objective.
- [ ] Data behaviour on rollback, recovery, or after the point of no return is defined.
- [ ] Upgrade/downgrade/version-skew paths are defined and tested where relevant.

## Agent readiness

- [ ] Repository instructions, patterns, tests, schemas, and generated boundaries were inspected.
- [ ] Exact paths are used; generic architecture guesses are absent.
- [ ] Fixed, preferred, and open decisions are distinguishable.
- [ ] Blocking, delegated, and deferred questions are classified.
- [ ] Readiness-resolution work is distinct from implementation slices and has evidence targets and decision rules.
- [ ] Implementation slices appear only for accepted scope and map to requirement IDs and objective verification.
- [ ] Tasks are independently verifiable and small enough to review.
- [ ] Parallel tasks have independent write sets; shared contracts have one owner.
- [ ] Stop/escalation conditions cover destructive, public-interface, security, privacy, and hard-to-rollback decisions.
- [ ] Independent review is planned for high-impact work.

## Lifecycle

- [ ] Owner, reviewers, advisory/blocking authority, artifact status, implementation-readiness verdict, and decision deadline are clear.
- [ ] `Conditionally ready` contains no gating approval, product decision, safety evidence, or mandatory specialist review required before starting the named scope; any later completion or rollout gate is explicit.
- [ ] The spec is version controlled or has an equivalent change history.
- [ ] Code, tasks, ADRs, tests, and rollout evidence can be traced.
- [ ] Maintenance, freshness, supersession, and archival rules are clear.

## Implementation-ready gate

Do not mark ready if any are true:

- a mandatory requirement lacks verification;
- a blocking question remains unresolved;
- product behaviour must still be invented during implementation;
- destructive migration, security/privacy boundary, or public API impact is undecided;
- production rollout has no containment and no accepted rollback or roll-forward/recovery strategy;
- exact repository context or verification commands required by the implementation scope being authorized are unknown;
- critical specialist review is missing.
