from playwright.sync_api import Page, expect
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
        chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        input_field_email = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        input_field_email.fill('user@gmail.com')

        input_field_username = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        input_field_username.fill('username')

        input_field_password = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        input_field_password.fill('password')

        button_registration = chromium_page.get_by_test_id('registration-page-registration-button')
        button_registration.click()

        dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_title).to_be_visible()
        expect(dashboard_title).to_have_text('Dashboard')

