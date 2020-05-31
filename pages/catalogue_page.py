from selenium.webdriver.common.by import By
from .base import BasePage
from selenium.webdriver.support.ui import Select


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

    def change_list_view(self):
        self.find(locator=self.LIST_VIEW_BUTTON).click()
        assert self.is_element_present(locator=self.CHECK_ACTIVE_VIEW_ELEMENT)

    def side_bar_menu_click(self, menu_button):
        menu_buttons = self.finds(locator=self.SIDEBAR_MENU)
        if menu_button in [0, len(menu_buttons)]:
            menu_object = menu_buttons[menu_button]
            text_in_menu_object = menu_object.text
            print(text_in_menu_object)
            menu_buttons[menu_button].click()
            page_header = self.find(locator=self.HEADER_2).text
            assert page_header in text_in_menu_object

    def go_to_product_card(self, product):
        product_button = self.find(locator=(By.XPATH, product))
        prod_name = self.find(locator=(By.XPATH, product)).text
        product_button.click()
        name_on_page = self.find(locator=self.PRODUCT_CARD_NAME).text
        assert prod_name in name_on_page

    def sort_dropdown(self, index, expected_text):
        dropdown = Select(self.find(locator=self.SORT_DROPDOWN))
        dropdown.select_by_index(index)
        dropdown_text = self.find(locator=self.SELECTED_DROPDOWN).text
        assert dropdown_text == expected_text

    def show_dropdown(self, index, expected_text):
        dropdown = Select(self.find(locator=self.SHOW_DROPDOWN))
        dropdown.select_by_index(index)
        dropdown_text = self.find(locator=self.SELECTED_SHOW_DROPDOWN).text
        print(dropdown_text)
        assert dropdown_text == expected_text
