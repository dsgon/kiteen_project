import pytest
import allure
from steps.DemoQASteps.HomeSteps import HomeSteps as home
from steps.DemoQASteps.MenuSteps import MenuSteps as menu
from steps.DemoQASteps.menu.switchTo_steps import SwitchToSteps as switchTo
from steps.DemoQASteps.FrameSteps import FrameSteps as frame

class TestFrame:

    text_to_input = "This is a sample"

    @allure.description('User navigate until Frame module')
    def setup_method(self):
        home().clickOnSkipSingIn()
        menu().clickOnSwitchTo()
        switchTo().clickOnFramesOption().takeScreenshot()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('User write into a Frame element')
    @allure.title('User write into a Frame element')
    @pytest.mark.smoke
    def test_verifyElementInsideSingleFrame(self):
        frame().verifySingleInput().setTextSingleInput(self.text_to_input).takeScreenshot()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('User write into a Frame that is into another Frame element')
    @allure.title('User write into a Frame that is into another Frame element')
    def test_verifyElementInsideTwoFrames(self):
        frame().verifyIframeWithIframeButton().clickOnIframeWithIframeButton().\
            verifyInputInFrames().setTextOnInputInsideFrames(self.text_to_input).takeScreenshot()

    def teardown_method(self):
        frame().closeBrowser()
