# Worked Mini-Spec Example

Use this example to resist template gravity. It demonstrates a rigorous **not-ready** response when the request is solution-first and lacks evidence. Adapt the reasoning; do not copy caching-specific requirements into unrelated work.

## Input

> Add Redis so the dashboard is fast. Cache results for a while. Ship behind a flag and test it.

## Output

# Dashboard response-time improvement

**Status:** Not ready — product measurements and repository evidence are unresolved.
**Decision owner / acceptance authority:** `[BLOCKING: product owner for freshness and performance; technical owner after repository inspection]`

## Decision summary

The dashboard reportedly responds too slowly, but no baseline workload or accepted latency objective is supplied. Redis is a candidate, not an accepted requirement. Select an approach only after measuring the current path and comparing caching with query, indexing, batching, and precomputation improvements.

## Context and evidence

| Claim | Evidence | Confidence | Implication |
|---|---|---:|---|
| Dashboard performance is unacceptable | Original proposal only | Low | Establish affected journey and baseline before selecting a design |
| Redis addresses the bottleneck | No profiling or repository evidence | Low | Treat Redis as an option, not a fixed constraint |

## Goals / non-goals

**Goals**

- Improve the measured response time of the agreed dashboard journey under a representative workload.
- Preserve correctness, authorisation boundaries, and approved freshness semantics.
- Permit controlled enablement and rollback.

**Non-goals**

- Replacing unrelated storage or caching systems.
- Changing dashboard-visible business semantics.
- Selecting Redis before the bottleneck and alternatives are evaluated.

## Requirements and acceptance

- **FR-CACHE:** When optimisation is enabled, an eligible request must return a result consistent with approved freshness and authorisation rules.
- **FR-BYPASS:** Operators must be able to disable or bypass the optimisation without deploying a new build.
- **SEC-ISOLATION:** Results must not be reused across tenant, user, role, or permission boundaries unless equivalence is explicitly established and tested.
- **DATA-FRESHNESS:** Expiration and invalidation must implement `[BLOCKING: product-approved freshness rule]`.
  **Pass:** tests cover fresh, permitted-stale, invalidated, and bypass behaviour.
- **OPS-DEGRADED:** If an optimisation dependency is unavailable, the dashboard must follow `[BLOCKING: approved fallback behaviour]` without returning unauthorised or malformed data or causing unbounded source load.
- **QR-LATENCY:** Under `[BLOCKING: representative workload and reference environment]`, the dashboard must meet `[BLOCKING: approved latency target and measurement method]`.
- **QR-CORRECTNESS:** Optimised and unoptimised paths must produce equivalent authorised results except where the approved freshness policy permits a difference.

## Proposed design and alternatives

Evaluate:

- optimise the existing query or indexes;
- remove duplicate requests or batch work;
- precompute/materialise dashboard data;
- use an existing application cache;
- add Redis;
- retain the current implementation if evidence does not justify complexity.

Select the simplest option satisfying accepted requirements. Record operating cost, key composition, sensitive-data handling, invalidation, stampede control, stale-data behaviour, dependency failure, cache bypass, and repository fit.

## Risks, rollout, and rollback

- Risks: stale results, cross-user leakage, key collision, cache stampede, excess source load, sensitive-data retention, and disagreement between paths.
- Roll out using `[DELEGATED: established feature-control mechanism found during repository inspection]`.
- Compare cohorts using approved latency, error, fallback, staleness, source-load, and result-equivalence signals.
- Roll back by disabling the optimisation. Decide whether cached data requires deletion or may expire before rollout approval.

## Verification

Required evidence:

- profiling/tracing identifying the bottleneck;
- tests for eligibility, key composition, expiration, invalidation, stampede mitigation, bypass, and fallback;
- integration tests for hit, miss, dependency failure, and authorisation isolation;
- result-equivalence tests;
- workload validation against the approved target;
- rollout and rollback validation.

Exact paths and commands remain **blocking until repository inspection**.

## Open questions

- **Blocking:** Which journey and users are affected?
- **Blocking:** What baseline, workload, environment, metric, and target define success?
- **Blocking:** How stale may each datum be, and which events require invalidation?
- **Blocking:** What happens when the optimisation dependency fails?
- **Delegated:** Profile the implementation and compare options using repository evidence.
- **Delegated:** Identify existing feature-control, telemetry, and test conventions.

## Implementation slices

Do not authorise implementation. After blockers resolve:

1. **TASK-MEASURE:** Establish repository-grounded baseline and bottleneck evidence.
2. **TASK-DECIDE:** Compare options and record the selected design.
3. **TASK-CONTRACT:** Add correctness, isolation, freshness, and degraded-behaviour tests.
4. **TASK-IMPLEMENT:** Implement the selected option behind established control.
5. **TASK-VALIDATE:** Exercise rollout and rollback using the approved measurement method.

## Why this example is small but rigorous

It omits irrelevant full-template sections, uses explicit placeholders instead of fabricated facts, removes an unvalidated mechanism from the requirement, preserves decision ownership, defines testable contracts, and refuses implementation until product and repository evidence exist.
