from playwright.sync_api import expect, Page
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    button_courses = chromium_page_with_state.get_by_test_id('courses-drawer-list-item-title-text')
    button_courses.click()

    title_courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(title_courses).to_have_text('Courses')

    block_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(block_icon).to_be_visible()

    result_text_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(result_text_block).to_be_visible()
    expect(result_text_block).to_have_text('There is no results')

    description_text_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_text_block).to_be_visible()
    expect(description_text_block).to_have_text('Results from the load test pipeline will be displayed here')
