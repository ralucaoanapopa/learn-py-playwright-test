from playwright.sync_api import Page

from pages.base import BasePage

class LoginPage(BasePage):

    username_input_id = "input[id='userName']"
    password_input_id = "input[id='password']"
    login_btn_id = "button[id='login']"
    title = "ToolsQA"

    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.username_input = page.locator(self.username_input_id)
        self.password_input = page.locator(self.password_input_id)
        self.login_btn = page.locator(self.login_btn_id)

    def load(self):
        self.page.goto(self.login_URL)

    def login_form(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()

    def get_error_login_msg(self):
        self.err_login = self.page.locator("#name")
        return self.err_login.text_content()