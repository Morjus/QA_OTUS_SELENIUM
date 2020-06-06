import time
from pages.product_card_page import ProductCardPage


def test_add_to_basket_button(browser):
    page = ProductCardPage(browser, url="http://localhost/index.php?route=product/product&path=57&product_id=49")
    page.open()
    prod_name, name_in_message, name_in_basket = page.add_to_basket()
    assert prod_name == name_in_message == name_in_basket, 'Names differ'


def test_review_tab(browser):
    page = ProductCardPage(browser, url="http://localhost/index.php?route=product/product&path=57&product_id=49")
    page.open()
    page.open_review_tab()
    text = page.write_review()
    assert "Thank you for your review. It has been submitted to the webmaster for approval." in text, \
        f'No success message, got {text}'


def test_add_to_fav_button(browser):
    page = ProductCardPage(browser, url="http://localhost/index.php?route=product/product&path=57&product_id=49")
    page.open()
    page.add_to_fav_button()


def test_additional_image(browser):
    page = ProductCardPage(browser, url="http://localhost/index.php?route=product/product&path=57&product_id=49")
    page.open()
    page.open_additional_images()


def test_go_to_device_types(browser):
    page = ProductCardPage(browser, url="http://localhost/index.php?route=product/product&path=57&product_id=49")
    page.open()
    device_type, device_header = page.go_to_device_types()
    assert device_type == device_header, f"{device_type} not equal {device_header}"
