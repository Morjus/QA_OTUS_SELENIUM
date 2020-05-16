from selenium.webdriver.common.by import By


class CataloguePageLocators:
    SIDEBAR_MENU = (By.CSS_SELECTOR, '.list-group > *')
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, '[id="list-view"].btn.btn-default > *')
    PRODUCTS_LIST = (By.XPATH, '// *[ @ id = "content"] / div[4] / *')
    SORT_DROPDOWN = (By.CSS_SELECTOR, '#input-sort')
    SHOW_DROPDOWN = (By.CSS_SELECTOR, '#input-limit')

