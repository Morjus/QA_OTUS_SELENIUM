from locators.MainPage import MainPageLocators
import time


def test_search_field(browser):
    link = "http://localhost/"
    browser.get(link)
    target = browser.find_element(*MainPageLocators.SEARCH_FIELD)
    target = target.send_keys("Iphone")
    time.sleep(5)
    # assert target == "Your Store", "No such element"


def test_search_button(browser):
    link = "http://localhost/"
    browser.get(link)
    target = browser.find_element(*MainPageLocators.SEARCH_BUTTON)
    target = target.click()
    time.sleep(5)


def test_basket_button(browser):
    link = "http://localhost/"
    browser.get(link)
    target = browser.find_element(*MainPageLocators.BASKET_BUTTON)
    target = target.click()
    time.sleep(5)


def test_my_acc_dropdown(browser):
    link = "http://localhost/"
    browser.get(link)
    target = browser.find_element(*MainPageLocators.MY_ACC_DROPDOWN)
    target = target.click()
    time.sleep(5)


def test_adv_swiper_bullets(browser):
    link = "http://localhost/"
    browser.get(link)
    target = browser.find_elements(*MainPageLocators.ADV_SWIPER_BULLETS)
    for element in target:
        element = element.click()
        time.sleep(2)
    time.sleep(5)
