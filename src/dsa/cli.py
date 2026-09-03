import argparse

from dsa import scaffold
from dsa.paths import ROOT

DIFFICULTIES = ("easy", "medium", "hard", "unknown")

PENDING_COMMANDS = (
    ("log", "Record an attempt at a problem"),
    ("due", "Show the problems due for review"),
    ("readme", "Regenerate the generated README blocks"),
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
