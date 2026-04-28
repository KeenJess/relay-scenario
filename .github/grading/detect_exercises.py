"""Stage 1: Detect which exercises a student completed and extract self-assessment scores."""

import json
import os
import re
from pathlib import Path

SUBMISSION_PATH = Path(os.environ.get("SUBMISSION_PATH", "my-work"))

# Expected file structure per level
EXPECTED_FILES = {
    "level-1": {
        "exercises": [
            "initial-reactions.md",
            "smart-dependencies-problem-statement.md",
            "smart-dependencies-discovery.md",
            "smart-dependencies-spec.md",
        ],
        "capstone": "capstone-self-assessment.md",
    },
    "level-2": {
        "exercises": [
            "sprint-plan.md",
            "handoff-doc.md",
            "iteration-log.md",
            "stakeholder-update.md",
            "delivery-validation.md",
        ],
        "capstone": "capstone-self-assessment.md",
    },
    "level-3": {
        "exercises": [
            "executive-brief.md",
            "tooling-strategy.md",
            "adoption-plan.md",
            "adoption-metrics.md",
            "sustainability-plan.md",
        ],
        "capstone": "capstone-self-assessment.md",
    },
}


def parse_self_scores(content: str) -> dict[str, int]:
    """Extract 'Your score: N' lines from a self-assessment file."""
    scores = {}
    # Match patterns like "**Your score:** 4" or "Your score: 3"
    section_pattern = re.compile(r"###\s+\d+\.\s+(.+)")
    score_pattern = re.compile(r"\*?\*?Your score:?\*?\*?\s*(\d)")

    current_section = None
    for line in content.splitlines():
        section_match = section_pattern.search(line)
        if section_match:
            current_section = section_match.group(1).strip()
        score_match = score_pattern.search(line)
        if score_match and current_section:
            scores[current_section] = int(score_match.group(1))
    return scores


def detect():
    results = {
        "completed_levels": [],
        "exercise_counts": {},
        "self_scores": {},
        "has_capstone": False,
        "has_byop": False,
    }

    for level, expected in EXPECTED_FILES.items():
        level_path = SUBMISSION_PATH / level
        if not level_path.exists():
            continue

        # Count completed exercises
        found = [f for f in expected["exercises"] if (level_path / f).exists()]
        results["exercise_counts"][level] = {
            "completed": len(found),
            "total": len(expected["exercises"]),
            "files": found,
        }

        # Check for capstone self-assessment
        capstone_path = level_path / expected["capstone"]
        if capstone_path.exists():
            results["has_capstone"] = True
            results["completed_levels"].append(level)
            scores = parse_self_scores(capstone_path.read_text())
            if scores:
                results["self_scores"][level] = scores

        # Check for BYOP work
        byop_files = list(level_path.glob("byop-*"))
        if byop_files:
            results["has_byop"] = True

    # Write outputs for GitHub Actions
    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a") as f:
            f.write(f"has_capstone={'true' if results['has_capstone'] else 'false'}\n")
            f.write(f"completed_levels={','.join(results['completed_levels'])}\n")
            f.write(f"has_byop={'true' if results['has_byop'] else 'false'}\n")

    # Write full detection results for downstream stages
    os.makedirs("grading-results", exist_ok=True)
    with open("grading-results/detection.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"Detected: {len(results['completed_levels'])} levels completed")
    for level, counts in results["exercise_counts"].items():
        print(f"  {level}: {counts['completed']}/{counts['total']} exercises")
    if results["self_scores"]:
        for level, scores in results["self_scores"].items():
            total = sum(scores.values())
            print(f"  {level} self-assessment: {total}/{len(scores) * 5}")


if __name__ == "__main__":
    detect()
