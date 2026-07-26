# Specify v1.1 Evaluation

## Method

The v1.1 candidate was compared with the published v1.0.0 skill snapshot (`96dc7683d517eb8903dc6df3c0280d3883eeb3de`).

- Three realistic prompts were run in fresh contexts against both skill versions.
- The cases tested mixed prose/visual transformation, a solution-first mini-spec, and strict review-only behavior.
- An independent grader received anonymized A/B outputs, six assertions per case, and a holistic rubric.
- The rubric scored usefulness per token, intent preservation, provenance, non-fabrication, proportionality, and implementation readiness.
- A separate blind evaluator judged the old and new descriptions against 20 realistic trigger queries: 10 positive and 10 difficult near-miss negatives.

The comparison emphasized aggregate quality rather than case-win count. A version can narrowly lose a case while still being more concise, passing more explicit assertions, and scoring better overall.

## Output-quality results

| Evaluation | Old assertions | New assertions | Old words | New words | Old holistic mean | New holistic mean |
|---|---:|---:|---:|---:|---:|---:|
| Mixed-artifact transform | 5/6 | 6/6 | 2,528 | 1,772 | 3.83 | 4.83 |
| Solution-first mini-spec | 6/6 | 6/6 | 1,635 | 1,011 | 4.83 | 4.67 |
| Review-only mode | 6/6 | 6/6 | 536 | 544 | 5.00 | 4.83 |
| **Overall** | **17/18** | **18/18** | **4,699** | **3,327** | **4.55** | **4.78** |

The v1.1 candidate used **29.2% fewer words**, passed every explicit assertion, and improved the aggregate holistic score. Its largest gain was the mixed-artifact case: it preserved source intent and visual ambiguity while meeting the mini-spec ceiling that v1.0.0 exceeded.

Two v1.0.0 outputs won narrow case-level preferences. The mini-spec baseline offered more implementation scaffolding, and the review baseline used stronger source locations. The v1.1 workflow intentionally avoids decomposing unresolved work, but it was updated to require stable headings or line ranges for review findings where available.

## Trigger results

| Description | True positives | True negatives | False positives | False negatives | Accuracy | Precision | Recall |
|---|---:|---:|---:|---:|---:|---:|---:|
| v1.0.0 | 10 | 4 | 6 | 0 | 70% | 62.5% | 100% |
| v1.1 candidate | 10 | 10 | 0 | 0 | 100% | 100% | 100% |

Both descriptions covered all intended specification tasks. The v1.0.0 description over-triggered on accepted-spec implementation, RFC summarization, mechanical diagram rendering, ADR explanation, sprint administration, and migration execution. The v1.1 boundary preserved recall while excluding straightforward coding, debugging, explanation, and execution-only work.

## Limitations

- This was an initial three-case comparison, not a variance study across repeated runs and models.
- Assertions combine mechanical checks, such as word counts, with independent semantic grading.
- The trigger test used an independent blind evaluator rather than the Claude host classifier because the local Claude CLI OAuth session had expired.
- Human preference still matters for how much implementation scaffolding a team wants in a not-ready mini-spec.

The repository retains six output-quality cases, 36 assertions, 20 trigger cases, and deterministic schema/path checks so later iterations can broaden the sample and measure variance.
