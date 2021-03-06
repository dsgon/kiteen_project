from pages.DemoQAPages import MenuPage as page
from core.steps.BaseSteps import BaseStep
from core.assertion import assertion
import allure

class MenuSteps(BaseStep):

    @allure.step
    def verifySwitchToOption(self):
        assertion.assertTrue('Unable to find SwitchTo Option on Menu', page.getOptionSwitchTo().isDisplayed())
        return self

    @allure.step
    def clickOnSwitchTo(self):
        self.verifySwitchToOption()
        page.getOptionSwitchTo().click()
        return self

    