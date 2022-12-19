from playwright.sync_api import Page

class LoginPage:
    base_URL = "https://demoqa.com/"
    login_URL = base_URL + "login"
    title = "ToolsQA"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.locator("input[id='userName']")
        self.password_input = page.locator("input[id='password']")
        self.login_btn = page.locator("button[id='login']")

    def load(self) -> None:
        self.page.goto(self.login_URL)

    def login_form(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()

    def get_error_login_msg(self):
        self.err_login = self.page.locator("#name")
        return self.err_login.text_content()