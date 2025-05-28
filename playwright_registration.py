from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    input_field_email = page.get_by_test_id('registration-form-email-input').locator('input')
    input_field_email.fill('user.name@gmail.com')

    input_field_username = page.get_by_test_id('registration-form-username-input').locator('input')
    input_field_username.fill('username')

    input_field_password = page.get_by_test_id('registration-form-password-input').locator('input')
    input_field_password.fill('password')

    button_registration = page.get_by_test_id('registration-page-registration-button')
    button_registration.click()

    title_dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(title_dashboard).to_be_visible()
    expect(title_dashboard).to_have_text('Dashboard')

    page.wait_for_timeout(5000)
