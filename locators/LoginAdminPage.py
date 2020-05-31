from selenium.webdriver.common.by import By


class LoginAdminPageLocators:
    UNAME_FIELD = (By.CSS_SELECTOR, '#input-username')
    PASSW_FIELD = (By.CSS_SELECTOR, '#input-password')
    FORGOTTEN_PASS = (By.CSS_SELECTOR, '.help-block a')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#input-email')
    CANCEL_BUTTON = (By.CSS_SELECTOR, '.text-right a')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '#header div ul li:nth-child(2) a')
    CATALOG_MENU = (By.CSS_SELECTOR, '#menu-catalog a')
    PRODUCTS_PAGE = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(2) > a')
