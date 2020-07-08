from selenium.webdriver.common.by import By
from .base import BasePage
import allure
import logging


class ProductCardPage(BasePage):
    # Basket
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#button-cart')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".btn-group+h1")
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible a")
    PROD_NAME_IN_BASKET = (By.CSS_SELECTOR, ".text-left a")
    BASKET_BUTTON = (By.CSS_SELECTOR, "#cart button #cart-total")
    # Review tab
    REVIEW_TAB = (By.CSS_SELECTOR, '.nav.nav-tabs :nth-child(2) > a')
    REVIEW_HEADER = (By.CSS_SELECTOR, "#review + h2")
    INPUT_NAME = (By.CSS_SELECTOR, "#input-name")
    INPUT_TEXT = (By.CSS_SELECTOR, "#input-review")
    RADIO_BUTTON = (By.CSS_SELECTOR, '[type="radio"][value="5"]')
    SUBMIT_REVIEW = (By.CSS_SELECTOR, "#button-review")
    MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    # Fav
    ADD_TO_FAV_BUTTON = (By.CSS_SELECTOR, '.btn-group [data-original-title="Add to Wish List"]')
    ADDITIONAL_IMAGES = (By.CSS_SELECTOR, '.image-additional > a')
    # Images
    IMAGE = (By.CSS_SELECTOR, ".mfp-img")
    CLOSE_IMAGE = (By.CSS_SELECTOR, '[title="Close (Esc)"]')
    # DEVICE_TYPES
    TO_DEVICE_TYPES = (By.CSS_SELECTOR, '.breadcrumb li:nth-last-child(2)')
    TYPE_HEADER = (By.CSS_SELECTOR, "h2")

    def __init__(self, driver, url=None):
        super().__init__(driver)
        self.driver = driver
        self.base_url = url
        self.logger = logging.getLogger(type(self).__name__)

    @allure.story("Добавление в корзину")
    def add_to_basket(self):
        with allure.step(f"Ищу название продукта в {self.PRODUCT_NAME}"):
            prod_name = self.find(locator=self.PRODUCT_NAME).text
        with allure.step(f"Добавляю продукт в корзину {self.ADD_TO_BASKET_BUTTON}"):
            self.find(locator=self.ADD_TO_BASKET_BUTTON).click()
        name_in_message = self.find(locator=self.NAME_IN_MESSAGE).text
        with allure.step(f"Продукт в сообщении: {name_in_message}"):
            with allure.step(f"Нажимаю на кнопку корзины {self.BASKET_BUTTON}"):
                self.find(locator=self.BASKET_BUTTON).click()
        name_in_basket = self.find(locator=self.PROD_NAME_IN_BASKET).text
        self.logger.info(
            f"Found prod_name:{prod_name} name_in_message:{name_in_message} name_in_basket:{name_in_basket}")
        with allure.step(f"Найдено название продукта в корзине {name_in_basket}"):
            return prod_name, name_in_message, name_in_basket

    @allure.story("Просмотр обзоров")
    def open_review_tab(self):
        with allure.step(f"Нажимаю на кнопку обзоров {self.REVIEW_TAB}"):
            self.find(locator=self.REVIEW_TAB).click()
        review_header = self.find(locator=self.REVIEW_HEADER).text
        with allure.step(f"Найден текст продукта в корзине {review_header}"):
            self.logger.info("Review tab opened")
            assert "Write a review" == review_header, f"Wrong header name, got: {review_header}"

    @allure.story("Отправка обзора")
    def write_review(self):
        with allure.step(f"Отправляю имя обзорщика в {self.INPUT_NAME}"):
            self.find(locator=self.INPUT_NAME).send_keys("Ivan")
        with allure.step(f"Отправляю текст обзора в {self.INPUT_TEXT}"):
            self.find(locator=self.INPUT_TEXT).send_keys("""Galaxy Tab S6 Lite - 
        твой незаменимый помощник в создании заметок, которого легко взять с собой. 
        Планшет оснащен большим 10.4-дюймовым экраном в тонком и легком корпусе, 
        интерфейсом One UI 2 и электронным пером S Pen прямо из коробки. 
        Вне зависимости от того, занимаешься ли ты рисованием, учишься или играешь, 
        Galaxy Tab S6 Lite создан, чтобы быть здесь и сейчас.""")
        with allure.step(f"Нажимаю на радиокнопку {self.RADIO_BUTTON}"):
            self.find(locator=self.RADIO_BUTTON).click()
        with allure.step(f"Отправляю обзор с помощью кнопки {self.SUBMIT_REVIEW}"):
            self.find(locator=self.SUBMIT_REVIEW).click()
        text = self.find(locator=self.MESSAGE).text
        with allure.step(f"Найден текст об успехе отправки {text}"):
            self.logger.info(f"Final message after click{text}")
        return text

    @allure.story("Добавление в избранное")
    def add_to_fav_button(self):
        with allure.step(f"Нажимаю на кнопку избранное {self.ADD_TO_FAV_BUTTON}"):
            self.find(locator=self.ADD_TO_FAV_BUTTON).click()
        with allure.step(f"Проверяю, что сообщение об успехе появилось: {self.MESSAGE}"):
            self.is_element_present(locator=self.MESSAGE)
            self.logger.info(f"Element presented: {self.MESSAGE}")

    @allure.story("Просмотр изображений продукта")
    def open_additional_images(self):
        with allure.step(f"Нажимаю на изображения {self.ADDITIONAL_IMAGES}"):
            self.find(locator=self.ADDITIONAL_IMAGES).click()
            with allure.step(f"Нажимаю на изображение {self.IMAGE}"):
                self.find(locator=self.IMAGE).click()
                with allure.step(f"Нажимаю на изображение {self.IMAGE}"):
                    self.find(locator=self.IMAGE).click()
                    with allure.step(f"Нажимаю на изображение {self.IMAGE}"):
                        self.find(locator=self.IMAGE).click()
                        with allure.step(f"Нажимаю на изображение {self.IMAGE}"):
                            self.find(locator=self.IMAGE).click()
                            with allure.step(f"Закрываю просмотренные изображения {self.CLOSE_IMAGE}"):
                                self.find(locator=self.CLOSE_IMAGE).click()
        assert self.is_element_present(locator=self.ADDITIONAL_IMAGES), f"Element {self.ADDITIONAL_IMAGES} not found!"
        self.logger.info(f"Images clicked and closed")

    @allure.story("Переход к типам устройств")
    def go_to_device_types(self):
        with allure.step(f"Беру текст из {self.TO_DEVICE_TYPES}"):
            device_type = self.find(locator=self.TO_DEVICE_TYPES).text
        with allure.step(f"Нажимаю на кнопку {self.TO_DEVICE_TYPES}"):
            self.find(locator=self.TO_DEVICE_TYPES).click()
        device_header = self.find(locator=self.TYPE_HEADER).text
        with allure.step(f"Обнаружен текст {device_header}"):
            self.logger.info(f"Elements presented: device_type: {device_type} device_header:{device_header}")
            return device_type, device_header
