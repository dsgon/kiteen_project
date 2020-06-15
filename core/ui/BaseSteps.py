from core.driver.WebDriver import WebDriver as Driver
from core.assertion.Assertion import Assertion
from Lib import datetime  
from Lib.abc import ABC
import allure


class BaseStep (ABC):

    """
        BasePage is a Abstract class that offer somes methods to do somes actions without an WebUIElement
    """

    @allure.step
    def getTitle(self):
        """
            A method to get the title for the current page.
            :return: str
        """
        return Driver.getInstance().title

    @allure.step
    def goToUrl(self, url):
        """
            A method to go at specify URL.
            :param url: str
        """
        Driver.getInstance().get(url)

    @allure.step
    def closeBrowser(self):
        """
            A method to close the current Browser
        """
        Driver.closeDriver()

    @allure.step
    def verifyPageTitle(self,titleExpected):
        """
            Verify Title from the current page with the Expected value

            :param titleExpected: str
            :return: self
        """
        Assertion().assertEquals(expectedValue=titleExpected,actualValue=self.getTitle())
        return self

    @allure.step
    def takeScreenshot(self,name=str(datetime.datetime.now())):
        """
            Take a screenshot in PNG format and attach it into allure report.
            Receive a name for the image. By default set the current timestamp for the name.

            :params name: str
        """
        allure.attach(Driver.getInstance().get_screenshot_as_png(),name,attachment_type=allure.attachment_type.PNG)