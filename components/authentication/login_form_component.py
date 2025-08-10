from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')

    def fill(self, email: str, password_value: str):
        self.email_input.clear()
        self.password_input.clear()
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)
        self.password_input.fill(password_value)
        expect(self.password_input).to_have_value(password_value)

    def check_visible(self, email: str, password_value: str):
        expect(self.email_input).to_be_visible()
        expect(self.email_input).to_have_text(email)
        expect(self.password_input).to_be_visible()
        expect(self.password_input).to_have_text(password_value)
