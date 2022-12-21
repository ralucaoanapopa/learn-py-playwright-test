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
    expect(all_items_prices.nth(2)).to_have_text(product_Backpack_price)


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


def test_should_be_able_to_provide_information_on_checkout(before_all_after_all):
    page = before_all_after_all

    checkout_page = CheckoutPage(page)

    checkout_page.click_checkout()

    expect(page).to_have_url(checkout_page.checkout_one_url)
    expect(checkout_page.get_title_checkout()).to_have_text(checkout_one_title)
    checkout_page.enter_checkout_info(first_name, last_name, postal_code)
    expect(checkout_page.get_button_continue_checkout()).to_have_text(continue_checkout)


def test_should_be_able_to_see_overview_on_checkout(before_all_after_all):
    page = before_all_after_all

    checkout_page = CheckoutPage(page)

    checkout_page.click_continue()
    expect(page).to_have_url(checkout_page.checkout_two_url)
    expect(checkout_page.get_title_checkout()).to_have_text(checkout_two_title)
    expect(checkout_page.get_cart_quantity()).to_have_text(cart_quantity)
    expect(checkout_page.get_cart_description()).to_have_text(cart_description)

    expect(checkout_page.get_button_cancel()).to_have_text(cancel_checkout)
    expect(checkout_page.get_button_finish()).to_have_text(finish_checkout)

    expect(checkout_page.get_cart_items_list()).to_have_count(3)
    all_items = checkout_page.get_cart_items_list()

    expect(all_items.nth(0)).to_contain_text(product_BoltTShirt)
    expect(all_items.nth(1)).to_contain_text(product_Backpack)
    expect(all_items.nth(2)).to_contain_text(product_Jacket)

    expect(checkout_page.get_items_price_list()).to_have_count(3)
    all_items_prices = checkout_page.get_items_price_list()
    expect(all_items_prices.nth(0)).to_have_text(product_BoltTShirt_price)
    expect(all_items_prices.nth(1)).to_have_text(product_Backpack_price)
    expect(all_items_prices.nth(2)).to_have_text(product_FleeceJacket_price)


def test_should_be_able_to_see_total_price_and_shipping_information_on_checkout(before_all_after_all):
    page = before_all_after_all

    checkout_page = CheckoutPage(page)

    expect(page).to_have_url(checkout_page.checkout_two_url)
    all_summary_info = checkout_page.elements_by_class(checkout_page.summary_info_class)
    expect(all_summary_info.nth(0)).to_have_text(payment_information_label)
    expect(all_summary_info.nth(1)).to_have_text(shipping_information_label)

    all_summary_values = checkout_page.elements_by_class(checkout_page.summary_value_class)
    expect(all_summary_values.nth(0)).to_have_text(payment_information_value)
    expect(all_summary_values.nth(1)).to_have_text(shipping_information_value)

    expect(checkout_page.elements_by_class(checkout_page.summary_subtotal_class)).to_have_text(total_item_price)
    expect(checkout_page.elements_by_class(checkout_page.summary_tax_class)).to_have_text(tax_price)
    expect(checkout_page.elements_by_class(checkout_page.summary_total_class)).to_have_text(total_price)


def test_should_be_able_to_finish_order_from_checkout(before_all_after_all):
    page = before_all_after_all

    checkout_page = CheckoutPage(page)

    checkout_page.click_finish()
    expect(page).to_have_url(checkout_page.checkout_final_url)
    expect(checkout_page.get_title_checkout()).to_have_text(checkout_final_title)

    expect(checkout_page.elements_by_class(checkout_page.complete_header_class)).to_have_text(complete_header)
    expect(checkout_page.elements_by_class(checkout_page.complete_text_class)).to_have_text(complete_text)
    expect(checkout_page.elements_by_class(checkout_page.final_image_class)).to_have_attribute("src", final_img)


def test_should_be_able_to_navigate_back_to_inventory_after_order_was_sent(before_all_after_all):
    page = before_all_after_all

    checkout_page = CheckoutPage(page)

    checkout_page.click_back()
    expect(page).to_have_url(checkout_page.inventory_url)
    

def test_should_not_be_able_to_navigate_back_to_send_order_without_any_products(before_all_after_all):
    page = before_all_after_all

    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    inventory_page.click_shopping_cart()
    expect(page).to_have_url(inventory_page.cart_url)

    checkout_page.click_checkout()
    expect(page).to_have_url(checkout_page.checkout_one_url)

    checkout_page.enter_checkout_info(first_name, last_name, postal_code)
    checkout_page.click_continue()
    expect(page).to_have_url(checkout_page.checkout_two_url)

    checkout_page.click_finish()
    expect(page).to_have_url(checkout_page.checkout_final_url)

    pytest.fail(f"Should not be able to sent order without any products")

def test_should_not_be_able_to_see_overview_without_providing_shipping_information(before_all_after_all):
    page = before_all_after_all

    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    page.goto(checkout_page.checkout_one_url)
    expect(page).to_have_url(checkout_page.checkout_one_url)

    checkout_page.click_continue()
    element_err = checkout_page.elements_by_class(checkout_page.error_validation_class)
    expect(element_err).to_have_text(error_checkout_first_name)

    checkout_page.enter_first_name(first_name)
    checkout_page.click_continue()
    expect(element_err).to_have_text(error_checkout_last_name)

    checkout_page.enter_last_name(last_name)
    checkout_page.click_continue()
    expect(element_err).to_have_text(error_checkout_postal_code)

    checkout_page.enter_postal_code(postal_code)
    checkout_page.click_continue()
    expect(page).to_have_url(checkout_page.checkout_two_url)

    inventory_page.logout_user()
    expect(page).to_have_url(inventory_page.base_url)
