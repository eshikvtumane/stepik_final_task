from selenium.webdriver.common.by import By


class MainPageLocators():
    MAIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

    LOGIN_USERNAME_TEXTBOX = (By.ID, 'id_login-username')
    LOGIN_PASSWORD_TEXTBOX = (By.ID, 'id_login-password')
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name^="login_submit"]')

    REGISTER_LOGIN_TEXTBOX = (By.ID, 'id_registration-email')
    REGISTER_PASSPORT_TEXTBOX = (By.ID, 'id_registration-password1')
    REGISTER_CONFIRM_PASSPORT_TEXTBOX = (By.ID, 'id_registration-password2')
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name^="registration_submit"]')

    SUCCESS_REGISTER = (By.CSS_SELECTOR, 'div#messages>div>div>i.icon-ok-sign')


class ProductPageLocators():
    ADD_ITEM_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form>button[type^="submit"]')
    PRODUCT_NAME_TEXT = (By.CSS_SELECTOR, '.product_main>h1')
    SUCCESS_ADD_PRODUCT_TO_BASKET_TEXT = (By.CSS_SELECTOR, '.alertinner>strong:nth-child(1)')
    PRICE_TEXT = (By.CSS_SELECTOR, '.product_main>.price_color')
    MESSAGE_PRICE_TEXT = (By.CSS_SELECTOR, '.alertinner>p>strong')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini>span>a')
    BASKET_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]//p[contains(text(),"Your basket is empty.")]')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
