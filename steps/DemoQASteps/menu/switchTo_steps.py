from pages.DemoQAPages.Menu import switchTo_page as page
from steps.BaseSteps import BaseStep
from core.assertion.Assertion import Assertion
import allure

class SwitchToSteps(BaseStep):

    @allure.step
    def verifyFramesOption(self):
        Assertion.assertTrue('Unable to find Frames option',page.getFrameOption().isDisplayed())
        return self

    @allure.step
    def clickOnFramesOption(self):
        self.verifyFramesOption()
        page.getFrameOption().click()
        return self

    @allure.step
    def verifyAlertsOption(self):
        Assertion.assertTrue('Unable to find Alerts option',page.getAlertsOption().isDisplayed())
        return self

    @allure.step
    def clickOnAlertsOption(self):
        self.verifyAlertsOption()
        page.getAlertsOption().click()
        return self