import os
import shutil
import subprocess
import configparser
from .form_logs import FormLogs
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

    def __check_file_form_configs(self):
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)

        if not os.path.exists(self.path):
            open(self.path, "w").close()

    def write_file_form_configs(self):
        self.__check_file_form_configs()

        try:
            self.__config.read(self.path)
        except (configparser.MissingSectionHeaderError, configparser.ParsingError):
            pass

        with open(self.path, "w") as file:
            self.__config.write(file)

    @staticmethod
    def form_configs_exist(name: str) -> bool:
        folder = os.path.join(GlobalConfigs.home_path, name)

        return os.path.exists(folder)

    @staticmethod
    def get_all_configs() -> list[str]:
        configs = []

        for folder_name in os.listdir(GlobalConfigs.home_path):
            folder = os.path.join(GlobalConfigs.home_path, folder_name)
            if os.path.isdir(os.path.join(GlobalConfigs.home_path, folder)):
                configs.append(folder_name)

        return sorted(configs)

    @staticmethod
    def remove_config(name: str):
        if FormConfigs.form_configs_exist(name):
            folder = os.path.join(GlobalConfigs.home_path, name)
            shutil.rmtree(folder)
        else:
            print("Error form not found!")
            exit(1)

    @staticmethod
    def edit_config(name: str):
        if FormConfigs.form_configs_exist(name):
            file_config = os.path.join(GlobalConfigs.home_path, name, f"{name}_configs.cfg")
            subprocess.Popen(["gedit", file_config])
        else:
            print("Error form not found!")
            exit(1)
