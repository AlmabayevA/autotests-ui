from playwright.sync_api import Page, expect

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.course_view_component import CourseViewComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent

from  elements.text import Text
from elements.icon import Icon

from pages.base_page import BasePage

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.course_view_menu = CourseViewMenuComponent(page)
        self.course_view = CourseViewComponent(page)
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.toolbar_view = CoursesListToolbarViewComponent(page)
        
        self.courses_title = Text(page, 'courses-list-toolbar-title-text', 'Course Title')
        self.create_course_button = Text(page, 'courses-list-toolbar-create-course-button', 'Button')

        self.empty_view_icon = Icon(page, 'courses-list-empty-view-icon', 'Empty Icon')
        self.empty_view_title = Text(page, 'courses-list-empty-view-title-text', 'Empty Title')
        self.empty_view_description = Text(page, 'courses-list-empty-view-description-text', 'Empty Description')

    def check_visible_courses_title(self):
        self.courses_title.check_visible()
        self.courses_title.check_have_text('Courses')

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

