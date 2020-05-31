from pages.admin_page import AdminLoginPage
from pages.product_page import AdminProductPage


def test_login_add_product(browser):
    page = AdminLoginPage(browser)
    page.open()
    page.login("user", "bitnami1")


def test_add_product(browser):
    page = AdminProductPage(browser)
    page.open()
    page.login("user", "bitnami1")
    page.go_to_product_page()
    page.add_new_product_page()
    page.add_general_tab_info("Fly Ezzy")
    page.add_data_tab_info()


def test_change_product(browser):
    page = AdminProductPage(browser)
    page.open()
    page.login("user", "bitnami1")
    page.go_to_product_page()
    page.change_random_product()


def test_remove_product(browser):
    page = AdminProductPage(browser)
    page.open()
    page.login("user", "bitnami1")
    page.go_to_product_page()
    page.remove_random_product()

