from locators.LoginAdminPage import LoginAdminPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


def clickable_waiter(driver, wait_time, *args):
    try:
        element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable(*args))
        return element
    except Exception as error:
        print(f"Error is:", error)
        return False


@pytest.mark.skip
def test_login_existed_user(browser):
    link = "http://localhost/admin/"
    browser.get(link)
    email_field = clickable_waiter(browser, 5, LoginAdminPageLocators.UNAME_FIELD)
    email_field.send_keys('user')
    passw_field = clickable_waiter(browser, 5, LoginAdminPageLocators.PASSW_FIELD)
    passw_field.send_keys('bitnami1')
    passw_field.submit()


def test_logout_existed_user(browser):
    test_login_existed_user(browser)
    logout = clickable_waiter(browser, 5, LoginAdminPageLocators.LOGOUT_BUTTON)
    logout.click()


def test_product_tables(browser):
    test_login_existed_user(browser)
    catalog_menu = clickable_waiter(browser, 5, LoginAdminPageLocators.CATALOG_MENU)
    catalog_menu.click()
    products_page = clickable_waiter(browser, 5, LoginAdminPageLocators.PRODUCTS_PAGE)
    products_page.click()
    wait = WebDriverWait(browser, 3)
    wait.until(EC.title_is("Products"))


@pytest.mark.skip
def test_forgotten_passw(browser):
    link = "http://localhost/admin/"
    browser.get(link)
    forgotten_pass_link = clickable_waiter(browser, 5, LoginAdminPageLocators.FORGOTTEN_PASS)
    forgotten_pass_link.click()
    email_field = clickable_waiter(browser, 5, LoginAdminPageLocators.EMAIL_FIELD)
    email_field.send_keys('example@example.com')
    email_field.submit()


@pytest.mark.skip
def test_cancel_button(browser):
    link = "http://localhost/admin/"
    browser.get(link)
    forgotten_pass_link = clickable_waiter(browser, 5, LoginAdminPageLocators.FORGOTTEN_PASS)
    forgotten_pass_link.click()
    cancel_button = clickable_waiter(browser, 5, LoginAdminPageLocators.CANCEL_BUTTON)
    cancel_button.click()
    time.sleep(5)
