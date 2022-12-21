from playwright.sync_api import expect
from pages.login_sauce import LoginSaucePage
from pages.inventory import InventoryPage
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

    inventory_page = InventoryPage(page)
    inventory_page.logout_user()

    expect(page).to_have_url(login_page.base_url)

def test_login_with_invalid_credentials(before_all_after_all):
    page = before_all_after_all

    login_page = LoginSaucePage(page)

    login_page.load()
    login_page.login_form(invalid_data, user_pass)

    expect(login_page.get_error_msg_login()).to_be_visible()
    expect(login_page.get_error_msg_login()).to_have_text(error_msg_invalid_credentials)