from playwright.sync_api import sync_playwright, expect

# from playwright_registration import button_registration

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    button_registration = page.get_by_test_id('registration-page-registration-button')
    expect(button_registration).to_be_disabled()

    input_email_fill = page.get_by_test_id('registration-form-email-input').locator('input')
    input_email_fill.fill('user.name@gmail.com')

    input_username_fill = page.get_by_test_id('registration-form-username-input').locator('input')
    input_username_fill.fill('username')

    input_password_fill = page.get_by_test_id('registration-form-password-input').locator('input')
    input_password_fill.fill('password')

    expect(button_registration).not_to_be_disabled()


