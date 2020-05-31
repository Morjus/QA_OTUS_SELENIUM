from pages.login_customer_page import CustomerLoginPage


def test_new_customer_button(browser):
    page = CustomerLoginPage(browser, url="http://localhost/index.php?route=account/login")
    page.open()
    page.go_reg_new_user()
    page.reg_new_user()


def test_reset_password(browser):
    page = CustomerLoginPage(browser, url="http://localhost/index.php?route=account/login")
    page.open()
    page.reset_forgotten_password()


def test_login_existed_user(browser):
    page = CustomerLoginPage(browser, url="http://localhost/index.php?route=account/login")
    page.open()
    page.login_existed_user()


def test_go_to_main_page(browser):
    page = CustomerLoginPage(browser, url="http://localhost/index.php?route=account/login")
    page.open()
    page.go_to_main_page()
