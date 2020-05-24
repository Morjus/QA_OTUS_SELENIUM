from locators.AdminProductPage import LoginAdminPageLocators, AddProductPageLocators, ProductPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import random
import time
import pytest


def click_wait(driver, *args, wait_time=5):
    try:
        element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable(*args))
        return element
    except TypeError as error:
        print(f"TypeError:", error)
        return False


@pytest.mark.skip
def test_login_existed_user(browser):
    link = "http://localhost/admin/"
    browser.get(link)
    email_field = click_wait(browser, LoginAdminPageLocators.UNAME_FIELD)
    email_field.send_keys('user')
    passw_field = click_wait(browser, LoginAdminPageLocators.PASSW_FIELD)
    passw_field.send_keys('bitnami1')
    passw_field.submit()


@pytest.mark.skip
def test_product_tables(browser):
    test_login_existed_user(browser)
    catalog_menu = click_wait(browser, LoginAdminPageLocators.CATALOG_MENU)
    catalog_menu.click()
    products_page = click_wait(browser, LoginAdminPageLocators.PRODUCTS_PAGE)
    products_page.click()
    wait = WebDriverWait(browser, 3)
    wait.until(EC.title_is("Products"))


def test_add_product(browser):
    test_product_tables(browser)
    button = click_wait(browser, LoginAdminPageLocators.ADD_PRODUCT_BUTTON).click()
    # General tab
    name_field = click_wait(browser, AddProductPageLocators.PRODUCT_NAME_FIELD).send_keys("Fly Ezzy")
    script = 'document.querySelector(".note-editable.panel-body p").' \
             'innerHTML = "Fly Ezzy 10 – классический мобильный телефон. ";'
    browser.execute_script(script)
    meta_field = click_wait(browser, AddProductPageLocators.META_FIELD).send_keys("Fly")
    # Switch to data tab
    data_tab = click_wait(browser, AddProductPageLocators.DATA_TAB).click()
    model = click_wait(browser, AddProductPageLocators.MODEL_FIELD).send_keys("product22")
    price = click_wait(browser, AddProductPageLocators.PRICE_FIELD).send_keys("30.0000")
    select_tax_class = Select(click_wait(browser, AddProductPageLocators.TAX_CLASS)).select_by_index(1)
    quantity = click_wait(browser, AddProductPageLocators.QUANTITY_FIELD).send_keys("2342")
    out_of_stock = Select(click_wait(browser, AddProductPageLocators.OUT_OF_STOCK_STATUS)).select_by_index(1)
    length = click_wait(browser, AddProductPageLocators.DIMENSION_L).send_keys("50")
    width = click_wait(browser, AddProductPageLocators.DIMENSION_W).send_keys("107")
    height = click_wait(browser, AddProductPageLocators.DIMENSION_H).send_keys("15")
    weight = click_wait(browser, AddProductPageLocators.WEIGHT_FIELD).send_keys("70")
    sort_order = click_wait(browser, AddProductPageLocators.SORT_ORDER_FIELD).clear()
    input_value_to_sort = click_wait(browser, AddProductPageLocators.SORT_ORDER_FIELD).send_keys("0")
    submit = click_wait(browser, AddProductPageLocators.SUBMIT_BUTTON).click()
    success_text = click_wait(browser, AddProductPageLocators.SUCCESS_MESSAGE).text
    assert "Success: You have modified products!" in success_text, "No success message"
    time.sleep(10)


def test_change_product(browser):
    test_product_tables(browser)
    edit_buttons = WebDriverWait(browser, 1).\
        until(EC.visibility_of_all_elements_located(ProductPageLocators.EDIT_BUTTONS))
    random_button_number = random.randrange(0, len(edit_buttons)+1)
    random_button = edit_buttons[random_button_number].click()
    title = click_wait(browser, ProductPageLocators.EDIT_PROD_TITLE).text
    assert "Edit Product" in title, "No 'Edit Product' in title"


def test_remove_product(browser):
    test_product_tables(browser)
    checkboxes = WebDriverWait(browser, 1). \
        until(EC.visibility_of_all_elements_located(ProductPageLocators.CHECKBOXES))
    random_checkboxes_number = random.randrange(1, len(checkboxes)+1)
    random_checkbox = checkboxes[random_checkboxes_number].click()

    delete_button = click_wait(browser, ProductPageLocators.DELETE_BUTTON).click()
    alert_obj = browser.switch_to.alert
    alert_obj.accept()
    success_text = click_wait(browser, AddProductPageLocators.SUCCESS_MESSAGE).text
    assert "Success: You have modified products!" in success_text, "No success message"
    time.sleep(10)


