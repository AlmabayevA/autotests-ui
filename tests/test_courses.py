import pytest
from playwright.sync_api import expect, Page

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
        page = chromium_page_with_state
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()

        no_results_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_results_text).to_be_visible()

        empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_icon).to_be_visible()

        empty_description_text = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(empty_description_text).to_be_visible()
