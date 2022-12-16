import pytest
from playwright.sync_api import expect

herokuapp_dropdown_URL = 'https://the-internet.herokuapp.com/dropdown'
page_title = 'The Internet'
dropdown_id = '#dropdown'
option_1_label = "Option 1"
option_2_value = "2"

testpages_basic_form_URL = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'
multiple_select_xpath = "xpath=//select[@name='multipleselect[]']"
option_1_value = 'ms1'
option_3_value = 'ms3'

dropdown_xpath = "xpath=//select[@name='dropdown']"
option_5_value = 'dd5'
dropdown_options = "xpath=//select[@name='dropdown']/option"

@pytest.fixture(scope="session", autouse=True)
def before_all_after_all(playwright):
    # Go to the starting url before all tests
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    page = context.new_page()

    yield page
    page.close()

def test_handle_dropdown_herokuapp(before_all_after_all):
    page = before_all_after_all

    page.goto(herokuapp_dropdown_URL)
    expect(page).to_have_title(page_title)

    dropdown_elem = page.locator(dropdown_id)
    # select option based on value
    dropdown_elem.select_option(value = option_2_value)
    # label
    dropdown_elem.select_option(label = option_1_label)
    # index
    dropdown_elem.select_option(index = 2)

def test_select_multiple_values_from_test_pages(before_all_after_all):
    page = before_all_after_all

    page.goto(testpages_basic_form_URL)

    multiple_select_elem =  page.locator(multiple_select_xpath)

    multiple_select_elem.select_option(value = [option_1_value, option_3_value])

def test_count_all_options_from_a_dropdown_using_element_handle(before_all_after_all):
    page = before_all_after_all

    page.goto(testpages_basic_form_URL)

    page.wait_for_selector(dropdown_xpath)
    dropdown = page.query_selector(dropdown_xpath)
    available_options = dropdown.query_selector_all('option')
    assert len(available_options) == 6
    
def test_count_all_options_from_a_dropdown_using_locator(before_all_after_all):
    page = before_all_after_all

    page.goto(testpages_basic_form_URL)

    expect(page.locator(dropdown_options)).to_have_count(6)

def test_get_value_of_the_selected_option_via_index(before_all_after_all):
    page = before_all_after_all

    page.goto(testpages_basic_form_URL)

    page.select_option(dropdown_xpath, index = 4)

    text_option =  page.eval_on_selector(dropdown_xpath, "elem => elem.value")
    assert text_option == option_5_value