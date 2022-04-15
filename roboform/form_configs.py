import os
from .log import FormLogs
from .global_config import GlobalConfigs


class FormConfigs:

    def __init__(self, name: str):
        self.path = os.path.join(GlobalConfigs.home_path, f"{self.name}_configs.cfg")
        self.name = name
        self.log = FormLogs(name)
