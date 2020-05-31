import time
from pages.product_card_page import ProductCardPage


def test_add_to_basket_button(browser):
    page = ProductCardPage(browser, url="http://localhost/index.php?route=product/product&path=57&product_id=49")
    page.open()
    page.add_to_basket()


def test_review_tab(browser):
    page = ProductCardPage(browser, url="http://localhost/index.php?route=product/product&path=57&product_id=49")
    page.open()
    page.open_review_tab()
    page.write_review()


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
    page.go_to_device_types()
