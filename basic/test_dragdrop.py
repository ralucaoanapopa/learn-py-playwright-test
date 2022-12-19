import pytest
from playwright.sync_api import expect

drag_drop_URL = 'https://the-internet.herokuapp.com/drag_and_drop'
page_title = 'The Internet'
element_a_id = '#column-a'
element_b_id = '#column-b'

drag_drop_jQuery_URL = 'https://jqueryui.com/droppable/'
page_title_jQuery = 'Droppable | jQuery UI'
elem_draggable_id = '#draggable'
elem_droppable_id = '#droppable'

@pytest.fixture(scope="session", autouse=True)
def before_all_after_all(playwright):
    
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    page = context.new_page()

    yield page
    page.close()

def test_drag_element_over_another_element(before_all_after_all):
    page = before_all_after_all

    page.goto(drag_drop_URL)
    assert page.title() is not None
    expect(page).to_have_title(page_title)

    source = page.locator(element_a_id)
    dest = page.locator(element_b_id)

    if source and dest:
        source_bound = source.bounding_box()
        dest_bound = dest.bounding_box()
        if source_bound and dest_bound:
            page.mouse.move(source_bound["x"], source_bound["y"])
            page.mouse.down()
            page.mouse.move(dest_bound["x"], dest_bound["y"])
            page.mouse.up()

            expect(page.locator(element_a_id)).to_have_text('B')
            expect(page.locator(element_b_id)).to_have_text('A')
        else:
            raise("No such element")

def test_drag_and_drop_on_jQuery_website(before_all_after_all):
    page = before_all_after_all

    page.goto(drag_drop_jQuery_URL)
    assert page.title() is not None
    expect(page).to_have_title(page_title_jQuery)

    frame = page.frame(url = "/resources/demos/droppable/default.html")

    if frame:
        source = frame.locator(elem_draggable_id)
        dest = frame.locator(elem_droppable_id)

        if source and dest:
            source_bound = source.bounding_box()
            dest_bound = dest.bounding_box()
            if source_bound and dest_bound:
                page.mouse.move(source_bound["x"], source_bound["y"])
                page.mouse.down()
                page.mouse.move(dest_bound["x"], dest_bound["y"])
                page.mouse.up()

                expect(frame.locator(elem_droppable_id)).to_have_text('Dropped!')
            else:
                raise("No such element")