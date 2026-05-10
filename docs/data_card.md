# Data Card: Material Observation Style RLHF Dataset

## Dataset Summary

This is a 100-record preference-pair dataset for training or evaluating prose style models. Each record contains a prompt, a rejected answer, a chosen answer, and a rubric explaining the preference.

The target style emphasizes concrete observable behavior, embodied action, material evidence, visible inference, procedural competence, and socially embedded dialogue.

## Intended Uses

Suitable for:

- Direct Preference Optimization (DPO)
- Reward model training
- RLHF preference modeling
- Style-transfer evaluation
- Fine-tuning small creative-writing adapters
- Regression tests for prose style adherence

## Not Intended For

Not suitable as a standalone factual dataset. The examples are synthetic prose-writing samples and should not be treated as historical, geographic, or technical facts.

## Data Schema

| Field | Type | Description |
|---|---:|---|
| `id` | string | Stable unique record ID |
| `category` | string | Style category being tested |
| `prompt` | string | User-facing instruction |
| `rejected` | string | Lower-quality answer |
| `chosen` | string | Preferred answer |
| `rubric` | string | Preference rationale |

## Style Categories

The dataset covers constraints such as:

- Concrete observable behavior
- Physical action over behavioral summary
- Specific material observation
- Embodied detail over generalized presence
- Visible inference from Dominic's point of view
- Accumulated implication through recurrence
- Grounded trade speech
- Interruption and overlap in dialogue
- Socially embedded dry humor
- Recurring material motifs
- Layered coexistence rather than reductive explanation
- Continuing physical motion rather than literary punchlines
- Physical manifestation of emotion
- Procedural competence
- Institutional/material texture
- Pattern recognition through recurrence
- Cumulative paragraph rhythm

## Quality Notes

The dataset is compact and style-specific. It is best used as a high-signal supplemental dataset rather than a broad writing corpus.

Recommended evaluation approach:

1. Hold out 10–20 records for validation.
2. Inspect generated outputs manually for concrete behavior, material evidence, and recurrence.
3. Penalize abstract explanations, narrator cleverness, faux-perceptive summaries, and polished aphorisms.

## Limitations

- Synthetic examples may overrepresent one prose register.
- The setting vocabulary is concentrated around offices, bridges, tolls, roads, ledgers, forts, freight, and institutional paperwork.
- The dataset is too small for broad stylistic generalization without augmentation.
- No demographic or personal data is included.

## License

This dataset is licensed under Creative Commons Attribution 4.0 International (`CC-BY-4.0`).

Reusers may share and adapt the dataset, including for commercial purposes, provided they give appropriate attribution and indicate whether changes were made.

Suggested attribution:

```text
Material Observation Style RLHF Dataset, version 1.0, licensed under CC-BY-4.0.
```

## Suggested Citation

```text
Material Observation Style RLHF Dataset, version 1.0.
Synthetic preference-pair dataset for concrete prose style training.
Licensed under CC-BY-4.0.
```
