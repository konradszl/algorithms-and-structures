import json

from pathlib import Path

CASES = json.loads((Path(__file__).parent.parent / "cases.json").read_text())

def test_cases(solution):
    for case in CASES:
        assert solution.get_concatenation(*case["input"]) == case["expected"]
