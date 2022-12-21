from playwright.sync_api import Page, expect

from pages.base import BasePage

class InventoryPage(BasePage):

    burger_menu_id = "button[id='react-burger-menu-btn']"
    logout_id = "#logout_sidebar_link"
    inventory_list_class = ".inventory_list"
    select_sort_class = ".product_sort_container"
    shopping_cart_class = ".shopping_cart_link"
    option_ZA_xpath = "xpath=//option[@value='za']"
    item_labels_class = ".inventory_item_label"
    item_names_class = '.inventory_item_name'
    active_filter_class = ".active_option"
    onesie_id = "#add-to-cart-sauce-labs-onesie"
    onesie_remove_id = "#remove-sauce-labs-onesie"
    bolt_Tshirt_id = "#add-to-cart-sauce-labs-bolt-t-shirt"
    bolt_Tshirt_remove_id = "#remove-sauce-labs-bolt-t-shirt"
    backpack_Id = "#add-to-cart-sauce-labs-backpack"
    backpack_remove_id = "#remove-sauce-labs-backpack"
    fleece_Jacket_id = "#add-to-cart-sauce-labs-fleece-jacket"
    fleece_Jacket_remove_id = "#remove-sauce-labs-fleece-jacket"
    shopping_cart_badge_class = ".shopping_cart_badge"

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

    def get_shopping_cart(self):
        return self.page.locator(self.shopping_cart_class)
    
    def get_products_list(self):
        return self.page.locator(self.inventory_list_class)

    def get_select_sort_filter(self):
        return self.page.locator(self.select_sort_class)

    def get_item_labels_list(self):
        return self.page.locator(self.item_labels_class)

    def get_active_filter_option(self):
        return self.page.locator(self.active_filter_class)

    def get_item_names_list(self):
        return self.page.locator(self.item_names_class)

    def click_filter_name_desc(self):
        option_za = self.page.locator(self.option_ZA_xpath)
        expect(option_za).to_be_hidden()
        self.get_select_sort_filter().select_option(value='za')

    def click_filter_name_asc(self):
        self.get_select_sort_filter().select_option(value='az')

    def click_filter_price_desc(self):
        self.get_select_sort_filter().select_option(value='hilo')

    def click_filter_price_asc(self):
        self.get_select_sort_filter().select_option(value='lohi')

    def add_product_to_shopping_cart(self, product_id):
        product_to_add =  self.page.locator(product_id)
        product_to_add.click()

    def button_remove_product(self, product_id):
        return self.page.locator(product_id)
    
    def get_shopping_cart_badge(self):
        return self.page.locator(self.shopping_cart_badge_class)

    def click_shopping_cart(self):
        self.page.locator(self.shopping_cart_class).click()