import pytest, time, base64
from playwright.sync_api import expect

books_demoqa_URL = 'https://demoqa.com/books'
book_img_xpath = "xpath=//img[@src='/images/bookimage3.jpg']"
page_title = "ToolsQA"

@pytest.fixture(scope="session", autouse=True)
def before_all_after_all(playwright):
    
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    page = context.new_page()
    page.goto(books_demoqa_URL)
    expect(page).to_have_title(page_title)

    yield page
    page.close()

def test_take_screenshot_for_page(before_all_after_all):
    page = before_all_after_all

    page.screenshot(path="screenshots/" + str(time.time()) +"-page.png")

def test_take_screenshot_for_full_page(before_all_after_all):
    page = before_all_after_all

    page.screenshot(path="screenshots/" + str(time.time()) +"-full-page.png", full_page=True)

def test_take_screenshot_for_an_element(before_all_after_all):
    page = before_all_after_all

    book_imgs = page.locator(book_img_xpath)
    first_img = book_imgs.first
    first_img.screenshot(path="screenshots/" + str(time.time()) +"-book.png")

def test_capture_screenshot_into_buffer(before_all_after_all):
    page = before_all_after_all

    screenshot_bytes = page.screenshot()
    imgdata = base64.b64encode(screenshot_bytes)
    filename = 'screenshots/base64_encoded.txt'
    with open(filename, 'wb') as f:
        f.write(imgdata)