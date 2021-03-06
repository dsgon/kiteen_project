from pages.DemoQAPages.Menu import switchTo_page as page
from core.steps.BaseSteps import BaseStep
from core.assertion import assertion
import allure

class SwitchToSteps(BaseStep):

    @allure.step
    def verifyFramesOption(self):
        assertion.assertTrue('Unable to find Frames option',page.getFrameOption().isDisplayed())
        return self

    @allure.step
    def clickOnFramesOption(self):
        self.verifyFramesOption()
        page.getFrameOption().click()
        return self

    @allure.step
    def verifyAlertsOption(self):
        assertion.assertTrue('Unable to find Alerts option',page.getAlertsOption().isDisplayed())
        return self

    @allure.step
    def clickOnAlertsOption(self):
        self.verifyAlertsOption()
        page.getAlertsOption().click()
        return self