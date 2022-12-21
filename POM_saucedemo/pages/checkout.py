from playwright.sync_api import Page, expect

from pages.base import BasePage

class CheckoutPage(BasePage):

    title_class = ".title"
    quantity_class = ".cart_quantity_label"
    description_class = ".cart_desc_label"
    item_class = ".cart_item"
    footer_class = ".cart_footer"
    continue_button_id = "#continue-shopping"
    checkout_button_id = "#checkout"
    item_price_class = ".inventory_item_price"
    onesie_remove_id = "#remove-sauce-labs-onesie"

    def __init__(self, page: Page):
        super().__init__()
        self.page = page

    def get_title_checkout(self):
        return self.page.locator(self.title_class)

    def get_cart_quantity(self):
        return self.page.locator(self.quantity_class)

    def get_cart_description(self):
        return self.page.locator(self.description_class)

    def get_footer_section(self):
        return self.page.locator(self.footer_class)

    def get_continue_shopping(self):
        return self.page.locator(self.continue_button_id)

    def get_checkout(self):
        return self.page.locator(self.checkout_button_id)

    def get_cart_items_list(self):
        return self.page.locator(self.item_class)

    def get_items_price_list(self):
        return self.page.locator(self.item_price_class)

    def click_continue_shopping(self):
        self.get_continue_shopping().click()

    def remove_product(self, product_id):
        product_to_remove = self.page.locator(product_id)
        product_to_remove.click()