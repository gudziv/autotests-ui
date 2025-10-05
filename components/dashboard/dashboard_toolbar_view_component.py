import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from  elements.text import Text
from  elements.image import Image


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'dashboard-toolbar-title-text', 'Title')

        self.students_title = Text(page, 'students-widget-title-text', 'Students')
        self.students_chart = Image(page, 'students-bar-chart', 'students-bar-chart')

        self.activities_title = Text(page, 'activities-widget-title-text', 'Activities')
        self.activities_chart = Image(page, 'activities-line-chart', 'activity-bar-chart')

        self.courses_title = Text(page,'courses-widget-title-text', 'Courses')
        self.courses_chart = Image(page,'courses-pie-chart', 'courses-pie-chart')

        self.scores_title = Text(page, 'scores-widget-title-text', 'Scores')
        self.scores_chart = Image(page,'scores-scatter-chart', 'scores-scatter-chart')
    
    @allure.step('Check visible dashboard toolbar view')
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Dashboard')

        self.students_title.check_visible()
        self.students_title.check_have_text('Students')

        self.activities_title.check_visible()
        self.activities_title.check_have_text('Activities')
