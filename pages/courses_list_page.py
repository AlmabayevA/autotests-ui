from playwright.sync_api import Page, expect

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent

from pages.base_page import BasePage

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.course_view = CourseViewComponent(page)
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.toolbar_view = CoursesListToolbarViewComponent(page)
        
        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')

    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

