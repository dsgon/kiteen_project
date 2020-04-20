from Lib import unittest
from steps.HomeSteps import HomeSteps
from core.driver.WebDriver import WebDriver
import time

class HelloWorld(unittest.TestCase):

    def test_aboutUsValid(self):
        HomeSteps().verifyAboutUsButton().clickOnAboutUs()

    def test_aboutUsQuotes(self):
        HomeSteps().verifyAboutUsButton().mouseOnAboutUs().clickOnQuotesOption()

    def test_getText(self):
        HomeSteps().verifyTextLearnMore()

    def test_moveUntil(self):
        HomeSteps().moveUntilStatusLink()

    def test_goTo(self):
        HomeSteps().goTo("http://www.practia.global/practia-academy/Paginas/default.aspx")
        
    def test_verifyElementInsideFrame(self):
        HomeSteps().goTo("https://demoqa.com/iframe-practice-page/")\
            .moveUntilIFramePracticeOption().verifyTitleFrame()\
                .clickOnSeleniumInJavaOption().verifySeleniumTutorial()

    def tearDown(self):
        WebDriver.closeDriver()

if __name__ == '__main__':  
    unittest.main()