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
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, '.fa.fa-plus')


class AddProductPageLocators:
    # General tab
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, '#input-name1')
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, '.note-editable.panel-body p')
    META_FIELD = (By.CSS_SELECTOR, "#input-meta-title1")
    # Data tab
    DATA_TAB = (By.CSS_SELECTOR, '[href="#tab-data"]')
    MODEL_FIELD = (By.CSS_SELECTOR, "#input-model")
    PRICE_FIELD = (By.CSS_SELECTOR, "#input-price")
    TAX_CLASS = (By.CSS_SELECTOR, "#input-tax-class")
    QUANTITY_FIELD = (By.CSS_SELECTOR, "#input-quantity")
    OUT_OF_STOCK_STATUS = (By.CSS_SELECTOR, "#input-stock-status")
    DIMENSION_L = (By.CSS_SELECTOR, "#input-length")
    DIMENSION_W = (By.CSS_SELECTOR, "#input-width")
    DIMENSION_H = (By.CSS_SELECTOR, "#input-height")
    WEIGHT_FIELD = (By.CSS_SELECTOR, "#input-weight")
    SORT_ORDER_FIELD = (By.CSS_SELECTOR, "#input-sort-order")
    # Links tab
    LINK_TAB = (By.CSS_SELECTOR, '[href="#tab-links"]')
    MANUFACTURER_FIELD = (By.CSS_SELECTOR, '#input-manufacturer')
    CATEGORIES_FIELD = (By.CSS_SELECTOR, '#input-category')
    RELATED_PRODS_FIELD = (By.CSS_SELECTOR, "#input-related")
    # Image tab
    IMAGE_TAB = (By.CSS_SELECTOR, '[href="#tab-image"]')
    IMAGE_THUMBNAIL = (By.CSS_SELECTOR, '#thumb-image')
    ADD_IMG_THUMB = (By.CSS_SELECTOR, '.fa.fa-pencil')
    ADD_BUTTON = (By.CSS_SELECTOR, ".fa.fa-plus-circle")
    # General
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".fa.fa-save")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")


class ProductPageLocators:
    EDIT_BUTTONS = (By.CSS_SELECTOR, '[data-original-title="Edit"]')
    EDIT_PROD_TITLE = (By.CSS_SELECTOR, '.panel-title')
    CHECKBOXES = (By.CSS_SELECTOR, '[type="checkbox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, ".fa.fa-trash-o")