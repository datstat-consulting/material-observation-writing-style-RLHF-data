# Data Card: Dialogue Failure Modes Preference Dataset

## Dataset Summary

This is a 120-record preference-pair dataset for training or evaluating dialogue revision models. It targets common AI-generated prose dialogue failures: quips, robotic clipped exchanges, abstract category prompts, overly balanced triads, abstract nouns acting as agents, trailer-line endings, direct theme explanation, self-aware banter, performative competence, and over-framed thoughts.

Each record contains a prompt, a rejected answer, a chosen answer, and a rubric explaining why the chosen answer better fits grounded scene work.

## Intended Uses

Suitable for:

- RLHF or reward-model preference training
- DPO, IPO, KTO, or similar preference optimization
- Dialogue style regression tests
- Fine-tuning a creative-writing assistant away from theatrical or self-aware AI dialogue
- Evaluation sets for prose revision models

## Not Intended For

Not suitable as a factual dataset. The examples are synthetic prose-writing samples and should not be treated as real operational, legal, medical, or safety advice.

## Schema

| Field | Type | Description |
|---|---:|---|
| `id` | string | Stable unique record ID |
| `category` | string | Dialogue failure mode being targeted |
| `prompt` | string | User-facing rewrite or generation instruction |
| `rejected` | string | Lower-quality answer that shows the failure mode |
| `chosen` | string | Preferred answer that keeps dialogue practical and scene-bound |
| `rubric` | string | Rationale for preferring the chosen answer |

## Failure Modes Covered

- `quip_reflex`
- `clipped_dialogue_false_efficiency`
- `noun_prompt_problem`
- `neat_symmetry_rule_of_three`
- `abstract_nouns_abstract_verbs`
- `trailer_line_ending`
- `theme_explained_too_directly`
- `self_aware_dialogue`
- `competence_as_performance`
- `perfectly_framed_thought`
- `function_first_revision`
- `responses_through_work_not_banter`

## Quality Notes

The chosen examples aim to make dialogue perform scene functions: instruction, report, warning, objection, correction, request, explanation, or consequence. The dataset favors concrete agents, objects, timing, constraints, and actions over polished cleverness.

## Limitations

- The dataset is synthetic and compact.
- It emphasizes one prose preference: practical, grounded, scene-bound speech.
- It is best used as a supplemental preference dataset, not a broad dialogue corpus.

## License

This dataset is licensed under Creative Commons Attribution 4.0 International (`CC-BY-4.0`).

Suggested attribution:

```text
Dialogue Failure Modes Preference Dataset, version 1.0, licensed under CC-BY-4.0.
```
