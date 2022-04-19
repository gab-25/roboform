import sys
from .cli import run, Cmd


def main(argv: list = None):
    if argv is None:
        argv = sys.argv[1:]

    try:
        cmd = Cmd(argv[0]) if len(argv) > 0 else None
    except ValueError:
        print("Error command not valid!\n")
        cmd = Cmd.HELP

    if len(argv) > 1:
        run(cmd, argv[1:])
    else:
        run(cmd)


if __name__ == "__main__":
    main()
