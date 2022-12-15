import pytest, os
from playwright.sync_api import Page, expect

base_URL = 'https://demoqa.com/text-box'

page_title = "ToolsQA"

label_fullName_id = '#userName-label'
label_email_id = '#userEmail-label'
label_currentAddress = '#currentAddress-label'
label_PermanentAddress = '#permanentAddress-label'

fullName_id = '#userName'
email_id = '#userEmail'
currentAddress_id = '#currentAddress'
permanentAddress_id = '#permanentAddress'

fullName_data = 'Test Playwright'
email_data = 'letmetest@tools.com'
currentAddress_data = 'here'
permanentAddress_data = 'there'

submitBtn_id = '#submit'
output_id = '#output'
nameOutput_id = '#name'
emailOutput_id = '#email'
currentAddressOutput_xpath = "xpath=//p[@id='currentAddress']"
permanentAddressOutput_xpath = "xpath=//p[@id='permanentAddress']"

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=400)
    context = browser.new_context()

    page = context.new_page()
    page.goto(base_URL)
    yield page
    page.close()

def test_enter_data_on_text_box_page(before_each_after_each):
    page = before_each_after_each
    expect(page).to_have_url(base_URL)
    expect(page).to_have_title(page_title)

    # check labels:
    expect(page.locator(label_fullName_id)).to_have_text('Full Name')
    expect(page.locator(label_email_id)).to_have_text('Email')
    expect(page.locator(label_currentAddress)).to_have_text('Current Address')
    expect(page.locator(label_PermanentAddress)).to_have_text('Permanent Address')

    # enter data in fields:
    page.locator(fullName_id).fill(fullName_data)
    page.locator(email_id).fill(email_data)
    page.locator(currentAddress_id).type(currentAddress_data)
    page.locator(permanentAddress_id).fill(permanentAddress_data)

    page.locator(submitBtn_id).click()

    page.wait_for_selector(output_id)

    expect(page.locator(nameOutput_id)).to_contain_text(fullName_data)
    expect(page.locator(emailOutput_id)).to_contain_text(email_data)
    expect(page.locator(currentAddressOutput_xpath)).to_contain_text(currentAddress_data)
    expect(page.locator(permanentAddressOutput_xpath)).to_contain_text(permanentAddress_data)

def test_enter_data_with_check_for_None(before_each_after_each):
    page = before_each_after_each

    name = page.locator(fullName_id)
    if name is not None:
        name.fill(fullName_data)

    if page.locator(email_id) is not None:
        page.locator(email_id).fill(email_data)

    if page.locator(currentAddress_id) is not None:
        page.locator(currentAddress_id).fill(currentAddress_data)

    if page.locator(permanentAddress_id) is not None:
        page.locator(permanentAddress_id).fill(permanentAddress_data)

    page.locator(submitBtn_id).click()

    page.wait_for_selector(output_id)

    expect(page.locator(nameOutput_id)).to_contain_text(fullName_data)
    expect(page.locator(emailOutput_id)).to_contain_text(email_data)
    expect(page.locator(currentAddressOutput_xpath)).to_contain_text(currentAddress_data)
    expect(page.locator(permanentAddressOutput_xpath)).to_contain_text(permanentAddress_data)


    