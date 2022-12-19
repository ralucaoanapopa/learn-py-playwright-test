from playwright.sync_api import expect
from pages.profile import ProfilePage
from pages.login import LoginPage
from mydata import *
import pytest, os

user_name = os.environ.get('USERNAME_QA')
user_pass = os.environ.get('PASSWORD_QA')

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

    login_page = LoginPage(page)

    login_page.load()
    login_page.login_form(user_name, user_pass)
    expect(page).to_have_title(login_page.title)

    profile_page = ProfilePage(page)
    expect(page).to_have_url(profile_page.profile_URL)
    assert profile_page.get_username_value() == user_name

    profile_page.logout()
    expect(page).to_have_url(login_page.login_URL)

def test_login_with_invalid_password(before_all_after_all):
    page = before_all_after_all

    login_page = LoginPage(page)

    login_page.load()
    login_page.login_form(user_name, invalid)

    assert login_page.get_error_login_msg() == error_msg_login

def test_login_with_invalid_username(before_all_after_all):
    page = before_all_after_all

    login_page = LoginPage(page)

    login_page.load()
    login_page.login_form(invalid, user_pass)

    assert login_page.get_error_login_msg() == error_msg_login

