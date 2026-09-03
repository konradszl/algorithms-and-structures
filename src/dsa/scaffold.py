import re
from collections.abc import Sequence
from datetime import date
from pathlib import Path

from dsa.paths import PROBLEMS, TEMPLATES

NUMBER_PREFIX = re.compile(r"^\d+-")
PLATFORM_URLS = {"leetcode": "https://leetcode.com/problems"}


def problem_name(slug: str) -> str:
    return NUMBER_PREFIX.sub("", slug)


def derive_title(slug: str) -> str:
    words = problem_name(slug).split("-")

    return " ".join(word.capitalize() for word in words)


def derive_url(platform: str, slug: str) -> str:
    url = PLATFORM_URLS.get(platform)

    if url is None:
        return ""

    return f"{url}/{problem_name(slug)}"


def _replacements(
    platform: str,
    slug: str,
    difficulty: str = "unknown",
    title: str | None = None,
    url: str | None = None,
    patterns: Sequence[str] = (),
    added: date | None = None,
) -> dict[str, str]:
    if added is None:
        added = date.today()

    if title is None:
        title = derive_title(slug)

    if url is None:
        url = derive_url(platform, slug)

    return {
        "{{id}}": f"{platform}/{slug}",
        "{{title}}": title,
        "{{url}}": url,
        "{{platform}}": platform,
        "{{difficulty}}": difficulty,
        "{{patterns}}": ", ".join(patterns),
        "{{added}}": added.isoformat(),
    }


def create(
    platform: str,
    slug: str,
    *,
    difficulty: str = "unknown",
    title: str | None = None,
    url: str | None = None,
    patterns: Sequence[str] = (),
    added: date | None = None,
) -> Path:
    if slug == "" or "\\" in slug or "/" in slug or slug.startswith("."):
        raise ValueError(f"{slug!r} is not a usable directory name")

    directory = PROBLEMS / platform / slug

    if directory.exists():
        raise FileExistsError(f"{directory} already exists")

    replacements = _replacements(
        platform,
        slug,
        difficulty=difficulty,
        title=title,
        url=url,
        patterns=patterns,
        added=added,
    )

    directory.mkdir(parents=True)

    for template in sorted(TEMPLATES.iterdir()):
        if not template.is_file():
            continue

        content = template.read_text()

        for placeholder, value in replacements.items():
            content = content.replace(placeholder, value)

        (directory / template.name).write_text(content)

    return directory
