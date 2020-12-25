from pages.DemoQAPages import HomePage as page
from core.steps.BaseSteps import BaseStep
from core.assertion import assertion
import allure

class HomeSteps (BaseStep):

    @allure.step
    def verifyButtonSkipSingIn(self):
        assertion.assertTrue('Unable to find Skip Sing In button', page.getButtonSkipSingIn().isDisplayed())
        return self

    @allure.step
    def clickOnSkipSingIn(self):
        self.verifyButtonSkipSingIn()
        page.getButtonSkipSingIn().click()
        return self