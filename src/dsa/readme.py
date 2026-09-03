import re

from dsa.paths import README, ROOT
from dsa.problems import Problem, load_problems

PROBLEMS_START = "<!-- PROBLEMS:START -->"
PROBLEMS_END = "<!-- PROBLEMS:END -->"

DIFFICULTY_EMOJI = {"easy": "🟢", "medium": "🟡", "hard": "🔴"}


def difficulty_emoji(difficulty: str) -> str:
    return DIFFICULTY_EMOJI.get(difficulty, "❔")


def problem_table(problems: list[Problem]) -> str:
    if not problems:
        return "No problems yet. Run `dsa new` to scaffold one."

    rows = [
        "| Problem | Difficulty | Patterns |",
        "| --- | --- | --- |",
    ]

    for problem in problems:
        path = problem.directory.relative_to(ROOT).as_posix()
        link = f"[{problem.title}]({path})"
        patterns = ", ".join(problem.patterns)

        rows.append(f"| {link} | {difficulty_emoji(problem.difficulty)} | {patterns} |")

    return "\n".join(rows)


def replace_block(text: str, start: str, end: str, body: str) -> str:
    pattern = re.compile(f"{re.escape(start)}.*?{re.escape(end)}", re.DOTALL)

    if not pattern.search(text):
        raise ValueError(f"{README.name} has no {start} ... {end} block")

    return pattern.sub(lambda _: f"{start}\n{body}\n{end}", text)


def render() -> str:
    table = problem_table(load_problems())

    return replace_block(README.read_text(), PROBLEMS_START, PROBLEMS_END, table)


def write(check: bool = False) -> bool:
    current = README.read_text()
    updated = render()

    if current == updated:
        return False

    if not check:
        README.write_text(updated)

    return True
