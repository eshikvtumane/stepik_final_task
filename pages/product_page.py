from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_card(self)->bool:
        try:
            self.browser.find_element(*ProductPageLocators.ADD_ITEM_BUTTON).click()
            return True
        except NoSuchElementException:
            return False

    def get_product_name(self)->str:
        try:
            return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_TEXT).text
        except NoSuchElementException:
            return None

    def get_success_message_after_add_product_to_basket(self)->str:
        WebDriverWait(self.browser, 20).until(expected_conditions.presence_of_element_located(ProductPageLocators.SUCCESS_ADD_PRODUCT_TO_BASKET_TEXT))
        try:
            return self.browser.find_element(*ProductPageLocators.SUCCESS_ADD_PRODUCT_TO_BASKET_TEXT).text
        except NoSuchElementException:
            return None

    def get_price(self)->str:
        try:
            return self.browser.find_element(*ProductPageLocators.PRICE_TEXT).text
        except NoSuchElementException:
            return None

    def get_price_from_message(self)->str:
        WebDriverWait(self.browser, 20).until(expected_conditions.presence_of_element_located(ProductPageLocators.MESSAGE_PRICE_TEXT))
        try:
            return self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_TEXT).text
        except NoSuchElementException:
            return None

    def check_product_name_on_page_and_in_message(self):
        result = self.get_success_message_after_add_product_to_basket()
        product_name = self.get_product_name()

        assert result == product_name, 'Product name dont equal'

    def check_price_on_page_and_in_message(self):
        price = self.get_price()
        price_from_message = self.get_price_from_message()
        assert price == price_from_message, 'Price dont equal'