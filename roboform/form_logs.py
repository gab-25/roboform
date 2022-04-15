import os
from .global_configs import GlobalConfigs


class FormLogs:

    def __init__(self, name: str):
        self.path = os.path.join(GlobalConfigs.home_path, f"{self.name}_logs.txt")
        self.name = name
