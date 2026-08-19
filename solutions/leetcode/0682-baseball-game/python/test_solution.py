import json

from pathlib import Path
from solution import cal_points

CASES = json.loads((Path(__file__).parent.parent / "cases.json").read_text())

def test_cases():
    for case in CASES:
        assert cal_points(*case["input"]) == case["expected"]
