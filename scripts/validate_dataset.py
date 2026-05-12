#!/usr/bin/env python3
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASETS = [
    {
        "jsonl": ROOT / "data" / "rlhf_material_observation_style_dataset.jsonl",
        "csv": ROOT / "data" / "rlhf_material_observation_style_dataset.csv",
        "metadata": ROOT / "data" / "metadata.json",
    },
    {
        "jsonl": ROOT / "data" / "dialogue_failure_modes_preference_dataset.jsonl",
        "csv": ROOT / "data" / "dialogue_failure_modes_preference_dataset.csv",
        "metadata": ROOT / "data" / "dialogue_failure_modes_metadata.json",
    },
]

REQUIRED_FIELDS = ["id", "category", "prompt", "rejected", "chosen", "rubric"]

def load_jsonl(path: Path):
    records = []
    with path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON on line {i} in {path.name}: {e}") from e
    return records

def validate_dataset(spec):
    errors = []
    records = load_jsonl(spec["jsonl"])

    ids = set()
    for idx, rec in enumerate(records, start=1):
        for field in REQUIRED_FIELDS:
            if field not in rec:
                errors.append(f"{spec['jsonl'].name} record {idx} missing field: {field}")
            elif not isinstance(rec[field], str) or not rec[field].strip():
                errors.append(f"{spec['jsonl'].name} record {idx} has empty/non-string field: {field}")

        rec_id = rec.get("id")
        if rec_id in ids:
            errors.append(f"{spec['jsonl'].name} duplicate id: {rec_id}")
        ids.add(rec_id)

        if rec.get("chosen") == rec.get("rejected"):
            errors.append(f"{spec['jsonl'].name} record {rec_id} has identical chosen and rejected outputs")

    with spec["csv"].open("r", encoding="utf-8", newline="") as f:
        csv_records = list(csv.DictReader(f))
    if len(csv_records) != len(records):
        errors.append(f"{spec['csv'].name} row count {len(csv_records)} does not match JSONL count {len(records)}")

    metadata = json.loads(spec["metadata"].read_text(encoding="utf-8"))
    if metadata.get("record_count") != len(records):
        errors.append(f"{spec['metadata'].name} record_count {metadata.get('record_count')} does not match JSONL count {len(records)}")

    if metadata.get("license") != "CC-BY-4.0":
        errors.append(f"{spec['metadata'].name} license must be CC-BY-4.0")

    return records, errors

def main():
    all_errors = []
    for spec in DATASETS:
        records, errors = validate_dataset(spec)
        all_errors.extend(errors)
        print(f"Validated {spec['jsonl'].name}: {len(records)} records")

    if all_errors:
        print("Validation errors:")
        for err in all_errors:
            print(f"- {err}")
        raise SystemExit(1)

    print("No validation errors found")

if __name__ == "__main__":
    main()
