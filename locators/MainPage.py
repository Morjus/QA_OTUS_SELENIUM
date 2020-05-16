from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, '[name="search"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.btn.btn-default.btn-lg')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn.btn-inverse.btn-lg')
    MY_ACC_DROPDOWN = (By.CSS_SELECTOR, '[title="My Account"]')
    ADV_SWIPER_BULLETS = (By.CSS_SELECTOR, '.swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets > * ')

