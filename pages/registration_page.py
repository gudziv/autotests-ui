from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = page.get_by_test_id('registration-page-registration-button')

    def fill_registration_form(self, email: str, username: str, password_value: str):
        self.registration_form.fill(email, username, password_value)
        self.registration_form.check_visible(email, username, password_value)

    def click_registration_button(self):
        self.registration_button.click()
