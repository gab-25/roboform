import sys
from .cli import run


def main(argv: list = None):
    if argv is None:
        argv = sys.argv[1:]

    if len(argv) > 1:
        run(argv[0], argv[1:])
    else:
        run(argv)


if __name__ == "__main__":
    main()
