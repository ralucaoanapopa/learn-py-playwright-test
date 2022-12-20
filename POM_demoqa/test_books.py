from playwright.sync_api import expect
from pages.books import BooksPage
from mydata import *
import pytest, os

user_name = os.environ.get('USERNAME_QA')
user_pass = os.environ.get('PASSWORD_QA')

@pytest.fixture(scope="session", autouse=True)
def before_all_after_all(playwright):
    # create context for all tests
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    page = context.new_page()

    yield page
    page.close()

def test_anonymous_user_can_see_book_store_list_and_login_button(before_all_after_all):
    page = before_all_after_all

    books_page = BooksPage(page)

    books_page.load()
    expect(page).to_have_url(books_page.books_URL)

    expect(books_page.get_book_header()).to_have_text(book_store_header)
    expect(books_page.get_login_btn()).to_be_visible()
    expect(books_page.get_table_head()).to_be_visible()

    table_columns = books_page.get_table_header_columns()
    expect(table_columns).to_have_count(4)

    expect(table_columns.nth(0)).to_have_text(table_column_one)
    expect(table_columns.nth(1)).to_have_text(table_column_two)
    expect(table_columns.nth(2)).to_have_text(table_column_three)
    expect(table_columns.nth(3)).to_have_text(table_column_four)

    expect(books_page.get_table_body()).to_be_visible()
    table_rows = books_page.get_table_rows()
    expect(table_rows).to_have_count(10)