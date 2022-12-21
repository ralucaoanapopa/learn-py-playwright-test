from playwright.sync_api import Page, expect

from pages.base import BasePage

class InventoryPage(BasePage):

    burger_menu_id = "button[id='react-burger-menu-btn']"
    logout_id = "#logout_sidebar_link"

    def __init__(self, page: Page):
        super().__init__()
        self.page = page

    def load(self):
        self.page.goto(self.inventory_url)

    def get_burger_menu(self):
        return self.page.locator(self.burger_menu_id)

    def get_logout_link(self):
        return self.page.locator(self.logout_id)

    def click_burger_menu(self):
        self.get_burger_menu().click()

    def click_logout(self):
        self.get_logout_link().click()

    def logout_user(self):
        expect(self.get_burger_menu()).to_be_visible()
        self.click_burger_menu()
        self.click_logout()
