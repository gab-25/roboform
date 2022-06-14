from enum import Enum
from .global_configs import GlobalConfigs
from .form_configs import FormConfigs
from .form_logs import FormLogs


class Cmd(Enum):
    CREATE = "create", "create a form configs"
    LIST = "list", "get all form configs"
    REMOVE = "remove", "remove a form configs"
    EDIT = "edit", "edit a form configs"
    LOGS = "logs", "show a form logs"
    SETTINGS = "settings", "edit a roboform settings"

    def __new__(cls, value: str, help: str):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.help = help
        return obj

    @staticmethod
    def names():
        return list(map(lambda c: c.name, Cmd))

    @staticmethod
    def values():
        return list(map(lambda c: c.value, Cmd))


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


def create_config(name: str = None) -> FormConfigs:
    print("\nCREATE FORM CONFIG")
    name_already_insert = False
    while name is None or name.strip() == "":
        if name_already_insert:
            print("Error name not valid!")

        name = input("NAME: ")
        name_already_insert = True

    if FormConfigs.form_configs_exist(name):
        print("Error form configs already exist!")
    else:
        form_configs = FormConfigs(name)
        form_configs.write_file_form_configs()

        print("Form configs created!")

        return form_configs


def list_configs() -> list[str]:
    print("\nLIST ALL FORM CONFIG")
    configs = FormConfigs.get_all_configs()

    for id_config, config in enumerate(configs):
        print(f"{id_config+1}. {config}")

    return configs


def remove_config(name: str) -> bool:
    print("\nREMOVE FORM CONFIG")
    if name is None or name.strip() == "":
        configs = list_configs()
        opt = select_option(len(configs))
        name = configs[opt-1]

    if FormConfigs.remove_config(name):
        print("Form config removed!")
        return True
    else:
        print("Error form not found!")
        return False


def edit_config(name: str) -> bool:
    print("\nEDIT FORM CONFIG")
    if name is None or name.strip() == "":
        configs = list_configs()
        opt = select_option(len(configs))
        name = configs[opt-1]

    if FormConfigs.edit_config(name):
        print("Form config opened!")
        return True
    else:
        print("Error form not found!")
        return False


def show_form_logs(name: str) -> bool:
    print("\nSHOW FORM LOGS")
    if name is None or name.strip() == "":
        configs = list_configs()
        opt = select_option(len(configs))
        name = configs[opt-1]

    if FormLogs.show_log(name):
        print("Form logs opened!")
        return True
    else:
        print("Error file form logs not found!")
        return False


def edit_settings() -> bool:
    print("\nEDIT SETTINGS")
    global_configs: GlobalConfigs = GlobalConfigs.get_instance()
    global_configs.check_file_global_configs()

    if global_configs.edit_global_configs():
        print("Settings opened!")
        return True
    else:
        print("Error file settings not found!")
        return False


def run(cmd: Cmd = None, args: list = None):
    global_configs: GlobalConfigs = GlobalConfigs.get_instance()
    global_configs.check_file_global_configs()

    name = args[0] if args is not None else None

    try:
        if cmd is None or not cmd:
            cmd = print_menu()

        if cmd == Cmd.CREATE:
            create_config(name)

        if cmd == Cmd.LIST:
            list_configs()

        if cmd == Cmd.REMOVE:
            remove_config(name)

        if cmd == Cmd.EDIT:
            edit_config(name)

        if cmd == Cmd.SETTINGS:
            edit_settings()

        if cmd == Cmd.LOGS:
            edit_settings()
    except (KeyboardInterrupt, EOFError):
        print("\nBye Bye")
        exit(0)
