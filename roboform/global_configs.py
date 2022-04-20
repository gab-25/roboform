import os


class GlobalConfigs:
    __instance = None
    __header_file = "       ROBOFORM CONFIGS\n" \
                    "***********************************"
    home_path = os.path.join(os.path.expanduser("~"), "roboform")
    email_sender = "noreply@roboform.com"
    properties = {"smtp_client": "",
                  "smtp_user": "",
                  "smtp_password": ""}

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
        self.__read_file_global_configs()

        with open(self.path, "w") as file:
            file.write(f"{self.__header_file}\n")
            for prop, value in self.properties.items():
                file.write(f"{prop}={value}\n")

    def __read_file_global_configs(self):
        with open(self.path, "r") as file:
            for line in file.readlines():
                array_prop = line.replace("\n", "").split("=")
                if array_prop[0] in self.properties:
                    self.properties[array_prop[0]] = array_prop[1]
