from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str) -> None:
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-empty-view-icon', 'empty_icon')
        self.title = Text(page,f'{identifier}-empty-view-title-text', 'title')
        self.description = Text(page, f'{identifier}-empty-view-description-text', 'description')

    def check_visible(self, title: str, description: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.description.check_visible()
        self.description.check_have_text(description)
