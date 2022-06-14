import argparse
from .cli import run, Cmd


def main():
    parser = argparse.ArgumentParser(prog="roboform", description="automatic form compiler")
    subparser = parser.add_subparsers(title="commands", description="roboform commands", dest="command")

    parser_cmd = None
    for cmd in Cmd:
        parser_cmd = subparser.add_parser(cmd.value, help=cmd.help)
        parser_cmd.add_argument("--name", type=str, required=False, help=cmd.help)

    args = parser.parse_args()

    cmd = Cmd(args.command) if args.command is not None else None
    name: str = args.name if hasattr(args, "name") else None

    run(cmd, name)


if __name__ == "__main__":
    main()
