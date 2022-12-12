import pytest
from playwright.sync_api import Page

baseURL = 'https://the-internet.herokuapp.com/'

def test_launch_browser(page: Page):
    page.goto(baseURL)

@pytest.mark.only_browser("firefox")
def test_visit_website(page: Page):
    page.goto(baseURL)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    iphone_11 = playwright.devices['iPhone 11 Pro']
    return {
        **browser_context_args,
        **iphone_11,
    }