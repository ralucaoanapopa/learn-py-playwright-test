from playwright.sync_api import expect
from pages.login_sauce import LoginSaucePage
from pages.inventory import InventoryPage
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


def test_shopping_cart_products_list_and_filter_dropdown_are_displayed(before_all_after_all):
    page = before_all_after_all

    inventory_page = InventoryPage(page)

    expect(inventory_page.get_shopping_cart()).to_be_visible()
    expect(inventory_page.get_products_list()).to_be_visible()
    expect(inventory_page.get_select_sort_filter()).to_be_visible()
    expect(inventory_page.get_item_labels_list()).to_have_count(6)
    expect(inventory_page.get_active_filter_option()).to_have_text(filter_name_asc)

    all_product_names = inventory_page.get_item_names_list()
    expect(all_product_names.nth(0)).to_have_text(product_Backpack)


def test_should_be_able_to_filter_products_by_Name_Z_to_A(before_all_after_all):
    page = before_all_after_all
    inventory_page = InventoryPage(page)

    expect(inventory_page.get_active_filter_option()).to_have_text(filter_name_asc)
    inventory_page.click_filter_name_desc()
    expect(inventory_page.get_active_filter_option()).to_have_text(filter_name_desc)

    all_product_names = inventory_page.get_item_names_list()
    expect(all_product_names.nth(0)).to_have_text(product_AllThings)


def test_should_be_able_to_filter_products_by_Price_High_to_Low(before_all_after_all):
    page = before_all_after_all
    inventory_page = InventoryPage(page)

    inventory_page.click_filter_price_desc()
    expect(inventory_page.get_active_filter_option()).to_have_text(filter_price_desc)

    all_product_names = inventory_page.get_item_names_list()
    expect(all_product_names.nth(0)).to_have_text(product_Jacket)


def test_should_be_able_to_filter_products_by_Name_A_to_Z(before_all_after_all):
    page = before_all_after_all
    inventory_page = InventoryPage(page)

    inventory_page.click_filter_name_asc()
    expect(inventory_page.get_active_filter_option()).to_have_text(filter_name_asc)

    all_product_names = inventory_page.get_item_names_list()
    expect(all_product_names.nth(0)).to_have_text(product_Backpack)


def test_should_be_able_to_filter_products_by_Price_Low_to_High(before_all_after_all):
    page = before_all_after_all
    inventory_page = InventoryPage(page)

    inventory_page.click_filter_price_asc()
    expect(inventory_page.get_active_filter_option()).to_have_text(filter_price_asc)

    all_product_names = inventory_page.get_item_names_list()
    expect(all_product_names.nth(0)).to_have_text(product_Onesie)


def test_should_be_able_to_add_products_to_shopping_cart(before_all_after_all):
    page = before_all_after_all
    inventory_page = InventoryPage(page)

    inventory_page.add_product_to_shopping_cart(inventory_page.onesie_id)
    expect(inventory_page.button_remove_product(inventory_page.onesie_remove_id)).to_be_visible()
    expect(inventory_page.get_shopping_cart_badge()).to_have_text("1")
    inventory_page.add_product_to_shopping_cart(inventory_page.bolt_Tshirt_id)
    expect(inventory_page.button_remove_product(inventory_page.bolt_Tshirt_remove_id)).to_be_visible()
    expect(inventory_page.get_shopping_cart_badge()).to_have_text("2")

    inventory_page.logout_user()
    expect(page).to_have_url(inventory_page.base_url)