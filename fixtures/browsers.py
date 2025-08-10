import  pytest
from playwright.sync_api import Playwright


@pytest.fixture
def chromium_page(playwright: Playwright) :
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)  # , slow_mo=850
    context =  browser.new_context()
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

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    yield page
    browser.close()
