import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from locators.CataloguePage import CataloguePageLocators


def test_products_view_page(browser):
    link = "http://localhost//index.php?route=product/category&path=20"
    browser.get(link)
    target = browser.find_element(*CataloguePageLocators.LIST_VIEW_BUTTON)
    time.sleep(5)
    target.click()
    time.sleep(5)


def test_sidebar_menu(browser):
    link = "http://localhost//index.php?route=product/category&path=20"
    browser.get(link)
    target = browser.find_elements(*CataloguePageLocators.SIDEBAR_MENU)
    target[3].click()
    time.sleep(5)


@pytest.mark.parametrize("product",
                        [f'// *[ @ id = "content"] / div[4] / div[{num}] / div / div[2] / div[1] / h4 / a' for
                         num in range(1, 3)])
def test_products_in_grid(browser, product):
    link = "http://localhost//index.php?route=product/category&path=20"
    browser.get(link)
    target = browser.find_element(By.XPATH, product)
    target.click()
    time.sleep(1)


def test_sort_dropdown(browser):
    link = "http://localhost//index.php?route=product/category&path=20"
    browser.get(link)
    dropdown = Select(browser.find_element(*CataloguePageLocators.SORT_DROPDOWN))
    dropdown.select_by_index(4)
    time.sleep(5)


def test_show_dropdown(browser):
    link = "http://localhost//index.php?route=product/category&path=20"
    browser.get(link)
    dropdown = Select(browser.find_element(*CataloguePageLocators.SHOW_DROPDOWN))
    dropdown.select_by_index(4)
    time.sleep(5)
