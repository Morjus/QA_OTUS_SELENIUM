from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePage(object):

    def __init__(self, driver, url="http://localhost/admin/"):
        self.driver = driver
        self.base_url = url  # https://demo.opencart.com/admin/

    def find(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def finds(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def is_element_present(self, locator, time=10):
        try:
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
        except NoSuchElementException:
            return False
        return True

    def open(self):
        return self.driver.get(self.base_url)
