from selenium.webdriver.common.by import By


class LoginAdminPageLocators:
    UNAME_FIELD = (By.CSS_SELECTOR, '#input-username')
    PASSW_FIELD = (By.CSS_SELECTOR, '#input-password')
    FORGOTTEN_PASS = (By.CSS_SELECTOR, '.help-block a')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#input-email')
    CANCEL_BUTTON = (By.CSS_SELECTOR, '.text-right a')
