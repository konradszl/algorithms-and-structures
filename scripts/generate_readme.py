import yaml
import re

from pathlib import Path

table_markdown = [
    "| Problem | Platform | Difficulty | Tags | Languages |",
    "| --- | --- | --- | --- | --- |"
]
difficulty_emojis = {
    "easy": "🟢",
    "medium": "🟡",
    "hard": "🔴"
}

for problem_yml in sorted(Path("solutions").rglob("problem.yml")):
    data = yaml.safe_load(problem_yml.read_text())
    slug = problem_yml.parent.name
    solution_link = f"[{slug}]({problem_yml.parent.as_posix()})"
    tags = ", ".join(data["tags"])
    languages = ", ".join(data["languages"])
    difficulty = difficulty_emojis.get(data["difficulty"], "❔")
    table_row = f"| {solution_link} | {data["platform"]} | {difficulty} | {tags} | {languages} |"

    table_markdown.append(table_row)

start, end = "<!-- PROBLEMS:START -->", "<!-- PROBLEMS:END -->"
readme = Path("README.md").read_text()
pattern = re.compile(f"{re.escape(start)}.*?{re.escape(end)}", re.DOTALL)
readme = pattern.sub(f"{start}\n{"\n".join(table_markdown)}\n{end}", readme)

Path("README.md").write_text(readme)
