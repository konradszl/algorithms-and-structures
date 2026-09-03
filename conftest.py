import importlib.util
from types import ModuleType

import pytest


@pytest.fixture
def solution(request: pytest.FixtureRequest) -> ModuleType:
    path = request.path.parent / "solution.py"
    spec = importlib.util.spec_from_file_location("solution", path)

    if spec is None or spec.loader is None:
        raise ImportError(f"no loadable solution.py next to {request.path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module
