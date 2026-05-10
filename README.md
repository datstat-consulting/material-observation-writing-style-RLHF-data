# Material Observation Style RLHF Dataset

Preference-pair dataset for training or evaluating prose style models with RLHF, DPO, IPO, KTO, or reward-model workflows.

The dataset teaches a concrete, material-observation prose style: visible action over abstraction, procedural competence over aestheticized competence, recurring documentary evidence over thesis narration, and grounded dialogue over concept-label exchange.

## Contents

```text
data/
  rlhf_material_observation_style_dataset.jsonl
  rlhf_material_observation_style_dataset.csv
  metadata.json
docs/
  data_card.md
scripts/
  validate_dataset.py
```

## Dataset format

Each record is a preference pair:

```json
{
  "id": "rlhf_pattern_046",
  "category": "pattern_recognition_through_recurrence",
  "prompt": "Rewrite: 'Dominic realized the institutions were connected.'",
  "rejected": "Dominic realized the institutions were connected.",
  "chosen": "Dominic found the same drafting error in a customs petition, a bridge estimate, and a militia requisition.",
  "rubric": "Avoid explanatory realization. Let recurrence produce inference."
}
```

Fields:

| Field | Description |
|---|---|
| `id` | Stable record identifier |
| `category` | Targeted style constraint |
| `prompt` | Instruction or writing task |
| `rejected` | Undesired output that violates the style rule |
| `chosen` | Preferred output that follows the style rule |
| `rubric` | Human-readable rationale for preference |

## Quick validation

```bash
python scripts/validate_dataset.py
```

Expected result:

```text
Loaded 100 records
No validation errors found
```

## License

This dataset is released under **Creative Commons Attribution 4.0 International (`CC-BY-4.0`)**.

You may share and adapt the dataset, including for commercial purposes, provided you give appropriate attribution and indicate whether changes were made.

Suggested attribution:

```text
Material Observation Style RLHF Dataset, version 1.0, licensed under CC-BY-4.0.
```
