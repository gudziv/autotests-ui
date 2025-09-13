import pytest
from playwright.sync_api import Page

from fixtures.browsers import chromium_page

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage

from pages.dashboard.dashboard_page import DashboardPage


@pytest.fixture()
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)

@pytest.fixture()
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)

@pytest.fixture()
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page)

@pytest.fixture()
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page_with_state)

@pytest.fixture()
def course_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(chromium_page_with_state)

@pytest.fixture()
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=chromium_page_with_state)

# import pytest
# from playwright.sync_api import Page
#
# from fixtures.browsers import chromium_page
# from pages.courses_list_page import CoursesListPage
# from pages.login_page import LoginPage
# from pages.registration_page import RegistrationPage
# from pages.dashboard_page import DashboardPage
# from pages.create_course_page import CreateCoursePage
#
#
# @pytest.fixture()
# def login_page(chromium_page: Page) -> LoginPage:
#     return LoginPage(page=chromium_page)
#
# @pytest.fixture()
# def registration_page(chromium_page: Page) -> RegistrationPage:
#     return RegistrationPage(page=chromium_page)
#
# @pytest.fixture()
# def dashboard_page(chromium_page: Page) -> DashboardPage:
#     return DashboardPage(page=chromium_page)
#
# @pytest.fixture()
# def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
#     return DashboardPage(page=chromium_page_with_state)
#
# @pytest.fixture()
# def course_list_page(chromium_page_with_state: Page) -> CoursesListPage:
#     return CoursesListPage(chromium_page_with_state)
#
# @pytest.fixture()
# def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
#     return CreateCoursePage(page=chromium_page_with_state)