from playwright.sync_api import Page

class BooksPage:
    base_URL = "https://demoqa.com/"
    books_URL = base_URL + "books"
    login_URL = base_URL + "login"

    book_header_xpath = "xpath=//div[@class='main-header']"
    login_btn = "button[id='login']"
    logout_btn = "text=Log out"
    table_head_class = ".rt-thead.-header"
    table_header_class = ".rt-resizable-header-content"
    table_body_class = ".rt-tbody"
    table_body_rows_class = ".rt-tr-group"
    book_titles_xpath = "xpath=//span[@class='mr-2']"
    search_input_id = "#searchBox"
    no_rows_class = ".rt-noData"
    username_value_id = '#userName-value'

    def __init__(self, page: Page) -> None:
        self.page = page

    def load(self) -> None:
        self.page.goto(self.books_URL)

    def get_book_header(self):
        return self.page.locator(self.book_header_xpath)

    def get_login_btn(self):
        return self.page.locator(self.login_btn)

    def get_logout_btn(self):
        return self.page.locator(self.logout_btn)

    def get_table_head(self):
        return self.page.locator(self.table_head_class)

    def get_table_header_columns(self):
        return self.page.locator(self.table_header_class)

    def get_table_body(self):
        return self.page.locator(self.table_body_class)
    
    def get_table_rows(self):
        return self.page.locator(self.table_body_rows_class)

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

    def get_no_rows(self):
        return self.page.locator(self.no_rows_class)