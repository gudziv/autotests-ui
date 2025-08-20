from components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.input import Input


class RegistrationFormComponent (BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page,'registration-form-email-input', 'Email')
        self.username_input = Input(page, 'registration-form-username-input', 'Username')
        self.password_input = Input(page,'registration-form-password-input', 'Password')

    def fill(self, email: str, username: str, password_value: str):
        self.email_input.clear_field()
        self.username_input.clear_field()
        self.password_input.clear_field()

        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password_value)

        self.email_input.check_have_value(email)
        self.username_input.check_have_value(username)
        self.password_input.check_have_value(password_value)

    def check_visible(self, email: str, username: str, password_value: str):
        self.email_input.check_visible()
        self.email_input.check_have_text(email)
        self.username_input.check_visible()
        self.username_input.check_have_text(username)
        self.password_input.check_visible()
        self.password_input.check_have_text(password_value)
