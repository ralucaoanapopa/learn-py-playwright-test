from playwright.sync_api import expect
from pages.login_sauce import LoginSaucePage
from pages.inventory import InventoryPage
from pages.checkout import CheckoutPage
from mydata import *
import pytest, os

user_name = os.environ.get('USER_SAUCE')
user_pass = os.environ.get('PASSWORD_SAUCE')

@pytest.fixture(scope="session", autouse=True)
def before_all_after_all(playwright):
    # create context for all tests
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    page = context.new_page()

    login_page = LoginSaucePage(page)

    login_page.load()
    login_page.login_form(user_name, user_pass)
    expect(page).to_have_title(site_title)
    expect(page).to_have_url(login_page.inventory_url)

    yield page
    page.close()


def test_should_be_able_to_add_products_to_shopping_cart(before_all_after_all):
    page = before_all_after_all

    inventory_page = InventoryPage(page)

    inventory_page.add_product_to_shopping_cart(inventory_page.onesie_id)
    expect(inventory_page.button_remove_product(inventory_page.onesie_remove_id)).to_be_visible()
    expect(inventory_page.get_shopping_cart_badge()).to_have_text("1")
    inventory_page.add_product_to_shopping_cart(inventory_page.bolt_Tshirt_id)
    expect(inventory_page.button_remove_product(inventory_page.bolt_Tshirt_remove_id)).to_be_visible()
    expect(inventory_page.get_shopping_cart_badge()).to_have_text("2")
    inventory_page.add_product_to_shopping_cart(inventory_page.backpack_Id)
    expect(inventory_page.button_remove_product(inventory_page.backpack_remove_id)).to_be_visible()
    expect(inventory_page.get_shopping_cart_badge()).to_have_text("3")


def test_should_be_able_to_see_shopping_cart_content(before_all_after_all):
    page = before_all_after_all

    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    inventory_page.click_shopping_cart()
    expect(page).to_have_url(inventory_page.cart_url)
    expect(checkout_page.get_title_checkout()).to_have_text(cart_title)
    expect(checkout_page.get_cart_quantity()).to_have_text(cart_quantity)
    expect(checkout_page.get_cart_description()).to_have_text(cart_description)
    expect(checkout_page.get_footer_section()).to_be_visible()
    expect(checkout_page.get_continue_shopping()).to_be_visible()
    expect(checkout_page.get_continue_shopping()).to_have_text(continue_shopping)
    expect(checkout_page.get_checkout()).to_be_visible()

    expect(checkout_page.get_cart_items_list()).to_have_count(3)
    all_items = checkout_page.get_cart_items_list()
    expect(all_items.nth(0)).to_contain_text(product_Onesie)
    expect(all_items.nth(1)).to_contain_text(product_BoltTShirt)
    expect(all_items.nth(2)).to_contain_text(product_Backpack)

    expect(checkout_page.get_items_price_list()).to_have_count(3)
    all_items_prices = checkout_page.get_items_price_list()
    expect(all_items_prices.nth(0)).to_have_text(product_Onesie_price)
    expect(all_items_prices.nth(1)).to_have_text(product_BoltTShirt_price)
    expect(all_items_prices.nth(2)).to_have_text(product_Backpack_Price)


def test_should_be_able_to_navigate_to_inventory_page(before_all_after_all):
    page = before_all_after_all

    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    checkout_page.click_continue_shopping()
    expect(page).to_have_url(checkout_page.inventory_url)

    expect(inventory_page.button_remove_product(inventory_page.onesie_remove_id)).to_be_visible()
    expect(inventory_page.button_remove_product(inventory_page.bolt_Tshirt_remove_id)).to_be_visible()
    expect(inventory_page.button_remove_product(inventory_page.backpack_remove_id)).to_be_visible()

    inventory_page.add_product_to_shopping_cart(inventory_page.fleece_Jacket_id)
    expect(inventory_page.button_remove_product(inventory_page.fleece_Jacket_remove_id)).to_be_visible()
    expect(inventory_page.get_shopping_cart_badge()).to_have_text("4")


def test_should_be_able_to_remove_product_from_cart(before_all_after_all):
    page = before_all_after_all

    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    inventory_page.click_shopping_cart()
    expect(page).to_have_url(checkout_page.cart_url)

    expect(checkout_page.get_cart_items_list()).to_have_count(4)
    all_items = checkout_page.get_cart_items_list()
    expect(all_items.nth(0)).to_contain_text(product_Onesie)
    expect(all_items.nth(1)).to_contain_text(product_BoltTShirt)
    expect(all_items.nth(2)).to_contain_text(product_Backpack)
    expect(all_items.nth(3)).to_contain_text(product_Jacket)

    checkout_page.remove_product(checkout_page.onesie_remove_id)
    expect(checkout_page.get_cart_items_list()).to_have_count(3)

    inventory_page.logout_user()
    expect(page).to_have_url(inventory_page.base_url)
