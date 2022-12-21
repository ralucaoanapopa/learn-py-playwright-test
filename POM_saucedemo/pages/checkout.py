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

    first_name_id = "#first-name"
    last_name_id = "#last-name"
    postal_code_id = "#postal-code"
    continue_checkout_button_id = "#continue"

    cancel_button_id = "#cancel"
    summary_info_class = ".summary_info_label"
    summary_value_class = ".summary_value_label"
    summary_subtotal_class= ".summary_subtotal_label"
    summary_tax_class= ".summary_tax_label"
    summary_total_class= ".summary_total_label"

    finish_checkout_button_id = "#finish"
    complete_header_class = ".complete-header"
    complete_text_class = ".complete-text"
    final_image_class = ".pony_express"
    back_button_id = "#back-to-products"

    error_validation_class = ".error-message-container.error"

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

    def click_checkout(self):
        self.page.locator(self.checkout_button_id).click()

    def enter_first_name(self, first):
        self.page.locator(self.first_name_id).fill(first)
    
    def enter_last_name(self, last):
        self.page.locator(self.last_name_id).fill(last)

    def enter_postal_code(self, code):
        self.page.locator(self.postal_code_id).fill(code)

    def enter_checkout_info(self, first, last, code):
        self.enter_first_name(first)
        self.enter_last_name(last)
        self.enter_postal_code(code)

    def get_button_continue_checkout(self):
        return self.page.locator(self.continue_checkout_button_id)

    def click_continue(self):
        self.get_button_continue_checkout().click()

    def get_button_cancel(self):
        return self.page.locator(self.cancel_button_id)

    def get_button_finish(self):
        return self.page.locator(self.finish_checkout_button_id)

    def elements_by_class(self, element):
        return self.page.locator(element)
    
    def click_finish(self):
        self.get_button_finish().click()

    def click_back(self):
        self.page.locator(self.back_button_id).click()