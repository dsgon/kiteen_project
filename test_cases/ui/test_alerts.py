import pytest
import allure
from steps.DemoQASteps.HomeSteps import HomeSteps as home
from steps.DemoQASteps.MenuSteps import MenuSteps as menu
from steps.DemoQASteps.menu.switchTo_steps import SwitchToSteps as switchTo_steps
from steps.DemoQASteps.alerts_steps import AlertsSteps as alerts_steps

@allure.description('User navigate until Frame module')
def setup():
    home().clickOnSkipSingIn()
    menu().clickOnSwitchTo()
    switchTo_steps().clickOnAlertsOption()

@allure.severity(allure.severity_level.NORMAL)
@allure.description('User open an alert message with OK button and pick OK')
@allure.title('User open an alert with OK button and pick OK')
def test_open_alert_ok():
    alerts_steps().openDialogOK().acceptAlert()

@allure.severity(allure.severity_level.NORMAL)
@allure.description('User open an alert message with OK and Cancel buttons and pick Cancel')
@allure.title('User open an alert with OK and Cancel buttons and pick Cancel')
def test_open_alert_okcancel_cancel():
    alerts_steps().selectAlertWithOkAndCancelOption().openDialogOKCancel().declineAlert().takeScreenshot()

@allure.severity(allure.severity_level.NORMAL)
@allure.description('User open an alert message with OK and Cancel buttons and pick OK')
@allure.title('User open an alert with OK and Cancel buttons and pick OK')
def test_open_alert_okcancel_ok():
    alerts_steps().selectAlertWithOkAndCancelOption().openDialogOKCancel().acceptAlert().takeScreenshot()

@allure.severity(allure.severity_level.NORMAL)
@allure.description('User open an alert message with a Textbox and set a message')
@allure.title('User open an alert with a Textbox and set a message')
@pytest.mark.smoke
def test_open_alert_textbox_message():
    message = 'Kiteen'
    alerts_steps().selectAlertWithTextboxOption().openDialogTextbox()\
        .writeMessageOnAlert(message).acceptAlert().verifyMessage(message).takeScreenshot()

@allure.severity(allure.severity_level.NORMAL)
@allure.description('User open an alert message with a Textbox and pick Cancel')
@allure.title('User open an alert with a Textbox and pick Cancel')
def test_open_alert_textbox_cancel():
    alerts_steps().selectAlertWithTextboxOption().openDialogTextbox()\
        .declineAlert().takeScreenshot()

def teardown():
    alerts_steps().closeBrowser()