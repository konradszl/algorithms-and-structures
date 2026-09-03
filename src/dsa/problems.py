from dataclasses import dataclass
from datetime import date
from pathlib import Path

import yaml

from dsa.paths import PROBLEMS


@dataclass(frozen=True)
class Problem:
    id: str
    title: str
    url: str
    platform: str
    difficulty: str
    patterns: tuple[str, ...]
    added: date | None

    @property
    def slug(self) -> str:
        return self.id.split("/", 1)[1]

    @property
    def directory(self) -> Path:
        return PROBLEMS / self.id


def _as_date(value: object) -> date | None:
    if isinstance(value, date):
        return value

    if isinstance(value, str) and value.strip():
        return date.fromisoformat(value.strip())

    return None


def read_problem(problem_yml: Path) -> Problem:
    data = yaml.safe_load(problem_yml.read_text()) or {}
    slug = problem_yml.parent.name
    platform = problem_yml.parent.parent.name
    patterns = data.get("patterns") or []

    return Problem(
        id=f"{platform}/{slug}",
        title=str(data.get("title") or slug),
        url=str(data.get("url") or ""),
        platform=platform,
        difficulty=str(data.get("difficulty") or "unknown").lower(),
        patterns=tuple(
            str(pattern).strip() for pattern in patterns if str(pattern).strip()
        ),
        added=_as_date(data.get("added")),
    )


def load_problems() -> list[Problem]:
    if not PROBLEMS.exists():
        return []

    problems = [read_problem(path) for path in PROBLEMS.rglob("problem.yml")]

    return sorted(problems, key=lambda problem: problem.id)
