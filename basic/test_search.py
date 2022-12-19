import pytest
from playwright.sync_api import expect

books_demoqa_URL = 'https://demoqa.com/books'
book_title_xpath = "xpath=//div[@class='main-header']"
book_title_data = 'Book Store'

page_title = "ToolsQA"

book_title_class_xpath = "xpath=//span[@class='mr-2']"

title_list = ['Git Pocket Guide', 'Learning JavaScript Design Patterns', 'Designing Evolvable Web APIs with ASP.NET',
                'Speaking JavaScript', 'You Don\'t Know JS', 'Programming JavaScript Applications',
                'Eloquent JavaScript, Second Edition', 'Understanding ECMAScript 6']

@pytest.fixture(scope="session", autouse=True)
def before_all_after_all(playwright):
    # create context for all tests
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    yield context
    context.close()

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(before_all_after_all):
    # use context for all test, but page for each test
    context = before_all_after_all

    page = context.new_page()
    page.goto(books_demoqa_URL)

    expect(page).to_have_url(books_demoqa_URL)
    expect(page).to_have_title(page_title)

    expect(page.locator(book_title_xpath)).to_have_text(book_title_data)

    yield page
    page.close()

def test_table_has_10_rows(before_each_after_each):
    page = before_each_after_each

    all_rows = page.get_by_role('rowgroup')
    assert all_rows.count() is 10

    # easier
    expect(page.get_by_role("rowgroup")).to_have_count(10)

def test_all_book_titles_from_the_list(before_each_after_each):
    page = before_each_after_each

    expect(page.locator(book_title_class_xpath)).to_have_count(8)

    all_book_titles = page.locator(book_title_class_xpath)
    assert (all_book_titles.count()) is 8

    # assert entire list at once
    # https://playwright.dev/python/docs/locators#assert-all-text-in-a-list
    expect(all_book_titles).to_have_text(title_list)

    # assert each book title from the list
    # https://playwright.dev/python/docs/locators#rare-use-cases
    count = all_book_titles.count()
    for index in range(count):
        assert all_book_titles.nth(index).text_content() == title_list[index]

    index = 0
    for title in title_list:
        title_display = all_book_titles.nth(index).text_content()
        assert title_display == title
        index = index + 1

