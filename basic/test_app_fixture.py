import pytest
from playwright.sync_api import Page, expect

base_url = "https://playwright.dev/"
intro_path = "docs/intro"
intro_url = base_url + intro_path
get_started_class = ".getStarted_Sjon"
community_path = "community/welcome"
community_url = base_url + community_path
python_path = "python/"
base_url_py = base_url + python_path
dropdown_link_class = ".dropdown__link"
xpath_python_option = 'xpath=//a[@href="/python/"]'
navbar_item_list_class = ".navbar__item.dropdown.dropdown--hoverable"

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    # Go to the starting url before each test
    page.goto(base_url)
    yield
    print("afterEach")

def test_main_navigation(page: Page):
    expect(page).to_have_url(base_url)

def test_navigate_to_get_started_page(page: Page):
    get_started_btn = page.locator(get_started_class)
    expect(get_started_btn).to_have_attribute("href", "/docs/intro")

    get_started_btn.click()
    expect(page).to_have_url(intro_url)

def test_navigate_to_community_page(page: Page):
    community_link = page.get_by_role("link", name="Community")
    expect(community_link).to_have_attribute("href", "/community/welcome")

    community_link.click()
    expect(page).to_have_url(community_url)

def test_choose_python(page: Page):
    nav_bar_list = page.locator(dropdown_link_class)
    expect(nav_bar_list).to_have_count(4)

    # click on navbar in order to make interactable all 4 items from list
    page.locator(navbar_item_list_class).click()

    python_link = page.locator(xpath_python_option)
    expect(python_link).to_have_text("Python")

    python_link.click()
    expect(page).to_have_url(base_url_py)
