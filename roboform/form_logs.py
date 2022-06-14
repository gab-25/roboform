import os
import subprocess
from datetime import datetime
from .global_configs import GlobalConfigs


class FormLogs:

    def __init__(self, name: str):
        self.folder_path = os.path.join(GlobalConfigs.home_path, name)
        self.path = os.path.join(self.folder_path, f"{name}_logs.txt")
        self.name = name

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

    @staticmethod
    def form_logs_exist(name: str) -> bool:
        folder = os.path.join(GlobalConfigs.home_path, name)

        return os.path.exists(folder)

    @staticmethod
    def show_log(name: str) -> bool:
        file_log = os.path.join(GlobalConfigs.home_path, name, f"{name}_logs.txt")
        if FormLogs.form_logs_exist(name):
            file_log = os.path.join(GlobalConfigs.home_path, name, f"{name}_logs.txt")
            subprocess.Popen(["gedit", file_log])
            return True
        else:
            return False
