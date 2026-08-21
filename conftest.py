import importlib.util
import pytest

from pathlib import Path

@pytest.fixture
def solution(request):
    path = Path(request.path).parent / "solution.py"
    spec = importlib.util.spec_from_file_location("solution", path)
    module = importlib.util.module_from_spec(spec)
    
    spec.loader.exec_module(module)

    return module
