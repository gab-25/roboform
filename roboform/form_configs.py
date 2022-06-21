import os
import shutil
import subprocess
import configparser

from .form_logs import FormLogs
from .bot import Bot
from .global_configs import GlobalConfigs


class FormConfigs:
    __config = configparser.ConfigParser()
    __config["FORM_CONFIGS"] = {"email_send": "true",
                                "send_to": "",
                                "schedule_at": "[]"}

    def __init__(self, name: str):
        self.folder_path = os.path.join(GlobalConfigs.home_path, name)
        self.path = os.path.join(self.folder_path, f"{name}_configs.cfg")
        self.logs = FormLogs(name)
        self.name = name

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

    def __check_file_form_configs(self):
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)

        if not os.path.exists(self.path):
            open(self.path, "w").close()

    def create_configs(self) -> bool:
        self.__check_file_form_configs()

        try:
            self.__config.read(self.path)
        except (configparser.MissingSectionHeaderError, configparser.ParsingError):
            return False

        with open(self.path, "w") as file:
            self.__config.write(file)

        return True

    def remove_configs(self) -> bool:
        if os.path.exists(self.folder_path):
            shutil.rmtree(self.folder_path)
            return True
        else:
            return False

    def edit_configs(self) -> bool:
        if os.path.exists(self.path):
            subprocess.Popen(["gedit", self.path])
            return True
        else:
            return False

    def run_configs(self) -> bool:
        if os.path.exists(self.path):
            config =  self.__config
            bot = Bot(config)
            bot.exec()

            return True
        else:
            return False
