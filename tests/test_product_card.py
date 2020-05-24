from locators.ProductCardPage import ProductCardPageLocators
import time

# "https://demo.opencart.com/"

def test_add_to_basket_button(browser):
    link = "http://localhost/index.php?route=product/product&path=57&product_id=49"
    browser.get(link)
    target = browser.find_element(*ProductCardPageLocators.ADD_TO_BASKET_BUTTON)
    target.click()
    time.sleep(5)


def test_review_tab(browser):
    link = "http://localhost/index.php?route=product/product&path=57&product_id=49"
    browser.get(link)
    target = browser.find_element(*ProductCardPageLocators.REVIEW_TAB)
    target.click()
    time.sleep(5)


def test_add_to_fav_button(browser):
    link = "http://localhost/index.php?route=product/product&path=57&product_id=49"
    browser.get(link)
    target = browser.find_element(*ProductCardPageLocators.ADD_TO_FAV_BUTTON)
    target.click()
    time.sleep(5)


def test_additional_image(browser):
    link = "http://localhost/index.php?route=product/product&path=57&product_id=49"
    browser.get(link)
    target = browser.find_element(*ProductCardPageLocators.ADDITIONAL_IMAGES)
    target.click()
    time.sleep(5)


def test_go_to_device_types(browser):
    link = "http://localhost/index.php?route=product/product&path=57&product_id=49"
    browser.get(link)
    target = browser.find_element(*ProductCardPageLocators.TO_DEVICE_TYPES)
    target.click()
    time.sleep(5)