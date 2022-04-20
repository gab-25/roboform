from enum import Enum
from .global_configs import GlobalConfigs
from .form_configs import FormConfigs


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


def print_menu() -> Cmd:
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
    except (KeyboardInterrupt, EOFError):
        print("\nBye Bye")
        exit(0)

    return Cmd[names[int(opt)-1]]


def create_config(name: str):
    if name is None or name.strip() == "":
        print("Error name not valid!")
        exit(1)

    if FormConfigs.form_configs_exist(name):
        print("Error form configs already exist!")
    else:
        FormConfigs(name)
        print("Form configs created!")


def list_configs():
    pass


def remove_config():
    pass


def edit_config():
    pass


def run(cmd: Cmd = None, args: list = None):
    GlobalConfigs.get_instance().check_file_global_configs()

    if cmd is None or not cmd:
        cmd = print_menu()

    if cmd == Cmd.HELP:
        print_help()

    if cmd == Cmd.CREATE:
        create_config(args[0] if args is not None else None)

    if cmd == Cmd.LIST:
        list_configs()

    if cmd == Cmd.REMOVE:
        remove_config()

    if cmd == Cmd.EDIT:
        edit_config()
