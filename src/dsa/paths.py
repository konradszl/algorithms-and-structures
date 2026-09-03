from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROBLEMS = ROOT / "problems"
TEMPLATES = ROOT / "templates" / "problem"
ATTEMPTS = ROOT / "progress" / "attempts.jsonl"
README = ROOT / "README.md"
