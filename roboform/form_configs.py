import os
import shutil
import subprocess
import toml

from roboform import constants
from .bot import Bot
from .global_configs import GlobalConfigs


class FormConfigs:
    CONFIGS_DEFAULT = {"url": "",
                       "email_send": True,
                       "send_to": "",
                       "schedule_at": ""}

    def __init__(self, name: str):
        self.folder_path = os.path.join(GlobalConfigs.home_path, name)
        self.path = os.path.join(self.folder_path, f"{name}_configs.cfg")
        self.name = name
        self.configs = {constants.FORM_CONFIGS_HEADER: self.CONFIGS_DEFAULT}

    @staticmethod
    def form_configs_exist(name: str) -> bool:
        folder = os.path.join(GlobalConfigs.home_path, name)

        return os.path.exists(folder)

    @staticmethod
    def get_all_configs() -> list[str]:
        configs = []

        for folder_name in os.listdir(GlobalConfigs.home_path):
            folder = os.path.join(GlobalConfigs.home_path, folder_name)
            if os.path.isdir(folder) and not folder_name.startswith("."):
                configs.append(folder_name)

        return sorted(configs)

    def __check_file_form_configs(self) -> bool:
        if not os.path.exists(self.folder_path):
            return False

        if os.path.exists(self.path):
            self.configs = toml.load(self.path)
            self.configs[constants.FORM_CONFIGS_HEADER] = self.CONFIGS_DEFAULT | self.configs.get(constants.FORM_CONFIGS_HEADER, {})

        with open(self.path, "w") as file:
            toml.dump(self.configs, file)
        return True

    def create_configs(self) -> bool:
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)
            with open(self.path, "w") as file:
                toml.dump(self.configs, file)
            return True
        else:
            return False

    def remove_configs(self) -> bool:
        if os.path.exists(self.folder_path):
            shutil.rmtree(self.folder_path)
            return True
        else:
            return False

    def edit_configs(self) -> bool:
        if self.__check_file_form_configs():
            subprocess.Popen([GlobalConfigs.get_instance().get_default_editor(), self.path])
            return True
        else:
            return False

    def run_configs(self) -> bool:
        if self.__check_file_form_configs():
            bot = Bot(self.name, self.configs)
            bot.exec()
            return True
        else:
            return False
