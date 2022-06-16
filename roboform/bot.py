from configparser import ConfigParser
from selenium import webdriver


class Bot:

    def __init__(self, configs: ConfigParser) -> None:
        self.driver = webdriver.Firefox(executable_path="./geckodriver")
        self.configs =  configs

    def exec(self) -> bool:
        self.driver.get("http://www.python.org")
