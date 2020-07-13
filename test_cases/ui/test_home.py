import pytest
import allure
from steps.DemoQASteps.HomeSteps import HomeSteps as home
from steps.DemoQASteps.MenuSteps import MenuSteps as menu


@allure.severity(allure.severity_level.NORMAL)
@allure.description('User Skip Sing In Proccess')
@allure.title('User Skip Sing In Proccess')
def test_skip_singin():
    home().clickOnSkipSingIn()
    menu().verifySwitchToOption().takeScreenshot()

def teardown():
    menu().closeBrowser()