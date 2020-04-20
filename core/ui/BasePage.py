from Lib.abc import ABC
from core.driver.WebDriver import WebDriver as Driver
from core.ui.FrameElement import FrameElement

class BasePage (ABC):


    """
        BasePage is a Abstract class that offer somes methods to do somes actions without an WebUIElement
    """

    def getTitle(self):
        """
            A method to get the title for the current page.
            @return str
        """
        Driver.getInstance().getTitle()

    def goToUrl(self, url):
        """
            A method to go at specify URL.
            @param url : str
        """
        Driver.getInstance().get(url)