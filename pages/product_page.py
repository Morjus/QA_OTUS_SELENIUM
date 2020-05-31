from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .admin_page import AdminLoginPage
import random


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
    ADD_IMG_THUMB = (By.CSS_SELECTOR, '.fa.fa-pencil')
    ADD_BUTTON = (By.CSS_SELECTOR, ".fa.fa-plus-circle")
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

    def add_general_tab_info(self, product_name):
        self.find(locator=self.PRODUCT_NAME_FIELD).send_keys(product_name)
        script = f'document.querySelector(".note-editable.panel-body p"). innerHTML = "{product_name} – классический мобильный телефон. ";'
        self.driver.execute_script(script)
        self.find(locator=self.META_FIELD).send_keys("Fly")

    def add_data_tab_info(self):
        self.find(locator=self.DATA_TAB).click()
        self.find(locator=self.MODEL_FIELD).send_keys("product22")
        self.find(locator=self.PRICE_FIELD).send_keys("30.0000")
        Select(self.find(locator=self.TAX_CLASS)).select_by_index(1)
        self.find(locator=self.QUANTITY_FIELD).send_keys("2342")
        Select(self.find(locator=self.OUT_OF_STOCK_STATUS)).select_by_index(1)
        self.find(locator=self.DIMENSION_L).send_keys("50")
        self.find(locator=self.DIMENSION_W).send_keys("107")
        self.find(locator=self.DIMENSION_H).send_keys("15")
        self.find(locator=self.WEIGHT_FIELD).send_keys("70")
        self.find(locator=self.SORT_ORDER_FIELD).clear()
        self.find(locator=self.SORT_ORDER_FIELD).send_keys("0")
        self.find(locator=self.SAVE_BUTTON).click()
        success_text = self.find(locator=self.SUCCESS_MESSAGE).text
        assert "Success: You have modified products!" in success_text, "No success message"

    def change_random_product(self):
        edit_buttons = self.finds(locator=self.EDIT_BUTTONS)
        random_button_number = random.randrange(0, len(edit_buttons) + 1)
        random_button = edit_buttons[random_button_number].click()
        title = self.find(locator=self.EDIT_PROD_TITLE).text
        assert "Edit Product" in title, "No 'Edit Product' in title"

    def remove_random_product(self):
        checkboxes = self.finds(locator=self.CHECKBOXES)
        random_checkboxes_number = random.randrange(1, len(checkboxes) + 1)
        checkboxes[random_checkboxes_number].click()
        self.find(locator=self.DELETE_BUTTON).click()
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()
        success_text = self.find(locator=self.SUCCESS_MESSAGE).text
        assert "Success: You have modified products!" in success_text, "No success message"
