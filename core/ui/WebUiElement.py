from core.ui.BaseElement import BaseElement


class WebUiElement (BaseElement,):

    def __init__(self, locator):
        self.elementBy = locator

    def click(self):
        self.get(self.elementBy).click()