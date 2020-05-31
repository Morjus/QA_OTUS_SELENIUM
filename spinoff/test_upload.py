from pages.base import BasePage
from pages.product_page import AdminProductPage
import time
import os


def test_upload_mozilla_web(browser):
    # Initialize page
    page = BasePage(browser, url="https://developer.mozilla.org/ru/docs/Web/HTML/Element/Input/file")
    page.open()
    # Get path to file
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'jpg_pass.JPG')
    # Switch to frame
    page.driver.switch_to.frame(0)
    input_manager = page.driver.find_element_by_css_selector('[name="myFile"]')
    input_manager.send_keys(filename)
    time.sleep(4)


def test_add_image_to_opencart(browser):
    page = AdminProductPage(browser)
    page.open()
    page.login("user", "bitnami1")
    page.go_to_product_page()
    page.add_image_to_product()
