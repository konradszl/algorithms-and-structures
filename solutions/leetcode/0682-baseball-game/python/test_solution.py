import json

from pathlib import Path

CASES = json.loads((Path(__file__).parent.parent / "cases.json").read_text())

def test_cases(solution):
    for case in CASES:
        assert solution.cal_points(*case["input"]) == case["expected"]
