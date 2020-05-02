from pages.HomePage import HomePage

#TO-DO: migrate responsibility to another Step
class HomeSteps(object):

    def __init__(self):
        self.__page = HomePage()

    def goTo(self, url):
        self.__page.goToUrl(url)
        return self

    def verifyTitleFrame(self):
        assert True == self.__page.getSiteDescription_Frame().isDisplayed()
        return self

    def moveUntilIFramePracticeOption(self):
        self.__page.getIFramePracticeOption().scrollUntilThis()
        return self

    def clickOnSeleniumInJavaOption(self):
        self.__page.getSeleniumInJavaOption_Frame().clickByJavaScript()
        return self

    def verifySeleniumTutorial(self):
        assert True == self.__page.getSeleniumTutotialTitle_Frame().isDisplayed()
        return self