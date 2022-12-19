from playwright.sync_api import expect

base_URL = 'https://the-internet.herokuapp.com/'
page_title = "The Internet"

def test_chromium(playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    page.goto(base_URL)
    expect(page).to_have_title(page_title)
    browser.close()

def test_chromium_msedge_channel(playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, channel="msedge", slow_mo=300)
    page = browser.new_page()
    page.goto(base_URL)
    expect(page).to_have_title(page_title)
    browser.close()

def test_firefox(playwright):
    firefox = playwright.firefox
    browser = firefox.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    page.goto(base_URL)
    expect(page).to_have_title(page_title)
    browser.close()

def test_webkit(playwright):
    webkit = playwright.webkit
    browser = webkit.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    page.goto(base_URL)
    expect(page).to_have_title(page_title)
    browser.close()