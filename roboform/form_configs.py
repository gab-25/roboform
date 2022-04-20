import os
from .log import FormLogs
from .global_config import GlobalConfigs


class FormConfigs:

    def __init__(self, name: str):
        self.__header_file = f"       {name} CONFIGS\n" \
                             f"***********************************"
        self.path = os.path.join(GlobalConfigs.home_path, f"{self.name}_configs.cfg")
        self.properties = {"email_send:" "true"}
        self.name = name
        self.log = FormLogs(name)
