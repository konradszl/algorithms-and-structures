import argparse

from dsa import readme, scaffold
from dsa.paths import ROOT

DIFFICULTIES = ("easy", "medium", "hard", "unknown")

PENDING_COMMANDS = (
    ("log", "Record an attempt at a problem"),
    ("due", "Show the problems due for review"),
    ("stats", "Show strength per pattern"),
)


def _pattern_list(value: str) -> tuple[str, ...]:
    return tuple(pattern.strip() for pattern in value.split(",") if pattern.strip())


def _new(args: argparse.Namespace) -> None:
    try:
        directory = scaffold.create(
            args.platform,
            args.slug,
            difficulty=args.difficulty,
            title=args.title,
            url=args.url,
            patterns=args.patterns,
        )
    except (FileExistsError, ValueError) as error:
        raise SystemExit(f"dsa new: {error}") from error

    print(f"Created {directory.relative_to(ROOT)}")


def _readme(args: argparse.Namespace) -> None:
    try:
        changed = readme.write(check=args.check)
    except ValueError as error:
        raise SystemExit(f"dsa readme: {error}") from error

    if not changed:
        print("README.md is up to date")
        return

    if args.check:
        raise SystemExit("dsa readme: README.md is out of date, run 'dsa readme'")

    print("Updated README.md")


def _not_implemented(args: argparse.Namespace) -> None:
    raise NotImplementedError(f"'dsa {args.command}' is not implemented yet")


def _add_new_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser("new", help="Scaffold a new problem directory")

    parser.add_argument("platform", help="Platform hosting the problem, e.g. leetcode")
    parser.add_argument("slug", help="Directory name, e.g. 0020-valid-parentheses")
    parser.add_argument(
        "--title", help="Display title (derived from the slug by default)"
    )
    parser.add_argument("--url", help="Problem URL (derived from the slug by default)")
    parser.add_argument(
        "--difficulty",
        choices=DIFFICULTIES,
        default="unknown",
        help="Problem difficulty (default: unknown)",
    )
    parser.add_argument(
        "--patterns",
        type=_pattern_list,
        default=(),
        help="Comma separated patterns, e.g. stack,string",
    )

    parser.set_defaults(func=_new)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dsa",
        description="Practice log and scaffolding for algorithm problems.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    _add_new_parser(subparsers)

    readme_parser = subparsers.add_parser(
        "readme", help="Regenerate the generated README blocks"
    )
    readme_parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if the README is out of date instead of rewriting it",
    )
    readme_parser.set_defaults(func=_readme)

    for name, help_text in PENDING_COMMANDS:
        subparser = subparsers.add_parser(name, help=help_text)
        subparser.set_defaults(func=_not_implemented)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    args.func(args)


if __name__ == "__main__":
    main()
