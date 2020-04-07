from core.driver.WebDriver import WebDriver

class BaseElement(object):

    def __init__(self):
        self.driver = WebDriver().getInstance()

    def get(self, elementBy):
        return self.driver.find_element(elementBy)