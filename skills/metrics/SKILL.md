---
name: metrics
description: Identifies, defines, implements, and verifies actionable software, product, delivery, reliability, and AI-system metrics. Use when the user asks what to measure, wants KPIs or a measurement plan, needs telemetry or instrumentation added to a repository, wants a dashboard or alert metric designed, or mentions funnels, adoption, retention, SLIs/SLOs, DORA metrics, experiment guardrails, evaluation metrics, metric quality, or cardinality. Also use when existing metrics are misleading, unactionable, expensive, privacy-sensitive, or inconsistent. Do not use for a one-off arithmetic calculation or for logs/traces when no metric or measurement decision is involved.
license: MIT
compatibility: Designed for Claude Code and compatible Agent Skills clients; implementation requires repository file/search and execution tools.
metadata:
  author: lpbayliss
  version: "0.1.0"
---

# Metrics Workflow

Create the smallest trustworthy measurement system that supports a real decision. A metric is useful only when its meaning, source, quality, and response are clear.

When the user asks to **add, create, instrument, or implement** metrics in a repository, carry the work through code, tests, and local verification. When they ask **what to measure**, stop at a decision-ready measurement plan unless implementation is also requested.

## Non-negotiables

- Start from the decision or behaviour the metric must inform; do not begin with available fields or a generic KPI catalogue.
- Inspect the current code, schemas, telemetry stack, naming conventions, dashboards, tests, privacy rules, and deployment path before proposing repository-specific instrumentation.
- Do not invent baselines, targets, event semantics, user consent, data availability, or causal claims.
- Define the population, numerator, denominator, time basis, aggregation, dimensions, exclusions, and owner before treating a metric as implementation-ready.
- Prefer a small set of outcome, driver, and guardrail metrics over a large dashboard.
- Keep identifiers, free text, secrets, and unbounded values out of metric dimensions. Treat cardinality and privacy as design constraints.
- Verify emitted measurements and query semantics; compiling code is not evidence that a metric is correct.

## Choose a mode

| Mode | Use when | Default result |
|---|---|---|
| **Discover** | The user needs to know what to measure | Metric tree and prioritized contracts |
| **Audit** | Existing metrics may be wrong, noisy, costly, or unactionable | Findings, corrected definitions, and migration plan |
| **Implement** | The user asks to add or create metrics | Working instrumentation, tests, queries/config where in scope, and verification evidence |
| **Diagnose** | A metric changed or disagrees with reality | Semantic/data-path investigation and evidence-backed explanation |

Modes may be combined. Use Discover before Implement when metric semantics are not already accepted.

## Load only what is needed

- Read [metric contracts](references/metric-contracts.md) whenever defining or reviewing a metric.
- Read the [implementation guide](references/implementation-guide.md) for repository instrumentation, dashboards, alerts, or metric migrations.
- Read [framework selection](references/framework-selection.md) only when choosing metrics across product, reliability, delivery, experiments, or AI systems.

## Execution loop

Track multi-step work, but report results rather than process narration:

- [ ] Frame the decision and scope
- [ ] Inspect evidence and the measurement path
- [ ] Select the smallest useful metric set
- [ ] Write implementation-ready contracts
- [ ] Implement through the existing stack when requested
- [ ] Verify semantics, emission, aggregation, and operational use

### 1. Frame the decision

Identify:

- the decision, behaviour, or risk this measurement should inform;
- the entity and population being measured;
- who owns the metric and what action they can take;
- required freshness and decision cadence;
- whether the request is exploratory, reporting, operational alerting, experimentation, or evaluation;
- whether implementation is requested.

Ask only when a missing answer materially changes semantics, privacy, safety, cost, or the implementation boundary. Otherwise proceed with a clearly labelled assumption or unresolved field.

A target is not required to begin measurement. If no accepted target exists, establish a baseline and decision rule without fabricating a threshold.

### 2. Inspect evidence and the measurement path

For repository work, inspect local instructions and find the actual path from source event to consumption:

```text
user/system behaviour → instrumentation point → SDK/collector → transport → storage → query → dashboard/alert/decision
```

Locate existing telemetry initialization, wrappers, semantic conventions, event schemas, analytics code, tests, dashboard or alert configuration, sampling, retention, and deployment controls. Reuse the established stack unless there is evidence it cannot express the metric safely.

For an existing metric, trace the current definition end to end. Compare code, warehouse/query logic, dashboard labels, and human interpretation; naming agreement alone does not prove semantic agreement.

Record evidence with exact paths, symbols, queries, or authoritative URLs. Mark inaccessible stages as unverified.

### 3. Select the smallest useful metric set

Build a compact metric tree:

1. **Outcome** — whether the desired user or system result occurred.
2. **Drivers** — controllable behaviours or system properties expected to influence the outcome.
3. **Guardrails** — harms, regressions, cost, reliability, fairness, or quality that must not worsen.
4. **Diagnostics** — dimensions or supporting measurements needed to explain movement; add only when they change an investigation.

