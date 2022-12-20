from playwright.sync_api import expect
from pages.login_sauce import LoginSaucePage
from mydata import *
import pytest, os

user_name = os.environ.get('USER_SAUCE')
user_pass = os.environ.get('PASSWORD_SAUCE')

@pytest.fixture(scope="session", autouse=True)
def before_all_after_all(playwright):
    # create context for all tests
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    page = context.new_page()

    yield page
    page.close()

def test_login_with_valid_credentials(before_all_after_all):
    page = before_all_after_all

    login_page = LoginSaucePage(page)

    login_page.load()
    login_page.login_form(user_name, user_pass)
    expect(page).to_have_title(site_title)
    expect(page).to_have_url(login_page.inventory_url)