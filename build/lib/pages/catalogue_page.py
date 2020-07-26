from selenium.webdriver.common.by import By
from .base import BasePage
from selenium.webdriver.support.ui import Select
import logging
import allure


class CataloguePage(BasePage):
    SIDEBAR_MENU = (By.CSS_SELECTOR, '.list-group > *')
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, '[id="list-view"].btn.btn-default > *')
    PRODUCTS_LIST = (By.XPATH, '// *[ @ id = "content"] / div[4] / *')
    SORT_DROPDOWN = (By.CSS_SELECTOR, '#input-sort')
    SELECTED_DROPDOWN = (By.CSS_SELECTOR, '#input-sort option[selected="selected"]')
    SHOW_DROPDOWN = (By.CSS_SELECTOR, '#input-limit')
    SELECTED_SHOW_DROPDOWN = (By.CSS_SELECTOR, '#input-limit option[selected="selected"]')
    CHECK_ACTIVE_VIEW_ELEMENT = (By.CSS_SELECTOR, '[id="list-view"].btn.btn-default.active')
    HEADER_2 = (By.CSS_SELECTOR, "h2")
    PRODUCT_CARD_NAME = (By.CSS_SELECTOR, ".btn-group + h1")

    def __init__(self, driver, url=None):
        super().__init__(driver)
        self.driver = driver
        self.base_url = url
        self.logger = logging.getLogger(type(self).__name__)

    def change_list_view(self):
        with allure.step(f"Нажимаю кнопку {self.LIST_VIEW_BUTTON}"):
            self.find(locator=self.LIST_VIEW_BUTTON).click()
        self.logger.info(f"Change list view")
        return self.is_element_present(locator=self.CHECK_ACTIVE_VIEW_ELEMENT)

    def side_bar_menu_click(self, menu_button):
        with allure.step(f"Ищу кнопки меню {self.LIST_VIEW_BUTTON}"):
            menu_buttons = self.finds(locator=self.SIDEBAR_MENU)
        # if menu_button in [0, len(menu_buttons)]:
        menu_object = menu_buttons[menu_button]
        text_in_menu_object = menu_object.text
        with allure.step(f"Нажимаю на кнопку {menu_buttons[menu_button]}"):
            menu_buttons[menu_button].click()
        page_header = self.find(locator=self.HEADER_2).text
        self.logger.info(f"{page_header} and {text_in_menu_object} is on page")
        assert page_header in text_in_menu_object, f"{page_header} not equal {text_in_menu_object}, clicks missing"

    def go_to_product_card(self, product):
        with allure.step(f"Ищу кнопку продукта {(By.XPATH, product)}"):
            product_button = self.find(locator=(By.XPATH, product))
            prod_name = self.find(locator=(By.XPATH, product)).text
        with allure.step(f"Нашел {prod_name} и нажимаю на кнопку {product_button.locator}"):
            product_button.click()
        name_on_page = self.find(locator=self.PRODUCT_CARD_NAME).text
        with allure.step(f"Нашел текст {name_on_page}"):
            self.logger.info(f"{prod_name} and {name_on_page} found")
            return prod_name, name_on_page

    def sort_dropdown(self, index, expected_text):
        dropdown = Select(self.find(locator=self.SORT_DROPDOWN))
        with allure.step(f"Выбираю кнопку под номером {index}"):
            dropdown.select_by_index(index)
        dropdown_text = self.find(locator=self.SELECTED_DROPDOWN).text
        self.logger.info(f"{dropdown_text} and {expected_text} found")
        with allure.step(f"Найден текст {dropdown_text}"):
            return dropdown_text, expected_text

    def show_dropdown(self, index, expected_text):
        dropdown = Select(self.find(locator=self.SHOW_DROPDOWN))
        with allure.step(f"Выбираю кнопку под номером {index}"):
            dropdown.select_by_index(index)
        dropdown_text = self.find(locator=self.SELECTED_SHOW_DROPDOWN).text
        with allure.step(f"Найден текст {dropdown_text}"):
            self.logger.info(f"{dropdown_text} and {expected_text} found")
            return dropdown_text, expected_text
