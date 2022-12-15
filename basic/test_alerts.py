import pytest
from playwright.sync_api import expect

base_URL = 'https://demoqa.com/alerts'
page_title = "ToolsQA"

button_one = '#alertButton'
button_three = '#confirmButton'
button_four = '#promtButton'

confirm_result_id = "#confirmResult"
confirm_message = "Cancel"
accept_message = "Accept this prompt alert"
prompt_result_id = '#promptResult'

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()

    page = context.new_page()
    page.goto(base_URL)
    expect(page).to_have_url(base_URL)
    expect(page).to_have_title(page_title)
    yield page
    page.close()

def test_accept_simple_alert(before_each_after_each):
    page = before_each_after_each

    # create a listener in order to accept
    page.on("dialog", lambda dialog: dialog.accept())

    # launch the simple alert
    page.locator(button_one).click()
    
def test_cancel_alert(before_each_after_each):
    page = before_each_after_each

    page.on("dialog", lambda dialog: dialog.dismiss())

    # launch the confirm alert
    page.locator(button_three).click()

    expect(page.locator(confirm_result_id)).to_contain_text(confirm_message)

def test_handle_prompt_alert(before_each_after_each):
    page = before_each_after_each

    page.on("dialog", lambda dialog: dialog.accept(accept_message))
    page.locator(button_four).click()

    # launch the prompt alert
    expect(page.locator(prompt_result_id)).to_contain_text(accept_message)
    