from playwright.sync_api import Page

from POM_demoqa.pages.base import BasePage


class BooksPage(BasePage):

    login_btn = "button[id='login']"
    logout_btn = "text=Log out"
    table_head_selector = "table thead"
    table_header_selector = "table thead th"
    table_body_selector = "table tbody"
    table_body_rows_selector = "table tbody tr"
    book_titles_xpath = "xpath=//span[@class='mr-2']"
    search_input_id = "#searchBox"
    username_value_id = '#userName-value'
    previous_btn = "button:text-is('Previous')"
    next_btn = "button:text-is('Next')"
    pagination_text_xpath = "xpath=//span[contains(text(),'Page ')]"

    def __init__(self, page: Page):
        super().__init__()
        self.page = page

    def load(self):
        self.page.goto(self.books_URL)

    def get_book_header(self):
        return self.page.locator(self.book_header_xpath)

    def get_login_btn(self):
        return self.page.locator(self.login_btn)

    def get_logout_btn(self):
        return self.page.locator(self.logout_btn)

    def get_table_head(self):
        return self.page.locator(self.table_head_selector)

    def get_table_header_columns(self):
        return self.page.locator(self.table_header_selector)

    def get_table_body(self):
        return self.page.locator(self.table_body_selector)

    def get_table_rows(self):
        return self.page.locator(self.table_body_rows_selector)

    def get_all_book_titles(self):
        return self.page.locator(self.book_titles_xpath)

    def click_login(self):
        self.get_login_btn().click()

    def click_logout(self):
        self.get_logout_btn().click()

    def get_username_value(self):
        return self.page.locator(self.username_value_id)

    def get_search_input(self):
        return self.page.locator(self.search_input_id)

    def search_by_keyword(self, keyword):
        self.page.locator(self.search_input_id).fill(keyword)

    def get_previous_btn(self):
        return self.page.locator(self.previous_btn)

    def get_next_btn(self):
        return self.page.locator(self.next_btn)

    def get_pagination_text(self):
        return self.page.locator(self.pagination_text_xpath)
