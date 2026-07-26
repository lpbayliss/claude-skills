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

## Post-comparison readiness-boundary validation

An independent domain review of the initial candidate found three release-blocking semantic gaps: artifact lifecycle and implementation readiness were conflated, not-ready discovery work could be mislabeled as implementation slices, and the eval suite had no positive readiness cases. The workflow, template, checklist, example, and eval suite were repaired together. A fresh independent re-review returned **Ready** with no semantic regression.

Five positive and boundary cases were then run in fresh contexts against the repaired skill:

| Evaluation | Assertions | Words | Boundary exercised |
|---|---:|---:|---|
| Accepted repository issue contract | 6/6 | 298 | `Ready` for an exact low-risk code/test scope |
| Conditional implementation scope | 6/6 | 339 | Coding may start; a post-implementation smoke result still gates release |
| Accepted greenfield bootstrap | 6/6 | 460 | User-authorized future paths are not reported as observed files |
| Accepted roll-forward update | 6/6 | 731 | Artifact remains Accepted while revocation is separately `Not ready` pending evidence |
| Bounded architecture spike | 6/6 | 740 | `Ready` for evidence gathering and `Not ready` for product implementation |
| **Overall** | **30/30** | **2,568** | Five distinct readiness boundaries |

Independent graders passed all 30 assertions. Across the four scored compact/boundary outputs, readiness semantics and non-fabrication averaged 5.0/5; proportionality averaged 4.5/5. The roll-forward update received a separate six-assertion pass.

## Limitations

- The blind A/B comparison covered three cases, and the repaired-skill follow-up covered five single runs; neither is a variance study across repeated runs and models.
- Assertions combine mechanical checks, such as word counts, with independent semantic grading.
- The trigger test used an independent blind evaluator rather than the Claude host classifier because the local Claude CLI OAuth session had expired.
- Human preference still matters for how much implementation scaffolding a team wants in a not-ready mini-spec.

The repository retains eleven output-quality cases, 66 assertions, 20 trigger cases, and deterministic schema, path, and eval-category checks so later iterations can broaden the executed sample and measure variance.
