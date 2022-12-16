import pytest
from playwright.sync_api import expect

base_URL = 'https://demoqa.com/'
browser_windows_demoqa_URL = base_URL + 'browser-windows'
sample_demoqa_URL = base_URL + 'sample'
page_title = 'ToolsQA'

btn_newTab_id = '#tabButton'
h1_content_id = '#sampleHeading'
content_sample_page = 'This is a sample page'

base_letcode_URL = 'https://letcode.in/'
windows_letcode_URL = base_letcode_URL + 'windows'
homepage_letcode_URL = base_letcode_URL + 'test'
signin_letcode_URL = base_letcode_URL + 'signin'
product_letcode_URL = base_letcode_URL + 'letxpath'
alert_letcode_URL = base_letcode_URL + 'alert'
dropdowns_letcode_URL = base_letcode_URL + 'dropdowns'
btn_home_id = '#home'
btn_multiple_id = '#multi'
btn_simple_alert_id = '#accept'

@pytest.fixture(scope="session", autouse=True)
def before_all_after_all(playwright):
    # create context for all tests
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    yield context
    context.close()

def test_single_page_handling_on_demoqa(before_all_after_all):
    context = before_all_after_all

    page = context.new_page()
    page.goto(browser_windows_demoqa_URL)
    expect(page).to_have_title(page_title)
    expect(page).to_have_url(browser_windows_demoqa_URL)

    # get page after a specific action (eg: click a button)
    with context.expect_page() as new_page_info:
        page.locator(btn_newTab_id).click() # opens a new tab
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    expect(new_page).to_have_url(sample_demoqa_URL)

    assert new_page.inner_text(h1_content_id) == content_sample_page
    new_page.close()
    page.close()

def test_single_page_handling_on_letcode(before_all_after_all):
    context = before_all_after_all

    page = context.new_page()
    page.goto(windows_letcode_URL)
    expect(page).to_have_url(windows_letcode_URL)

    with context.expect_page() as new_page_info:
        page.locator(btn_home_id).click() # opens a new tab
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    expect(new_page).to_have_url(homepage_letcode_URL)

    new_page.click('text="Log in"')
    expect(new_page).to_have_url(signin_letcode_URL)

    # activates tab from which started test
    page.bring_to_front()
    page.click('text="Product"')
    expect(page).to_have_url(product_letcode_URL)
    new_page.close()
    page.close()

def test_multiple_pages_handling_on_letcode(before_all_after_all):
    context = before_all_after_all

    page = context.new_page()
    page.goto(windows_letcode_URL)
    expect(page).to_have_url(windows_letcode_URL)

    page.locator(btn_multiple_id).click()
    context.on("page", page.wait_for_load_state())

    all_pages = context.pages
    assert len(all_pages) == 3

    expect(all_pages[0]).to_have_url(windows_letcode_URL)
    expect(all_pages[1]).to_have_url(alert_letcode_URL)
    expect(all_pages[2]).to_have_url(dropdowns_letcode_URL)

    all_pages[1].bring_to_front()
    all_pages[1].on("dialog", lambda dialog: dialog.accept())

    all_pages[1].click(btn_simple_alert_id)