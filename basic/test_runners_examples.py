import pytest
from playwright.sync_api import Page

base_URL = 'https://the-internet.herokuapp.com/'

def test_launch_browser(page: Page):
    page.goto(base_URL)

@pytest.mark.only_browser("firefox")
def test_visit_website(page: Page):
    page.goto(base_URL)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    iphone_11 = playwright.devices['iPhone 11 Pro']
    return {
        **browser_context_args,
        **iphone_11,
    }