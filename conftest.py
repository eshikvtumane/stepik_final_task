import random

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, es...")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart")
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(30)

    yield browser
    print("\nquit")
    time.sleep(5)
    browser.quit()


@pytest.fixture(scope="function")
def generate_email():
    yield str(time.time()) + "@fakemail.org"


@pytest.fixture(scope="function")
def generate_password():
    hash = random.getrandbits(128)
    yield "%032x" % hash