from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input = Input(page, 'login-form-password-input', 'Password')

    def fill(self, email: str, password_value: str):
        self.email_input.clear_field()
        self.password_input.clear_field()

        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.password_input.fill(password_value)
        self.password_input.check_have_value(password_value)

    def check_visible(self, email: str, password_value: str):
        self.email_input.check_visible()
        self.email_input.check_have_text(email)
        self.password_input.check_visible()
        self.password_input.check_have_value(password_value)
