"""Stage 3: Record anonymized scores for aggregate proof-point reporting.

Writes anonymized score data to grading-results/aggregate.jsonl.
A separate scheduled workflow can collect these into the _data branch
for marketing dashboards.

Privacy: student identity is hashed — only level scores and timestamps are stored.
"""

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

STUDENT_HASH = os.environ.get("STUDENT_HASH", "unknown")
GRADING_RESULTS = Path(os.environ.get("GRADING_RESULTS", "grading-results/scores.json"))


def main():
    scores = json.loads(GRADING_RESULTS.read_text())

    # Build anonymized record
    record = {
        "student_id": hashlib.sha256(STUDENT_HASH.encode()).hexdigest()[:12],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "levels": {},
    }

    for level, result in scores.items():
        if "error" in result:
            continue
        record["levels"][level] = {
            "ai_total": result.get("total_score"),
            "max_score": result.get("max_score"),
            "passing": result.get("passing"),
            "criteria_scores": {
                c["name"]: {
                    "ai": c.get("ai_score"),
                    "self": c.get("self_score"),
                }
                for c in result.get("criteria", [])
            },
        }

    # Append to aggregate file (one JSON record per line)
    aggregate_path = Path("grading-results/aggregate.jsonl")
    with open(aggregate_path, "a") as f:
        f.write(json.dumps(record) + "\n")

    print(f"Recorded anonymized scores for student {record['student_id']}")
    print(f"Levels graded: {list(record['levels'].keys())}")


if __name__ == "__main__":
    main()
