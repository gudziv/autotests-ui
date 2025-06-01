from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        input_field_email = page.get_by_test_id('registration-form-email-input').locator('input')
        input_field_email.fill('user@gmail.com')

        input_field_username = page.get_by_test_id('registration-form-username-input').locator('input')
        input_field_username.fill('username')

        input_field_password = page.get_by_test_id('registration-form-password-input').locator('input')
        input_field_password.fill('password')

        button_registration = page.get_by_test_id('registration-page-registration-button')
        button_registration.click()

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        button_courses = page.get_by_test_id('courses-drawer-list-item-title-text')
        button_courses.click()

        title_courses = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(title_courses).to_have_text('Courses')

        block_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(block_icon).to_be_visible()

        result_text_block = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(result_text_block).to_be_visible()
        expect(result_text_block).to_have_text('There is no results')

        description_text_block = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(description_text_block).to_be_visible()
        expect(description_text_block).to_have_text('Results from the load test pipeline will be displayed here')
