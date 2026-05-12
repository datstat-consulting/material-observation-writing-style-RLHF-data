# Data Files

This repository currently contains two preference-pair datasets.

## 1. Material Observation Style RLHF Dataset

Files:

- `rlhf_material_observation_style_dataset.jsonl`
- `rlhf_material_observation_style_dataset.csv`
- `metadata.json`

Focus: concrete observable behavior, material evidence, institutional texture, visible inference, procedural competence, and cumulative implication.

## 2. Dialogue Failure Modes Preference Dataset

Files:

- `dialogue_failure_modes_preference_dataset.jsonl`
- `dialogue_failure_modes_preference_dataset.csv`
- `dialogue_failure_modes_metadata.json`

Focus: training away from quips, robotic clipped dialogue, noun-prompt exchanges, neat triads, abstract concept speech, trailer-line endings, direct theme explanation, self-aware banter, performative competence, and over-framed thoughts.

Both datasets use this preference-pair schema:

```json
{
  "id": "stable record id",
  "category": "targeted style category",
  "prompt": "instruction/input",
  "rejected": "undesired output",
  "chosen": "preferred output",
  "rubric": "reason chosen is better"
}
```
