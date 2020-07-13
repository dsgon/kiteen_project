from pages.DemoQAPages.FramePage import FramePage as page
from steps.BaseSteps import BaseStep
from core.assertion.Assertion import Assertion
import allure

class FrameSteps(BaseStep):

    def __init__(self):
        self.__page = page()

    @allure.step
    def verifySingleInput(self):
        Assertion.assertTrue("Input is not Displayed",self.__page.getSingleInput().isDisplayed())
        return self

    @allure.step
    def setTextSingleInput(self,text):
        self.__page.getSingleInput().setText(text)
        return self

    @allure.step
    def verifyIframeWithIframeButton(self):
        Assertion.assertTrue("Button is not Displayed",self.__page.getButtonIframeWithIframe().isDisplayed())
        return self

    @allure.step
    def clickOnIframeWithIframeButton(self):
        self.__page.getButtonIframeWithIframe().click()
        return self

    @allure.step
    def verifyInputInFrames(self):
        Assertion.assertTrue("Input is not Displayed",self.__page.getInputInFrames().isDisplayed())
        return self

    @allure.step
    def setTextOnInputInsideFrames(self,text):
        self.__page.getInputInFrames().setText(text)
        return self