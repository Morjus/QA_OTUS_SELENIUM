from selenium.webdriver.common.by import By
from .base import BasePage
import time
import logging
import allure


class MainPage(BasePage):
    # Search
    SEARCH_FIELD = (By.CSS_SELECTOR, '[name="search"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.btn.btn-default.btn-lg')
    SEARCH_HEADER = (By.CSS_SELECTOR, '.col-sm-12 h1')
    PRODUCT_CARD = (By.CSS_SELECTOR, 'h4')
    # Basket
    BASKET_BUTTON = (By.CSS_SELECTOR, '.fa.fa-shopping-cart')
    BASKET_HEADER = (By.CSS_SELECTOR, ".col-sm-12 h1")
    # Main page
    MY_ACC_DROPDOWN = (By.CSS_SELECTOR, '[title="My Account"]')
    ACC_DROPDOWN = (By.CSS_SELECTOR, ".dropdown-menu.dropdown-menu-right li a")
    HEADER = (By.CSS_SELECTOR, "col-sm-9 h1")
    ADV_SWIPER_BULLETS = (By.CSS_SELECTOR,
                          '.swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets > * ')

    def __init__(self, driver, url=None):
        super().__init__(driver)
        self.driver = driver
        self.base_url = url
        self.logger = logging.getLogger(type(self).__name__)

    @allure.story("Работоспособность поиска")
    def search_field(self, product):
        with allure.step(f"Отправляю в поисковое поле {self.SEARCH_FIELD} продукт {product}"):
            self.find(locator=self.SEARCH_FIELD).send_keys(product)
        self.logger.info(f"{product} sended to {self.SEARCH_FIELD}")
        with allure.step(f"Нажимаю кнопку поиска {self.SEARCH_BUTTON}"):
            self.find(locator=self.SEARCH_BUTTON).click()
        with allure.step(f"Ищу имя {product} в {self.SEARCH_HEADER}"):
            assert product in self.find(locator=self.SEARCH_HEADER).text
            return self.finds(locator=self.PRODUCT_CARD)

    @allure.story("Переход к корзине")
    def go_to_basket(self):
        with allure.step(f"Нажимаю кнопку корзины {self.BASKET_BUTTON}"):
            self.find(locator=self.BASKET_BUTTON).click()
        self.logger.info(f"Basket page opened")
        header = self.find(locator=self.BASKET_HEADER).text
        with allure.step(f"Найден текст {header}"):
            return header

    @allure.story("Нажатие на дропдауны")
    def check_dropdown(self, number):
        with allure.step(f"Ищу кнопки дропдауна {self.ACC_DROPDOWN}"):
            buttons = self.finds(locator=self.ACC_DROPDOWN)
        with allure.step(f"Нажимаю на элемент внутри дропдауна {self.MY_ACC_DROPDOWN}"):
            self.find(locator=self.MY_ACC_DROPDOWN).click()
        text = buttons[number].text.lower()
        buttons[number].click()
        self.logger.info(f"Button: {buttons[number]} clicked")
        return text

    @allure.story("Клик по витрине брендов")
    def adv_swiper_bullets(self):
        with allure.step(f"Ищу кнопки витрины {self.ADV_SWIPER_BULLETS}"):
            bullets = self.finds(locator=self.ADV_SWIPER_BULLETS)
        for element in bullets:
            with allure.step(f"Нажимаю на кнопку витрины {element}"):
                element.click()
                self.logger.info(f"Button: {element} clicked")
                time.sleep(0.2)
