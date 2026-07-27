# Abstract and notes: adaptive thermal control for battery modules

## Draft abstract

Temperature imbalance accelerates degradation in high-power battery modules. We evaluated an adaptive controller that redistributes cooling flow using a reduced-order thermal model. In simulation across 24 synthetic drive cycles, the controller reduced peak cell-to-cell temperature difference by 18% relative to a fixed-flow baseline. In three benchtop module runs using one repeated drive cycle, the median reduction was 11%, with observed results ranging from 7% to 14%. Pump energy increased by 4% in those runs. No long-duration degradation, vehicle-level, extreme-ambient, or failure-injection testing has been completed. These results suggest adaptive flow allocation can reduce short-horizon temperature imbalance, but do not yet establish improved battery life or vehicle-level efficiency.

## Method notes

- Reduced-order model calibrated from the same module design used in benchtop tests.
- Simulation includes sensor noise but not sensor dropout.
- Fixed-flow baseline uses the current lab default, not an optimized fixed-flow policy.
- Three benchtop runs are technical replicates on one physical module.
- Controller update interval: 500 ms.
- Safety controller retains authority to override flow commands.

## Desired conference outcome

The speaker wants controls and battery researchers to understand the controller concept, challenge the evaluation design, and discuss what validation would justify a larger vehicle-level study.

## Talk constraints

- 12 minutes speaking, 3 minutes questions.
- Mixed audience: control researchers, battery thermal specialists, and industry engineers.
- The full paper has 14 figures; only two are decisive:
  1. controller/system schematic;
  2. simulated and benchtop temperature-imbalance comparison with uncertainty/range.
