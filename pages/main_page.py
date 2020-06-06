from selenium.webdriver.common.by import By
from .base import BasePage
import time


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

    def search_field(self, product):
        self.find(locator=self.SEARCH_FIELD).send_keys(product)
        self.find(locator=self.SEARCH_BUTTON).click()
        assert product in self.find(locator=self.SEARCH_HEADER).text
        return self.finds(locator=self.PRODUCT_CARD)

    def go_to_basket(self):
        self.find(locator=self.BASKET_BUTTON).click()
        return self.find(locator=self.BASKET_HEADER).text

    def check_dropdown(self, number):
        buttons = self.finds(locator=self.ACC_DROPDOWN)
        self.find(locator=self.MY_ACC_DROPDOWN).click()
        text = buttons[number].text.lower()
        buttons[number].click()
        return text

    def adv_swiper_bullets(self):
        bullets = self.finds(locator=self.ADV_SWIPER_BULLETS)
        for element in bullets:
            element.click()
            time.sleep(0.2)
