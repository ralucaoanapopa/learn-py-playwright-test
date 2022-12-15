from playwright.sync_api import Playwright, expect
import os

base_URL = 'https://demoqa.com/'
login_URL = base_URL+'login'
profile_URL = base_URL+'profile'

page_title = "ToolsQA"

user_name = os.environ.get('USERNAME_QA')
user_pass = os.environ.get('PASSWORD_QA')

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=400)
    context = browser.new_context(
        record_video_dir="../videos/"
    )
    page = context.new_page()

    page.goto(login_URL)
    page.get_by_placeholder("UserName").click()
    page.get_by_placeholder("UserName").fill(user_name)
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(user_pass)
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_title(page_title)
    expect(page).to_have_url(profile_URL)
    page.get_by_role("button", name="Log out").click()
    expect(page).to_have_url(login_URL)

    context.close()
    browser.close()
