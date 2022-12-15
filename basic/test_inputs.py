import pytest
from playwright.sync_api import expect

base_URL = 'https://demoqa.com/text-box'

page_title = "ToolsQA"

label_full_name_id = '#userName-label'
label_email_id = '#userEmail-label'
label_current_address = '#currentAddress-label'
label_permanent_address = '#permanentAddress-label'

full_name_id = '#userName'
email_id = '#userEmail'
current_address_id = '#currentAddress'
permanent_address_id = '#permanentAddress'

full_name_data = 'Test Playwright'
email_data = 'letmetest@tools.com'
current_address_data = 'here'
permanent_address_data = 'there'

submit_btn_id = '#submit'
output_id = '#output'
name_output_id = '#name'
email_output_id = '#email'
current_address_output_xpath = "xpath=//p[@id='currentAddress']"
permanent_address_output_xpath = "xpath=//p[@id='permanentAddress']"

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=400)
    context = browser.new_context()

    page = context.new_page()
    page.goto(base_URL)

    expect(page).to_have_url(base_URL)
    expect(page).to_have_title(page_title)

    yield page
    page.close()

def test_enter_data_on_text_box_page(before_each_after_each):
    page = before_each_after_each

    # check labels:
    expect(page.locator(label_full_name_id)).to_have_text('Full Name')
    expect(page.locator(label_email_id)).to_have_text('Email')
    expect(page.locator(label_current_address)).to_have_text('Current Address')
    expect(page.locator(label_permanent_address)).to_have_text('Permanent Address')

    # enter data in fields:
    page.locator(full_name_id).fill(full_name_data)
    page.locator(email_id).fill(email_data)
    page.locator(current_address_id).type(current_address_data)
    page.locator(permanent_address_id).fill(permanent_address_data)

    page.locator(submit_btn_id).click()

    page.wait_for_selector(output_id)

    expect(page.locator(name_output_id)).to_contain_text(full_name_data)
    expect(page.locator(email_output_id)).to_contain_text(email_data)
    expect(page.locator(current_address_output_xpath)).to_contain_text(current_address_data)
    expect(page.locator(permanent_address_output_xpath)).to_contain_text(permanent_address_data)

def test_enter_data_with_check_for_None(before_each_after_each):
    page = before_each_after_each

    name = page.locator(full_name_id)
    if name is not None:
        name.fill(full_name_data)

    if page.locator(email_id) is not None:
        page.locator(email_id).fill(email_data)

    if page.locator(current_address_id) is not None:
        page.locator(current_address_id).fill(current_address_data)

    if page.locator(permanent_address_id) is not None:
        page.locator(permanent_address_id).fill(permanent_address_data)

    page.locator(submit_btn_id).click()

    page.wait_for_selector(output_id)

    expect(page.locator(name_output_id)).to_contain_text(full_name_data)
    expect(page.locator(email_output_id)).to_contain_text(email_data)
    expect(page.locator(current_address_output_xpath)).to_contain_text(current_address_data)
    expect(page.locator(permanent_address_output_xpath)).to_contain_text(permanent_address_data)


    