import pytest
from pages.catalogue_page import CataloguePage


def test_products_view_page(browser):
    page = CataloguePage(browser, url="http://localhost//index.php?route=product/category&path=20")
    page.open()
    page.change_list_view()


@pytest.mark.parametrize("menu_button", [i for i in range(0, 10)])
def test_sidebar_menu(browser, menu_button):
    page = CataloguePage(browser, url="http://localhost//index.php?route=product/category&path=20")
    page.open()
    page.side_bar_menu_click(menu_button)


@pytest.mark.parametrize("product",
                         [f'// *[ @ id = "content"] / div[4] / div[{num}] / div / div[2] / div[1] / h4 / a' for
                          num in range(1, 9)])
def test_go_to_product_card(browser, product):
    page = CataloguePage(browser, url="http://localhost//index.php?route=product/category&path=20")
    page.open()
    page.go_to_product_card(product)


@pytest.mark.parametrize("index, expected_text", [
    (0, "Default"),
    (1, "Name (A - Z)"),
    (2, "Name (Z - A)"),
    (3, "Price (Low > High)"),
    (4, "Price (High > Low)"),
    (5, "Rating (Highest)"),
    (6, "Rating (Lowest)"),
    (7, "Model (A - Z)"),
    (8, "Model (Z - A)")])
def test_sort_dropdown(browser, index, expected_text):
    page = CataloguePage(browser, url="http://localhost//index.php?route=product/category&path=20")
    page.open()
    page.sort_dropdown(index, expected_text)


@pytest.mark.parametrize("index, expected_text", [
    (0, "15"),
    (1, "25"),
    (2, "50"),
    (3, "75"),
    (4, "100")])
def test_sort_dropdown(browser, index, expected_text):
    page = CataloguePage(browser, url="http://localhost//index.php?route=product/category&path=20")
    page.open()
    page.show_dropdown(index, expected_text)
