from locators.LoginAdminPage import LoginAdminPageLocators
import time


def test_login_existed_user(browser):
    link = "http://localhost/admin/"
    browser.get(link)
    email_field = browser.find_element(*LoginAdminPageLocators.UNAME_FIELD)
    email_field.send_keys('user')
    passw_field = browser.find_element(*LoginAdminPageLocators.PASSW_FIELD)
    passw_field.send_keys('bitnami1')
    passw_field.submit()
    time.sleep(5)


def test_forgotten_passw(browser):
    link = "http://localhost/admin/"
    browser.get(link)
    forgotten_pass_link = browser.find_element(*LoginAdminPageLocators.FORGOTTEN_PASS)
    forgotten_pass_link.click()
    email_field = browser.find_element(*LoginAdminPageLocators.EMAIL_FIELD)
    email_field.send_keys('example@example.com')
    email_field.submit()
    time.sleep(5)


def test_cancel_button(browser):
    link = "http://localhost/admin/"
    browser.get(link)
    forgotten_pass_link = browser.find_element(*LoginAdminPageLocators.FORGOTTEN_PASS)
    forgotten_pass_link.click()
    time.sleep(5)
    cancel_button = browser.find_element(*LoginAdminPageLocators.CANCEL_BUTTON)
    cancel_button.click()
    time.sleep(5)