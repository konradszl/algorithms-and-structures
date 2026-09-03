import json
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest

CASES_PATH = Path(__file__).parent / "cases.json"
CASES: list[dict[str, Any]] = json.loads(CASES_PATH.read_text())

if not CASES:
    pytest.skip("no cases written yet", allow_module_level=True)


def test_cases(solution: ModuleType) -> None:
    for case in CASES:
        assert solution.solve(*case["input"]) == case["expected"]
