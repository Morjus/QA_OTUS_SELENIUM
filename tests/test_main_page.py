from pages.main_page import MainPage
import pytest


@pytest.mark.parametrize("product", ["iPhone", "MacBook"])
def test_search_field(browser, product):
    page = MainPage(browser, url="http://localhost/")
    page.open()
    page.search_field(product)


def test_basket_button(browser):
    page = MainPage(browser, url="http://localhost/")
    page.open()
    page.go_to_basket()


@pytest.mark.parametrize("number", [0, 1])
def test_my_acc_dropdown(browser, number):
    page = MainPage(browser, url="http://localhost/")
    page.open()
    page.check_dropdown(number)


def test_adv_swiper_bullets(browser):
    page = MainPage(browser, url="http://localhost/")
    page.open()
    page.adv_swiper_bullets()
