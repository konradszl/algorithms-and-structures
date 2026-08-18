import argparse

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
LANG_FILES = {
    "python": [
        "solution.py",
        "test_solution.py"
    ],
    "cpp": [
        "solution.cpp"
        "test_solution.cpp"
    ],
    "go": [
        "solution.go",
        "solution_test.go"
    ]
}

def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("platform")
    parser.add_argument("slug")
    parser.add_argument("--difficulty", default="unknown")
    parser.add_argument("--tags", default="")
    parser.add_argument("--langs", default="python")

    args = parser.parse_args()

    langs = [lang.strip() for lang in args.langs.split(",") if lang.strip()]
    problem_dir = ROOT / "solutions" / args.platform / args.slug

    if problem_dir.exists():
        raise SystemExit(f"{problem_dir} already exists")

    problem_dir.mkdir(parents=True)

    (problem_dir / "problem.tml").write_text(
        f"platform: {args.platform}\n"
        f"difficulty: {args.difficulty}\n" 
        f"tags: [{args.tags}]\n"
        f"languages: [{', '.join(langs)}]\n"
    )
    (problem_dir / "cases.json").write_text("[]\n")

    for lang in langs:
        lang_dir = problem_dir / lang
        lang_dir.mkdir()

        for filename in LANG_FILES[lang]:
            content = (TEMPLATES / lang / filename).read_text()
            (lang_dir / filename).write_text(content)

    print(f"Created {problem_dir.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
