from locators.LoginCustomerPage import LoginCustomerPageLocators
import time


def test_new_customer_button(browser):
    link = "http://localhost/index.php?route=account/login"
    browser.get(link)
    target = browser.find_element(*LoginCustomerPageLocators.NEW_CUSTOMER)
    target.click()
    time.sleep(3)


def test_forgotten_passw_button(browser):
    link = "http://localhost/index.php?route=account/login"
    browser.get(link)
    target = browser.find_element(*LoginCustomerPageLocators.FORGOTTEN_PASSWORD)
    target.click()
    time.sleep(3)


def test_login_existed_user(browser):
    link = "http://localhost/index.php?route=account/login"
    browser.get(link)
    email_field = browser.find_element(*LoginCustomerPageLocators.EMAIL_TEXT_FIELD)
    email_field.send_keys('user@user.ru')
    passw_field = browser.find_element(*LoginCustomerPageLocators.PASSW_TEST_FIELD)
    passw_field.send_keys('user')
    passw_field.submit()
    time.sleep(3)


def test_go_to_main_page_button(browser):
    link = "http://localhost/index.php?route=account/login"
    browser.get(link)
    target = browser.find_element(*LoginCustomerPageLocators.GO_TO_MAIN_PAGE)
    target.click()
    time.sleep(3)
