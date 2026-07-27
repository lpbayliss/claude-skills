# Framework Selection

Frameworks are prompts for coverage, not substitutes for a metric contract. Select only the part that matches the decision.

## Product and user outcomes

Use an outcome/driver/guardrail tree for most product work.

Potential lenses:

- acquisition or eligible population;
- activation or first value;
- repeated value/retention;
- task success and quality;
- satisfaction or trust where measured validly;
- revenue/cost only where tied to the actual product decision;
- guardrails for reliability, abuse, privacy, support burden, or exclusion.

Avoid treating page views, raw signups, or time spent as success without evidence that they represent user value.

For funnels, define eligibility, ordering, identity, conversion window, retries, and re-entry. For cohorts, define cohort entry and observation maturity.

## Reliability and operations

For user-facing services, latency, traffic, errors, and saturation are useful starting lenses, not mandatory dashboard sections. Prefer service-level indicators tied to user-visible outcomes.

An SLI contract needs an event population, good-event criterion or distribution, measurement point, and window. An SLO target requires owner acceptance and should drive a response such as release policy, capacity work, or investigation. Do not manufacture SLOs from industry folklore.

Use symptom-based alerting for paging. Diagnostic resource metrics can support investigation without becoming page conditions.

## Software delivery

DORA-style software delivery measures can assess throughput and instability at a service/team system boundary. Define deploy, change, failure, recovery, and scope from local delivery semantics before calculating anything.

Do not use individual developer activity, commits, lines changed, tickets closed, or hours as productivity outcomes. They are easy to game and encourage local optimization.

Pair delivery measures with product/reliability outcomes when evaluating a process change; faster activity is not useful if value, stability, or team sustainability degrades.

## Experiments and causal questions

Before choosing metrics, define:

- hypothesis and intervention;
- randomization/assignment unit;
- eligibility and exposure;
- primary outcome and analysis window;
- guardrails;
- minimum detectable effect or decision rule when available;
- sample-ratio mismatch, novelty, interference, and attrition checks.

Instrumentation does not establish causality. If randomization is unavailable, label the analysis observational and identify confounding risks.

## AI and agent systems

Measure the task outcome before model internals. A useful compact set may include:

- task success or accepted outcome using a defined evaluator;
- quality dimensions and critical-failure rate;
- human intervention/escalation;
- end-to-end latency;
- cost/resource use per completed or accepted outcome;
- tool/API failure and retry behaviour;
- safety, privacy, or policy guardrails.

Define evaluator version, test-set composition, sample policy, judge calibration, and uncertainty. Separate offline benchmark scores from production outcomes. Track distribution and critical failures, not only a mean score.

For agentic workflows, distinguish attempts, turns, tool calls, completion, user acceptance, and durable task success. Token count or turn count alone is not quality.

## Business and financial metrics

Use accepted finance/domain definitions and authoritative source systems. Revenue, margin, churn, and lifetime value vary materially by accounting and cohort policy. If the owner has not fixed the definition, do not choose one silently; write the decision required.

## Selection test

For each proposed metric, ask:

1. What exact decision changes if this moves?
2. Could it move while the real outcome does not?
3. What harmful optimization could it encourage?
4. Is a paired outcome or guardrail needed?
5. Can the repository/data path measure it reliably and safely?
6. What is the smallest set that still distinguishes success from failure?
