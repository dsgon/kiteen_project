from pages.DemoQAPages import AlertsPage as page
from core.steps.BaseSteps import BaseStep
from core.assertion.Assertion import Assertion
import allure

class AlertsSteps(BaseStep):

    @allure.step
    def selectAlertWithOkOption(self):
        page.getOptionAlertOk().click()
        return self

    @allure.step
    def selectAlertWithOkAndCancelOption(self):
        page.getOptionAlertOkCancel().click()
        return self

    @allure.step
    def selectAlertWithTextboxOption(self):
        page.getOptionAlertTextbox().click()
        return self

    @allure.step
    def verifyButtonAlertOK(self):
        Assertion.assertTrue('Unable to find the button to display an alert box with OK',page.getButtonAlertOK().isDisplayed())
        return self

    @allure.step
    def openDialogOK(self):
        self.verifyButtonAlertOK()
        page.getButtonAlertOK().click()
        return self

    @allure.step
    def verifyOkAndCancelOption(self):
        Assertion.assertTrue('Unable to find the OK and Cancel option',page.getButtonAlertOKCancel().isDisplayed())
        return self

    @allure.step
    def verifyButtonAlertOKCancel(self):
        Assertion.assertTrue('Unable to find the button to display an alert box with OK and Cancel options',page.getButtonAlertOKCancel().isDisplayed())
        return self

    @allure.step
    def openDialogOKCancel(self):
        self.verifyButtonAlertOKCancel()
        page.getButtonAlertOKCancel().click()
        return self

    @allure.step
    def verifyButtonAlertTextbox(self):
        Assertion.assertTrue('Unable to find the button to display an alert with Textbox',page.getButtonAlertTextbox().isDisplayed())
        return self

    @allure.step
    def openDialogTextbox(self):
        self.verifyButtonAlertTextbox()
        page.getButtonAlertTextbox().click()
        return self

    @allure.step
    def writeMessageOnAlert(self, message):
        self._BaseStep__setTextOnAlertMessage(message)
        return self

    @allure.step
    def verifyMessage(self, message):
        expected_format = 'Hello {} How are you today'.format(message)
        Assertion.assertEquals('The message is not equal:',expected_format,page.getMessageText().getText())
        return self