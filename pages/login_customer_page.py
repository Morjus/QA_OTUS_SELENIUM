from selenium.webdriver.common.by import By
from .base import BasePage


class CustomerLoginPage(BasePage):
    NEW_CUSTOMER = (By.CSS_SELECTOR, '.well > a')
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, '.form-group > a')
    EMAIL_TEXT_FIELD = (By.CSS_SELECTOR, '#input-email')
    PASSW_TEST_FIELD = (By.CSS_SELECTOR, '#input-password')
    GO_TO_MAIN_PAGE = (By.CSS_SELECTOR, '.breadcrumb li a')
    REG_HEADER = (By.CSS_SELECTOR, ".col-sm-9 h1")
    LOGIN_HEADER = (By.CSS_SELECTOR, ".col-sm-9 h2")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".form-group + .btn.btn-primary")
    FEATURED = (By.CSS_SELECTOR, "h3")
    # Register fields
    FIRST_NAME = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#input-confirm')
    NEWSLETTER = (By.CSS_SELECTOR, '.radio-inline [value="1"]')
    PRIVCY = (By.CSS_SELECTOR, '[name="agree"]')
    CONTINUE = (By.CSS_SELECTOR, '.btn.btn-primary')
    OK_MESSAGE = (By.CSS_SELECTOR, ".alert")

    def __init__(self, driver, url=None):
        super().__init__(driver)
        self.driver = driver
        self.base_url = url

    def go_reg_new_user(self):
        self.find(locator=self.NEW_CUSTOMER).click()
        assert "Register Account" == self.find(locator=self.REG_HEADER).text

    def reg_new_user(self):
        self.find(locator=self.FIRST_NAME).send_keys('Ivan')
        self.find(locator=self.LAST_NAME).send_keys('Ivanov')
        self.find(locator=self.EMAIL).send_keys('morjus@yandex.ru')
        self.find(locator=self.TELEPHONE).send_keys('222222')
        self.find(locator=self.PASSWORD).send_keys("1234")
        self.find(locator=self.PASSWORD_CONFIRM).send_keys("1234")
        self.find(locator=self.PRIVCY).click()
        self.find(locator=self.CONTINUE).click()
        assert "Your Account Has Been Created!" == self.find(locator=self.REG_HEADER).text

    def reset_forgotten_password(self):
        self.find(locator=self.FORGOTTEN_PASSWORD).click()
        assert "Forgot Your Password?" == self.find(locator=self.REG_HEADER).text
        self.find(locator=self.EMAIL).send_keys('morjus@yandex.ru')
        self.find(locator=self.CONTINUE).click()
        print(self.find(
            locator=self.OK_MESSAGE).text)
        assert "An email with a confirmation link has been sent your email address." == self.find(
            locator=self.OK_MESSAGE).text

    def login_existed_user(self):
        self.find(locator=self.EMAIL).send_keys('user@user.ru')
        self.find(locator=self.PASSWORD).send_keys('user')
        self.find(locator=self.LOGIN_BUTTON).click()
        assert "My Account" == self.find(locator=self.LOGIN_HEADER).text

    def go_to_main_page(self):
        self.find(locator=self.GO_TO_MAIN_PAGE).click()
        assert "Featured" == self.find(locator=self.FEATURED).text
