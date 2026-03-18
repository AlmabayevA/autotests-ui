import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text
from elements.image import Image

class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.identifier = identifier
        self.chart_type = chart_type

        self.title = Text(page, f"{identifier}-widget-title-text", 'Title')
        self.chart = Image(page, f"{identifier}-{chart_type}-chart", 'Chart')

    @allure.step('Check visible title and chart ')
    def check_visible(self):
        self.title.check_visible()
        self.chart.check_visible()
