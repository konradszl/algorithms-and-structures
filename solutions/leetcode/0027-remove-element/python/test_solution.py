import json

from pathlib import Path

CASES = json.loads((Path(__file__).parent.parent / "cases.json").read_text())

def test_cases(solution):
    for case in CASES:
        assert solution.remove_element(*case["input"]) == case["expected"]
