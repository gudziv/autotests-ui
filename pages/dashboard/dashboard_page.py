from playwright.sync_api import Page

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent

from pages.base_page import BasePage


class DashboardPage (BasePage):
    def __init__(self, page: Page):
        super ().__init__ (page)
        
        self.navbar = NavbarComponent (page)
        
        self.sidebar = SidebarComponent (page)
        
        self.dashboard_toolbar_view = DashboardToolbarViewComponent (page)
    
    def check_visible_dashboard_title(self):
        self.dashboard_toolbar_view.title.check_visible ()
        self.dashboard_toolbar_view.title.check_have_text ('Dashboard')
    
    def check_visible_scores_chart(self):
        self.dashboard_toolbar_view.scores_chart.check_visible ()
        self.dashboard_toolbar_view.scores_title.check_have_text ('Scores')
        self.dashboard_toolbar_view.scores_chart.check_visible ()
    
    def check_visible_dashboard_toolbar_view(self):
        self.dashboard_toolbar_view.check_visible ()
        self.dashboard_toolbar_view.title.check_have_text ('Dashboard')
    
    def check_visible_students_chart(self):
        self.dashboard_toolbar_view.students_chart.check_visible ()
        self.dashboard_toolbar_view.students_title.check_have_text ('Students')
    
    def check_visible_activities_chart(self):
        self.dashboard_toolbar_view.activities_chart.check_visible ()
        self.dashboard_toolbar_view.activities_title.check_have_text ('Activities')
    
    def check_visible_courses_chart(self):
        self.dashboard_toolbar_view.courses_chart.check_visible ()
        self.dashboard_toolbar_view.courses_title.check_have_text ('Courses')
