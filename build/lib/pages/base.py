from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import logging
import allure


class BasePage(object):

    def __init__(self, driver, url="http://localhost/admin/"):
        self.driver = driver
        self.base_url = url  # https://demo.opencart.com/admin/
        self.logger = logging.getLogger(type(self).__name__)

    def find(self, locator, time=10):
        self.logger.info(f"Finding element:{locator}")
        with allure.step(f"Ищу элемент {locator}"):
            try:
                return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                              message=f"Can't find element by locator {locator}")
            except NoSuchElementException as e:
                allure.attach(body=self.driver.get_screenshot_as_png(),
                              name=f"{self.driver.session_id}",
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError(e.msg)

    def finds(self, locator, time=10):
        self.logger.info(f"Finding elements:{locator}")
        with allure.step(f"Ищу элементы {locator}"):
            try:
                return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                              message=f"Can't find elements by locator {locator}")
            except NoSuchElementException as e:
                allure.attach(body=self.driver.get_screenshot_as_png(),
                              name=f"{self.driver.session_id}",
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError(e.msg)

    def is_element_present(self, locator, time=10):
        self.logger.info(f"Finding element exists:{locator}")
        with allure.step(f"Проверяю наличие элемента на странице {locator}"):
            try:
                WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                       message=f"Can't find elements by locator {locator}")
            except NoSuchElementException:
                return False
            return True

    def open(self):
        with allure.step(f"Открыаю страницу {self.base_url}"):
            self.logger.info(f"Opening:{self.base_url}")
            return self.driver.get(self.base_url)
