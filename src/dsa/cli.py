import argparse

COMMANDS = (
    ("new", "Scaffold a new problem directory"),
    ("log", "Record an attempt at a problem"),
    ("due", "Show the problems due for review"),
    ("readme", "Regenerate the generated README blocks"),
    ("stats", "Show strength per pattern"),
)


def _not_implemented(args: argparse.Namespace) -> None:
    raise NotImplementedError(f"'dsa {args.command}' is not implemented yet")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dsa",
        description="Practice log and scaffolding for algorithm problems.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    for name, help_text in COMMANDS:
        subparser = subparsers.add_parser(name, help=help_text)
        subparser.set_defaults(func=_not_implemented)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    args.func(args)


if __name__ == "__main__":
    main()
