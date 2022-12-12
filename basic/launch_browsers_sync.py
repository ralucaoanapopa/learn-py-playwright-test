from playwright.sync_api import sync_playwright, Page

base_URL = 'https://the-internet.herokuapp.com/'

def test_chromium(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto(base_URL)
    
    browser.close()

def test_firefox(playwright):
    chromium = playwright.firefox
    browser = chromium.launch()
    page = browser.new_page()
    page.goto(base_URL)
    
    browser.close()

def test_webkit(playwright):
    chromium = playwright.webkit
    browser = chromium.launch()
    page = browser.new_page()
    page.goto(base_URL)
    
    browser.close()

with sync_playwright() as playwright:
    test_chromium(playwright)
    test_firefox(playwright)
    test_webkit(playwright)