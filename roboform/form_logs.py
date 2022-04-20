import os
from datetime import datetime
from .global_configs import GlobalConfigs


class FormLogs:

    def __init__(self, name: str):
        self.folder_path = os.path.join(GlobalConfigs.home_path, name)
        self.path = os.path.join(self.folder_path, f"{name}_logs.txt")
        self.name = name

        self.__check_file_form_logs()

    def __check_file_form_logs(self):
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)

        if not os.path.exists(self.path):
            open(self.path, "w").close()

    def print_log(self, message: str):
        with open(self.path, "w") as file:
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            file.write(f"{timestamp} [{self.name}]: {message}\n")
