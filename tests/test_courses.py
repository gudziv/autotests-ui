import pytest
from playwright.sync_api import  expect, Page
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage


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


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(chromium_page_with_state: Page, course_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        chromium_page_with_state.goto(
                'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
        )
        create_course_page.check_visible_create_course_title()
        create_course_page.check_disabled_create_course_button()
        create_course_page.check_visible_image_preview_empty_view()
        create_course_page.check_visible_image_upload_view()
        create_course_page.check_visible_create_course_form(
                title='',
                description='',
                estimated_time='',
                max_score='0',
                min_score='0'
        )
        create_course_page.check_visible_exercises_title()
        create_course_page.check_visible_create_exercise_button()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.upload_preview_image('./testdata/files/image.png')
        create_course_page.check_visible_image_upload_view()
        create_course_page.fill_create_course_form(
                title="Playwright",
                estimated_time="2 weeks",
                description="Playwright",
                max_score="100",
                min_score="10"
        )
        create_course_page.click_create_course_button()
        course_list_page.check_visible_courses_title()
        course_list_page.check_visible_create_course_button()
        course_list_page.check_visible_course_card(
                index=0,
                title="Playwright",
                max_score="100",
                min_score="10",
                estimated_time = "2 weeks"
        )
