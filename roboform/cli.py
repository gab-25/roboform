from enum import Enum


class Cmd(Enum):
    HELP = "--help"
    CREATE = "--create"
    LIST = "--list"
    REMOVE = "--remove"
    EDIT = "--edit"

    @staticmethod
    def names():
        return list(map(lambda c: c.name, Cmd))


def print_help():
    str_help = "USAGE: roboform [command]\n\n" \
               "COMMANDS:\n" \
               "--help      show usage tool\n" \
               "--create    create a new form configs\n" \
               "--list      get all form configs\n" \
               "--remove    remove a form configs\n" \
               "--edit      edit a form configs"
    print(str_help)


def print_menu():
    str_menu = ""
    names = Cmd.names()
    for i, cmd_name in enumerate(names):
        str_menu += f"{i+1}. {cmd_name} \n"
    print(str_menu)

    try:
        opt = int(input("SELECT AN OPTION: "))
        if opt == 0 or opt > len(names):
            raise ValueError()
    except ValueError:
        print("Error option selected not found.")
        exit(1)

    return Cmd[names[int(opt)-1]]


def run(cmd: Cmd = None, args: list = None):
    if cmd is None or not cmd:
        cmd = print_menu()
        print(cmd)

    if cmd[0] == Cmd.HELP.value:
        print_help()
