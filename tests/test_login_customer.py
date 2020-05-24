from locators.LoginCustomerPage import LoginCustomerPageLocators
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


def test_new_customer_button(browser):
    link = "http://localhost/index.php?route=account/login"
    browser.get(link)
    target = clickable_waiter(browser, 5, LoginCustomerPageLocators.NEW_CUSTOMER)
    target.click()


def test_forgotten_passw_button(browser):
    link = "http://localhost/index.php?route=account/login"
    browser.get(link)
    target = clickable_waiter(browser, 5, LoginCustomerPageLocators.FORGOTTEN_PASSWORD)
    target.click()


def test_login_existed_user(browser):
    link = "http://localhost/index.php?route=account/login"
    browser.get(link)
    email_field = clickable_waiter(browser, 5, LoginCustomerPageLocators.EMAIL_TEXT_FIELD)
    email_field.send_keys('user@user.ru')
    passw_field = clickable_waiter(browser, 5, LoginCustomerPageLocators.EMAIL_TEXT_FIELD)
    passw_field.send_keys('user')
    passw_field.submit()


def test_go_to_main_page_button(browser):
    link = "http://localhost/index.php?route=account/login"
    browser.get(link)
    target = clickable_waiter(browser, 5, LoginCustomerPageLocators.GO_TO_MAIN_PAGE)
    target.click()
