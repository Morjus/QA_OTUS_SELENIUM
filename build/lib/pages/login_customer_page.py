from selenium.webdriver.common.by import By
from .base import BasePage
import logging
import allure


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
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="content"]/div/div/a')

    def __init__(self, driver, url=None):
        super().__init__(driver)
        self.driver = driver
        self.base_url = url
        self.logger = logging.getLogger(type(self).__name__)

    @allure.story("Переход на страницу регистрации")
    def go_reg_new_user(self):
        with allure.step(f"Нажимаю на кнопку {self.NEW_CUSTOMER}"):
            self.find(locator=self.NEW_CUSTOMER).click()
        header = self.find(locator=self.REG_HEADER).text
        with allure.step(f"Найден текст {header}"):
            self.logger.info(f"Registration page opened")
            assert "Register Account" in header, f"No such header on page, got {header}"

    @allure.story("Регистрация нового пользователя")
    def reg_new_user(self):
        with allure.step(f"Отправляю имя в {self.FIRST_NAME}"):
            self.find(locator=self.FIRST_NAME).send_keys('Ivan')
        with allure.step(f"Отправляю фамилию в {self.LAST_NAME}"):
            self.find(locator=self.LAST_NAME).send_keys('Ivanov')
        with allure.step(f"Отправляю адрес почты в {self.EMAIL}"):
            self.find(locator=self.EMAIL).send_keys('uvan@user.ru')
        with allure.step(f"Отправляю телефонный номер в {self.TELEPHONE}"):
            self.find(locator=self.TELEPHONE).send_keys('222222')
        with allure.step(f"Отправляю пароль в {self.PASSWORD}"):
            self.find(locator=self.PASSWORD).send_keys("1234")
        with allure.step(f"Подтверждаю пароль в {self.PASSWORD_CONFIRM}"):
            self.find(locator=self.PASSWORD_CONFIRM).send_keys("1234")
        with allure.step(f"Подтверждаю согласие на обработку данных {self.PRIVCY}"):
            self.find(locator=self.PRIVCY).click()
        with allure.step(f"Нажимаю далее {self.CONTINUE}"):
            self.find(locator=self.CONTINUE).click()
        header = self.find(locator=self.REG_HEADER).text
        with allure.step(f"Найден текст {header}. Пользователь зарегистрирован"):
            self.is_element_present(locator=self.CONTINUE_BUTTON)
            self.logger.info(f"New user registered")
            return header

    @allure.story("Сброс пароля")
    def reset_forgotten_password(self):
        with allure.step(f"Нажимаю на сброс пароля {self.FORGOTTEN_PASSWORD}"):
            self.find(locator=self.FORGOTTEN_PASSWORD).click()
        assert "Forgot Your Password?" == self.find(locator=self.REG_HEADER).text
        with allure.step(f"Ввожу почту для нового пароля {self.EMAIL}"):
            self.find(locator=self.EMAIL).send_keys('morjus@yandex.ru')
            with allure.step(f"Нажимаю далее {self.CONTINUE}"):
                self.find(locator=self.CONTINUE).click()
        print(self.find(
            locator=self.OK_MESSAGE).text)
        success_message = self.find(
            locator=self.OK_MESSAGE).text
        with allure.step(f"Найден текст {success_message}"):
            self.logger.info(f"Password resend")
            return success_message

    @allure.story("Авторизация существующего пользователя")
    def login_existed_user(self):
        with allure.step(f"Ввожу почту в {self.EMAIL}"):
            self.find(locator=self.EMAIL).send_keys('user@user.ru')
            with allure.step(f"Ввожу пароль в {self.PASSWORD}"):
                self.find(locator=self.PASSWORD).send_keys('user')
        with allure.step(f"Нажимаю кнопку для авторизации {self.LOGIN_BUTTON}"):
            self.find(locator=self.LOGIN_BUTTON).click()
        header = self.find(locator=self.LOGIN_HEADER).text
        with allure.step(f"Найден текст {header}."):
            self.logger.info(f"Header:{header} found")
            return header

    @allure.story("Переход на главную страницу со страницы регистрации/авторизации")
    def go_to_main_page(self):
        with allure.step(f"Нажимаю на кнопку {self.GO_TO_MAIN_PAGE}"):
            self.find(locator=self.GO_TO_MAIN_PAGE).click()
        main_page_header = self.find(locator=self.FEATURED).text
        with allure.step(f"Найден текст {main_page_header}."):
            self.logger.info(f"Main page header:{main_page_header}")
            return main_page_header
