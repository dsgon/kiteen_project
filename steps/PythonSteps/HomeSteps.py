from core.ui.BaseSteps import BaseStep
from pages.PythonPage.HomePage import PythonHomePage
import allure

class PythonHomeSteps(BaseStep):

    def __init__(self):
        self.__page = PythonHomePage()

    @allure.step
    def clickOnAboutUs(self, withWait):
        """
            Click on 'About Us' option
        """
        self.__page.getAboutUs().click(withWait)
        return self

    @allure.step
    def verifyAboutUsButton(self):
        assert True == self.__page.getAboutUs().isDisplayed() , "button 'About Us' is not visible"
        return self

    @allure.step
    def mouseOnAboutUs(self):
        self.__page.getAboutUs().mouseOver()
        return self

    @allure.step
    def clickOnQuotesOption(self):
        self.__page.getQuotes().click()
        return self

    @allure.step
    def verifyTextLearnMore(self):
        expectedText = 'Learn More'
        actualText = self.__page.linkLearnMore().getText()
        assert expectedText == actualText , 'Not equals. We expected: "'+expectedText+'" and actual is: "'+actualText+'"'
        return self

    @allure.step
    def moveUntilStatusLink(self):
        self.__page.linkStatus().scrollUntilThis()
        return self

    @allure.step
    def verifyStatusLinkIsVisible(self):
        assert True == self.__page.linkStatus().isDisplayed() , "button 'Status' is not visible"
        return self

    @allure.step
    def verifyStatusLinkIsPresent(self):
        assert True == self.__page.linkStatus().isPresent() , "button 'Status' is not present"
        return self