from playwright.sync_api import expect
from pages.books import BooksPage
from pages.login import LoginPage
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

def test_anonymous_user_can_see_all_book_titles_from_book_store_table(before_all_after_all):
    page = before_all_after_all

    books_page = BooksPage(page)

    books_page.load()
    expect(page).to_have_url(books_page.books_URL)

    all_book_titles = books_page.get_all_book_titles()
    expect(all_book_titles).to_have_count(8)
    expect(all_book_titles).to_have_text(book_titles)

def test_anonymous_user_can_navigate_to_login_page_from_books_page(before_all_after_all):
    page = before_all_after_all

    books_page = BooksPage(page)

    books_page.load()
    expect(page).to_have_url(books_page.books_URL)

    expect(books_page.get_login_btn()).to_be_visible()
    books_page.click_login()
    expect(page).to_have_url(books_page.login_URL)

def test_authenticated_user_can_see_book_store_list_username_and_logout_button(before_all_after_all):
    page = before_all_after_all

    books_page = BooksPage(page)

    books_page.load()
    expect(page).to_have_url(books_page.books_URL)

    expect(books_page.get_login_btn()).to_be_visible()
    books_page.click_login()
    expect(page).to_have_url(books_page.login_URL)

    login_page = LoginPage(page)

    login_page.login_form(user_name, user_pass)
    expect(page).to_have_url(books_page.books_URL)

    expect(books_page.get_username_value()).to_have_text(user_name)
    expect(books_page.get_logout_btn()).to_be_visible()

    expect(books_page.get_table_head()).to_be_visible()

    table_columns = books_page.get_table_header_columns()
    expect(table_columns).to_have_count(4)

    expect(table_columns.nth(0)).to_have_text(table_column_one)
    expect(table_columns.nth(1)).to_have_text(table_column_two)
    expect(table_columns.nth(2)).to_have_text(table_column_three)
    expect(table_columns.nth(3)).to_have_text(table_column_four)

    all_book_titles = books_page.get_all_book_titles()
    expect(all_book_titles).to_have_count(8)
    expect(all_book_titles).to_have_text(book_titles)

    books_page.click_logout()
    expect(page).to_have_url(books_page.login_URL)

def test_anonymous_user_can_search_books_by_title(before_all_after_all):
    page = before_all_after_all

    books_page = BooksPage(page)

    books_page.load()

    expect(books_page.get_search_input()).to_be_visible()
    books_page.search_by_keyword(keyword_match_title)

    all_book_titles = books_page.get_all_book_titles()
    expect(all_book_titles).to_have_count(4)

    assert all_book_titles.nth(0).text_content() == book_titles[1]
    expect(all_book_titles.nth(1)).to_have_text(book_titles[3])
    expect(all_book_titles.nth(2)).to_have_text(book_titles[5])
    expect(all_book_titles.nth(3)).to_have_text(book_titles[6])

def test_no_rows_are_displayed_when_keyword_does_not_match_title_author_nor_publisher(before_all_after_all):
    page = before_all_after_all

    books_page = BooksPage(page)

    books_page.load()
    expect(books_page.get_search_input()).to_be_visible()
    books_page.search_by_keyword(keyword_no_match)
    expect(books_page.get_no_rows()).to_have_text(no_rows_text)