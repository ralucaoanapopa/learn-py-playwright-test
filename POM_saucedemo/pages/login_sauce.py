from playwright.sync_api import Page

from pages.base import BasePage

class LoginSaucePage(BasePage):

    username_input_id = "#user-name"
    password_input_id = "#password"
    login_btn_id = "#login-button"

    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.username_input = page.locator(self.username_input_id)
        self.password_input = page.locator(self.password_input_id)
        self.login_btn = page.locator(self.login_btn_id)

    def load(self):
        self.page.goto(self.base_url)

    def login_form(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()