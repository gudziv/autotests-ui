import pytest
import allure
from allure_commons.types import Severity

from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage

from tools.allure.epics import AllureEpic
from tools.allure.feaures import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.courses
@pytest.mark.regression
@allure.tag (AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, course_list_page: CoursesListPage):
        course_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        course_list_page.navbar.check_visible('username')
        course_list_page.sidebar.check_visible()
        course_list_page.toolbar_view.check_visible()
        course_list_page.check_visible_empty_view()

    @allure.title('Create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, course_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
        )
        create_course_page.create_courses_toolbar_view.check_visible()

        create_course_page.check_visible_create_course_title()
        create_course_page.check_disabled_create_course_button()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title='', description='', estimated_time='', max_score='0', min_score='0'
        )
        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.fill_create_course_form(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_courses_toolbar_view.click_create_course_button()
        
        course_list_page.toolbar_view.check_visible()

        course_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )
    @allure.title('Edit course')
    @allure.severity(Severity.NORMAL)
    def test_edit_course(self, course_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit (
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
        )
        create_course_page.fill_create_course_form (
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.image_upload_widget.upload_preview_image ('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible (is_image_uploaded=True)
        create_course_page.create_courses_toolbar_view.click_create_course_button()

        course_list_page.course_view.check_visible (
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )
        create_course_page.click_course_menu_button()
        create_course_page.click_course_menu_edit_button()

        create_course_page.fill_create_course_form(
            title="Playwright-python",
            estimated_time="3 weeks",
            description="Playwright with python",
            max_score="120",
            min_score="5"
        )
        create_course_page.create_courses_toolbar_view.click_create_course_button ()

        course_list_page.course_view.check_visible (
            index=0,
            title="Playwright-python",
            max_score="120",
            min_score="5",
            estimated_time="3 weeks"
        )
