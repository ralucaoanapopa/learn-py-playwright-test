from playwright.sync_api import Page

class ProfilePage:
    base_URL = "https://demoqa.com/"
    profile_URL = base_URL + "profile"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.logout_btn = page.locator("text=Log out")
        self.username_value = page.locator('#userName-value')

    def load(self) -> None:
        self.page.goto(self.profile_URL)
    
    def get_username_value(self):
        return self.username_value.text_content()

    def logout(self):
        self.logout_btn.click()
