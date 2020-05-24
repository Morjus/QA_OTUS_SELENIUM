from locators.ProductCardPage import ProductCardPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def clickable_waiter(driver, link, wait_time, *args):
    try:
        driver.get(link)
        element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable(*args))
        return element
    except Exception as error:
        print(f"Error is:", error)
        return False


def test_add_to_basket_button(browser):
    link = "http://localhost/index.php?route=product/product&path=57&product_id=49"
    button = clickable_waiter(browser, link, 5, ProductCardPageLocators.ADD_TO_BASKET_BUTTON)
    button.click()


def test_review_tab(browser):
    link = "http://localhost/index.php?route=product/product&path=57&product_id=49"
    button = clickable_waiter(browser, link, 5, ProductCardPageLocators.REVIEW_TAB)
    button.click()


def test_add_to_fav_button(browser):
    link = "http://localhost/index.php?route=product/product&path=57&product_id=49"
    button = clickable_waiter(browser, link, 5, ProductCardPageLocators.ADD_TO_FAV_BUTTON)
    button.click()


def test_additional_image(browser):
    link = "http://localhost/index.php?route=product/product&path=57&product_id=49"
    button = clickable_waiter(browser, link, 5, ProductCardPageLocators.ADDITIONAL_IMAGES)
    button.click()


def test_go_to_device_types(browser):
    link = "http://localhost/index.php?route=product/product&path=57&product_id=49"
    button = clickable_waiter(browser, link, 5, ProductCardPageLocators.TO_DEVICE_TYPES)
    button.click()
