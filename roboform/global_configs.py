import os


class GlobalConfigs:
    __instance = None
    home_path = os.path.join(os.path.expanduser("~"), "roboform")

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
            with open(self.path, "w") as file:
                file.write("      ROBOFORM CONFIGS\n"
                           "***********************************")
