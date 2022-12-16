import pytest
from playwright.sync_api import expect

base_letcode_URL = 'https://letcode.in/'
frames_letcode_URL = base_letcode_URL + 'frame'

first_frame_name = 'firstFr'
firstName_name = "input[name='fname']"
lastName_name = "input[name='lname']"
firstName_data = 'Hakuna'
lastName_data = 'Matata'
lastName_data_parent = 'Gandalf'
output_xpath = "xpath=//p[@class='title has-text-info']"
email_name = "input[name='email']"
email_data = 'hakuna.matata@test.com'

frames_demoqa_URL = 'https://demoqa.com/frames'
page_title = "ToolsQA"
frame_content = "This is a sample page"

@pytest.fixture(scope="session", autouse=True)
def before_all_after_all(playwright):
    
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    page = context.new_page()

    yield page
    page.close()

def test_interact_with_nested_frames_on_letcode(before_all_after_all):
    page = before_all_after_all

    page.goto(frames_letcode_URL)
    assert page.title() is not None

    frame = page.frame( name = first_frame_name )

    if frame is not None:
        frame.fill(firstName_name, firstName_data)
        frame.fill(lastName_name, lastName_data)

        expect(frame.locator(output_xpath)).to_contain_text(firstName_data + ' ' + lastName_data)

        frames =  frame.child_frames
        assert len(frames) is 2

        frames[1].fill(email_name, email_data)

        parentFrame = frames[1].parent_frame
        parentFrame.fill(lastName_name, lastName_data_parent)
        expect(frame.locator(output_xpath)).to_contain_text(firstName_data + ' ' + lastName_data_parent)
    else:
        raise("No such frame")

def test_interact_with_frames_on_demoqa(before_all_after_all):
    page = before_all_after_all

    page.goto(frames_demoqa_URL)
    assert page.title() is not None
    expect(page).to_have_title(page_title)

    frame_one = page.frame(url = "sample")
    if frame_one is not None:
        expect(frame_one.locator('h1')).to_have_text(frame_content)