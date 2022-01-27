from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "div:nth-child(1) .btn-group")


class BasketPageLocators:
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CORRECT_BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_ADDED_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages  div:nth-child(1) strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CORRECT_BOOK_PRICE = (By.CSS_SELECTOR, "#messages  div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages  div:nth-child(1) .alertinner")
