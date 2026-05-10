#!/usr/bin/env python3
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSONL_PATH = ROOT / "data" / "rlhf_material_observation_style_dataset.jsonl"
CSV_PATH = ROOT / "data" / "rlhf_material_observation_style_dataset.csv"
META_PATH = ROOT / "data" / "metadata.json"

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
                raise ValueError(f"Invalid JSON on line {i}: {e}") from e
    return records

def main():
    errors = []
    records = load_jsonl(JSONL_PATH)

    ids = set()
    for idx, rec in enumerate(records, start=1):
        for field in REQUIRED_FIELDS:
            if field not in rec:
                errors.append(f"Record {idx} missing field: {field}")
            elif not isinstance(rec[field], str) or not rec[field].strip():
                errors.append(f"Record {idx} has empty/non-string field: {field}")

        rec_id = rec.get("id")
        if rec_id in ids:
            errors.append(f"Duplicate id: {rec_id}")
        ids.add(rec_id)

        if rec.get("chosen") == rec.get("rejected"):
            errors.append(f"Record {rec_id} has identical chosen and rejected outputs")

    with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
        csv_records = list(csv.DictReader(f))
    if len(csv_records) != len(records):
        errors.append(f"CSV row count {len(csv_records)} does not match JSONL count {len(records)}")

    metadata = json.loads(META_PATH.read_text(encoding="utf-8"))
    if metadata.get("record_count") != len(records):
        errors.append(f"Metadata record_count {metadata.get('record_count')} does not match JSONL count {len(records)}")

    if metadata.get("license") != "CC-BY-4.0":
        errors.append("Metadata license must be CC-BY-4.0")

    print(f"Loaded {len(records)} records")
    if errors:
        print("Validation errors:")
        for err in errors:
            print(f"- {err}")
        raise SystemExit(1)

    print("No validation errors found")

if __name__ == "__main__":
    main()
