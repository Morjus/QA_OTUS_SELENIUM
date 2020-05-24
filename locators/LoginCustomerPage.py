from selenium.webdriver.common.by import By


class LoginCustomerPageLocators:
    NEW_CUSTOMER = (By.CSS_SELECTOR, '.well > a')
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, '.form-group > a')
    EMAIL_TEXT_FIELD = (By.CSS_SELECTOR, '#input-email')
    PASSW_TEST_FIELD = (By.CSS_SELECTOR, '#input-password')
    GO_TO_MAIN_PAGE = (By.CSS_SELECTOR, '.breadcrumb li a')
