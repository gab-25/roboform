import os
import time
from typing import Any, Dict

from selenium import webdriver

from roboform import constants
from roboform.form_logs import FormLogs
from .global_configs import GlobalConfigs


class Bot:

    def __init__(self, name: str, configs: Dict[str, Any]) -> None:
        tmp_path = os.path.join(GlobalConfigs.get_instance().home_path, ".tmp/")
        if not os.path.exists(tmp_path):
            os.mkdir(tmp_path)
        os.environ["TMPDIR"] = tmp_path

        profile_path = os.path.join(tmp_path, "roboform_profile")
        if not os.path.exists(profile_path):
            os.mkdir(profile_path)
        options = webdriver.FirefoxOptions()
        options.add_argument("-profile")
        options.add_argument(profile_path)

        self.driver = webdriver.Firefox(executable_path="./geckodriver", options=options)
        self.configs = configs
        self.logs = FormLogs(name)

    def exec(self) -> bool:
        url = self.configs[constants.FORM_CONFIGS_HEADER]["url"]
        self.driver.get(url)

        for config in self.configs:
            if not config == constants.FORM_CONFIGS_HEADER:
                try:
                    self.__exec_config(self.configs[config])
                except Exception as ex:
                    print(f"Error in form: {config}, cause: {ex}")
                    return False

        self.driver.quit()
        return True

    def __exec_config(self, config: Dict[str, Dict[str, Any]]):
        for items in config.items():
            comp = items[1]

            self.driver.switch_to.window(self.driver.window_handles[-1])

            if "wait" in comp:
                time.sleep(comp["wait"])

            try:
                if "id" in comp:
                    elem = self.driver.find_element_by_id(comp["id"])
                if "css_selector" in comp:
                    elem = self.driver.find_element_by_css_selector(comp["css_selector"])
                if "xpath" in comp:
                    elem = self.driver.find_element_by_xpath(comp["xpath"])
                if "class_name" in comp:
                    elem = self.driver.find_element_by_class_name(comp["class_name"])[1]
            except:
                raise Exception(f"element {items[0]} not found!")

            if comp["action"] == "insert":
                elem.clear()
                elem.send_keys(comp["text"])

            if comp["action"] == "click":
                elem.click()
