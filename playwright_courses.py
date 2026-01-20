from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    context.storage_state(path="browser-state.json")

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()

    no_results_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results_text).to_be_visible()

    empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_icon).to_be_visible()

    empty_description_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_description_text).to_be_visible()
