from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .admin_page import AdminLoginPage
import random
import os
import time
import logging
import allure


class AdminProductPage(AdminLoginPage):
    # General tab
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, '#input-name1')
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, '.note-editable.panel-body p')
    META_FIELD = (By.CSS_SELECTOR, "#input-meta-title1")
    # Data tab
    DATA_TAB = (By.CSS_SELECTOR, '[href="#tab-data"]')
    MODEL_FIELD = (By.CSS_SELECTOR, "#input-model")
    PRICE_FIELD = (By.CSS_SELECTOR, "#input-price")
    TAX_CLASS = (By.CSS_SELECTOR, "#input-tax-class")
    QUANTITY_FIELD = (By.CSS_SELECTOR, "#input-quantity")
    OUT_OF_STOCK_STATUS = (By.CSS_SELECTOR, "#input-stock-status")
    DIMENSION_L = (By.CSS_SELECTOR, "#input-length")
    DIMENSION_W = (By.CSS_SELECTOR, "#input-width")
    DIMENSION_H = (By.CSS_SELECTOR, "#input-height")
    WEIGHT_FIELD = (By.CSS_SELECTOR, "#input-weight")
    SORT_ORDER_FIELD = (By.CSS_SELECTOR, "#input-sort-order")
    # Links tab
    LINK_TAB = (By.CSS_SELECTOR, '[href="#tab-links"]')
    MANUFACTURER_FIELD = (By.CSS_SELECTOR, '#input-manufacturer')
    CATEGORIES_FIELD = (By.CSS_SELECTOR, '#input-category')
    RELATED_PRODS_FIELD = (By.CSS_SELECTOR, "#input-related")
    # Image tab
    IMAGE_TAB = (By.CSS_SELECTOR, '[href="#tab-image"]')
    IMAGE_THUMBNAIL = (By.CSS_SELECTOR, '#thumb-image')
    ADD_IMG_THUMB = (By.CSS_SELECTOR, '#button-image')
    ADD_BUTTON = (By.CSS_SELECTOR, ".fa.fa-plus-circle")
    INPUT_FOR_IMG = (By.CSS_SELECTOR, "label + .note-image-input.form-control")
    MADE_BY_JS_INPUT = (By.CSS_SELECTOR, '#hard')
    CLOSE = (By.CSS_SELECTOR, ".close")
    # General
    SAVE_BUTTON = (By.CSS_SELECTOR, ".fa.fa-save")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    # Edit
    EDIT_BUTTONS = (By.CSS_SELECTOR, '[data-original-title="Edit"]')
    EDIT_PROD_TITLE = (By.CSS_SELECTOR, '.panel-title')
    CHECKBOXES = (By.CSS_SELECTOR, '[type="checkbox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, ".fa.fa-trash-o")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)

    @allure.story("Добавление описания на главную вкладку товара")
    def add_general_tab_info(self, product_name):
        with allure.step(f"Ищу поле {self.PRODUCT_NAME_FIELD}"):
            self.find(locator=self.PRODUCT_NAME_FIELD).send_keys(product_name)
        script = f'document.querySelector(".note-editable.panel-body p"). innerHTML = "{product_name} – классический мобильный телефон. ";'
        with allure.step(f"Выполняю скрипт поле {script}"):
            self.driver.execute_script(script)
        self.logger.info(f"Script work well")
        with allure.step(f"Отправляю название в поле {self.META_FIELD}"):
            self.find(locator=self.META_FIELD).send_keys("Fly")

    @allure.story("Добавление размеров и количество товара")
    def add_data_tab_info(self):
        with allure.step(f"Переключаюсь на вкладку с данными товара {self.DATA_TAB}"):
            self.find(locator=self.DATA_TAB).click()
        with allure.step(f"Отправляю название в поле {self.MODEL_FIELD}"):
            self.find(locator=self.MODEL_FIELD).send_keys("product22")
        with allure.step(f"Отправляю цену в поле {self.PRICE_FIELD}"):
            self.find(locator=self.PRICE_FIELD).send_keys("30.0000")
        with allure.step(f"Выбираю из dropdown {self.TAX_CLASS} тип товара"):
            Select(self.find(locator=self.TAX_CLASS)).select_by_index(1)
        with allure.step(f"Отправляю количество товара в поле {self.QUANTITY_FIELD}"):
            self.find(locator=self.QUANTITY_FIELD).send_keys("2342")
        with allure.step(f"Выбираю состояние товара из dropdown {self.OUT_OF_STOCK_STATUS}"):
            Select(self.find(locator=self.OUT_OF_STOCK_STATUS)).select_by_index(1)
        with allure.step(f"Отправляю длину товара в поле {self.DIMENSION_L}"):
            self.find(locator=self.DIMENSION_L).send_keys("50")
        with allure.step(f"Отправляю ширину товара в поле {self.DIMENSION_W}"):
            self.find(locator=self.DIMENSION_W).send_keys("107")
        with allure.step(f"Отправляю высоту товара в поле {self.DIMENSION_H}"):
            self.find(locator=self.DIMENSION_H).send_keys("15")
        with allure.step(f"Отправляю вес товара в поле {self.WEIGHT_FIELD}"):
            self.find(locator=self.WEIGHT_FIELD).send_keys("70")
        with allure.step(f"Отправляю количство заказов в поле {self.META_FIELD}"):
            self.find(locator=self.SORT_ORDER_FIELD).clear()
            self.find(locator=self.SORT_ORDER_FIELD).send_keys("0")
        with allure.step(f"Нажимаю на кнопку {self.SAVE_BUTTON}"):
            self.find(locator=self.SAVE_BUTTON).click()
        success_text = self.find(locator=self.SUCCESS_MESSAGE).text
        with allure.step(f"Найден текст {success_text}"):
            self.logger.info(f"Success message presented: {success_text}")
            return success_text

    @allure.story("Изменение случайного продукта в списке продуктов")
    def change_random_product(self):
        with allure.step(f"Ищу все кнопки редактирования на странице {self.EDIT_BUTTONS}"):
            edit_buttons = self.finds(locator=self.EDIT_BUTTONS)
        random_button_number = random.randrange(0, len(edit_buttons) + 1)
        random_button = edit_buttons[random_button_number].click()
        with allure.step(f"Выбрал случайную кнопку, и нажал {random_button}"):
            self.logger.info(f"Random button clicked: {edit_buttons[random_button_number]}")
        title = self.find(locator=self.EDIT_PROD_TITLE).text
        with allure.step(f"Найден текст {title}"):
            return title

    @allure.story("Удаление случайного продукта в списке продуктов")
    def remove_random_product(self):
        with allure.step(f"Ищу все чекбоксы на странице {self.CHECKBOXES}"):
            checkboxes = self.finds(locator=self.CHECKBOXES)
        random_checkboxes_number = random.randrange(1, len(checkboxes) + 1)
        checkboxes[random_checkboxes_number].click()
        with allure.step(f"Собираюсь нажать на {self.DELETE_BUTTON}"):
            self.find(locator=self.DELETE_BUTTON).click()
        with allure.step(f"Переключаюсь на алерт"):
            alert_obj = self.driver.switch_to.alert
            alert_obj.accept()
        self.logger.info(f"Alert accepted.")
        success_text = self.find(locator=self.SUCCESS_MESSAGE).text
        with allure.step(f"Алерт принят, текст {success_text} найден"):
            return success_text

    def add_image_to_product(self):
        edit_product = self.finds(locator=self.EDIT_BUTTONS)[3].click()
        self.find(locator=self.IMAGE_TAB).click()
        self.find(locator=self.IMAGE_THUMBNAIL).click()
        self.find(locator=self.ADD_IMG_THUMB).click()
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'jpg_pass.JPG')
        #time.sleep(4)
        js = '''
        document.getElementById("button-upload").setAttribute("onclick","document.getElementById('hard').click();");
        var element = document.getElementById("button-upload");
        var x = document.createElement("INPUT");
        x.setAttribute("type", "file");
        x.setAttribute("name", "name");
        x.setAttribute("style", "display")
        x.setAttribute("id", "hard");
        element.appendChild(x);'''
        self.driver.execute_script(js)
        input_manager = self.find(locator=self.MADE_BY_JS_INPUT)
        input_manager.send_keys(filename)
        time.sleep(5)
        self.find(locator=self.CLOSE).click()
        #alert = self.driver.switch_to.alert
        #time.sleep(5)
        #alert.accept()
