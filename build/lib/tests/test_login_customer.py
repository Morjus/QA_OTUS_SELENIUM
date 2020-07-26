from pages.login_customer_page import CustomerLoginPage
import allure


@allure.feature('Регистрация')
def test_new_customer_button(browser):
    page = CustomerLoginPage(browser, url="http://localhost/index.php?route=account/login")
    page.open()
    page.go_reg_new_user()
    created_acc = page.reg_new_user()
    assert "Your Account Has Been Created!" == created_acc, f"No such header on page, got {created_acc}"


@allure.feature('Авторизация')
def test_reset_password(browser):
    page = CustomerLoginPage(browser, url="http://localhost/index.php?route=account/login")
    page.open()
    success_message = page.reset_forgotten_password()
    assert "An email with a confirmation link has been sent your email address." == success_message, \
        f"No OK message, got {success_message}"


@allure.feature('Авторизация')
def test_login_existed_user(browser):
    page = CustomerLoginPage(browser, url="http://localhost/index.php?route=account/login")
    page.open()
    header = page.login_existed_user()
    assert "My Account" == header, f"No such header on page, got {header}"


@allure.feature('Переход к главной странице со страницы регистрации')
def test_go_to_main_page(browser):
    page = CustomerLoginPage(browser, url="http://localhost/index.php?route=account/login")
    page.open()
    main_page_header = page.go_to_main_page()
    assert "Featured" == main_page_header, f"No such header on page, got {main_page_header}"
