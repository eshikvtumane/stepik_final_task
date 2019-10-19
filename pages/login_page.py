from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.url == 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'

    def should_be_login_form(self):
        result = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert result

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        result = self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert result

    def register_new_user(self, email, password):
        self.browser.get('http://selenium1py.pythonanywhere.com/ru/accounts/login/')
        self.browser.find_element(*LoginPageLocators.REGISTER_LOGIN_TEXTBOX).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSPORT_TEXTBOX).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSPORT_TEXTBOX).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON).click()

        # try:
        #     WebDriverWait(self.browser, 20).until(expected_conditions.presence_of_element_located(*LoginPageLocators.SUCCESS_REGISTER))
        #     return True
        # except:
        #     return False


