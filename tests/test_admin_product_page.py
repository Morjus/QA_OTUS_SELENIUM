from pages.admin_page import AdminLoginPage
from pages.product_page import AdminProductPage
import logging
import allure


@allure.feature('Авторизация администратора')
def test_login_add_product(browser):
    page = AdminLoginPage(browser)
    page.open()
    header = page.login("user", "bitnami1")
    assert header == "Dashboard", f"No 'Dashboard' header, got {header}"


@allure.feature('Каталог продуктов администратора')
def test_add_product(browser):
    page = AdminProductPage(browser)
    page.open()
    page.login("user", "bitnami1")
    page.go_to_product_page()
    page.add_new_product_page()
    page.add_general_tab_info("Fly Ezzy")
    success_message = page.add_data_tab_info()
    browser_logs = page.driver.get_log("browser")
    logger = logging.getLogger(__name__)
    logger.info('====== Started browser logs ======')
    for row in browser_logs:
        logger.info(row)
    logger.info('====== Finished browser logs ======')

    assert "Success: You have modified products!" in success_message, "No success message"


@allure.feature('Каталог продуктов администратора')
def test_change_product(browser):
    page = AdminProductPage(browser)
    page.open()
    page.login("user", "bitnami1")
    page.go_to_product_page()
    title = page.change_random_product()
    assert "Edit Product" in title, "No 'Edit Product' in title"


@allure.feature('Каталог продуктов администратора')
def test_remove_product(browser):
    page = AdminProductPage(browser)
    page.open()
    page.login("user", "bitnami1")
    page.go_to_product_page()
    with allure.step(f"Удаляю случайный продукт из каталога"):
        success_message = page.remove_random_product()
    logger = logging.getLogger(__name__)
    logger.info('====== Started browser logs ======')
    for row in page.driver.har['log']:
        logger.info(row)
    logger.info('====== Finished browser logs ======')
    assert "Success: You have modified products!" in success_message, "No success message"
