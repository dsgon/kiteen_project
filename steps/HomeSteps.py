from pages.HomePage import HomePage

class HomeSteps(object):

    def __init__(self):
        self.__page = HomePage()

    def clickOnAboutUs(self):
        self.__page.getAboutUs().click()
        return self

    def verifyAboutUsButton(self):
        assert True == self.__page.getAboutUs().isDisplayed()
        return self

    def verifyPageTitle(self):
        expectedTitle = 'About Python™ | Python.or'
        assert expectedTitle == self.__page.getTitle() , 'Not equals. We expected: "'+expectedTitle+'" and actual is: "'+self.__page.getTitle+'"'
        return self

    def mouseOnAboutUs(self):
        self.__page.getAboutUs().mouseOver()
        return self

    def clickOnQuotesOption(self):
        self.__page.getQuotes().click()
        return self

    def verifyTextLearnMore(self):
        expectedText = 'Learn More'
        actualText = self.__page.linkLearnMore().getText()
        assert expectedText == actualText , 'Not equals. We expected: "'+expectedText+'" and actual is: "'+actualText+'"'
        return self

    def moveUntilStatusLink(self):
        self.__page.linkStatus().scrollUntilThis()
        return self

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