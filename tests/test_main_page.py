from pages.main_page import MainPage
import pytest


@pytest.mark.parametrize("product", ["iPhone", "MacBook"])
def test_search_field(browser, product):
    page = MainPage(browser, url="http://localhost/")
    page.open()
    product_cards = page.search_field(product)
    for each in product_cards:
        assert product in each.text, f"No {product} in {each.text}"


def test_basket_button(browser):
    page = MainPage(browser, url="http://localhost/")
    page.open()
    text = page.go_to_basket()
    assert "Shopping Cart" == text, f"Header is wrong, got {text}"


@pytest.mark.parametrize("number", [0, 1])
def test_my_acc_dropdown(browser, number):
    page = MainPage(browser, url="http://localhost/")
    page.open()
    text = page.check_dropdown(number)
    assert text in page.driver.current_url, f"{text} not equal {page.driver.current_url}"


def test_adv_swiper_bullets(browser):
    page = MainPage(browser, url="http://localhost/")
    page.open()
    page.adv_swiper_bullets()
