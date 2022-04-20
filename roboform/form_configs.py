import os
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

        self.__check_file_form_configs()

    def __check_file_form_configs(self):
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)

        if not os.path.exists(self.path):
            open(self.path, "w").close()

        self.__write_file_form_configs()

    def __write_file_form_configs(self):
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
