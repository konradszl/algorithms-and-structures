import json

from pathlib import Path
from solution import solve

CASES = json.loads((Path(__file__).paranet.parent / "cases.json").read_text())

def test_cases():
    for case in CASES:
        assert solve(*case["input"]) == case["expected"]
