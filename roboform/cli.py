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


def select_option(max_opt: int) -> int:
    try:
        opt = int(input("SELECT AN OPTION: "))
        if opt == 0 or opt > max_opt:
            raise ValueError()
    except ValueError:
        print("Error option selected not found.")
        exit(1)

    return opt


def print_menu() -> Cmd:
    print("\nMENU ROBOFORM")
    str_menu = ""
    names = Cmd.names()
    for i, cmd_name in enumerate(names):
        str_menu += f"{i+1}. {cmd_name} \n"
    print(str_menu)

    opt = select_option(len(names))

    return Cmd[names[opt-1]]


def print_help():
    print("\nHELP ROBOFORM")
    str_help = "USAGE: roboform [command]\n\n" \
               "COMMANDS:\n" \
               "--help      show usage tool\n" \
               "--create    create a new form configs\n" \
               "--list      get all form configs\n" \
               "--remove    remove a form configs\n" \
               "--edit      edit a form configs"
    print(str_help)


def create_config(name: str):
    print("\nCREATE FORM CONFIG")
    count = 0
    while name is None or name.strip() == "":
        if count > 0:
            print("Error name not valid!")

        name = input("NAME: ")
        count += 1

    if FormConfigs.form_configs_exist(name):
        print("Error form configs already exist!")
    else:
        FormConfigs(name)
        print("Form configs created!")


def list_configs():
    print("\nLIST ALL FORM CONFIG")
    configs = FormConfigs.get_all_configs()

    for id_config, config in enumerate(configs):
        print(f"{id_config+1}. {config}")


def remove_config(name: str):
    print("\nREMOVE FORM CONFIG")
    if name is None or name.strip() == "":
        list_configs()
        configs = FormConfigs.get_all_configs()
        opt = select_option(len(configs))
        name = configs[opt-1]

    FormConfigs.remove_config(name)
    print("Form config removed!")


def edit_config(name: str):
    print("\nEDIT FORM CONFIG")
    if name is None or name.strip() == "":
        list_configs()
        configs = FormConfigs.get_all_configs()
        opt = select_option(len(configs))
        name = configs[opt-1]

    FormConfigs.edit_config(name)
    print("Form config opened!")


def run(cmd: Cmd = None, args: list = None):
    GlobalConfigs.get_instance().check_file_global_configs()
    name = args[0] if args is not None else None

    try:
        if cmd is None or not cmd:
            cmd = print_menu()

        if cmd == Cmd.HELP:
            print_help()

        if cmd == Cmd.CREATE:
            create_config(name)

        if cmd == Cmd.LIST:
            list_configs()

        if cmd == Cmd.REMOVE:
            remove_config(name)

        if cmd == Cmd.EDIT:
            edit_config(name)
    except (KeyboardInterrupt, EOFError):
        print("\nBye Bye")
        exit(0)
