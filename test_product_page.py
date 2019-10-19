import pytest
import time

from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    item_page = ProductPage(browser, link)
    item_page.open()
    item_page.add_to_card()
    item_page.solve_quiz_and_get_code()

    item_page.check_product_name_on_page_and_in_message()
    item_page.check_price_on_page_and_in_message()


@pytest.mark.need_review
@pytest.mark.tt
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    basket_page = BasketPage(browser, link)
    basket_page.open()
    basket_page.open_basket()
    basket_page.is_basket_empty()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    item_page = ProductPage(browser, link)
    item_page.open()
    item_page.add_to_card()
    item_page.is_not_element_present()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


@pytest.mark.xfail(strict=True)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    item_page = ProductPage(browser, link)
    item_page.open()
    item_page.add_to_card()
    item_page.is_not_element_present(*ProductPageLocators.SUCCESS_ADD_PRODUCT_TO_BASKET_TEXT)


@pytest.mark.login_auth
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page_login = LoginPage(browser, link)
        page_login.open()
        page_login.register_new_user(email, password)
        page_base = BasePage(browser, link)
        page_base.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        item_page = ProductPage(browser, link)
        item_page.open()
        item_page.add_to_card()
        item_page.check_product_name_on_page_and_in_message()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        item_page = ProductPage(browser, link)
        item_page.open()
        item_page.is_not_element_present(*ProductPageLocators.SUCCESS_ADD_PRODUCT_TO_BASKET_TEXT)

