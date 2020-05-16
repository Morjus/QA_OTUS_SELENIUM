from selenium.webdriver.common.by import By


class ProductCardPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#button-cart')
    REVIEW_TAB = (By.CSS_SELECTOR, '.nav.nav-tabs :nth-child(2) > a')
    ADD_TO_FAV_BUTTON = (By.CSS_SELECTOR, '.btn-group [data-original-title="Add to Wish List"]')
    ADDITIONAL_IMAGES = (By.CSS_SELECTOR, '.image-additional > a')
    TO_DEVICE_TYPES = (By.CSS_SELECTOR, '.breadcrumb li:nth-last-child(2)')
