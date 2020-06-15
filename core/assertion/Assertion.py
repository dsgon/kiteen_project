from core.driver.WebDriver import WebDriver
from Lib import datetime
import allure
import pytest

class Assertion():

    """
        Class to handle Assertions to do verifications in our Test Cases.
    """

    def assertTrue(self,failedMessage,value):
        """
            Verify that the input value is True. Otherwise, the Assertion will fail and take a ScreenShot automatically
            and add the Allure report the failed message

            :failedMessage: str
            :value: bool
        """
        try:
            assert True == value
        except:
            self.__on_failure_screesnshot()
            pytest.fail(failedMessage,False)

    def assertFalse(self,failedMessage,value):
        """
            Verify that the input value is False. Otherwise, the Assertion will fail and take a ScreenShot automatically
            and add the Allure report the failed message

            :failedMessage: str
            :value: bool
        """
        try:
            assert False == value
        except:
            self.__on_failure_screesnshot()
            pytest.fail(failedMessage,False)

    def assertEquals(self,failedMessage='', expectedValue=None, actualValue=None):
        """
            Verify that the value of the inputs is Equals. Otherwise, the Assertion will fail and take a ScreenShot automatically
            and add the Allure report the failed message

            :expectedValue: Obj
            :actualValue: Obj
        """
        try:
            assert expectedValue == actualValue
        except:
            self.__on_failure_screesnshot()
            pytest.fail("Not equals. Expected: '{}' but Actual is: '{}'. {}".format(expectedValue,actualValue,failedMessage),False)

    def assertNotEquals(self,failedMessage='', expectedValue=None, actualValue=None):
        """
            Verify that the value of the inputs is Not Equals. Otherwise, the Assertion will fail and take a ScreenShot automatically
            and add the Allure report the failed message

            :expectedValue: Obj
            :actualValue: Obj
        """
        try:
            assert expectedValue != actualValue
        except:
            self.__on_failure_screesnshot()
            pytest.fail("Equals. Expected: '{}' but Actual is: '{}'. {}".format(expectedValue,actualValue,failedMessage),False)

    def __on_failure_screesnshot(self):
        """
            Private method to take a Screenshot if an Assertion fails.
        """
        allure.attach(WebDriver.getInstance().get_screenshot_as_png(),str(datetime.datetime.now()),attachment_type=allure.attachment_type.PNG)