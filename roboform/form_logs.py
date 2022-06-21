import os
import subprocess
from datetime import datetime

from roboform import constants
from .global_configs import GlobalConfigs


class FormLogs:

    def __init__(self, name: str):
        self.folder_path = os.path.join(GlobalConfigs.home_path, name)
        self.path = os.path.join(self.folder_path, f"{name}_logs.txt")
        self.name = name

    @staticmethod
    def form_logs_exist(name: str) -> bool:
        folder = os.path.join(GlobalConfigs.home_path, name)

        return os.path.exists(folder)

    def __check_file_form_logs(self):
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)

        if not os.path.exists(self.path):
            open(self.path, "w").close()

    def print_log(self, message: str):
        self.__check_file_form_logs()

        with open(self.path, "w") as file:
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            file.write(f"{timestamp} [{self.name}]: {message}\n")

    def show_log(self) -> bool:
        if os.path.exists(self.path):
            subprocess.Popen([GlobalConfigs.get_instance().get_default_editor(), self.path])
            return True
        else:
            return False
