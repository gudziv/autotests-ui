from pages.base_page import BasePage
from playwright.sync_api import Page, expect



class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.field_input_email = page.get_by_test_id('registration-form-email-input').locator('input')
        self.field_input_username = page.get_by_test_id('registration-form-username-input').locator('input')
        self.field_input_password = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')

    def fill_registration_form(self, email: 'str', username: 'str', password: 'str'):
        self.field_input_email.clear()
        self.field_input_username.clear()
        self.field_input_password.clear()
        self.field_input_email.fill(email)
        self.field_input_username.fill(username)
        self.field_input_password.fill(password)
        expect(self.field_input_email).to_have_value(email)
        expect(self.field_input_username).to_have_value(username)
        expect(self.field_input_password).to_have_value(password)

    def click_registration_button(self):
        self.registration_button.click()

