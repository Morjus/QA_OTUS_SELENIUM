from selenium.webdriver.common.by import By
from .base import BasePage
import logging
import allure


class AdminLoginPage(BasePage):

    UNAME_FIELD = (By.CSS_SELECTOR, '#input-username')
    PASSW_FIELD = (By.CSS_SELECTOR, '#input-password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button')
    FORGOTTEN_PASS = (By.CSS_SELECTOR, '.help-block a')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#input-email')
    CANCEL_BUTTON = (By.CSS_SELECTOR, '.text-right a')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '#header div ul li:nth-child(2) a')
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, '.fa.fa-plus')
    HEADER = (By.CSS_SELECTOR, 'h1')
    CATALOG_MENU = (By.CSS_SELECTOR, '#menu-catalog a')
    PRODUCTS_PAGE = (By.XPATH, '//*[@id="collapse1"]/li[2]/a')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)

    def _set_username_(self, name):
        self.find(locator=self.UNAME_FIELD).clear()
        with allure.step(f"Отправляю логин {name} в {self.UNAME_FIELD}"):
            self.find(locator=self.UNAME_FIELD).send_keys(name)

    def _set_password_(self, passw):
        self.find(locator=self.PASSW_FIELD).clear()
        with allure.step(f"Отправляю пароль {passw} в {self.PASSW_FIELD}"):
            self.find(locator=self.PASSW_FIELD).send_keys(passw)

    def login(self, UNAME_FIELD, PASSW_FIELD):
        self._set_username(UNAME_FIELD)
        self._set_password(PASSW_FIELD)
        with allure.step(f"Нажимаю кнопку {self.SUBMIT_BUTTON}"):
            self.find(locator=self.SUBMIT_BUTTON).click()
        text = self.find(locator=self.HEADER).text
        self.logger.info(f"Logged to admin page")
        return text

    def go_to_product_page(self):
        with allure.step(f"Нажимаю на кнопку {self.CATALOG_MENU}"):
            self.find(locator=self.CATALOG_MENU).click()
        with allure.step(f"Нажимаю кнопку {self.PRODUCTS_PAGE}"):
            self.find(locator=self.PRODUCTS_PAGE).click()
        text = self.find(locator=self.HEADER).text
        self.logger.info(f"Opened product page")
        assert text == "Products"

    def add_new_product_page(self):
        with allure.step(f"Нажимаю на кнопку {self.ADD_PRODUCT_BUTTON}"):
            self.find(locator=self.ADD_PRODUCT_BUTTON).click()
        self.logger.info(f"Clicked to: {self.ADD_PRODUCT_BUTTON}")
