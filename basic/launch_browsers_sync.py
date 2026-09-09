from playwright.sync_api import sync_playwright, expect

from page_titles import PageTitles

base_URL = 'https://the-internet.herokuapp.com/'


def use_chromium(playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    page.goto(base_URL)
    expect(page).to_have_title(PageTitles.HEROKU)
    browser.close()


def use_firefox(playwright):
    chromium = playwright.firefox
    browser = chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    page.goto(base_URL)
    expect(page).to_have_title(PageTitles.HEROKU)
    browser.close()


def use_webkit(playwright):
    chromium = playwright.webkit
    browser = chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    page.goto(base_URL)
    expect(page).to_have_title(PageTitles.HEROKU)
    browser.close()


with sync_playwright() as playwright:
    use_chromium(playwright)
    use_firefox(playwright)
    use_webkit(playwright)
