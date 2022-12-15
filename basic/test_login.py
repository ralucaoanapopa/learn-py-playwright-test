import pytest, os
from playwright.sync_api import expect

base_URL = 'https://demoqa.com/'
login_URL = base_URL+'login'
profile_URL = base_URL+'profile'

page_title = "ToolsQA"

username_id = '#userName'
passwd_id = '#password'
login_btn_id = '#login'
username_value_id = '#userName-value'

user_name = os.environ.get('USERNAME_QA')
user_pass = os.environ.get('PASSWORD_QA')

@pytest.fixture(scope="session", autouse=True)
def before_all_after_all(playwright):
    # Go to the starting url before all tests
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()

    page = context.new_page()
    page.goto(login_URL)

    expect(page).to_have_url(login_URL)
    expect(page).to_have_title(page_title)

    yield page
    page.close()

def test_login_with_valid_credentials(before_all_after_all):
    page = before_all_after_all
    
    page.fill(username_id, user_name)
    page.fill(passwd_id, user_pass)
    page.click(login_btn_id)

    expect(page).to_have_title(page_title)
    expect(page).to_have_url(profile_URL)
    expect(page.locator(username_value_id)).to_have_text(user_name)

    page.click("text=Log out")
    expect(page).to_have_url(login_URL)

def test_login_generated_with_codegen(before_all_after_all) -> None:
    page = before_all_after_all
    page.get_by_placeholder("UserName").fill(user_name)

    page.get_by_placeholder("Password").fill(user_pass)
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_title(page_title)
    expect(page).to_have_url(profile_URL)
    page.click("text=Log out")
    expect(page).to_have_url(login_URL)