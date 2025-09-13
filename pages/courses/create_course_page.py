from playwright.sync_api import Page

from pages.base_page import BasePage
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from  components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)

        self.create_course_exercise_form = CreateCourseExerciseFormComponent(page)

        self.image_upload_widget = ImageUploadWidgetComponent(page, identifier='create-course-preview')

        self.create_courses_toolbar_view = CreateCourseToolbarViewComponent(page)

        self.create_course_form = CreateCourseFormComponent(page)

        self.create_course_exercises_toolbar_view = CreateCourseExercisesToolbarViewComponent(page)

        self.exercises_empty_view = EmptyViewComponent(page, identifier='create-course-exercises')

    def check_visible_create_course_title(self):
        self.create_courses_toolbar_view.check_visible(is_create_course_disabled=True)

    def click_create_course_button(self):
        self.create_courses_toolbar_view.create_course_button.click()

    def check_visible_create_course_button(self):
        self.create_courses_toolbar_view.create_course_button.check_visible()

    def check_disabled_create_course_button(self):
        self.create_courses_toolbar_view.create_course_button.check_disabled()

    def check_visible_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_form.check_visible(title, estimated_time, description, max_score, min_score)

    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_form.fill(title, estimated_time, description, max_score, min_score)

    def check_visible_exercises_title(self):
        self.create_course_exercises_toolbar_view.title.check_visible()

    def click_create_exercises_button(self):
        self.create_course_exercises_toolbar_view.click_create_exercise_button()

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )

# from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
# from  components.navigation.navbar_component import NavbarComponent
# from components.views.empty_view_component import EmptyViewComponent
# from components.views.image_upload_widget_component import ImageUploadWidgetComponent
# from pages.base_page import BasePage
# from playwright.sync_api import Page
# from components.courses.create_course_form_component import CreateCourseFormComponent
# from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
# from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
#
#
# class CreateCoursePage(BasePage):
#     def __init__(self, page: Page):
#         super().__init__(page)
#
#         self.navbar = NavbarComponent(page)
#
#         self.create_course_form = CreateCourseExerciseFormComponent(page)
#
#         self.image_upload_widget = ImageUploadWidgetComponent(page, identifier='create-course-preview')
#
#         self.toolbar_courses = CreateCourseToolbarViewComponent(page)
#
#         self.course_form = CreateCourseFormComponent(page)
#
#         self.exercises_toolbar = CreateCourseExercisesToolbarViewComponent(page)
#
#         self.exercises_empty_view = EmptyViewComponent(page, identifier='create-course-exercises')
#
#     def check_visible_create_course_title(self):
#         self.toolbar_courses.check_visible(is_create_course_disabled=True)
#
#     def click_create_course_button(self):
#         self.toolbar_courses.create_course_button.click()
#
#     def check_visible_create_course_button(self):
#         self.toolbar_courses.create_course_button.check_visible()
#
#     def check_disabled_create_course_button(self):
#         self.toolbar_courses.create_course_button.check_disabled()
#
#     def check_visible_create_course_form(
#             self,
#             title: str,
#             estimated_time: str,
#             description: str,
#             max_score: str,
#             min_score: str
#     ):
#         self.course_form.check_visible(title, estimated_time, description, max_score, min_score)
#
#     def fill_create_course_form(
#             self,
#             title: str,
#             estimated_time: str,
#             description: str,
#             max_score: str,
#             min_score: str
#     ):
#         self.course_form.fill(title, estimated_time, description, max_score, min_score)
#
#     def check_visible_exercises_title(self):
#         self.exercises_toolbar.title.check_visible()
#
#     def click_create_exercises_button(self):
#         self.exercises_toolbar.click_create_exercise_button()
#
#     def check_visible_exercises_empty_view(self):
#         self.exercises_empty_view.check_visible(
#             title='There is no exercises',
#             description='Click on "Create exercise" button to create new exercise'
#         )
