import pytest
from playwright.sync_api import expect

upload_demoqa_URL = 'https://demoqa.com/upload-download'
page_title_demoqa = "ToolsQA"
upload_herokuapp = 'https://the-internet.herokuapp.com/upload'
page_title_heroku = 'The Internet'

file_path_a = 'videos/afile.webm'
file_path_b = 'videos/bfile.webm'

upload_id = '#uploadFile'
input_type_file = "input[type='file']"

drag_drop_id = '#drag-drop-upload'

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()

    page = context.new_page()
    page.goto(upload_demoqa_URL)
    expect(page).to_have_url(upload_demoqa_URL)
    expect(page).to_have_title(page_title_demoqa)
    yield page
    page.close()

def test_upload_file_using_set_input_files_when_input_has_id(before_each_after_each):
    page = before_each_after_each

    page.set_input_files(upload_id, file_path_a)

def test_upload_file_using_set_input_files_when_use_input_as_selector(before_each_after_each):
    page = before_each_after_each

    page.set_input_files(input_type_file, file_path_b)

def test_upload_files_using_on_function(before_each_after_each):
    page = before_each_after_each
    page.goto(upload_herokuapp)

    expect(page).to_have_url(upload_herokuapp)
    expect(page).to_have_title(page_title_heroku)

    with page.expect_file_chooser() as fc_info:
        page.locator(drag_drop_id).click()
    file_chooser = fc_info.value
    file_chooser.set_files([file_path_a, file_path_b])
