from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import logging


class BasePage(object):

    def __init__(self, driver, url="http://localhost/admin/"):
        self.driver = driver
        self.base_url = url  # https://demo.opencart.com/admin/
        self.logger = logging.getLogger(type(self).__name__)

    def find(self, locator, time=10):
        self.logger.info(f"Finding element:{locator}")
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def finds(self, locator, time=10):
        self.logger.info(f"Finding elements:{locator}")
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def is_element_present(self, locator, time=10):
        self.logger.info(f"Finding element exists:{locator}")
        try:
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
        except NoSuchElementException:
            return False
        return True

    def open(self):
        self.logger.info(f"Opening:{self.base_url}")
        return self.driver.get(self.base_url)
