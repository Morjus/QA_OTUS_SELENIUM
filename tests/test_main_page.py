from locators.MainPage import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def clickable_waiter(driver, wait_time, *args):
    try:
        element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable(*args))
        return element
    except Exception as error:
        print(f"Error is:", error)
        return False


def test_search_field(browser):
    link = "http://localhost/"
    browser.get(link)
    target = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(MainPageLocators.SEARCH_FIELD))
    target.send_keys("Iphone")


def test_search_button(browser):
    link = "http://localhost/"
    browser.get(link)
    button = clickable_waiter(browser, 5, MainPageLocators.SEARCH_BUTTON)
    button.click()


def test_basket_button(browser):
    link = "http://localhost/"
    browser.get(link)
    button = clickable_waiter(browser, 5, MainPageLocators.BASKET_BUTTON)
    button.click()


def test_my_acc_dropdown(browser):
    link = "http://localhost/"
    browser.get(link)
    dropdown = clickable_waiter(browser, 5, MainPageLocators.MY_ACC_DROPDOWN)
    dropdown.click()


def test_adv_swiper_bullets(browser):
    link = "http://localhost/"
    browser.get(link)
    time.sleep(1)
    targets = WebDriverWait(browser, 1).\
        until(EC.visibility_of_all_elements_located(MainPageLocators.ADV_SWIPER_BULLETS))
    if targets:
        for element in targets:
            element.click()
            time.sleep(0.2)
