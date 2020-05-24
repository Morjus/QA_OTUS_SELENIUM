import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.CataloguePage import CataloguePageLocators


def clickable_waiter(driver, wait_time, *args):
    try:
        element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable(*args))
        return element
    except Exception as error:
        print(f"Error is:", error)
        return False


def test_products_view_page(browser):
    link = "http://localhost//index.php?route=product/category&path=20"
    browser.get(link)
    button = clickable_waiter(browser, 5, CataloguePageLocators.LIST_VIEW_BUTTON)
    button.click()


def test_sidebar_menu(browser):
    link = "http://localhost//index.php?route=product/category&path=20"
    browser.get(link)
    target = browser.find_elements(*CataloguePageLocators.SIDEBAR_MENU)
    target[3].click()


@pytest.mark.parametrize("product",
                        [f'// *[ @ id = "content"] / div[4] / div[{num}] / div / div[2] / div[1] / h4 / a' for
                         num in range(1, 3)])
def test_products_in_grid(browser, product):
    link = "http://localhost//index.php?route=product/category&path=20"
    browser.get(link)
    button = clickable_waiter(browser, 5, (By.XPATH, product))
    button.click()


def test_sort_dropdown(browser):
    link = "http://localhost//index.php?route=product/category&path=20"
    browser.get(link)
    dropdown = clickable_waiter(browser, 5, CataloguePageLocators.SORT_DROPDOWN)
    dropdown = Select(dropdown)
    dropdown.select_by_index(4)


def test_show_dropdown(browser):
    link = "http://localhost//index.php?route=product/category&path=20"
    browser.get(link)
    dropdown = clickable_waiter(browser, 5, CataloguePageLocators.SHOW_DROPDOWN)
    dropdown = Select(dropdown)
    dropdown.select_by_index(4)
