from playwright.sync_api import Page

from POM_demoqa.pages.base import BasePage


class ProfilePage(BasePage):

    logout_btn_text = "text=Logout"
    username_value_id = "#userName-value"
    books_btn_id = "#gotoStore"

    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.logout_btn = page.locator(self.logout_btn_text)
        self.username_value = page.locator(self.username_value_id)
        self.books_btn = page.locator(self.books_btn_id)

    def load(self):
        self.page.goto(self.profile_URL)

    def get_username_value(self):
        return self.username_value.text_content()

    def logout(self):
        self.logout_btn.click()

    def go_to_books_page(self):
        self.books_btn.click()
