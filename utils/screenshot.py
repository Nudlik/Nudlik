import os.path
import time
from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class IScreenShot(ABC):

    @abstractmethod
    def make_screenshot(self, url: str, screen_name: str, tag: str) -> None:
        pass


class ScreenShot(IScreenShot):

    def __init__(self, browser_name: str, screen_root_dir: str) -> None:
        self.browser_name = browser_name.lower()
        self.driver = None
        self.screen_root_dir = screen_root_dir

    def make_screenshot(self, url: str, screen_name: str, tag: str) -> None:
        assert self.driver is not None, 'Browser is not open, use context manager to open it'
        self.driver.get(url)
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, tag)))
        except TimeoutException:
            time.sleep(10)
        self.driver.save_screenshot(os.path.join(self.screen_root_dir, screen_name))

    def __enter__(self):
        self.driver = self.get_driver()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()

    def get_driver(self):
        # TODO: тут пока не факт что на виртуальной машине гитхаба браузер откроется в нормальном разрешении
        web_drivers = {
            'firefox': webdriver.Firefox,
            'chrome': webdriver.Chrome,
        }
        return web_drivers.get(self.browser_name)()
