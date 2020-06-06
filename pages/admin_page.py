from selenium.webdriver.common.by import By
from .base import BasePage


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

    def _set_username_(self, name):
        self.find(locator=self.UNAME_FIELD).clear()
        self.find(locator=self.UNAME_FIELD).send_keys(name)

    def _set_password_(self, PASSW_FIELD):
        self.find(locator=self.PASSW_FIELD).clear()
        self.find(locator=self.PASSW_FIELD).send_keys(PASSW_FIELD)

    def login(self, UNAME_FIELD, PASSW_FIELD):
        self._set_username_(UNAME_FIELD)
        self._set_password_(PASSW_FIELD)
        self.find(locator=self.SUBMIT_BUTTON).click()
        text = self.find(locator=self.HEADER).text
        return text

    def go_to_product_page(self):
        self.find(locator=self.CATALOG_MENU).click()
        self.find(locator=self.PRODUCTS_PAGE).click()
        text = self.find(locator=self.HEADER).text
        assert text == "Products"

    def add_new_product_page(self):
        self.find(locator=self.ADD_PRODUCT_BUTTON).click()
