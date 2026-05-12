# Material Observation Style RLHF Dataset

Preference-pair dataset for training or evaluating prose style models with RLHF, DPO, IPO, KTO, or reward-model workflows.

These datasets teach a concrete, material-observation prose style: visible action over abstraction, procedural competence over aestheticized competence, recurring documentary evidence over thesis narration, and grounded dialogue over concept-label exchange.

The repository contains two compact, high-signal datasets:

1. Material Observation Style RLHF Dataset — trains toward concrete observable behavior, material evidence, institutional texture, visible inference, procedural competence, and cumulative implication.
2. Dialogue Failure Modes Preference Dataset — trains away from quips, robotic clipped dialogue, noun-prompt exchanges, neat triads, abstract concept speech, trailer-line endings, direct theme explanation, self-aware banter, performative competence, and over-framed thoughts.

## Contents

```text
data/
  README.md
  rlhf_material_observation_style_dataset.jsonl
  rlhf_material_observation_style_dataset.csv
  metadata.json
  dialogue_failure_modes_preference_dataset.jsonl
  dialogue_failure_modes_preference_dataset.csv
  dialogue_failure_modes_metadata.json
docs/
  data_card.md
  dialogue_failure_modes_data_card.md
scripts/
  validate_dataset.py
```

## Dataset format

Each record is a preference pair:

```json
{
  "id": "dialogue_away_081",
  "category": "competence_as_performance",
  "prompt": "Rewrite the cool line into executable instructions.",
  "rejected": "Bob watched the loading dock. “Leave it open enough to tempt them.”",
  "chosen": "Bob watched the loading dock. “Keep the left bay open. Stack the empties beside it so a driver has to slow before backing in.”",
  "rubric": "The chosen line can be obeyed."
}
```

Fields:

| Field | Description |
|---|---|
| `id` | Stable record identifier |
| `category` | Targeted style or dialogue failure mode |
| `prompt` | Instruction or writing task |
| `rejected` | Undesired output |
| `chosen` | Preferred output |
| `rubric` | Human-readable rationale for preference |

## Dataset sizes

| Dataset | Records |
|---|---:|
| Material Observation Style RLHF Dataset | 100 |
| Dialogue Failure Modes Preference Dataset | 120 |

## Quick validation

```bash
python scripts/validate_dataset.py
```

Expected result:

```text
Validated rlhf_material_observation_style_dataset.jsonl: 100 records
Validated dialogue_failure_modes_preference_dataset.jsonl: 120 records
No validation errors found
```

## License

This dataset is released under **Creative Commons Attribution 4.0 International (`CC-BY-4.0`)**.

You may share and adapt the dataset, including for commercial purposes, provided you give appropriate attribution and indicate whether changes were made.

Suggested attribution:

```text
Material Observation Style RLHF Dataset, version 1.0, licensed under CC-BY-4.0.
```