Prioritize each candidate using:

- **decision value** — will movement change a decision or action?
- **validity** — does it represent the intended construct?
- **feasibility** — can it be measured reliably with available data?
- **sensitivity** — can it detect meaningful change at the required cadence?
- **resistance to gaming** — what behaviour does optimization encourage?
- **cost and risk** — instrumentation, storage, cardinality, privacy, and operational burden.

Reject vanity metrics, duplicates, and measurements with no plausible response. Do not force one framework across every domain; use the framework reference only as a prompt for omissions.

### 4. Write implementation-ready contracts

Use the contract structure in [metric contracts](references/metric-contracts.md). Every implemented metric needs at least:

- stable name and plain-language intent;
- decision and owner;
- precise formula or instrument semantics;
- entity/population, inclusion and exclusion rules;
- time window, timestamp basis, aggregation, and late/duplicate handling where relevant;
- unit and allowed dimensions with bounded value sets;
- source and instrumentation point;
- data-quality checks and known limitations;
- interpretation, response, and target status (`accepted`, `baseline first`, or `unresolved`).

Distinguish counters, gauges, histograms/distributions, derived ratios, and business events. Avoid averaging percentiles, averaging averages without weights, or summing gauges whose semantics are not additive.

For ratios, define numerator and denominator from compatible populations and time bases. For latency or size distributions, retain distributions or histograms rather than only an average. For funnels, define ordering, identity, windows, retries, and re-entry. For experiments, define assignment unit, exposure, primary outcome, guardrails, and analysis population before instrumenting variants.

### 5. Implement through the existing stack

When implementation is requested and contracts are ready:

1. Create or reuse centrally defined instruments/events and naming helpers.
2. Instrument the authoritative transition, not every call site that happens to observe it.
3. Use semantic conventions already present in the repository or current authoritative conventions for the selected stack.
4. Keep dimensions bounded and non-sensitive. Prefer coarse status/reason enums over raw errors, paths, IDs, URLs, prompts, or arbitrary labels.
5. Preserve retry and idempotency semantics so attempts, successes, failures, and unique outcomes are not conflated.
6. Add tests at the lowest useful level plus an integration or local collection check when feasible.
7. Add recording rules, queries, dashboards, or alerts only when requested or already repository-managed. Keep the displayed label and query definition aligned with the contract.
8. Document rollout, compatibility, and removal of superseded metrics. Dual-publish only for a bounded migration with a comparison plan.

Do not silently introduce a new telemetry vendor or production dependency. If the repository lacks a measurement stack, present the smallest viable option and the decision required; implement it only after the user explicitly accepts that dependency and its operating/privacy implications.

### 6. Verify the result

Verification should cover the semantic and technical chain, proportionate to scope:

- **Definition:** formula and labels match the accepted contract.
- **Instrumentation:** expected paths emit once with correct values; failure/retry paths are tested.
- **Dimensions:** allowed values are bounded; sensitive and unique values are absent.
- **Aggregation:** reset, window, unit, bucket, denominator, missing-data, and duplicate behaviour are correct.
- **Pipeline:** a local/test collector or repository harness receives the measurement when available.
- **Consumption:** queries, dashboard labels, and alerts use the intended units and populations.
- **Quality:** invariants or reconciliation checks can detect drift.
- **Operational response:** owner and expected action are stated; alerts require an actionable human response.

Run the repository’s real format, lint, typecheck, and test commands for changed scope. Report the commands and observed outcomes. If end-to-end verification requires unavailable infrastructure, say exactly what was verified and what remains a rollout check.

## Default output

Keep the result proportional. For design-only work:

```markdown
## Measurement decision
[decision, scope, and why]

## Prioritized metrics
### `<metric_name>` — Outcome | Driver | Guardrail
- Decision/owner:
- Definition:
- Source/instrumentation:
- Dimensions:
- Quality/limitations:
- Response/target status:

## Rejected candidates
[only meaningful rejections]

## Next evidence
[baseline, implementation, or owner decision]
```

For implementation work, lead with what changed, then include the finalized contracts, files changed, verification evidence, and unresolved rollout checks.

## Gotchas

- A convenient proxy can become detached from the outcome it represents; pair it with an outcome or guardrail and state the limitation.
- Metric names are not definitions. `active_user`, `failure`, and `latency` are ambiguous without contracts.
- More dimensions improve slicing but increase cost, privacy exposure, sparse series, and false discoveries.
- Missing data is not zero. Retries are not unique users. Requests are not outcomes. Correlation is not causation.
- Dashboard availability does not make a metric actionable; someone must own the decision it informs.
- Alerts should reflect user-visible symptoms or imminent exhaustion and require a clear response; dashboards can carry broader diagnostics.
- Targets change incentives. Baseline first when the accepted threshold is unknown.
