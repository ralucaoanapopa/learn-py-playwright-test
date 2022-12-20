from playwright.sync_api import Page

class BooksPage:
    base_URL = "https://demoqa.com/"
    books_URL = base_URL + "books"
    title = "ToolsQA"

    book_header_xpath = "xpath=//div[@class='main-header']"
    login_btn = "button[id='login']"
    table_head_class = ".rt-thead.-header"
    table_header_class = ".rt-resizable-header-content"
    table_body_class = ".rt-tbody"
    table_body_rows_class = ".rt-tr-group"

    def __init__(self, page: Page) -> None:
        self.page = page

    def load(self) -> None:
        self.page.goto(self.books_URL)

    def get_book_header(self):
        return self.page.locator(self.book_header_xpath)

    def get_login_btn(self):
        return self.page.locator(self.login_btn)

    def get_table_head(self):
        return self.page.locator(self.table_head_class)

    def get_table_header_columns(self):
        return self.page.locator(self.table_header_class)

    def get_table_body(self):
        return self.page.locator(self.table_body_class)
    
    def get_table_rows(self):
        return self.page.locator(self.table_body_rows_class)
