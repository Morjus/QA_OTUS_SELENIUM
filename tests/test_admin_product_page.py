from pages.admin_page import AdminLoginPage
from pages.product_page import AdminProductPage


def test_login_add_product(browser):
    page = AdminLoginPage(browser)
    page.open()
    header = page.login("user", "bitnami1")
    assert header == "Dashboard", f"No 'Dashboard' header, got {header}"


def test_add_product(browser):
    page = AdminProductPage(browser)
    page.open()
    page.login("user", "bitnami1")
    page.go_to_product_page()
    page.add_new_product_page()
    page.add_general_tab_info("Fly Ezzy")
    success_message = page.add_data_tab_info()
    assert "Success: You have modified products!" in success_message, "No success message"


def test_change_product(browser):
    page = AdminProductPage(browser)
    page.open()
    page.login("user", "bitnami1")
    page.go_to_product_page()
    title = page.change_random_product()
    assert "Edit Product" in title, "No 'Edit Product' in title"


def test_remove_product(browser):
    page = AdminProductPage(browser)
    page.open()
    page.login("user", "bitnami1")
    page.go_to_product_page()
    success_message = page.remove_random_product()
    assert "Success: You have modified products!" in success_message, "No success message"

