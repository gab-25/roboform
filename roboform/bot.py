from configparser import ConfigParser
from selenium import webdriver
import os

from roboform.global_configs import GlobalConfigs


class Bot:

    def __init__(self, configs: ConfigParser) -> None:
        self.tmp_path = os.path.join(GlobalConfigs.get_instance().home_path, ".tmp/")
        if not os.path.exists(self.tmp_path):
            os.mkdir(self.tmp_path)
        os.environ["TMPDIR"] = self.tmp_path

        self.driver = webdriver.Firefox(executable_path="./geckodriver")
        self.configs = configs

    def exec(self) -> bool:
        self.driver.get("http://www.python.org")
