import pytest, os
from playwright.sync_api import Page, expect

base_URL = 'https://demoqa.com/'
login_URL = base_URL+'login'
profile_URL = base_URL+'profile'

page_title = "ToolsQA"

username_id = '#userName'
passwd_id = '#password'
loginBtn_id = '#login'

user_name = os.environ.get('USERNAME_QA')
user_pass = os.environ.get('PASSWORD_QA')

def test_login_with_valid_credentials(playwright, page: Page):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=200)
    page = browser.new_page()
    page.goto(login_URL)
    expect(page).to_have_url(login_URL)
    expect(page).to_have_title(page_title)

    page.fill(username_id, user_name)
    page.fill(passwd_id, user_pass)
    page.click(loginBtn_id)

    expect(page).to_have_title(page_title)
    expect(page).to_have_url(profile_URL)

    browser.close()