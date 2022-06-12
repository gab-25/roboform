import os
import configparser
import subprocess


class GlobalConfigs:
    __instance = None
    __config = configparser.ConfigParser()
    __config["SETTINGS"] = {"smtp_client": "",
                            "smtp_user": "",
                            "smtp_password": ""}

    home_path = os.path.join(os.path.expanduser("~"), "roboform")
    email_sender = "noreply@roboform.com"

    @staticmethod
    def get_instance():
        if GlobalConfigs.__instance is None:
            GlobalConfigs()

        return GlobalConfigs.__instance

    def __init__(self):
        if GlobalConfigs.__instance is not None:
            raise Exception("This class is a singleton class!")
        else:
            GlobalConfigs.__instance = self

        self.path = os.path.join(GlobalConfigs.home_path, "global_configs.cfg")

    def check_file_global_configs(self):
        if not os.path.exists(self.home_path):
            os.mkdir(self.home_path)

        if not os.path.exists(self.path):
            open(self.path, "w").close()

        self.__write_file_global_configs()

    def __write_file_global_configs(self):
        try:
            self.__config.read(self.path)
        except (configparser.MissingSectionHeaderError, configparser.ParsingError):
            pass

        with open(self.path, "w") as file:
            self.__config.write(file)

    def edit_global_configs(self) -> bool:
        if os.path.exists(self.path):
            subprocess.Popen(["gedit", self.path])
            return True
        else:
            return False
