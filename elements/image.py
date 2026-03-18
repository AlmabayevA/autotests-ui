from elements.base_element import BaseElement

class Image(BaseElement):
    @property
    def type(self) -> str:
        return "image"
